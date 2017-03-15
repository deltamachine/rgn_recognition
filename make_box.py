import os
from PIL import Image

def convert_picture():
    archive = []
    for d, dirs, files in os.walk(os.getcwd() + '/raw_data'):
        for f in files:
            path = os.path.join(d,f)
            archive.append(path)

    num = 0

    for picture in archive:
        image = Image.open(picture)
        path = os.getcwd() + '/training_data/rgn.handwriting.exp' + str(num) + '.tif'
        image.save(path)
        num+=1

def make_box():
    os.chdir(os.getcwd() + '/training_data')
    tiff_archive = []
    for d, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if 'tif' in f:
                path = os.path.join(d,f)
                tiff_archive.append(path)
                
    os.system ('cd C:\\Program Files (x86)\\Tesseract-OCR\\')
    
    for picture in tiff_archive:
        box_path = picture[:-4]
        os.system ('tesseract' + ' ' + picture + ' ' + box_path + ' batch.nochop makebox')
        
def main():
    convert_picture()
    make_box()

if __name__ == '__main__':
    main()

 
