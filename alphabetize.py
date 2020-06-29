def populate_dict(): # Creates a dictionary of all the letters of the alphabet as keys with 1 through 26 as their value
    for count, letter in enumerate(alphabet, start =1):
      lettter = letter.split()
      current_char = lettter[0]
      dict[current_char] = count
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dict = {}
word_one = input('Type the first word: ')
word_two = input('Type the second word: ')
shorter_length = len(word_one)
shorter_word,longer_word = word_one, word_two
words = zip(word_one, word_two)
word_list = list(words)
flag = True

populate_dict()
if len(word_one) > len(word_two):
    shorter_length = len(word_two)
    shorter_word,longer_word = word_two, word_one

for element in range(shorter_length):
    if dict[word_list[element][0]] == dict[word_list[element][1]]:
        continue
    if dict[word_list[element][0]] < dict[word_list[element][1]]:
        print(f'{word_one}, {word_two}')
        flag = False
        break
    if dict[word_list[element][0]] > dict[word_list[element][1]]:
        print(f'{word_two}, {word_one}')
        flag = False
        break
if flag:
    print(f'{shorter_word}, {longer_word}')

