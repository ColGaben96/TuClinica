# Tu Clinica <h5>Versión Python</h5>

## Descripción
El proyecto funciona con un servidor en Azure que se despliega utlizando el concepto de despliegue contínuo, permitiendo así una manera de ejecutar los proyectos más fácil. <br>
Para la instalación del proyecto no es necesario contar con un servidor de Django. Sin embargo, si así se requiere en la pestaña de Release podrá encontrar un archivo .zip donde podrá utilizar este proyecto a nivel de lógica de negocio y presentación. En cuánto a la persistencia esta no será posible por las configuraciones de seguridad que Azure provee.
## Requisitos Mínimos
### Sistema Operativo
<ul>
<li>Windows 10</li>
<li>Mac OS Big Sur</li>
<li>Ubuntu 18.04 o similares</li>
</ul>

### Hardware
<ul>
<li>1GB de espacio libre para descompresión y ejecución</li>
<li>4GB de RAM libres para la ejecución</li>
<li>Python 3</li>
<li>Conexión a internet</li>
</ul>

## ¿Cómo ejecutar?
### Si se usa un servidor físico
Se debe contar con al menos los componentes listados en requerimientos mínimos. <br>
<ol>
<li>Ubique el archivo .jar en una carpeta que usted pueda tener acceso y control en un futuro</li>
<li>Ejecute en la terminal deseada la siguiente lista de comandos uno por uno:
<pre>cd /..
cd ruta_carpeta_python
python manage.py runserver puerto</pre>
</li>
<li>Espere de 15 a 30 segundos mientras el sistema inicializa y conecta a la base de datos. <br>
Si esta no puede conectarse se generará un error. Si desea utilizarla escriba a <a href="mailto:gblancol@unbosque.edu.co">gblancol@unbosque.edu.co</a> con el asunto TuClinica-AccesoBD y en el cuerpo del correo su dirección IPv4.</li>
</ol>

### Si se usa Azure
Solamente debe subir cambios a la rama master. El desplegará automáticamente en la siguiente url: <pre> https://tuclinica.azurewebsites.net </pre>
## Autores
### Gabriel Blanco
<pre>gblancol@unbosque.edu.co</pre>
### Estefania Galindo
<pre>wgalindo@unbosque.edu.co</pre>
