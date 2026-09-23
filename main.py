from agents.research_agent import ResearchAgent
from agents.lab_agent import LabAgent

def main():
    print("🚀 Iniciando Orquestador Científico Multiagente...\n")
    
    researcher = ResearchAgent()
    lab_tech = LabAgent()
    
    # 1. Definimos el objetivo global del experimento
    objetivo_investigacion = "Nuevas aleaciones de titanio para prótesis"
    
    # 2. El investigador analiza el objetivo y genera un protocolo
    protocolo_descubierto = researcher.search_literature(objetivo_investigacion)
    print(f"-> [SALIDA INVESTIGADOR]: {protocolo_descubierto}\n")
    
    # 3. ORQUESTACIÓN: Pasamos el resultado exacto del agente 1 al agente 2
    print("⚙️ [ORQUESTADOR] Transfiriendo protocolo al área de laboratorio...\n")
    resultado_lab = lab_tech.run_experiment(protocolo_descubierto)
    
    # 4. Resultado final
    print(f"-> [SALIDA LABORATORIO]: {resultado_lab}")

if __name__ == "__main__":
    main()