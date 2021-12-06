<h1 align="center">CINE4U</h1>
<p align="center">Proyecto de aplicación destinada a empresas de cine</p>

## Cómo compilar y ejecutar la aplicación

En el repositorio debe descargar el ZIP, extraerlo en su computador, apretar el ejecutable main.exe y listo!

_Requisitos: Tener instalado Visual Studio Code para el ingreso de datos tipo Tiempo Unix en archivos.csv_

**Cuentas para probar el programa**

- Empleado: RUT: 20603557 | Contraseña: cami2000

- Administrador local: RUT: 17324511 | Contraseña: vgs2021 

- Administrador global: RUT: 16324522 | Contraseña: glo2021
## Manejo del tiempo en la aplicación (Tiempo Unix)

Para ingresar los datos referentes al tiempo, debe hacer uso de la página https://www.unixtimestamp.com/, en donde debe utilizar la opción de conversión y extraer el número entero del campo llamado "Unix Timestamp" y copiar ese número en los archivos que lo necesiten.

Se recomienda hacer el ingreso de datos de tipo Tiempo Unix en los archivos a través de Visual Studio Code para que sean ingresados como tipo texto, por Excel se podrían tomar como tipo número pudiendo ocasionar problemas haciendo que el programa se caiga. 
## Organización de carpetas (Datos)

El usuario solo debe modificar la carpeta **data** con los datos respectivos de su cine. 

- Dentro de la carpeta **data** deben existir: Subcarpetas con el nombre de cada local (en este caso el nombre del lugar) y 2 archivos csv, uno llamado **credenciales** y otro llamado **cupones**. 
    - En el archivo **credenciales** deben estar los datos para iniciar sesión: rut, contraseña, cargo y nombre del local. 
    
    - En el archivo **cupones** deben estar los datos de los cupones ya existentes: código del cupón, porcentaje que aplica (0-100) y un número que indica si ha sido utilizado (1) o no (0).

- Dentro de cada subcarpeta de local deben existir: Subcarpeta llamada **empleados**y 5 archivos csv: **empleados**, **funciones**, **peliculas**, **salas** y **ventas**. 
    - En el archivo **empleados** deben estar los datos de los empleados del local: nombre (de la forma nombre_apellido), rut (sin digito verificador ni puntos), sueldo (sin puntos) y la cantidad de ventas que ya ha hecho. 
    
    - En el archivo **funciones** deben estar los datos de las funciones de las películas: hora de inicio (en Tiempo Unix), número de la sala, ID de la película y cantidad de entradas vendidas. 
    
    - En el archivo **peliculas** deben estar los datos de las películas: nombre, ID, duración (en minutos), año, géneros (si es más de un género, en comillas y separados por comas), precio y un número que indica si está doblada (0) o subtitulada (1). 
    
    - En el archivo **salas** deben estar los datos de las salas del local: número de la sala, su capacidad (cantidad de personas que permite) y un número que indica si está habilitada (1) o deshabilitada (0). 
    
    - En el archivo **ventas** estarán los datos de las ventas realizadas por los empleados: rut del empleado, fecha en la que la realizó (en Tiempo Unix) y el precio de la venta. Luego de usar la aplicación, este archivo se habrá llenado con los datos correspondientes.

- Dentro de la subcarpeta **empleados** deben existir: Subcarpetas con los ruts de los empleados. Dentro de cada uno deben contener 2 archivos csv: **asistencia** y **horarios**.
    - En el archivo **asistencia** deben estar los datos del inicio de su horario (en Tiempo Unix) y el número (0) para que el programa pueda marcar asistencia. 
    
    - En el archivo **horarios** deben estar los datos de inicio y final de las jornadas de trabajo (en Tiempo Unix)
## Aspectos a considerar para un correcto funcionamiento 


- Para agregar los datos de ingreso, salida y asistencia de un nuevo empleado o un empleado existente, es necesario hacerlo a través de Visual Studio Code, ya que es muy probable que Excel cambie el formato de los datos ingresados y no reconozca todos los campos que se ingresan.

- Para que la función **Marcar asistencia** se active de forma correcta, se debe tener el cuidado de tener un horario que esté dentro del rango de la hora actual, es decir, tiene que segunda coincidir el día que le corresponde al empleado y además, debe marcar su asistencia dentro del rango de trabajo. Por ejemplo, si el empleado debe trabajar el 07/12/2021 y su hora de inicio es a las 08:00 y su hora de salida es a las 18:00, debe asegurarse de marcar la asistencia dentro de ese intervalo, sino el programa arrojará un error. 

- Si bien el programa crea un empleado nuevo, es necesario acceder a sus archivos horarios.csv y asistencia.csv desde fuera de la aplicación para asignarle sus horarios de ingreso y salida (en Tiempo Unix).

- La capacidad máxima de asientos por sala está delimitada por el campo capacidad del archivo salas.csv, por lo que al llegar al máximo de entradas vendidas de esa sala, no será posible realizar otra venta en esa misma sala.

- Si se llegase a borrar una subcarpeta de empleado y no se borran los datos de ingreso de este ni del archivo empleados.csv asociado al cine, el programa arrojará error al momento de querer ingresar, ya que no puede encontrar la dirección de sus documentos al momento de cargar los archivos.

- Para la opción **Modificar precios peliculas** del administrador_global, se debe seleccionar con el cursor del ratón la pelicula a la cual desea modificar su precio, escribir en el recuadro el nuevo precio y luego presionar modificar. Si se arrepintió de modificar algún precio, solo presione **Confirmar**.

- Para iniciar sesión con otra cuenta, es necesario cerrar y volver a ejecutar el programa.

- La función **Mostrar horario** del empleado muestra el horario correspondiente a la semana actual.
