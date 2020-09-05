#Autor >> AlfonzCS
#Creado en Python3
import cv2, sys, random, time
from time import sleep
from colorama import init, Fore

init()

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

           _      __                     __               __                    _            
    ____  (_)____/ /___  __________     / /_____     ____/ /________ __      __(_)___  ____ _
   / __ \/ / ___/ __/ / / / ___/ _ \   / __/ __ \   / __  / ___/ __ `/ | /| / / / __ \/ __ `/
  / /_/ / / /__/ /_/ /_/ / /  /  __/  / /_/ /_/ /  / /_/ / /  / /_/ /| |/ |/ / / / / / /_/ / 
 / .___/_/\___/\__/\__,_/_/   \___/   \__/\____/   \__,_/_/   \__,_/ |__/|__/_/_/ /_/\__, /  
/_/                                                                                 /____/   

         Autor -#- AlfonzMx Script para dibujar una imagen "Uso Personal"       
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)

def use():
	print("         Usage: drawing.py [image.jpg/png]")

try:
    #Inmagen
    image_file = sys.argv[1]
except:
    logo()
    use()
    exit()

try:
    print('[*] Iniciando...')
    sleep(0.5)
    print('[+] Mostrando Imagen...')
    image = cv2.imread(image_file)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayImageInv = 255 - grayImage
    grayImageInv = cv2.GaussianBlur(grayImageInv, (21, 21), 0)
    output = cv2.divide(grayImage, 255-grayImageInv, scale=256.0)
    cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("pencilsketch", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("image", image)
    cv2.imshow("pencilsketch", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('[-] Saliendo...')
except:
  print('[x] Error')
  print("[x] Verificar extencion nombre de la imagen")
