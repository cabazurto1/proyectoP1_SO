import subprocess

# Diccionario para almacenar los procesos en ejecución
processes = {}

def run_command(command):
    """Ejecuta un comando del sistema y devuelve su salida."""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar el comando: {e.stderr}"

def show_menu():
    """Muestra el menú de opciones."""
    print("\n===============================")
    print("  Gestor de Herramientas en Ubuntu")
    print("===============================\n")
    print("1. Mostrar 'top' (Visualizar procesos en ejecución)")
    print("2. Mostrar 'vmstat' (Estadísticas de memoria y CPU)")
    print("3. Mostrar 'lsof' (Listar archivos abiertos)")
    print("4. Mostrar 'tcpdump' (Capturar paquetes de red)")
    print("5. Mostrar 'netstat' (Mostrar conexiones de red)")
    print("6. Iniciar tarea")
    print("7. Detener tarea")
    print("8. Mostrar tareas en ejecución")
    print("9. Salir\n")
    print("===============================\n")
    choice = input("Seleccione una opción: ")
    return choice

def main():
    while True:
        choice = show_menu()
        
        if choice == '1':
            print("\nEjecutando 'top'...\n")
            output = run_command('top -b -n 1')
            print(output)
        
        elif choice == '2':
            print("\nEjecutando 'vmstat'...\n")
            output = run_command('vmstat')
            print(output)
        
        elif choice == '3':
            print("\nEjecutando 'lsof'...\n")
            output = run_command('lsof')
            print(output)
        
        elif choice == '4':
            print("\nEjecutando 'tcpdump'...\n")
            output = run_command('tcpdump -c 10')  # Captura solo 10 paquetes para no saturar la salida
            print(output)
        
        elif choice == '5':
            print("\nEjecutando 'netstat'...\n")
            output = run_command('netstat -tuln')
            print(output)
        
        elif choice == '6':
            task_name = input("Ingrese el nombre de la tarea a iniciar: ")
            print(f"Iniciando tarea: {task_name}...")
            # Ejecuta la tarea como un proceso en segundo plano y guarda el PID
            process = subprocess.Popen(['sleep', '60'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            processes[task_name] = process.pid  # Guarda el PID del proceso
    
        elif choice == '7':
            task_name = input("Ingrese el nombre de la tarea a detener: ")
            if task_name in processes:
                print(f"Deteniendo tarea: {task_name}...")
                pid = processes[task_name]
                subprocess.run(['kill', str(pid)])
                del processes[task_name]  # Elimina el proceso del diccionario
            else:
                print(f"No se encontró la tarea: {task_name}")
        
        elif choice == '8':
            print("\nTareas en ejecución:")
            for task, pid in processes.items():
                print(f"- {task} (PID: {pid})")
        
        elif choice == '9':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario. Saliendo...")
