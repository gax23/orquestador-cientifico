import time
import random

class LabEquipmentSDK:
    """Capa de abstracción (SDK) para enviar comandos a equipos físicos del laboratorio."""
    
    @staticmethod
    def set_temperature(device_id, target_temp):
        print(f"📡 [SDK_HARDWARE] Conectando a {device_id}...")
        print(f"🌡️ [SDK_HARDWARE] Calibrando temperatura a {target_temp}°C...")
        time.sleep(1) # Simulando latencia de red del equipo
        return True
        
    @staticmethod
    def run_spectrometer(sample_id):
        print(f"🔬 [SDK_HARDWARE] Iniciando análisis espectrométrico para muestra {sample_id}...")
        time.sleep(1.5)
        # Simulamos resultados posibles de la máquina
        return random.choice(["SUCCESS: Pureza 99.8%", "WARNING: Contaminación detectada", "ERROR: Falla de calibración"])