#include <time.h>
#include <stdbool.h>
#include "headers/list.h"
#include "headers/hashmap.h"
#include "headers/treemap.h"
#include "headers/structs.h"


struct Pelicula 
{
    char nombre[50];
    int anio;
    int stock;
    List *generos;
    HashMap *funciones;
    int precio;
    char formato[4];
    int dob_sub;
};

struct Sala
{
    int numero;
    int asientos_totales;
    int estado;
    Pelicula pelicula;
};

struct Horario
{
    time_t inicio;
    time_t final;
};

struct Funcion
{
    Horario horario;
    Sala sala;
    Pelicula pelicula;
    int entradas_vendidas;
};

struct Trabajador
{
    char nombre[20];
    char cine[50];
    char rut[10];
    int sueldo;
    char cargo[30]; // empleado, admin, admin_global
    Horario horario;
    char password[50];
    int ventas;
    List *asistencia;
};

struct Cine
{
    char nombre[30];
    int total_ventas;
    HashMap *trabajadores;
    HashMap *peliculas;
    List *salas;
};

struct Codigo
{
    bool usado;
    int descuento;
};