'''                       
Resize script adapted from Thung and Yang's trashnet (https://github.com/garythung/trashnet)              
Accepts images from an input folder, resizes them to dimensions specified in trashnet constants.py,   
and outputs them to a destination folder in subfolders by class.
'''

import os
import resize_constants
import numpy as np
from scipy import misc, ndimage
import imageio
import imageio.v2 as iio
from skimage.transform import resize
from skimage import img_as_ubyte
from pathlib import Path

def resize_(image, dim1, dim2):
    return resize(image, (dim1, dim2))


def fileWalk(directory, destPath):
    try:
        os.makedirs(destPath)
    except OSError:
        if not os.path.isdir(destPath):
            raise

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if len(file) <= 4 or file[-4:] != '.jpg':
                continue

            pic = iio.imread(os.path.join(subdir, file))
            dim1 = len(pic)
            dim2 = len(pic[0])
            if dim1 > dim2:
                pic = np.rot90(pic)
                
            picResized = resize_(pic, resize_constants.DIM1, resize_constants.DIM2)
            write_image_imageio(os.path.join(destPath, file), img_as_ubyte(picResized), quality=95)
            
def write_image_imageio(img_file, img, quality):
    #img = (np.clip(img, 0.0, 1.0) * 255.0 + 0.5).astype(np.uint8)
    kwargs = {}
    if os.path.splitext(img_file)[1].lower() in [".jpg", ".jpeg"]:
        if img.ndim >= 3 and img.shape[2] > 3:
            img = img[:,:,:3]
        kwargs["quality"] = quality
        kwargs["subsampling"] = 0
    iio.imwrite(img_file, img, **kwargs)
            
# def read_image_imageio(img_file):
#     img = imageio.v2.imread(img_file)
#     img = np.asarray(img).astype(np.float32)
#     if len(img.shape) == 2:
#         img = img[:,:,np.newaxis]
#     return img / 255.0

            
def main():

    parentPath = os.path.dirname(os.getcwd())

    prepath = Path("/Users/rohitmaheshwari/Documents/GitHub/trashnet/data/dataset-original")
    glassDir = os.path.join(prepath, 'glass')
    cardboardDir = os.path.join(prepath, 'cardboard')
    electricalCablesDir = os.path.join(prepath, 'electrical cables')
    electronicChipsDir = os.path.join(prepath, 'electronic chips')
    laptopsDir = os.path.join(prepath, 'laptops')
    smallAppliancesDir = os.path.join(prepath, 'small appliances')
    smartphonesDir = os.path.join(prepath, 'smartphones')
    glovesDir = os.path.join(prepath, 'gloves')
    masksDir = os.path.join(prepath, 'masks')
    medicinesDir = os.path.join(prepath, 'medicines')
    syringeDir = os.path.join(prepath, 'syringe')
    beverageCansDir = os.path.join(prepath, 'beverage cans')
    constructionScrapDir = os.path.join(prepath, 'construction scrap')
    metalContainersDir = os.path.join(prepath, 'metal containers')
    otherMetalObjectsDir = os.path.join(prepath, 'other metal objects')
    sprayCansDir = os.path.join(prepath, 'spray cans')
    newspaperDir = os.path.join(prepath, 'news paper')
    paperDir = os.path.join(prepath, 'paper')
    paperCupsDir = os.path.join(prepath, 'paper cups')
    tetraPakDir = os.path.join(prepath, 'tetra pak')
    cigaretteButtDir = os.path.join(prepath, 'cigarette butt')
    plasticBagsDir = os.path.join(prepath, 'plastic bags')
    plasticBottlesDir = os.path.join(prepath, 'plastic bottles')
    plasticContainersDir = os.path.join(prepath, 'plastic containers')
    plasticCupsDir = os.path.join(prepath, 'plastic cups')
    
    #plasticDir = os.path.join(prepath, 'plastic')
    #metalDir = os.path.join(prepath, 'metal')
    #trashDir = os.path.join(prepath, 'medical')
    #compostDir = os.path.join(prepath, 'e-waste')

    destPath = os.path.join(parentPath, '../../GitHub/trashnet/data/dataset-resized')

    try:
        os.makedirs(destPath)

    except OSError:
        if not os.path.isdir(destPath):
            raise


    #GLASS
    fileWalk(glassDir, os.path.join(destPath, 'glass'))

    #CARDBOARD
    fileWalk(cardboardDir, os.path.join(destPath, 'cardboard'))
    
    #COMPOST
    #fileWalk(compostDir, os.path.join(destPath, 'e-waste'))
    fileWalk(electricalCablesDir, os.path.join(destPath, 'electrical cables'))
    fileWalk(electronicChipsDir, os.path.join(destPath, 'electronic chips'))
    fileWalk(laptopsDir, os.path.join(destPath, 'laptops'))
    fileWalk(smallAppliancesDir, os.path.join(destPath, 'small appliances'))
    fileWalk(smartphonesDir, os.path.join(destPath, 'smartphones'))
    
    #TRASH
    #fileWalk(trashDir, os.path.join(destPath, 'medical'))
    fileWalk(glovesDir, os.path.join(destPath, 'gloves'))
    fileWalk(masksDir, os.path.join(destPath, 'masks'))
    fileWalk(medicinesDir, os.path.join(destPath, 'medicines'))
    fileWalk(syringeDir, os.path.join(destPath, 'syringe'))
    
    #METAL
    #fileWalk(metalDir, os.path.join(destPath, 'metal'))
    fileWalk(beverageCansDir, os.path.join(destPath, 'beverage cans'))
    fileWalk(constructionScrapDir, os.path.join(destPath, 'contstrcution scrap'))
    fileWalk(metalContainersDir, os.path.join(destPath, 'metal containers'))
    fileWalk(otherMetalObjectsDir, os.path.join(destPath, 'other metal objects'))
    fileWalk(sprayCansDir, os.path.join(destPath, 'spray cans'))
    
    
    #PAPER
    fileWalk(newspaperDir, os.path.join(destPath, 'news paper'))
    fileWalk(paperDir, os.path.join(destPath, 'paper'))
    fileWalk(paperCupsDir, os.path.join(destPath, 'paper cups'))
    fileWalk(tetraPakDir, os.path.join(destPath, 'tetra pak'))
            
    
    #PLASTIC
    #fileWalk(plasticDir, os.path.join(destPath, 'plastic'))
    fileWalk(cigaretteButtDir, os.path.join(destPath, 'cigarette butt'))
    fileWalk(plasticBagsDir, os.path.join(destPath, 'plastic bags'))
    fileWalk(plasticBottlesDir, os.path.join(destPath, 'plastic bottles'))
    fileWalk(plasticContainersDir, os.path.join(destPath, 'plastic containers'))
    fileWalk(plasticCupsDir, os.path.join(destPath, 'plastic cups'))

    

            
if __name__ == '__main__':
    main()
