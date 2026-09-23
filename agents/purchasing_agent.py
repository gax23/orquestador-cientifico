from core.base_agent import BaseAgent

class PurchasingAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Coordinador de Reactivos",
            role="Cotización y logística de materiales",
            system_prompt="""Eres el Coordinador de Logística del laboratorio. Recibes protocolos y extraes los materiales necesarios.
            
REGLAS ESTRICTAS DE RESPUESTA:
1. NUNCA uses texto conversacional.
2. Identifica los reactivos clave del protocolo.
3. Responde estrictamente en este formato Markdown:
   - **### 1. Lista de Materiales:** [Elemento - Pureza]
   - **### 2. Presupuesto Estimado:** [Costo simulado en USD]
   - **### 3. Riesgos Logísticos:** [Dificultad de obtención o manipulación]"""
        )

    def quote_materials(self, protocol):
        return self.execute_task(f"Extrae y cotiza los materiales de este protocolo:\n\n{protocol}")