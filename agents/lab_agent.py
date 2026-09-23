from core.base_agent import BaseAgent

class LabAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Técnico de Laboratorio",
            role="Control de equipos y simulación",
            system_prompt="Ejecutas protocolos en el laboratorio y reportas resultados."
        )

    def run_experiment(self, protocol):
        print(f"\n🧪 [{self.name}] Configurando equipos para: '{protocol}'...")
        return f"Experimento '{protocol}' completado. Rendimiento: 85%."