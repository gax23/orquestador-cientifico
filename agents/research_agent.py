from core.base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Investigador Jefe",
            role="Búsqueda y síntesis de literatura científica",
            system_prompt="Eres un agente especializado en extraer metodologías de artículos científicos. Tu objetivo es encontrar protocolos viables para los experimentos solicitados."
        )

    def search_literature(self, topic):
        """Simula la búsqueda de papers en bases de datos (ej. arXiv, PubMed)."""
        print(f"\n🔍 [{self.name}] Buscando literatura sobre: '{topic}'...")
        
        # Más adelante, aquí conectaremos una API real.
        simulated_results = f"Se encontraron 3 papers relevantes sobre {topic}. Extrayendo metodologías clave..."
        
        # Guardamos el hallazgo en la memoria del agente
        self.update_memory("assistant", simulated_results)
        
        return simulated_results