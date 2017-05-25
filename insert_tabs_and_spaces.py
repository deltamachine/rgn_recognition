import re
import sys


def add_spaces_and_tabs(box_file, text_file, output):
    counter = 0

    with open (output, 'w', encoding = 'utf-8') as file:
        for line in text_file:
            words =  line.split()

            for i in range(len(words)):
                num = len(words[i])
                last_sym = counter + num

                for j in range (counter, last_sym):
                    file.write('%s%s' % (box_file[j], '\n'))

                last_string = box_file[j].split()
                
                new_space_x = int(last_string[3]) + 5
                new_space_w = new_space_x + 5

                file.write('%s %s %s %s %s %s%s' % (' ', str(new_space_x), \
                    last_string[2], str(new_space_w), last_string[4], last_string[5], '\n'))

                if i == len(words) - 1:
                    new_tab_x = new_space_w + 5
                    new_tab_w = new_tab_x + 5

                    file.write('%s %s %s %s %s %s%s' % ('\t', str(new_tab_x), \
                        last_string[2], str(new_tab_w), last_string[4], last_string[5], '\n'))

                counter = counter + num

def main():
    box_file = sys.argv[1]
    text_file = sys.argv[2]
    output = sys.argv[3]

    with open (box_file, 'r', encoding = 'utf-8') as file:
        box_file = file.read().split('\n')

    with open (text_file, 'r', encoding = 'utf-8') as file:
        text_file = file.read().split('\n')

    add_spaces_and_tabs(box_file, text_file, output)

if __name__ == '__main__':
    main()
