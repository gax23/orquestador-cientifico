import os
import subprocess
from datetime import datetime
from agents.research_agent import ResearchAgent
from agents.lab_agent import LabAgent
from core.equipment_interface import LabEquipmentSDK  # Importamos el SDK de hardware
from agents.purchasing_agent import PurchasingAgent

def main():
    print("🚀 Iniciando Orquestador Científico Multiagente...\n")
    
    researcher = ResearchAgent()
    lab_tech = LabAgent()
    purchaser = PurchasingAgent()
    objetivo_investigacion = "starch bioplastic production"
    
    # 1. Diseño y Evaluación
    protocolo_descubierto = researcher.search_literature(objetivo_investigacion)

    print("\n📦 [ORQUESTADOR] Cotizando reactivos y materiales...\n")
    cotizacion = purchaser.quote_materials(protocolo_descubierto)
    # -----------------------------------
    
    print("\n⚙️ [ORQUESTADOR] Transfiriendo protocolo al área de laboratorio...\n")
    resultado_laboratorio = lab_tech.run_experiment(protocolo_descubierto)
    
    # 2. Ejecución Física (SDK)
    print("\n⚡ [ORQUESTADOR] Procesando comandos de hardware...")
    resultado_hardware = ""
    # Simulamos una lectura rápida del veredicto del LabAgent
    if "Rechazado" not in resultado_laboratorio:
        LabEquipmentSDK.set_temperature("Horno_Arco_Titanio", 2000)
        lectura = LabEquipmentSDK.run_spectrometer("Ti_Aleacion_001")
        resultado_hardware = f"**Ejecución de Hardware:** Completada exitosamente.\n**Lectura del Espectrómetro:** {lectura}"
    else:
        resultado_hardware = "**Ejecución de Hardware:** Abortada por fallas de viabilidad en el diseño inicial."
        print("⚠️ Protocolo rechazado por el Técnico. Hardware no iniciado.")

    # 3. Almacenamiento Estructurado de Registros
    print("\n💾 [ORQUESTADOR] Compilando y guardando registro experimental...")
    os.makedirs("registros_experimentales", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"registros_experimentales/experimento_{timestamp}.md"
    
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(f"# Registro Experimental: {objetivo_investigacion}\n\n")
        archivo.write(f"## 1. Diseño y Protocolo (Investigador Jefe)\n{protocolo_descubierto}\n\n")
        archivo.write("---\n\n")
        archivo.write(f"## 1.5 Presupuesto y Reactivos (Logística)\n{cotizacion}\n\n")
        archivo.write("---\n\n")
        archivo.write(f"## 2. Viabilidad y Simulación (Técnico de Laboratorio)\n{resultado_laboratorio}\n\n")
        archivo.write("---\n\n")
        archivo.write(f"## 3. Resultados de Equipos (SDK)\n{resultado_hardware}\n")
        
    print(f"✅ ¡Éxito! Registro guardado localmente en: {nombre_archivo}")

    # 4. Sincronización automática con GitHub
    print("\n☁️ [ORQUESTADOR] Subiendo registro a GitHub...")
    try:
        subprocess.run(["git", "add", "registros_experimentales/"], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", f"Automated log: Agrega registro experimental {timestamp}"], check=True, capture_output=True)
        subprocess.run(["git", "push"], check=True, capture_output=True)
        print("✅ ¡Registro subido exitosamente a tu repositorio en la nube!")
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode('utf-8').strip() if e.stderr else str(e)
        print(f"⚠️ Error al subir a GitHub. Detalle: {error_msg}")

if __name__ == "__main__":
    main()