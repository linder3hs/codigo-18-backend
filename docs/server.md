# Configuracion del servidor

Estos son los pasos para poder desplegar nuestro proyecto de `node` en `AWS`

## Crear una instancia en AWS

1. Ingresar a la consola de AWS y seleccionar la opción de `EC2`
2. Seleccionar la opción de `Launch Instance`
3. Seleccionar la imagen de `Ubuntu Server 24.04 LTS`
4. Seleccionar el tipo de instancia que se desea utilizar, es recomendable utilizar una instancia `t2.micro` ya que es gratuita
5. Configurar la instancia, en la sección de `Configure Instance Details` se puede dejar todo por defecto
6. Agregar almacenamiento, se puede dejar por defecto
7. Agregar tags, se puede dejar por defecto
8. Configurar el grupo de seguridad, se debe agregar un grupo de seguridad que permita el acceso a los puertos `22` y `80`
9. Revisar la configuración y lanzar la instancia
10. Crear un par de llaves para poder acceder a la instancia
11. Descargar el archivo `.pem` y guardarlo en un lugar seguro
12. Conectar a la instancia utilizando el comando `ssh -i "nombre-del-archivo.pem" ubuntu@ip-de-la-instancia`
13. Actualizar los paquetes de la instancia con el comando `sudo apt update`
14. Instalar `node` y `npm` con el comando `sudo apt install nodejs npm`
15. Instalar `pm2` en la instancia con el comando `sudo npm install pm2 -g`
16. Clonar el repositorio de `github` en la instancia con el comando `git clone url-del-repositorio`
17. Ingresar a la carpeta del proyecto y ejecutar el comando `npm install`
18. Dentro del proyecto vamos a construir el proyecto con el comando `npm run build`
19. Iniciar el servidor con el comando `pm2 start dist/src/app.js`
20. Esto estara corriendo en el puerto `9000` de la instancia, para poder acceder a la aplicación se debe abrir el puerto `80` en el grupo de seguridad de la instancia, pero para eso necesitamos hacer la configuración de `nginx`

## Instalar y Configurar `nginx`

1. Instalar `nginx` en la instancia con el comando `sudo apt install nginx`
2. Iniciar el servicio de `nginx` con el comando `sudo systemctl start nginx`
3. Configurar `nginx` para que redireccione el tráfico del puerto `80` al puerto `9000` donde se encuentra corriendo nuestra aplicación
4. Vamos a editar el archivo de configuración de `nginx` con el comando `sudo nano /etc/nginx/sites-available/default`
5. Dentro del archivo vamos a agregar la siguiente configuración

```nginx
server {
    listen 80;
    server_name _;
    location / {
        proxy_pass http://localhost:9000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

- Guardar los cambios y reiniciar el servicio de `nginx` con el comando `sudo systemctl restart nginx`
- Ahora se puede acceder a la aplicación en la instancia a través de la dirección de la instancia en el navegador
