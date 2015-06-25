import os
from PIL import Image, ImageChops, ImageEnhance
from time import gmtime, strftime

# you can change the image directory here
HOAX_IMAGES = './HoaxImages/'

def check_image(img_path, scale=20.0):
    """ Compute the Error Level Analysis for the given image
    
    Save a copy of the given image changing its quality level,
    in our case 95%, and compute the difference between this 
    image over the original. In addition, a scale is also 
    applied to the final result for better viewing.
    
    References: 
    http://blackhat.com/presentations/bh-dc-08/Krawetz/Whitepaper/bh-dc-08-krawetz-WP.pdf
    http://www.eecs.berkeley.edu/Pubs/TechRpts/2015/EECS-2015-85.pdf
    """
    try:
        img = Image.open(img_path)
    except FileNotFoundError:
        print ("File '"+ img_path +"' not found.")
        return
    
    # check the image format for JPEG only
    if img.format is not 'JPEG':
        log(img_path + ' is not a JPEG file')
        return

    log("Image size "+ str(img.size[0]) + "x" + str(img.size[1]))
    short_file_name = os.path.splitext(img_path)[0]
    
    # save a copy of the image with a different inferior quality level
    resaved_path = short_file_name + '_resaved'
    img.save(resaved_path, 'JPEG', quality=95)
    resaved_img = Image.open(resaved_path)
    
    # compute the difference between the given image and the image
    # generated applying a scale to increase the brightness
    ela_img = ImageChops.difference(img, resaved_img)
    ela_img = ImageEnhance.Brightness(ela_img).enhance(scale)
    ela_img.save(short_file_name + '_ela.jpg', 'JPEG', quality=100)
    
    os.remove(resaved_path)
    
    return ela_img

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
        ela_img = check_image(img_path)
        ela_img.show()
    elif option == '2':
        process_images(HOAX_IMAGES)
    else:
        print ('Try a valid option :)')
    option = get_menu()