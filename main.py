from agents.research_agent import ResearchAgent

def main():
    print("🚀 Iniciando Orquestador Científico Multiagente...")
    
    # Instanciamos al agente investigador
    researcher = ResearchAgent()
    
    # Probamos el método heredado de la clase base
    tarea_inicial = researcher.execute_task("Evaluar viabilidad de síntesis de un nuevo polímero")
    print(f"Resultado Tarea: {tarea_inicial}")
    
    # Probamos el método específico del investigador
    literatura = researcher.search_literature("Polímeros biodegradables de alta resistencia")
    print(f"Resultado Búsqueda: {literatura}")

if __name__ == "__main__":
    main()