import os
import re

def edit_box():
    list_of_files = os.listdir(os.getcwd() + '/training_data')
    counter = len(list_of_files) // 3
    
    os.chdir(os.getcwd() + '/training_data')

    for i in range (counter):
        box_name = 'rgn.handwriting.exp' + str(i) + '.box'
        txt_name = 'rgn.handwriting.exp' + str(i) + '.txt'

        with open (txt_name, 'r', encoding = "utf-8") as file:
            real_text = file.read()

        real_text = re.sub(' ', '', real_text)
        real_text = re.sub('\n', '', real_text)

        with open (box_name, 'r', encoding = "utf-8") as file:
            box_junk = file.read().split('\n')

        with open (box_name, 'w', encoding = "utf-8") as file:
            for i in range (len(real_text)):
                brand_new_box = list(box_junk[i])
                brand_new_box[0] = real_text[i]
                file.write (''.join(brand_new_box))
                file.write ('\n')
        
def main():
    edit_box()

if __name__ == '__main__':
    main()
