import requests
from itertools import *
from pyfiglet import Figlet

#That creates the banner.
custom_fig = Figlet(font='graffiti')
banner="\n\n\n"
banner+= custom_fig.renderText('WordFinder')
banner+="""


WordFinder v1.0 / created by l3us
GitHub repostory:https://github.com/l3us/WordFinder

This is a programme that search for the words that include the letters you've typed.
 
Type 'help' to get more information, type 'end' to end the loop.       
"""

help="""
Type one by one the letters of the words that you want to search.

For example:
    You want to search for the words that include 'a' or 'b' or 'c'.
    1.Run the programme.
    2.Type 'a' and press <Enter>.
    3.Type 'b' and press <Enter>.
    4.Type 'c' and press <Enter>.
    5.Type the max length for the words.
    6.Type the file name that will be saved in.
    7.Type 'end' to finish the loop.
"""
#ask_to_dictionary function:This function send a get request to Cambridge Dictionary.If there is a page like that(If status equal to 200), it writes the word in a text file.
def ask_to_dictionary(word):
    global word_count
    r = requests.get(f'https://dictionary.cambridge.org/dictionary/english/{word}',allow_redirects=False,headers={"User-Agent":"Mozilla/5.0"})
    print(word,'is being searched',' status:',r.status_code)
    if r.status_code==200:
        file = open(f'{t_file}.txt','a')
        file.write(word+'\n')
        file.close()
        word_count+=1
        print('A word was found in the dictionary:',word)

#ask function: A function for input the letters that be wanted to search.
def ask():
    letters=[]
    print('Type the letters.')
    while True:
        letter=input('Letter:')
        letters.append(letter)
        if 'end' in letters:
            letters.pop()
            break
        elif 'help' in letters:
            letters.pop()
            print(help)
    letters.sort()
    letters_as_str = ''
    for x in letters:
        letters_as_str+=x
    return letters_as_str

#bruteforce function:It creates all possible words.
def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
            for i in range(1, maxlength + 1)))

      

if __name__ == '__main__':
    global word_count
    global t_file
    print(banner)
    posibilities = list(bruteforce(ask(), int(input('Max length of the words:'))))
    print(f'There are {len(posibilities)} possible word that will be searched.')
    word_count=0
    t_file=input("Wordlist name(don't type any extensions.):")
    for i in posibilities:
        ask_to_dictionary(i)
    print('\n',word_count,f"words was found and they was saved to {t_file}.txt")
