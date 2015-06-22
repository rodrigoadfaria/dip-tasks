import os

from PIL import Image, ImageChops, ImageEnhance
from time import gmtime, strftime

HOAX_IMAGES = './HoaxImages/'

def check_image(img_path, scale=20.0, show=False):
    """ Calcula o Error Level Analysis para a imagem dada
    
    Salva uma cópia da imagem alterando sua qualidade, neste caso 95%,
    e calcula a diferença desta para a original. Uma escala também é
    aplicada no resultado final para facilitar a visualização.
    """
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        print ("File '"+ img_path +"' not found.")
        return
    
    # verifica se a imagem origem está no formato JPEG
    if img.format is not 'JPEG':
        log(img_path + ' is not a JPEG file')
        return

    log("Image size "+ str(img.size[0]) + "x" + str(img.size[1]))
    short_file_name = os.path.splitext(img_path)[0]
    
    # salva a imagem dada com uma qualidade inferior
    resaved_path = short_file_name + '_resaved'
    img.save(resaved_path, 'JPEG', quality=95)
    resaved_img = Image.open(resaved_path)
    
    # calcula a diferença entre a imagem original e a imagem alterada
    # aplicando uma escala para aumentar o brilho
    ela_img = ImageChops.difference(img, resaved_img)
    ela_img = ImageEnhance.Brightness(ela_img).enhance(scale)
    ela_img.save(short_file_name + '_ela.png')
    if (show):
        ela_img.show()
    
    os.remove(resaved_path)

def process_images(path):
    images = os.listdir(path)
    for file in images:
        check_image(path + file)
        
def log(msg):
    print (strftime("%a, %d %b %Y %H:%M:%S: ", gmtime()), msg)

def get_menu():
    return input("\n--------------------------------------------------------------"
                 "\n|                   ERROR LEVEL ANALYSIS                     |" +
                 "\n| Tell me what you wanna do:                                 |" +
                 "\n| 1 - Check image                                            |" +
                 "\n| 2 - Check hoax images                                      |" +
                 "\n| 3 - exit                                                   |" +
                 "\n--------------------------------------------------------------\n")

option = get_menu()

while option != '3':
    if option == '1':
        img_path = input("Give me the image path from here (e.g. ./imgs/data/original.jpg)\n")
        check_image(img_path, show=True)
    elif option == '2':
        process_images(HOAX_IMAGES)
    else:
        print ('Try a valid option :)')
    option = get_menu()