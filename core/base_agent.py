class BaseAgent:
    def __init__(self, name, role, system_prompt):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.memory = [{"role": "system", "content": self.system_prompt}]

    def update_memory(self, role, content):
        """Almacena el historial de la conversación para mantener el contexto."""
        self.memory.append({"role": role, "content": content})

    def execute_task(self, task):
        """
        Método central. Aquí simulamos el procesamiento inicial.
        Más adelante conectaremos esto a un LLM real (ej. DeepSeek o llama local).
        """
        print(f"\n⚙️ [{self.name} | {self.role}] Iniciando tarea...")
        self.update_memory("user", task)
        
        # Placeholder de la respuesta del agente
        response = f"Evaluando viabilidad de la tarea: '{task}'. Pendiente de motor de inferencia."
        self.update_memory("assistant", response)
        
        return response