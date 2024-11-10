# PDF a Imagen - Conversor en Python 🖼️
Este es un sencillo programa en Python que convierte cada página de un archivo PDF en una imagen individual en el formato que prefieras (por ejemplo, JPG o PNG). Es una herramienta útil para extraer contenido de PDF y tenerlo en un formato de imagen fácil de visualizar y compartir.

## Características 📋
- Convierte archivos PDF en imágenes (JPG, PNG, etc.).
- Configurable para guardar en distintos formatos de imagen.
- Permite especificar la ruta de destino donde guardar las imágenes.

## Requisitos ⚙️
Asegúrate de tener lo siguiente antes de usar el programa:
- **Python 3.6+**
- **Librerías**: Necesitarás instalar las librerías `pdf2image` y `Pillow`. Puedes hacerlo con:
  ```bash
  pip install pdf2image pillow
  ```
**Poppler**: Este programa depende de Poppler para leer PDFs. Instálalo siguiendo las instrucciones:
- **Windows**: Descarga Poppler desde [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows) y agrega su ruta (el directorio bin) al PATH del sistema.
- **MacOS**: Instala Poppler usando Homebrew con `brew install poppler`.
- **Linux**: Instala Poppler con `sudo apt install poppler-utils` (en distribuciones basadas en Debian).

## Instalación 🚀
Clona este repositorio en tu máquina local:
  ```bash
  git clone https://github.com/tu_usuario/tu_repositorio.git
  cd tu_repositorio
  ```

## Uso 📝
  **1.** Ejecuta el programa desde la consola, proporcionando el archivo PDF y el formato de imagen deseado como parámetros opcionales:
  ```bash
  python pdf2image_converter.py archivo.pdf [formato] [ruta_destino]
  ```
    -  **archivo.pdf**: El archivo PDF que deseas convertir.
    -  **[formato]**: (Opcional) El formato de salida de las imágenes (`jpg`, `png`, etc.). Predeterminado: `jpg`.
    -  **[ruta_destino]**: (Opcional) La carpeta donde quieres guardar las imágenes convertidas. Predeterminado: carpeta actual.

  **2.** Ejemplo: Si quieres convertir un archivo PDF llamado `documento.pdf` a imágenes PNG y guardarlas en una carpeta llamada `imagenes/`:

    ```bash
    python pdf2image_converter.py documento.pdf png imagenes/
    ```

  **3.** Salida: Las imágenes convertidas se guardarán con nombres en el formato `pagina_1.png`, `pagina_2.png`, etc.

## Código principal 📜
Aquí se muestra el fragmento principal del código, para entender cómo funciona:

```python
import sys
import os
from pdf2image import convert_from_path

# Configura los parámetros de entrada
archivo_pdf = sys.argv[1]
formato = sys.argv[2] if len(sys.argv) > 2 else 'jpg'
ruta_destino = sys.argv[3] if len(sys.argv) > 3 else '.'

# Convierte cada página del PDF a imagen
paginas = convert_from_path(archivo_pdf, dpi=300, poppler_path="C:/ruta/a/poppler/bin")

# Guarda cada página con el formato y en la ruta especificada
for i, pagina in enumerate(paginas):
    nombre_imagen = os.path.join(ruta_destino, f"pagina_{i + 1}.{formato}")
    pagina.save(nombre_imagen, formato.upper())
    print(f"La página {i + 1} se guardó correctamente como {nombre_imagen}")

```

## Notas adicionales 🗒️
  - Precaución con rutas: Asegúrate de que `Poppler` esté correctamente configurado en tu sistema, especialmente en Windows, para evitar errores de conversión.
  - Compatibilidad de formatos: `Pillow` soporta formatos populares como `JPEG`, `PNG`, `BMP`, y otros.

## Contribuir 🤝
¿Tienes alguna sugerencia o mejora? ¡Siéntete libre de contribuir! Puedes hacer un fork de este repositorio, realizar cambios y luego hacer un pull request.

## Licencia 📄
Este proyecto está licenciado bajo la MIT License. Para más detalles, consulta el archivo `LICENSE`.