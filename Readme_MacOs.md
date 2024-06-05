# Guía para Instalar Python, Tesseract, OpenCV y numpy en MacOS

## Paso 1: Instalar Python

1. **Descargar Python:**
   - Visita el sitio web oficial de Python: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/).
   - Haz clic en el botón de descarga para la última versión estable de Python.

2. **Ejecutar el Instalador de Python:**
   - Abre el archivo descargado para iniciar el instalador.
   - Sigue las instrucciones en pantalla para completar la instalación.

3. **Verificar la Instalación de Python:**
   - Abre una ventana de **Terminal**.
   - Escribe el siguiente comando y presiona Enter:
     ```sh
     python3 --version
     ```
   - Deberías ver la versión de Python que instalaste.

## Paso 2: Instalar Tesseract

1. **Instalar Homebrew (si no lo tienes ya instalado):**
   - Abre una ventana de **Terminal**.
   - Ejecuta el siguiente comando para instalar Homebrew:
     ```sh
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

2. **Instalar Tesseract usando Homebrew:**
   - En la misma ventana de **Terminal**, ejecuta:
     ```sh
     brew install tesseract
     ```

3. **Verificar la Instalación de Tesseract:**
   - En la ventana de **Terminal**, ejecuta:
     ```sh
     tesseract --version
     ```
   - Deberías ver la versión de Tesseract y otra información relevante.

## Paso 3: Instalar pytesseract, OpenCV y numpy

1. **Instalar pip (si no lo tienes ya instalado):**
   - En la ventana de **Terminal**, ejecuta:
     ```sh
     sudo easy_install pip
     ```

2. **Instalar pytesseract, OpenCV y numpy:**
   - En la ventana de **Terminal**, ejecuta:
     ```sh
     pip3 install pytesseract opencv-python-headless numpy
     ```

## Paso 4 (Opcional): Crear un Entorno Virtual

1. **Crear un Entorno Virtual:**
   - En la ventana de **Terminal**, navega a la carpeta donde quieres crear el entorno virtual. Luego ejecuta:
     ```sh
     python3 -m venv myenv
     ```
   - Esto creará un entorno virtual llamado `myenv`.

2. **Activar el Entorno Virtual:**
   - En la misma ventana de **Terminal**, ejecuta:
     ```sh
     source myenv/bin/activate
     ```
   - Deberías ver el nombre del entorno virtual en el prompt de la terminal, indicando que está activado.

3. **Instalar pytesseract, OpenCV y numpy en el Entorno Virtual:**
   - Con el entorno virtual activado, ejecuta:
     ```sh
     pip install pytesseract opencv-python-headless numpy
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
     pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

     # Ruta a la imagen
     file_path = 'auto001.jpg'

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

2. **Desactivar el Entorno Virtual (Solo para el paso 4 opcional, cuando hayas terminado):**
   - En la ventana de **Terminal**, simplemente ejecuta:
     ```sh
     deactivate
     ```

## Conclusión

Ahora tienes Python, Tesseract, `pytesseract`, OpenCV y `numpy` configurados y listos para usar en tu sistema MacOS. Puedes empezar a desarrollar tus proyectos de reconocimiento óptico de caracteres (OCR) y procesamiento de imágenes.
