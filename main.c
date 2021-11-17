#include <stdio.h>
#include "headers/login.h"
#include "headers/structs.h"
#include "headers/hashmap.h"

int main() {
    HashMap* trabajadores = cargar_credenciales();
    HashMap* cines = createMap(100);

    login(trabajadores, cines);
}