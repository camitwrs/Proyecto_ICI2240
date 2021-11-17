#include "hashmap.h"
#include "structs.h"

void *cargar_credenciales();

void login(HashMap *trabajadores, HashMap *cines);

void eleccion_menu(Trabajador* trabajador);

void menu_empleado(Trabajador* trabajador);

void menu_admin_local(Trabajador* trabajador);

void menu_admin_global(Trabajador* trabajador);