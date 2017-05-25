import re
import sys


def edit_box(box_name, txt_name, output):
    with open (txt_name, 'r', encoding = "utf-8") as file:
        real_text = file.read()

    real_text = re.sub(' ', '', real_text)
    real_text = re.sub('\n', '', real_text)

    with open (box_name, 'r', encoding = "utf-8") as file:
        box_junk = file.read().split('\n')

    with open (output, 'w', encoding = "utf-8") as file:
        for i in range (len(real_text)):
            brand_new_box = box_junk[i].split(' ')
            brand_new_box[0] = real_text[i]
            file.write ('%s%s' % (' '.join(brand_new_box), '\n'))

def main():
    box_name = sys.argv[1]
    txt_name = sys.argv[2]
    output = sys.argv[3]
        
    edit_box(box_name, txt_name, output)

if __name__ == '__main__':
    main()
