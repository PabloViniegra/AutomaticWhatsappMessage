# AutomaticWhatsappMessage
Pequeño Script de Python para enviar mensajes de Whatsapp.

# Cómo usarlo

Debe ejecutarlo desde una terminal. Puede abrir en una en
Windows pulsando **Windows + R** y escribiendo `cmd`.
Ubíquese en el script para poder ejecutarlo y escriba la
siguiente intrucción:

~~~
python3 messsage_whatsapp.py [número de teléfono] [mensaje a enviar] [número de repeticiones del mensaje]
~~~

### Consideraciones
1. El primer argumento [número de teléfono] debe ser escrito con su prefijo telefónico.
Esto es, si por ejemplo quiere enviar el mensaje a un número en españa llevara '+34' delante.
Puede escribir el número con espacios, el script lo gestionará, pero el formato es deseable es
`+34916xxxxxx`. Si el teléfono ocupa más de 12 carácteres saltará un error.

2. El segundo argumento es una cadena. Puede escribirlo sin comas si es solo una palabra.
Por ejemplo
~~~
python3 message_whatsapp.py +34916xxxxxx Hola 1
~~~
Enviaremos una vez el mensaje 'Hola' al número indicado.
Si desea enviar una cadena más larga con espacios entre ellos, la sintaxis cambia.
Debe rodearlo entre comillas para que el intérprete de Python no lo entienda como argumentos.
Por ejemplo
~~~
python3 message_whatsapp.py +34916xxxxxx "Hola, ¿Qué tal?" 1
~~~
Enviaremos una vez el mensaje 'Hola, ¿Qué tal?' al número indicado.

3. El tercer argumento debe ser un número obligatoriamente y especifica el número de veces
que el mensaje será lanzado. Si no es un número el script devolverá un error.

4. Los tres argumentos deben estar en la llamada del script, de otra forma, el script
devolverá un error escribiendo por pantalla cómo debe llamar al script.
