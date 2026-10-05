# validador_servidor.py

def revisar_estado_servidor(ping_ms, uso_cpu):
    """
    Evalúa si un servidor está sano o necesita reinicio.
    """
    if ping_ms > 100 or uso_cpu > 90:
        return "CRÍTICO: Aislar servidor"
    elif ping_ms > 50 and uso_cpu > 70:
        return "ADVERTENCIA: Monitorear de cerca"
    else:
        return "ESTABLE: Operación normal"

if __name__ == "__main__":
    print("Iniciando validación automatizada DevOps...")
    estado_1 = revisar_estado_servidor(20, 45)
    estado_2 = revisar_estado_servidor(120, 95)
    
    print(f"Servidor Web: {estado_1}")
    print(f"Servidor Base de Datos: {estado_2}")
    print("Validación completada con éxito.")
