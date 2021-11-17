#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "headers/hashmap.h"
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

void login(HashMap *usuarios) {
    bool login_correcto = false;
    char rut[256], password[256];

    while (login_correcto == false) {
        printf("Ingresa tu rut\n");
        fgets(rut, sizeof(rut), stdin);
        strtok(rut, "\n");

        printf("Ingresa tu contrasenia\n");
        fgets(password, sizeof(password), stdin);
        strtok(password, "\n");

        HashMapPair *usuarioPair = searchMap(usuarios, rut);
        
        if (usuarioPair != NULL) {
            Trabajador *trabajador = usuarioPair->value;

            if (strcmp(trabajador->password, password) == 0) {
                login_correcto = true;
                printf("Has iniciado sesion con exito\n");
                // aca se deberían importar las estructuras de cine/empleado y mostrar menu según cargo
            }
        }

        if (login_correcto == false)
            printf("Nombre de usuario o contrasenia incorrectos\n");
    }   
}