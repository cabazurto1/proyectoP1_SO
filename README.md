# Gestor de Herramientas en Ubuntu

Este proyecto consiste en un script Python que actúa como un gestor de herramientas en sistemas Ubuntu. El script permite a los usuarios iniciar, detener y monitorizar procesos, así como utilizar diversas herramientas del sistema para monitorear y administrar el rendimiento y los recursos del sistema.

## Características

- **Mostrar 'top'**: Visualizar procesos en ejecución.
- **Mostrar 'vmstat'**: Estadísticas de memoria y CPU.
- **Mostrar 'lsof'**: Listar archivos abiertos.
- **Mostrar 'tcpdump'**: Capturar paquetes de red.
- **Mostrar 'netstat'**: Mostrar conexiones de red.
- **Iniciar tarea**: Iniciar una nueva tarea como un proceso en segundo plano.
- **Detener tarea**: Detener una tarea en ejecución.
- **Mostrar tareas en ejecución**: Listar todas las tareas en ejecución con sus respectivos PIDs.

## Requisitos

- Ubuntu (o cualquier sistema operativo basado en Linux)
- Python 3

## Instalación

1. Clona el repositorio o descarga el archivo `gestor.py`.
2. Asegúrate de tener Python 3 instalado en tu sistema.
3. Instala las herramientas necesarias si no están ya instaladas:
    ```sh
    sudo apt-get update
    sudo apt-get install net-tools lsof tcpdump
    ```

## Uso

1. Ejecuta el script:
    ```sh
    python gestor.py
    ```

2. Selecciona una opción del menú:
    - Para iniciar una nueva tarea, selecciona la opción 6 e ingresa el nombre de la tarea. Por ejemplo, `sleep 60`.
    - Para detener una tarea, selecciona la opción 7 e ingresa el nombre de la tarea que deseas detener.
    - Para ver las tareas en ejecución, selecciona la opción 8.

## Ejemplo de Flujo

1. Inicia una tarea:
    ```sh
    ===============================
      Gestor de Herramientas en Ubuntu
    ===============================
    
    1. Mostrar 'top' (Visualizar procesos en ejecución)
    2. Mostrar 'vmstat' (Estadísticas de memoria y CPU)
    3. Mostrar 'lsof' (Listar archivos abiertos)
    4. Mostrar 'tcpdump' (Capturar paquetes de red)
    5. Mostrar 'netstat' (Mostrar conexiones de red)
    6. Iniciar tarea
    7. Detener tarea
    8. Mostrar tareas en ejecución
    9. Salir
    
    ===============================
    
    Seleccione una opción: 6
    Ingrese el nombre de la tarea a iniciar: mi_tarea
    Iniciando tarea: mi_tarea...
    ```

2. Ver las tareas en ejecución:
    ```sh
    ===============================
      Gestor de Herramientas en Ubuntu
    ===============================
    
    1. Mostrar 'top' (Visualizar procesos en ejecución)
    2. Mostrar 'vmstat' (Estadísticas de memoria y CPU)
    3. Mostrar 'lsof' (Listar archivos abiertos)
    4. Mostrar 'tcpdump' (Capturar paquetes de red)
    5. Mostrar 'netstat' (Mostrar conexiones de red)
    6. Iniciar tarea
    7. Detener tarea
    8. Mostrar tareas en ejecución
    9. Salir
    
    ===============================
    
    Seleccione una opción: 8
    
    Tareas en ejecución:
    - mi_tarea (PID: 1234)
    ```

3. Detener una tarea:
    ```sh
    ===============================
      Gestor de Herramientas en Ubuntu
    ===============================
    
    1. Mostrar 'top' (Visualizar procesos en ejecución)
    2. Mostrar 'vmstat' (Estadísticas de memoria y CPU)
    3. Mostrar 'lsof' (Listar archivos abiertos)
    4. Mostrar 'tcpdump' (Capturar paquetes de red)
    5. Mostrar 'netstat' (Mostrar conexiones de red)
    6. Iniciar tarea
    7. Detener tarea
    8. Mostrar tareas en ejecución
    9. Salir
    
    ===============================
    
    Seleccione una opción: 7
    Ingrese el nombre de la tarea a detener: mi_tarea
    Deteniendo tarea: mi_tarea...
    ```

## Notas

- Los comandos que se ejecutan deben estar disponibles en el sistema. Por ejemplo, `sleep 60` es un comando simple que duerme el proceso por 60 segundos.
- Asegúrate de tener los permisos necesarios para ejecutar y detener procesos en el sistema.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
