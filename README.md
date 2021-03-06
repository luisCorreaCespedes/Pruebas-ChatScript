# ChatBot Encuesta de Relevamiento de Información

_Bot comunicacional de Encuesta de Relevamiento de Información de un producto/servicio de una empresa para WhatsApp desarrollado en ChatScript_

Rellenar con más info ya sea inbound y outbound.

## Instalación 🔧

Crea una carpeta en alguna parte de tu computador (generalmente suele nombrarse la nueva carpeta como ChatScript, pero puedes asignarle el nombre que estimes conveniente), y clona este repositorio en la nueva carpeta creada con el siguiente comando:

```bash
git clone https://github.com/luisCorreaCespedes/Pruebas-ChatScript
```

## Modo Local (para desarrollo y testeo) ⚙️

En el directorio principal donde está instalado ChatScript, ve a la carpeta BINARIES:

```bash
cd BINARIES
```

Y ejecuta el motor de ChatScript:

### Windows
```bash
ChatScript
```

### Linux
```bash
./LinuxChatScript64 local
```
_NOTA_ - Para establecer el ejecutable en Linux: `chmod a+x ./LinuxChatScript64`

Esto cargará el motor de ChatScript y seguidamente te preguntará tu nombre de usuario. Puedes ingresar lo que quieras.
En este momento estarás hablando con el Bot por defecto llamado `Harry`.

## Modo Servidor (para producción)

En el directorio principal donde está instalado ChatScript, ve a la carpeta BINARIES y ejecuta el motor ChatScript como Servidor:

### Ejecutar el Servidor en Windows
```bash
ChatScript port=1024
```
### Ejecutar el Servidor en Linux
```bash
./LinuxChatScript64
```

Esto hará que el motor de ChatScript se cargue como Servidor. 

Para probar la comunicación Cliente-Servidor, necesitas un Cliente.
Para generar un Cliente, ejecuta una nueva ventana de comandos, ve a la carpeta BINARIES y ejecuta el siguiente comando:

### Ejeutar un Cliente (testeo) en Windows
```bash
ChatScript client=localhost:1024 
```

### Ejeutar un Cliente (testeo) en Linux
```bash
./LinuxChatScript64 client=localhost:1024
```

Esto hará que el motor de ChatScript se cargue como Cliente y puedas comunicarte con el Servidor. 


## Cómo construir un Bot

Ejecuta ChatScript en Modo Local. Desde la línea de comando escribe:

### INBOUND
```
:build inbound
```

### OUTBOUND
```
:build outbound
```

Y luego escribe:

```
:reset
```