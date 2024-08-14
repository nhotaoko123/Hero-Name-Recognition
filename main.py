import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

file_name='output.txt'
output_data = """"""

def get_image_files(folder_path):
    """
    This function is used to get all image file names

    @param folder_path: path of folder
    @type: string
    
    @return: a list containing all the information for the image file names
    @rtype: list
    """
    # Supported image extensions
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

    # List all files in the directory
    all_files = os.listdir(folder_path)

    # Filter out image files
    image_files = [f for f in all_files if f.lower().endswith(image_extensions)]

    return image_files

def template_matching(main_image_name, template_name, threshold=0.8):
    """
    This function is used to match an image to an image

    @param main_image_name: The main image
    @type: about '.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'
    @param template_name: The template image
    @type: about '.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'

    @return: name main_image_name plus template_name
    @rtype: string
    """
    # Load the main image and convert it to grayscale
    main_image_path = '../CV mini project/test_data/test_images/' + main_image_name
    template_path = '../CV mini project/test_data/lable_images/' + template_name
    main_image = cv.imread(main_image_path)
    assert main_image is not None, "file could not be read, check with os.path.exists()"
    gray_main = cv.cvtColor(main_image, cv.COLOR_BGR2GRAY)
    main_image_height, main_image_width = main_image.shape[:2]


    # Load the template image and convert it to grayscale
    template = cv.imread(template_path)
    assert template is not None, "file could not be read, check with os.path.exists()"
    template_height, template_width = template.shape[:2]

    if template_height > main_image_height:
        template_height = int(template_height * (main_image_height / template_height))

    if template_width > main_image_width:
        template_width = int(template_width * (main_image_width / template_width))
    
    resized_image = cv.resize(template, (template_width, template_height))
    gray_template = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
    
    # Get the width and height of the template
    w, h = gray_template.shape[::-1]

    # Perform template matching
    meths = 'cv.TM_CCOEFF_NORMED' #['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR','cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    method = eval(meths)

    result = cv.matchTemplate(gray_main, gray_template, method)

    # Set a threshold to detect the template
    loc = np.where(result >= threshold)
    if len(loc[0])>0:
        return main_image_name + '\t' + template_name.split('.')[0]
        # print(main_image_name.split('.')[0])
        # print(template_name.split('.')[0])
    else:
        return None

def write_txt(data, file_name='output.txt'):
    """
    This function is used to write txt file

    @param data: The text is writed to file
    @type: string
    @param file_name: name of file
    @type: string
    """
    # Open a file in write mode
    with open(file_name, 'w') as file:
        file.write(data)
    file.close()

main_image_paths = get_image_files('../CV mini project/test_data/test_images')
template_image_paths = get_image_files('../CV mini project/test_data/lable_images')
for main_image_path in main_image_paths:
    for template_image_path in template_image_paths:
        s_matched = template_matching(main_image_path, template_image_path)
        s_matched = '' if s_matched is None else s_matched + '\n'
        output_data = output_data + s_matched

if os.path.exists(file_name):
    write_txt('')

write_txt(output_data)
cv.destroyAllWindows()