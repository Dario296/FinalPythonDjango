# FinalPythonDjango

## Colaboradores:

- Darío Rodriguez - [Github profile](https://github.com/Dario296)

- Luis Tecchio - [Github profile](https://github.com/atreus23)

Para levantar el proyecto ejecutar el siguiente comando en la terminal:

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

## El proyecto dispone de una app llamada Blog donde se encuentra las siguientes rutas:

GET /: inicio muestra la pagina principal de la app.

GET nosotros/: muestra la pagina sobre nosotros de la app. 

GET blog/: muestra la pagina blog de la app donde tiene un listado de posteos y un buscador de los mismos y un botón para redireccionar a la pagina para crear un nuevo post.

GET blog/ver_mas/: te permite ver la información del posteo.

### En las siguientes rutas se requiere el registro a la pagina:

GET blog/crear/: muestra el formulario para crear un post. 

POST blog/crear/: crea un nuevo posteo con los datos enviados por POST.

POST blog/modificar/: te permite modificar los datos ingresados en el posteo siempre que seas el usuario que genero el posteo.

POST blog/eliminar/: te permite eliminar el posteo siempre que seas el usuario que genero el posteo.

## También contiene la app Usuario para poder registrarse e iniciar sesión donde se encuentran las siguientes rutas:

GET registrarse/: te muestra el formulario de registro.

POST registrarse/: te permite guardar los datos del registro.

### En las siguientes rutas se requiere el registro a la pagina:

GET ingresar/: te muestra el formulario de ingreso.

POST ingresar/: te permite ingresar si estas registrado.

POST salir/: te permite salir de la sesión.

GET salir/: te muestra un mensaje de despedida.

GET perfil/: muestra los datos del usuario.

GET perfil/editar/: te muestra el formulario de editar los datos del registro.

POST perfil/editar/: te permite guardar los datos editados.

GET perfil/editar_password/: te muestra el formulario para editar la contraseña.

POST perfil/editar_password/: te permite guardar la contraseña nueva.

## La ultima app es la de mensajes donde te permite enviar mensajes entre usuarios registrados, se encuentran las siguientes rutas:

### En las siguientes rutas se requiere el registro a la pagina:

GET lista_usuario/: te muestra la lista de usuarios registrados y un botón para poder ver los perfil.

GET lista_usuario/id?: te muestra el detalle del usuario seleccionado.

GET mensajes/: muestra la lista de todas las conversaciones.

GET hilo/id?: muestra la conversación con la persona seleccionada y el formulario para poder enviar un mensaje.

POST hilo/id?/enviar: envía un mensaje al usuario.

GET hilo/iniciar_hilo/username?/: abre el formulario para poder enviar el mensaje por primera vez a la persona.