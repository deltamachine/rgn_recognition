import sys


def create_wordlist(input, output):
	with open (input, 'r', encoding = 'utf-8') as file:
		words = file.read().split(' ')

	wordlist = list(set(words))
	wordlist.sort()

	with open (output, 'w', encoding = 'utf-8') as file:
		for word in wordlist:
			file.write ('%s%s' % (word, '\n'))

def main():
	input = sys.argv[1]
	output = sys.argv[2]

	create_wordlist(input, output)

if __name__ == '__main__':
    main()