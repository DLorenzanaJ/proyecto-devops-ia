import statistics

class AnalizadorDeRed:
    def __init__(self):
        # Simulamos la lectura de datos de telemetría de equipos de red
        self.dispositivos = [
            {"hostname": "Switch-Core-01", "ping_ms": 12, "perdida_paquetes": 0, "cpu": 45},
            {"hostname": "Router-Borde-02", "ping_ms": 150, "perdida_paquetes": 5, "cpu": 92},
            {"hostname": "AP-Ensamblaje-03", "ping_ms": 45, "perdida_paquetes": 1, "cpu": 60},
            {"hostname": "Switch-Distribucion-04", "ping_ms": 18, "perdida_paquetes": 0, "cpu": 55}
        ]

    def evaluar_estado(self, dispositivo):
        """Evalúa las métricas y determina el estado de salud del equipo."""
        if dispositivo["cpu"] > 90 or dispositivo["perdida_paquetes"] >= 5:
            return "🔴 CRÍTICO - Requiere intervención"
        elif dispositivo["ping_ms"] > 50 or dispositivo["perdida_paquetes"] > 0:
            return "🟡 ADVERTENCIA - Monitorear tráfico"
        else:
            return "🟢 ESTABLE - Operación óptima"

    def generar_informe(self):
        print("="*60)
        print(" SISTEMA DE ASEGURAMIENTO DE CALIDAD DE RED (AI-SQA)")
        print("="*60)
        print(f"{'HOSTNAME':<25} | {'LATENCIA':<10} | {'ESTADO'}")
        print("-" * 60)
        
        latencias = []
        alertas = 0

        for disp in self.dispositivos:
            estado = self.evaluar_estado(disp)
            latencias.append(disp["ping_ms"])
            if "CRÍTICO" in estado or "ADVERTENCIA" in estado:
                alertas += 1
                
            print(f"{disp['hostname']:<25} | {disp['ping_ms']:<7} ms | {estado}")

        print("-" * 60)
        print(" MÉTRICAS GLOBALES DE LA INFRAESTRUCTURA")
        print("-" * 60)
        print(f"Latencia promedio: {statistics.mean(latencias):.2f} ms")
        print(f"Dispositivos analizados: {len(self.dispositivos)}")
        print(f"Alertas detectadas: {alertas}")
        
        # Validación final para el Pipeline DevOps
        if alertas > len(self.dispositivos) / 2:
            print("\n❌ FALLO DE CALIDAD: Demasiadas alertas en la red. Despliegue denegado.")
            exit(1) # Esto hace que el pipeline de GitHub Actions marque error
        else:
            print("\n✅ VALIDACIÓN EXITOSA: La infraestructura es estable. Despliegue autorizado.")

if __name__ == "__main__":
    analizador = AnalizadorDeRed()
    analizador.generar_informe()
