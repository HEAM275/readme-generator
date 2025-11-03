# README.md Generator API

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Una API REST con FastAPI que genera archivos README.md en Markdown a partir de datos estructurados. Ideal para automatizar la documentación de tus proyectos.

## ✨ Características

- Genera Markdown válido según buenas prácticas de GitHub
- Soporta múltiples secciones: instalación, uso, endpoints, licencia, etc.
- Devuelve el README como JSON o como archivo descargable
- Campos opcionales: solo incluye lo que necesitas
- Compatible con entornos modernos (usa `uv` para entornos virtuales)

## 🚀 Instalación

```bash
git clone https://github.com/HEAM275/readme-generator.git
cd readme-generator
uv venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 📖 Uso

```python
uvicorn main:app --reload

# La API estará disponible en http://localhost:8000
```

### Endpoints disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/generate-readme` | Genera el contenido Markdown y lo devuelve en el cuerpo de la respuesta (formato JSON). |
| POST | `/download-readme` | Genera y devuelve directamente el archivo README.md para descargar. |

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor abre un issue o un pull request en el repositorio.

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.

## 🙏 Agradecimientos

Inspirado en las mejores prácticas de documentación de proyectos open source en GitHub.

## 📬 Soporte

¿Encontraste un bug o tienes una sugerencia? Abre un [issue](https://github.com/HEAM275/readme-generator/issues) en el repositorio.