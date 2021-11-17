#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "headers/hashmap.h"
#include "headers/login.h"
#include "headers/structs.h"
#include "structs.c"


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

void *crear_trabajador(char *rut, char *password, char *cargo, char *cine) {
    Trabajador *trabajador = malloc(sizeof(Trabajador));

    strcpy(trabajador->rut, rut);
    strcpy(trabajador->password, password);
    strcpy(trabajador->cargo, cargo);
    strcpy(trabajador->cine, cine);

    return trabajador;
}


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

void *cargar_cine(char *nombre_cine) {
    char *cine_folder = malloc(strlen("data/") + strlen(nombre_cine) + 1);
    strcat(cine_folder, "data/");
    strcat(cine_folder, nombre_cine);

    char *cine_archivo = malloc(strlen(cine_folder) + 100);


}

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

                cargar_cine(trabajador->cine);
                // aca se deberían importar las estructuras de cine/empleado y mostrar menu según cargo
                eleccion_menu(trabajador);
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

void eleccion_menu (Trabajador* trabajador)
{
    if(strcmp(trabajador->cargo, "empleado") == 0)
    {
        menu_empleado(trabajador);
    }
    if(strcmp(trabajador->cargo, "administrador_local") == 0)
    {
        menu_admin_local(trabajador);
    }
    if(strcmp(trabajador->cargo, "administrador_global") == 0)
    {
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