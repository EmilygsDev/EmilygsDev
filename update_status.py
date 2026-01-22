import re
import datetime

def update_readme():
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Personalized messages
    status_en = f"🛡️ **Phase:** Rust microservices optimization.\n\n> *Last sync: {timestamp} UTC*"
    status_es = f"🛡️ **Fase:** Optimización de microservicios en Rust.\n\n> *Sincronización: {timestamp} UTC*"
      
    # Update English version - Buscando las etiquetas específicas en el README
    pattern_en = r"(`)(.*?)(`)"
    content = re.sub(pattern_en, f"\\1\n{status_en}\n\\3", content, flags=re.DOTALL)

    # Update Spanish version - Buscando las etiquetas específicas en el README
    pattern_es = r"(`)(.*?)(`)"
    content = re.sub(pattern_es, f"\\1\n{status_es}\n\\3", content, flags=re.DOTALL)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
