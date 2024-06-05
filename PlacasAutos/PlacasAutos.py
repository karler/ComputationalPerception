import cv2
import pytesseract

# Ruta de Tesseract en Windows
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# Ruta de Tesseract en macOS
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
# Si usas un entorno virtual "env" no es necesario activar las rutas

placa = []
image = cv2.imread('auto001.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image',image)
cv2.moveWindow('Image',45,10)
cv2.waitKey(0)
