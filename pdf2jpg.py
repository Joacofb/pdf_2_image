import sys
from pdf2image import convert_from_path

# Verificar que el nombre del archivo fue pasado como parametro en la consola
if len(sys.argv) < 2:
    print('Para usar pdf2jpg: python pdf2jpg.py [tu_archivo.pdf]')
    sys.exit()

archivo_pdf = sys.argv[1]

# Convertir cada pagina del PDF en JPG
paginas = convert_from_path(archivo_pdf, dpi=300)

for i, pagina in enumerate(paginas):
    nombre_imagen = f"{archivo_pdf[:-4]}_{i + 1}.png"
    pagina.save(nombre_imagen, "PNG")
    print(f"La pagina {i + 1} se guardo correctamente como {nombre_imagen}")
