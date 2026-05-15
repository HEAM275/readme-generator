# API para Generar Readme.Md de proyectos

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Monolito para generar un Readme basico de una API o proyecto

## ✨ Características

- Genera el documento en formato Markdown
- Contiene varias secciones como instalacion, despliegue etc

## 🚀 Instalación

```bash
git clone https://github.com/HEAM275/readme-generator.git
uv venv ó python3 venv venv
source venv/bin/activate -->Linux  ó venv\Scripts\activate
pip install -r requirements.txt ó uv pip install -r pyproject.toml
```

### Endpoints disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/generate-readme` | Contenido Markdown del README.md |
| POST | `/api/download` | Descarga el archivo a partir de los datos ingresados en el template |

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.


[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/HEAM275/readme-generator)
