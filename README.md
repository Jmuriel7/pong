# Pong

Versión del clásico juego Pong hecho con python y pygame

## Como crear un entorno virtual

Para crear un entorno virtual con el nombre _env_ necesito utilizar
un módulo de python que se llama `venv`.

```
# en windowa 
python -m venv env
```

Evidentemente, podemos usar cualquier nombre para ponerle al entorno
virtual. de aquí en adelante, utilizaré _env_ como nombre de entorno,
pero puedes usar el que quieras.

## Cómo activar el entorno virtual

cuando se crea un entorno virtual, se preparan unos scripts con utilidades
para activar el entorno y un enlace simbólico a la versión de python que 
se va a usar y su versión correspondiente del gestor de paquetes `pip`.

Para activarlo, es necesario ejecutar el script de activación de la
siguente manera:

```
# en windows 
.\env\Scripts\activate

```
Si el entorno se ha activado correctamente veremos en promt del 
terminal el nombre del entorno activo entre paréntesis. En este 
caso veremos `(env)`.

## Gestor de paquetes: pip

- instalar un paquete nuevo: `pip install <nombre-del-paquete>`
- listar los paquetes instalasdos: `pip list`
- Listar paquetes en formato de dependencias: `pip freeze`

## Como desactivar el entorno virtual

Con el entorno virtual activado simplemente basta con 
ejecutar el siguiente comando:

```
deactivate
```

## Cómo eliminar un entorno virtual

Basta con eliminar el directorio que se ha creado al 
inicializar el entorno virtual. Esto elimina el entorno 
y todas las dependencias en él.