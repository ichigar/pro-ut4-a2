# UT4-A2. Recetas con GUI
## Características generales de la actividad

* Tipo: Investigación guiada
* Temporalización: 240' 
* Agrupamientos: 1 o 2 alumnos
* Producto: archivos con el código del programa solicitado

## Elementos curriculares:

**Resulatado de aprendizaje**:

**5.** Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases.

**Criterios de evaluación**:

**f**) Se han utilizado las herramientas del entorno de desarrollo para crear interfaces gráficos de usuario simples.
**g**) Se han programado controladores de eventos.
**h**) Se han escrito programas que utilicen interfaces gráficos para la entrada y salida de información.

**Contenidos**:

* Interfaces.
* Concepto de evento.
* Creación de controladores de eventos.

## Práctica

Vamos a hacer un programa gráfico que nos permita gestionar nuestra base de datos de recetas que tenemos almacenadas en un fichero de texto.

El código que nos permite gestionar en el fichero las recetas se basará en el que se creó en la prueba práctica de la actividad anterior.

Tenemos una versión con la mayoría de funciones que vamos a necesitar eh Github, en el [siguiente enlace](https://github.com/ichigar/pro/blob/main/ut3/recursos/ut3-ae1/recetas_v1.py).

Tendremos que elaborar una interfaz gráfica para dicha aplicación con las siguientes características:

* El programa tendrá una ventana principal en la que se mostrarán las diferentes operaciones que podremos realizar sobre nuestras recetas.
* Cada vez que seleccionemos una opción se abrirá una nueva ventana en la que se mostrará el resultado o si necesitamos parámetros se mostrará un formulario para que introduzcamos los parámetros.
* Si al introducir opciones se genera algún error mostrar una ventana de alerta con la información del mismo. Usar el componente de tkinter `messagebox`
* Las opciones serán:
    * Mostrar recetas (nombre de todas las recetas almacenadas)
    * Mostrar receta.
        * Nos pide el nombre de la receta
        * Si existe se muestra la información de la misma.
        * Si no existe se muestra un mensaje indicándolo. 
    * Mostrar recetas ingredientes
        * Introducimos hasta 4 ingredientes y se muestran todas la recetas que contienen todos los ingredientes introducidos
    * Nueva receta
        * Se nos pide el nombre, la duración y hasta 6 ingredientes y se añade la nueva receta al fichero
    * Añadir ingrediente
        * Se nos pregunta el nombre de la receta y el nuevo ingrediente y en caso de existir la receta y no tener dicho ingrediente se añade a la misma en el fichero
    * Eliminar receta
        * Se nos pregunta el nombre de la receta y si existe se elimina del fichero.

Para elaborar la interfaz gráfica con **tkinter** nos podemos puedes partir del [siguiente código](https://github.com/ichigar/pro/tree/main/ut4/recursos/ut4-a2/recetas) para elaborar la interfaz de nuestra aplicación

## Producto

Archivos del proyecto comprimidos en un zip.

