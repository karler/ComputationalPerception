# Guía para Instalar Python y Tesseract en Linux

## Paso 1: Instalar Python

1. **Actualizar el Sistema:**
   - Abre una ventana de **Terminal**.
   - Ejecuta el siguiente comando para actualizar la lista de paquetes:
     ```sh
     sudo apt update
     ```

2. **Instalar Python:**
   - Ejecuta el siguiente comando para instalar Python:
     ```sh
     sudo apt install python3 python3-pip python3-venv
     ```

3. **Verificar la Instalación de Python:**
   - En la ventana de **Terminal**, ejecuta:
     ```sh
     python3 --version
     ```
   - Deberías ver la versión de Python que instalaste.

## Paso 2: Instalar Tesseract

1. **Instalar Tesseract:**
   - En la ventana de **Terminal**, ejecuta:
     ```sh
     sudo apt install tesseract-ocr
     ```

2. **Verificar la Instalación de Tesseract:**
   - En la ventana de **Terminal**, ejecuta:
     ```sh
     tesseract --version
     ```
   - Deberías ver la versión de Tesseract y otra información relevante.

## Paso 3: Crear un Entorno Virtual e Instalar pytesseract

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

3. **Instalar pytesseract en el Entorno Virtual:**
   - Con el entorno virtual activado, ejecuta:
     ```sh
     pip install pytesseract
     ```

## Paso 4: Configurar pytesseract en tu Script de Python

1. **Importar y Configurar pytesseract en tu Script:**
   - En tu script de Python, importa el módulo `pytesseract` y establece la ruta de Tesseract si es necesario:
     ```python
     import pytesseract

     # Si Tesseract no está en el PATH o si prefieres definirlo explícitamente:
     pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

     # Uso de pytesseract para extraer texto de una imagen
     from PIL import Image
     text = pytesseract.image_to_string(Image.open('ruta_a_tu_imagen.png'))
     print(text)
     ```

2. **Desactivar el Entorno Virtual (cuando hayas terminado):**
   - En la ventana de **Terminal**, simplemente ejecuta:
     ```sh
     deactivate
     ```

## Conclusión

Ahora tienes Python, Tesseract y `pytesseract` configurados y listos para usar en tu sistema Linux, puedes empezar a desarrollar tus proyectos de reconocimiento óptico de caracteres (OCR).
