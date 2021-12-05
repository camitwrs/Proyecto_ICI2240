# Proyecto: CINE4U

## Cómo compilar y ejecutar la aplicacion:


**Aspectos a considerar para el funcionamiento correcto de la aplicación:**


* Los archivos de asistencia.csv y horarios.csv de cada empleado se guarda en una subcarpeta dentro de la carpeta del cine que le corresponde a cada uno. La carpeta que contiene a los empleados asociados tiene el nombre del cine, el cual a la vez es el nombre del lugar donde se encuentra (por ejemplo, el nombre de una ciudad). 

Para que la función "Marcar asistencia" se active de forma correcta, se debe tener el cuidado de tener un horario que esté dentro del rango de la hora actual, es decir, tiene que coincidir el día que le corresponde al empleado y además, debe marcar su asistencia dentro del rango de trabajo. Por ejemplo, si el empleado debe trabajar el 07/12/2021 y su hora de inicio es a las 08:00 y su hora de salida es a las 18:00, debe asegurarse de marcar la asistencia dentro de ese intervalo, sino el programa arrojará un error. También tener en consideración que para ingresar los datos en la carpeta data, específicamente los datos de horarios.csv y asistencia.csv, debe hacer uso de la página https://www.unixtimestamp.com/, en donde debe utilizar la segunda opción de conversión y extraer el número entero del campo llamado "Unix Timestamp" y copiar ese número en el archivo horarios.csv dentro de las carpetas de los empleados (separadas por rut), posicionando el horario de inicio al principio y el horario de salida al final. Además para ingresar datos en asistencia.csv, debe ingresar el horario inicial y poner un 0 al lado separado por una coma, quedando de esta forma: 1638741600,0