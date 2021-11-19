#include <time.h>
#include <stdbool.h>
#include "headers/list.h"
#include "headers/hashmap.h"
#include "headers/treemap.h"
#include "headers/structs.h"


struct Pelicula 
{
    char nombre[50];
    char id[10];
    int duracion;
    int anio;
    int dob_sub;
    int precio;
    List *generos;
    TreeMap *funciones; // Ordenado por tiempo POSIX de inicio de funcion.
};

struct Sala
{
    char id[3];
    int asientos_totales;
    int estado;
    TreeMap *funciones; // Ordenado por tiempo POSIX de tiempo de funcion.
    //Pelicula pelicula;
};

struct Horario
{
    time_t inicio;
    time_t final;
};

struct Funcion
{
    Horario *horario;
    Sala *sala;
    Pelicula *pelicula;
    int entradas_vendidas;
};

struct Trabajador
{
    char nombre[20];
    char cine[50];
    char rut[10];
    int sueldo;
    char cargo[30]; // empleado, admin, admin_global
    char password[50];
    int ventas;
    TreeMap *horario; // Ordenado por tiempo POSIX de inicio de horario.
    List *asistencia;
};

struct Cine
{
    char nombre[30];
    int total_ventas;
    HashMap *trabajadores; // Key -> RUT
    HashMap *peliculas; // Key -> nombre de pelicula
    HashMap *salas; // Key -> numero de sala
};

struct Asistencia
{
    time_t inicio;
    int asistencia;
};

struct Codigo
{
    bool usado;
    int descuento;
};