# Guía para Instalar Python y Tesseract en MacOS

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

## Paso 3: Instalar pytesseract 

1. **Instalar pip (si no lo tienes ya instalado):**
   - En la ventana de **Terminal**, ejecuta:
     ```sh
     sudo easy_install pip
     ```

2. **Instalar pytesseract:**
   - En la ventana de **Terminal**, ejecuta:
     ```sh
     pip3 install pytesseract
     ```
   - Si el anterior no funciona, **ejecuta**:
     ```sh
     pip install pytesseract
     ```

## Paso 3 (Opcional): Crear un Entorno Virtual e Instalar pytesseract

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
     pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

     # Uso de pytesseract para extraer texto de una imagen
     from PIL import Image
     text = pytesseract.image_to_string(Image.open('ruta_a_tu_imagen.png'))
     print(text)
     ```

2. **Desactivar el Entorno Virtual (Solo para el paso 3 opciona, cuando hayas terminado):**
   - En la ventana de **Terminal**, simplemente ejecuta:
     ```sh
     deactivate
     ```

## Conclusión

Ahora tienes Python, Tesseract y `pytesseract` configurados y listos para usar en tu sistema MacOS, puedes empezar a desarrollar tus proyectos de reconocimiento óptico de caracteres (OCR).
