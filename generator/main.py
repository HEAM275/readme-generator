from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import PlainTextResponse,HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional
import json


app = FastAPI()

app = FastAPI(
    title="README.md Generator API",
    description="API para generar archivos README.md en Markdown a partir de datos estructurados.",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

class ReadmeData(BaseModel):
    title: str
    description: Optional[str] = None
    features: Optional[List[str]] = None
    installation: Optional[List[str]] = None
    usage_example: Optional[str] = None
    endpoints: Optional[List[dict]] = None  # [{"method": "GET", "path": "/api", "description": "..."}]
    configuration: Optional[str] = None
    tests: Optional[str] = None
    deployment: Optional[str] = None
    contributing: Optional[str] = None
    license: Optional[str] = None
    acknowledgements: Optional[str] = None
    support: Optional[str] = None
    include_badges: Optional[bool] = False

def generate_markdown(data: ReadmeData) -> str:
    md = []

    # Título
    md.append(f"# {data.title}")
    md.append("")

    # Badges (solo licencia por ahora)
    if data.include_badges and data.license:
        safe_license = data.license.replace(" ", "%20")
        license_url = ""
        if data.license.upper() == "MIT":
            license_url = "https://opensource.org/licenses/MIT"
        elif data.license.upper() == "APACHE 2.0":
            license_url = "https://opensource.org/licenses/Apache-2.0"
        else:
            license_url = "https://opensource.org/licenses"

        badge = f"[![License](https://img.shields.io/badge/License-{safe_license}-blue.svg)]({license_url})"
        md.append(badge)
        md.append("")

    # Descripción
    if data.description:
        md.append(data.description)
        md.append("")

    # Características
    if data.features:
        md.append("## ✨ Características")
        md.append("")
        for feat in data.features:
            md.append(f"- {feat}")
        md.append("")

    # Instalación
    if data.installation:
        md.append("## 🚀 Instalación")
        md.append("")
        md.append("```bash")
        for cmd in data.installation:
            md.append(cmd.strip())
        md.append("```")
        md.append("")

    # Uso
    if data.usage_example:
        md.append("## 📖 Uso")
        md.append("")
        md.append("```python")
        md.append(data.usage_example.strip())
        md.append("```")
        md.append("")

    # Endpoints (tabla)
    if data.endpoints:
        md.append("### Endpoints disponibles")
        md.append("")
        md.append("| Método | Ruta | Descripción |")
        md.append("|--------|------|-------------|")
        for ep in data.endpoints:
            method = str(ep.get("method", "")).upper()
            path = str(ep.get("path", ""))
            desc = str(ep.get("description", ""))
            md.append(f"| {method} | `{path}` | {desc} |")
        md.append("")

    # Configuración
    if data.configuration:
        md.append("## ⚙️ Configuración")
        md.append("")
        md.append("```env")
        md.append(data.configuration.strip())
        md.append("```")
        md.append("")

    # Pruebas
    if data.tests:
        md.append("## 🧪 Pruebas")
        md.append("")
        md.append("```bash")
        md.append(data.tests.strip())
        md.append("```")
        md.append("")

    # Despliegue
    if data.deployment:
        md.append("## 📦 Despliegue")
        md.append("")
        md.append("```bash")
        md.append(data.deployment.strip())
        md.append("```")
        md.append("")

    # Contribuir
    if data.contributing:
        md.append("## 🤝 Contribuir")
        md.append("")
        md.append(data.contributing)
        md.append("")

    # Licencia
    if data.license:
        md.append("## 📄 Licencia")
        md.append("")
        md.append(f"Este proyecto está bajo la licencia **{data.license}**.")
        md.append("")

    # Agradecimientos
    if data.acknowledgements:
        md.append("## 🙏 Agradecimientos")
        md.append("")
        md.append(data.acknowledgements)
        md.append("")

    # Soporte
    if data.support:
        md.append("## 📬 Soporte")
        md.append("")
        md.append(data.support)
        md.append("")

    return "\n".join(md).strip()


# Endpoint 1: Devuelve el markdown como JSON
@app.post("/generate-readme", response_description="Contenido Markdown del README.md")
def generate_readme(data: ReadmeData):
    markdown_content = generate_markdown(data)
    return {"markdown": markdown_content}


# Endpoint 2: Devuelve el archivo README.md para descargar
@app.post("/download-readme", response_class=PlainTextResponse)
def download_readme(data: ReadmeData):
    markdown_content = generate_markdown(data)
    return PlainTextResponse(
        content=markdown_content,
        headers={
            "Content-Disposition": 'attachment; filename="README.md"',
            "Content-Type": "text/markdown; charset=utf-8"
        }
    )

# 🖥️ Página principal (formulario)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 📤 Endpoint para descargar (JSON → archivo)
@app.post("/api/download", response_class=PlainTextResponse)
def download_readme(data: ReadmeData):
    markdown = generate_markdown(data)
    return PlainTextResponse(
        content=markdown,
        headers={
            "Content-Disposition": 'attachment; filename="README.md"',
            "Content-Type": "text/markdown; charset=utf-8"
        }
    )

# (Opcional) Endpoint para previsualizar
@app.post("/api/preview")
def preview_readme(data: ReadmeData):
    return {"markdown": generate_markdown(data)}