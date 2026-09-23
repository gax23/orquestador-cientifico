import os
from groq import Groq
from dotenv import load_dotenv

# Cargamos la clave secreta desde el .env de forma segura
load_dotenv()
cliente_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

class BaseAgent:
    def __init__(self, name, role, system_prompt):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.memory = [{"role": "system", "content": self.system_prompt}]

    def update_memory(self, role, content):
        self.memory.append({"role": role, "content": content})

    def execute_task(self, task):
        print(f"\n⚙️ [{self.name}] Analizando y razonando (Motor Groq)...")
        
        self.update_memory("user", task)
        
        try:
            respuesta = cliente_groq.chat.completions.create(
                messages=self.memory,
                model="openai/gpt-oss-20b",
                temperature=0.2,
                max_tokens=1500  # Límite ampliado para protocolos completos
            )
            
            resultado_ia = respuesta.choices[0].message.content
            self.update_memory("assistant", resultado_ia)
            return resultado_ia
            
        except Exception as e:
            return f"Error en el motor de razonamiento: {str(e)}"