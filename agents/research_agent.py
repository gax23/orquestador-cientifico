import urllib.request
import xml.etree.ElementTree as ET
from core.base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Investigador Jefe",
            role="Diseño de protocolos y revisión de literatura",
            system_prompt="""Eres el Investigador Jefe de un laboratorio de ciencia de materiales. 
            
REGLAS ESTRICTAS DE GENERACIÓN DE REPORTES:
1. Tu objetivo es diseñar protocolos experimentales basándote OBLIGATORIAMENTE en la literatura científica proporcionada.
2. NUNCA uses saludos, introducciones ni texto de relleno.
3. DEBES estructurar tu respuesta en formato Markdown usando estas secciones exactas:
   - **### 1. Marco Teórico:** Breve justificación citando los conceptos de los papers proporcionados.
   - **### 2. Reactivos y Materiales:** Lista con pureza y proporciones.
   - **### 3. Procedimiento Paso a Paso:** Pasos numerados exactos.
   - **### 4. Riesgos Previstos:** Posibles fallas operativas."""
        )

    def fetch_arxiv_papers(self, query, max_results=3):
        # Traducimos espacios para la URL de la API
        search_query = query.replace(" ", "+")
        url = f'http://export.arxiv.org/api/query?search_query=all:{search_query}&start=0&max_results={max_results}'
        
        try:
            print(f"📚 [{self.name}] Buscando literatura científica real en arXiv sobre: '{query}'...")
            # Solicitud HTTP a arXiv
            response = urllib.request.urlopen(url)
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            ns = {'atom': 'http://www.w3.org/2005/Atom'}
            papers = []
            
            # Extraemos los títulos y resúmenes de los papers encontrados
            for entry in root.findall('atom:entry', ns):
                title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
                papers.append(f"Título: {title}\nResumen: {summary}")
                
            return "\n\n".join(papers) if papers else "No se encontraron papers específicos, utiliza tus conocimientos base."
            
        except Exception as e:
            return f"Error consultando base de datos: {e}"

    def search_literature(self, topic):
        # 1. El agente extrae los papers reales de la web
        literatura_real = self.fetch_arxiv_papers(topic)
        
        # 2. Inyectamos la literatura en el prompt para el modelo de Groq
        prompt_enriquecido = f"Diseña un protocolo completo y estructurado para: {topic}.\n\nBASA TU DISEÑO EN ESTOS PAPERS RECIENTES:\n{literatura_real}"
        
        return self.execute_task(prompt_enriquecido)