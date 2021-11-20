#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "headers/hashmap.h"
#include "headers/list.h"
#include "headers/login.h"
#include "headers/structs.h"
#include "structs.c"


int lower_than_int(void * key1, void * key2) {
    if(*(long int*)key1 < *(long int*)key2) return 1;
    return 0;
}

char *get_csv_field (char * tmp, int k) {
    int open_mark = 0;
    char* ret=(char*) malloc (100*sizeof(char));
    int ini_i=0, i=0;
    int j=0;
    while(tmp[i+1]!='\0'){

        if(tmp[i]== '\"'){
            open_mark = 1-open_mark;
            if(open_mark) ini_i = i+1;
            i++;
            continue;
        }

        if(open_mark || tmp[i]!= ','){
            if(k==j) ret[i-ini_i] = tmp[i];
            i++;
            continue;
        }

        if(tmp[i]== ','){
            if(k==j) {
               ret[i-ini_i] = 0;
               return ret;
            }
            j++; ini_i = i+1;
        }

        i++;
    }

    if(k==j) {
       ret[i-ini_i] = 0;
       return ret;
    }


    return NULL;
}

int obtener_cant_generos(char* str) {
   int cantGeneros = 0;
   char* token = strtok(str, ",");

   while( token != NULL ) {
      cantGeneros++;
      token = strtok(NULL, ",");
   }
   
   return cantGeneros;
}

void* obtener_generos(char* generos, int cantGeneros) {
    List *generosList = createList();

    if(generos[0] == 34 && generos[strlen(generos) - 1] == 34) {
        generos++;
        generos[strlen(generos)-1] = 0;
    }

    char* token = strtok(generos, ",");
   
    if (cantGeneros > 0) {
        char *genero = malloc(sizeof(char) * (strlen(token) + 1));
        strcpy(genero, token);
        pushBack(generosList, genero);
    }
    
    for(int i = 1; i < cantGeneros; i++) {
        token = strtok(NULL, ",");
        char *genero = malloc(sizeof(char) * (strlen(token) + 1));
        strcpy(genero, token);
        pushBack(generosList, genero);
    }

    return generosList;
}

void *crear_trabajador(char *rut, char *password, char *cargo, char *cine) {
    Trabajador *trabajador = malloc(sizeof(Trabajador));

    strcpy(trabajador->rut, rut);
    strcpy(trabajador->password, password);
    strcpy(trabajador->cargo, cargo);
    strcpy(trabajador->cine, cine);

    return trabajador;
}

// 1
void *cargar_credenciales() {
    char *path = "data/credenciales.csv";
    HashMap *trabajadores = createMap(100);
    FILE *archivo = fopen(path, "r");

    if (archivo == NULL)
        printf("Hubo un error al cargar los datos del programa");
    else {
        char linea[1024];
        char* rut;
        char* password;
        char* cargo;
        char* cine;

        while (fgets (linea, 1023, archivo) != NULL) {
            rut = get_csv_field(linea, 0);
            password = get_csv_field(linea, 1);
            cargo = get_csv_field(linea, 2);
            cine = get_csv_field(linea, 3);

            Trabajador *trabajador = crear_trabajador(rut, password, cargo, cine);
            insertMap(trabajadores, trabajador->rut, trabajador);
        }
    }

    return trabajadores;
}

int cargar_ventas(char *cine_folder) {
    char *ventas_archivo = malloc(strlen(cine_folder) + strlen("ventas.csv") + 1);
    strcpy(ventas_archivo, cine_folder);
    strcat(ventas_archivo, "ventas.csv");

    FILE *f = fopen(ventas_archivo, "r");
    int total_ventas = 0;

    if (f == NULL)
        printf("Hubo un error al cargar las ventas al programa.\n");
    else {
        char linea[1024];
        char* venta;

        // Se consume la primera linea, que trae los nombres de los fields.
        fgets (linea, 1024, f);

        while (fgets (linea, 1024, f) != NULL) {
            venta = get_csv_field(linea, 2);
            total_ventas += atoi(venta);
        }
    }

    free(ventas_archivo);
    return total_ventas;
}

void *cargar_horario_trabajador(char* cine_folder, char *rut) {
    TreeMap *horarios = createTreeMap(lower_than_int);

    char *horario_archivo = malloc(strlen(cine_folder) + strlen("empleados/") + strlen(rut) + strlen("horarios.csv") + 1);
    strcpy(horario_archivo, cine_folder);
    strcat(horario_archivo, "empleados/");
    strcat(horario_archivo, rut);
    strcat(horario_archivo, "/horarios.csv");

    FILE *f = fopen(horario_archivo, "r");

    if (f == NULL)
        printf("Hubo un error al cargar los horarios del trabajador %s al programa.\n", rut);
    else {
        char linea[1024];
        char *inicio;
        char *final;
        
        fgets(linea, 1024, f);

        while (fgets (linea, 1024, f) != NULL) {
            inicio = get_csv_field(linea, 0);
            final = get_csv_field(linea, 1);

            Horario *horario = malloc(sizeof(Horario));
            horario->inicio = atol(inicio);
            horario->final = atol(final);

            insertTreeMap(horarios, &horario->inicio, horario);
        }
    }

    free(horario_archivo);
    return horarios;
}

int cargar_ventas_trabajador(char* cine_folder, char* rut) {
    int total_ventas = 0;

    char *ventas_archivo = malloc(strlen(cine_folder) + strlen("ventas.csv") + 1);
    strcpy(ventas_archivo, cine_folder);
    strcat(ventas_archivo, "ventas.csv");

    FILE *f = fopen(ventas_archivo, "r");

    if (f == NULL)
        printf("Hubo un error al cargar los horarios del trabajador %s al programa.\n");
    else {
        char linea[1024];
        char *rutCSV;
        char *precio;

        while (fgets (linea, 1024, f) != NULL) {
            rutCSV = get_csv_field(linea, 0);

            if (strcmp(rutCSV, rut) == 0) 
                total_ventas += atoi(get_csv_field(linea, 2));
        }
    }

    free(ventas_archivo);
    return total_ventas;
} 

void *cargar_asistencia(char* cine_folder, char* rut) {
    List *asistenciaList = createList();

    char *asistencia_archivo = malloc(strlen(cine_folder) + strlen("empleados/") + strlen(rut) + strlen("asistencia.csv") + 1);
    strcpy(asistencia_archivo, cine_folder);
    strcat(asistencia_archivo, "empleados/");
    strcat(asistencia_archivo, rut);
    strcat(asistencia_archivo, "/asistencia.csv");

    FILE *f = fopen(asistencia_archivo, "r");

    if (f == NULL)
        printf("Hubo un error al cargar la asistencia del trabajador %s al programa.\n", rut);
    else {
        char linea[1024];
        char *horario_inicio;
        char *flag;

        while (fgets (linea, 1024, f) != NULL) {
            horario_inicio = get_csv_field(linea, 0);
            flag = get_csv_field(linea, 1);

            Asistencia *asistencia = malloc(sizeof(asistencia));
            asistencia->inicio = atol(horario_inicio);
            asistencia->asistencia = atoi(flag);

            pushBack(asistenciaList, asistencia);
        }
    }

    free(asistencia_archivo);
    return asistenciaList;
}

void *cargar_trabajador(HashMap *trabajadoresCine, Trabajador *trabajador, char* cine_folder, char* nombre, char* rut, char* sueldo, char* ventas) {
    strcpy(trabajador->nombre, nombre);
    trabajador->sueldo = atoi(sueldo);

    trabajador->horario = cargar_horario_trabajador(cine_folder, rut); 
    trabajador->ventas = cargar_ventas_trabajador(cine_folder, rut);
    trabajador->asistencia = cargar_asistencia(cine_folder, rut);
    insertMap(trabajadoresCine, trabajador->rut, trabajador);
}

void *cargar_trabajadores(char *cine_folder, HashMap *trabajadores, Trabajador* trabajador) {
    HashMap *trabajadoresCine = createMap(100);
    insertMap(trabajadoresCine, trabajador->rut, trabajador);

    char *trabajadores_archivo = malloc(strlen(cine_folder) + strlen("empleados.csv") + 1);
    strcpy(trabajadores_archivo, cine_folder);
    strcat(trabajadores_archivo, "empleados.csv");

    FILE *f = fopen(trabajadores_archivo, "r");

    if (f == NULL)
        printf("Hubo un error al cargar los trabajadores al programa.\n");
    else {
        char linea[1024];
        char* nombre;
        char* rut;
        char* sueldo;
        char* ventas;

        // Se consume la primera linea, que trae los nombres de los fields.
        fgets (linea, 1024, f);

        while (fgets (linea, 1024, f) != NULL) {
            nombre = get_csv_field(linea, 0);
            rut = get_csv_field(linea, 1);
            sueldo = get_csv_field(linea, 2);
            ventas = get_csv_field(linea, 3);

            HashMapPair *trabajadorPair = searchMap(trabajadores, rut);
            Trabajador *trabajadorAux = trabajadorPair->value;

            cargar_trabajador(trabajadoresCine, trabajadorAux, cine_folder, nombre, rut, sueldo, ventas);
        }
    }

    free(trabajadores_archivo);
    return trabajadores;
}

HashMap *cargar_salas(char *cine_folder) {
    HashMap *salas = createMap(10);

    char *salas_archivo = malloc(strlen(cine_folder) + strlen("salas.csv") + 1);
    strcpy(salas_archivo, cine_folder);
    strcat(salas_archivo, "salas.csv");

    FILE *f = fopen(salas_archivo, "r");

    if (f == NULL)
        printf("Hubo un error al cargar las ventas al programa.\n");
    else {
        char linea[1024];
        char* id;
        char* asientos_totales;
        char* estado;

        // Se consume la primera linea, que trae los nombres de los fields.
        fgets (linea, 1024, f);

        while (fgets (linea, 1024, f) != NULL) {
            id = get_csv_field(linea, 0);
            asientos_totales = get_csv_field(linea, 1);
            estado = get_csv_field(linea, 2);

            Sala *sala = malloc(sizeof(Sala));
            strcpy(sala->id, id);
            sala->asientos_totales = atoi(asientos_totales);
            sala->estado = atoi(estado);
            sala->funciones = createTreeMap(lower_than_int);

            insertMap(salas, sala->id, sala);
        }
    }

    free(salas_archivo);
    return salas;
}

void cargar_funciones(char *cine_folder, HashMap* peliculas, HashMap *salas) {
    char *salas_archivo = malloc(strlen(cine_folder) + strlen("funciones.csv") + 1);
    strcpy(salas_archivo, cine_folder);
    strcat(salas_archivo, "funciones.csv");

    FILE *f = fopen(salas_archivo, "r");

    if (f == NULL)
        printf("Hubo un error al cargar las funciones al programa.\n");
    else {
        char linea[1024];
        char* inicio;
        char* sala;
        char* nombre;
        char* id;
        char* entradas_vendidas;

        // Se consume la primera linea, que trae los nombres de los fields.
        fgets (linea, 1024, f);

        while (fgets (linea, 1024, f) != NULL) {
            inicio = get_csv_field(linea, 0);
            sala = get_csv_field(linea, 1);
            nombre = get_csv_field(linea, 2);
            id = get_csv_field(linea, 3);
            entradas_vendidas = get_csv_field(linea, 4);

            Funcion *funcion = malloc(sizeof(Funcion));
            funcion->entradas_vendidas = atoi(entradas_vendidas);

            // Se busca la instancia de la pelicula a la cual corresponde la función y se setea en funcion->pelicula.
            HashMapPair *peliculaPair = searchMap(peliculas, nombre);
            HashMap *combinaciones = peliculaPair->value;

            HashMapPair *combinacionPair = searchMap(combinaciones, id);
            Pelicula *pelicula = combinacionPair->value;

            funcion->pelicula = pelicula;

            // Se crea el horario que tendrá la pelicula.
            Horario *horario = malloc(sizeof(Horario));
            horario->inicio = atol(inicio);
            horario->final = atol(inicio) + (pelicula->duracion * 60);
            funcion->horario = horario;

            // Se agrega la funcion al treemap de funciones de la película. Key = tiempo POSIX del inicio de la función.
            insertTreeMap(pelicula->funciones, &horario->inicio, funcion);

            // Se busca la sala correspondiente.
            // Se guarda la referencia de la sala en el struct función, y también
            // la referencia de la funcion en el treemap de funciones en el struct sala.
            HashMapPair *salaPair = searchMap(salas, id);
            Sala *sala = salaPair->value;
            funcion->sala = sala;
            insertTreeMap(sala->funciones, &horario->inicio, funcion);
        }
    }
}

void *cargar_peliculas(char *cine_folder, HashMap *salas) {
    HashMap *peliculas = createMap(100);

    char *peliculas_archivo = malloc(strlen(cine_folder) + strlen("peliculas.csv") + 1);
    strcpy(peliculas_archivo, cine_folder);
    strcat(peliculas_archivo, "peliculas.csv");

    FILE *f = fopen(peliculas_archivo, "r");

     if (f == NULL)
        printf("Hubo un error al cargar las ventas al programa.\n");
    else {
        char linea[1024];
        char* nombre;
        char* id;
        char* duracion;
        char* anio;
        char* generos;
        char* precio;
        char* dob_sub;

        // Se consume la primera linea, que trae los nombres de los fields.
        fgets (linea, 1024, f);

        while (fgets (linea, 1024, f) != NULL) {
            nombre = get_csv_field(linea, 0);
            id = get_csv_field(linea, 1);
            duracion = get_csv_field(linea, 2);
            anio = get_csv_field(linea, 3);
            generos = get_csv_field(linea, 4);
            precio = get_csv_field(linea, 5);
            dob_sub = get_csv_field(linea, 6);

            Pelicula *pelicula = malloc(sizeof(Pelicula));
            strcpy(pelicula->nombre, nombre);
            strcpy(pelicula->id, id);
            pelicula->duracion = atoi(duracion);
            pelicula->anio = atoi(anio);
            pelicula->precio = atoi(precio);
            pelicula->dob_sub = atoi(dob_sub);
            pelicula->funciones = createTreeMap(lower_than_int);

            char *generosCopia = malloc(strlen(generos) + 1);
            strcpy(generosCopia, generos);
            int cant_generos = obtener_cant_generos(generosCopia);
            pelicula->generos = obtener_generos(generos, cant_generos);

            HashMapPair *peliculaPair = searchMap(peliculas, pelicula->nombre);

            // Si en el mapa películas se encuentra la key con el nombre de la película, se inserta el struct
            // película en el peliculaPair->value (que es otro HashMap que contiene las combinaciones).
            // Si no se encuentra, se crea el mapa combinaciones desde 0, se agrega la pelicula (key = id)
            // y por último se agrega el mapa combinaciones al mapa de peliculas (key = nombre película).
            if (peliculaPair != NULL) {
                insertMap(peliculaPair->value, pelicula->id, pelicula);
            } else {
                HashMap *combinaciones = createMap(100);
                insertMap(combinaciones, pelicula->id, pelicula);
                insertMap(peliculas, pelicula->nombre, combinaciones);
            }
        }
        
        // Una vez cargadas todas las peliculas, se cargan las funciones para cada unas de estas.
        cargar_funciones(cine_folder, peliculas, salas);
    }
}

void *cargar_cine(HashMap* trabajadores, Trabajador* trabajador) {
    Cine *cine = malloc(sizeof(Cine));

    // Creación del string que contiene la dirección a la carpeta del cine.
    char *cine_folder = calloc(1, strlen("data/") + strlen(trabajador->cine) + 1);
    strcat(cine_folder, "data/");
    strcat(cine_folder, trabajador->cine);
    strcat(cine_folder, "/");
    
    // Se asigna el nombre del cine.
    strcpy(cine->nombre, trabajador->cine);
    
    // Se asigna el total de ingresos del cine.
    cine->total_ventas = cargar_ventas(cine_folder);

    // Se crea el mapa de trabajadores y se cargan los datos.
    cine->trabajadores = cargar_trabajadores(cine_folder, trabajadores, trabajador);

    // Se crea la lista con salas y se cargan los datos.
    cine->salas = cargar_salas(cine_folder);

    // Se crea el mapa películas y se cargan los datos. Falta implementar una parte.
    cine->peliculas =  cargar_peliculas(cine_folder, cine->salas);
}
// 2
void login(HashMap *usuarios, HashMap *cines) {
    bool login_correcto = false;
    char rut[256], password[256];
    printf("-----LOGIN-----\n");
    while (login_correcto == false) {
        printf("Ingresa tu rut:\n");
        fgets(rut, sizeof(rut), stdin);
        strtok(rut, "\n");

        printf("Ingresa tu password:\n");
        fgets(password, sizeof(password), stdin);
        strtok(password, "\n");

        HashMapPair *usuarioPair = searchMap(usuarios, rut);
        
        if (usuarioPair != NULL) {
            Trabajador *trabajador = usuarioPair->value;

            if (strcmp(trabajador->password, password) == 0) {
                login_correcto = true;
                printf("Has iniciado sesion con exito!\n");

                eleccion_menu(usuarios, trabajador);
            }
        }

        if (login_correcto == false)
            printf("Nombre de usuario o password incorrectos, intentalo denuevo.\n");
    }   
}

int getChoice() {
    int validInput = 0;
    char inputChoice[3];

    while(validInput == 0) {
        scanf("%2s", inputChoice);
        fflush(stdin);
    
        if(isdigit(*inputChoice)){
            return atoi(inputChoice);
        } else {
            printf("La opcion que ingresaste no es valida.");
        }
    }
}

void eleccion_menu (HashMap* trabajadores, Trabajador* trabajador)
{
    if(strcmp(trabajador->cargo, "empleado") == 0)
    {
        cargar_cine(trabajadores, trabajador);
        menu_empleado(trabajador);
    }
    if(strcmp(trabajador->cargo, "administrador_local") == 0)
    {
        cargar_cine(trabajadores, trabajador);
        menu_admin_local(trabajador);
    }
    if(strcmp(trabajador->cargo, "administrador_global") == 0)
    {
        //cargar_cines(trabajador->cine);
        menu_admin_global(trabajador);
    }   
}

void menu_empleado(Trabajador* trabajador)
{
    int choice;

    while (choice != 0) {
        printf(" ---------------------------------------------------------------------- \n");
        printf("|                                                                      |\n");
        printf("|         MENU EMPLEADO                                                |\n");
        printf("|                                                                      |\n");
        printf("|         1: Realizar venta                                            |\n");
        printf("|         2: Marcar asistencia                                         |\n");
        printf("|         3: Informe ventas                                            |\n");
        printf("|         4: Horario                                                   |\n");
        printf("|         0: Salir                                                     |\n");
        printf("|                                                                      |\n");
        printf(" ----------------------------------------------------------------------\n");

        choice = getChoice();

        switch (choice) {
            case 1:
                break;
            case 2:

                break;
            case 3:

                break;
            case 4: 

                break;
        }
    }
}

void menu_admin_local(Trabajador* trabajador)
{
    int choice;

    while (choice != 0) {
        printf(" ---------------------------------------------------------------------- \n");
        printf("|                                                                      |\n");
        printf("|         MENU ADMINISTRADOR LOCAL                                     |\n");
        printf("|                                                                      |\n");
        printf("|         1: Resumen general                                           |\n");
        printf("|         2: Modificar cartelera                                       |\n");
        printf("|         3: Informacion del personal                                  |\n");
        printf("|         4: Modificar empleados                                       |\n");
        printf("|         5: Modificar horarios                                        |\n");
        printf("|         6: Modificar salas                                           |\n");
        printf("|         0: Salir                                                     |\n");
        printf("|                                                                      |\n");
        printf(" ----------------------------------------------------------------------\n");

        choice = getChoice();

        switch (choice) {
            case 1:

                break;
            case 2:

                break;
            case 3:

                break;
            case 4: 

                break;
            case 5: 

                break;
            case 6: 

                break;
        }
    }
}

void menu_admin_global (Trabajador* trabajador)
{
    int choice;

    while (choice != 0) {
        printf(" ---------------------------------------------------------------------- \n");
        printf("|                                                                      |\n");
        printf("|         MENU ADMINISTRADOR GLOBAL                                    |\n");
        printf("|                                                                      |\n");
        printf("|         1: Modificar administradores                                 |\n");
        printf("|         2: Modificar cine                                            |\n");
        printf("|         3: Mostrar informacion cines                                 |\n");
        printf("|         4: Modificar precios totales                                 |\n");
        printf("|         5: Generar cupones de descuento                              |\n");
        printf("|         6: Realizar reporte                                          |\n");
        printf("|         0: Salir                                                     |\n");
        printf("|                                                                      |\n");
        printf(" ----------------------------------------------------------------------\n");

        choice = getChoice();

        switch (choice) {
            case 1:

                break;
            case 2:

                break;
            case 3:

                break;
            case 4: 

                break;
            case 5: 

                break;
            case 6: 

                break;
        }
    }
}