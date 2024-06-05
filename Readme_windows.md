# Guía para Instalar Python, Tesseract, OpenCV y numpy en Windows

## Paso 1: Instalar Python

1. **Descargar Python:**
   - Visita el sitio web oficial de Python: [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Haz clic en el botón de descarga para la última versión estable de Python.

2. **Ejecutar el Instalador de Python:**
   - Abre el archivo descargado para iniciar el instalador.
   - **Importante:** Marca la casilla "Add Python to PATH" antes de hacer clic en "Install Now".

3. **Verificar la Instalación de Python:**
   - Abre una ventana de **Símbolo del sistema** (puedes buscar "cmd" en el menú de inicio).
   - Escribe el siguiente comando y presiona Enter:
     ```sh
     python --version
     ```
   - Deberías ver la versión de Python que instalaste.

## Paso 2: Instalar Tesseract

1. **Descargar Tesseract:**
   - Visita el repositorio oficial de Tesseract en GitHub: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki).
   - Haz clic en el enlace de descarga para Windows.

2. **Ejecutar el Instalador de Tesseract:**
   - Abre el archivo descargado para iniciar el instalador.
   - Sigue las instrucciones en pantalla para completar la instalación.
   - Anota la ruta de instalación de Tesseract, ya que la necesitarás para configurar las variables de entorno. La ruta por defecto suele ser algo como:
     ```
     C:\Program Files\Tesseract-OCR
     ```

## Paso 3: Configurar Tesseract en las Variables de Entorno

1. **Abrir Configuración de Variables de Entorno:**
   - Haz clic derecho en "Este equipo" o "Mi PC" en el escritorio o en el Explorador de archivos y selecciona "Propiedades".
   - En la ventana que se abre, selecciona "Configuración avanzada del sistema".
   - Haz clic en el botón "Variables de entorno...".

2. **Agregar Tesseract a la Variable de Entorno PATH:**
   - En la sección "Variables del sistema", busca y selecciona la variable "Path" y haz clic en "Editar".
   - En la ventana de edición, haz clic en "Nuevo" e ingresa la ruta de instalación de Tesseract (por ejemplo, `C:\Program Files\Tesseract-OCR`).
   - Haz clic en "Aceptar" en todas las ventanas abiertas para aplicar los cambios.
   - <img alt="Variables de entorno" src="img\w0.png" size/>

3. **Verificar la Configuración:**
   - Abre una nueva ventana de **Símbolo del sistema**.
   - Escribe el siguiente comando y presiona Enter:
     ```sh
     tesseract --version
     ```
   - Deberías ver la versión de Tesseract y otra información relevante.

## Paso 4: Instalar pytesseract, OpenCV y numpy

1. **Instalar pytesseract, OpenCV y numpy:**
   - Abre una ventana de **Símbolo del sistema**.
   - Ejecuta los siguientes comandos para instalar `pytesseract`, `opencv-python` y `numpy` usando `pip`:
     ```sh
     pip install pytesseract opencv-python numpy
     ```

## Paso 5: Configurar pytesseract y OpenCV en tu Script de Python

1. **Importar y Configurar pytesseract y OpenCV en tu Script:**
   - En tu script de Python, importa los módulos `pytesseract`, `cv2` y `numpy` y establece la ruta de Tesseract si es necesario:
     ```python
     import pytesseract
     import cv2
     import numpy as np
     import os

     # Si Tesseract no está en el PATH o si prefieres definirlo explícitamente:
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

     # Ruta a la imagen
     file_path = 'auto01.jpg'

     # Verificar si el archivo existe
     if not os.path.exists(file_path):
         print(f"File not found: {file_path}")
     else:
         # Cargar una imagen usando OpenCV
         image = cv2.imread(file_path)

         if image is None:
             print(f"Failed to load image: {file_path}")
         else:
             # Convertir la imagen a escala de grises
             gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

             # Usar pytesseract para extraer texto de la imagen
             text = pytesseract.image_to_string(gray)

             print(text)
     ```

## Conclusión

Ahora tienes Python, Tesseract, `pytesseract`, OpenCV y `numpy` configurados y listos para usar en tu sistema Windows. Puedes empezar a desarrollar tus proyectos de reconocimiento óptico de caracteres (OCR) y procesamiento de imágenes.
