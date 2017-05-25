import os
import re
import sys

        
def main():
    old_picture = sys.argv[1]
    new_picture = sys.argv[2]
    box_name = re.sub('\.tif', '', new_picture)

    os.system ('convert ' + old_picture + ' -brightness-contrast -50% -monochrome -normalize -sharpen 0x3.0 -morphology close diamond:0.05 ' + new_picture)
    os.system ('tesseract ' + new_picture + ' ' + box_name + ' batch.nochop makebox')

if __name__ == '__main__':
    main()
