import requests
from itertools import *
def ask_to_dictionary(word):
    global word_count
    r = requests.get(f'https://dictionary.cambridge.org/dictionary/english/{word}',allow_redirects=False,headers={"User-Agent":"Mozilla/5.0"})
    print(word,'is being searched',' status:',r.status_code)
    if not r.status_code==302:
        file = open(f'{t_file}.txt','a')
        file.write(word+'\n')
        file.close()
        word_count+=1
        print('A word was found in the dictionary:',word)


def ask():
    global dictionary
    dictionary={}
    letters=[]
    print('Type the letters')
    while True:
        letter=input('Letter:')
        letters.append(letter)
        if 'quit' in letters:
            letters.pop()
            break
    letters.sort()
    letters_as_str = ''
    for x in letters:
        letters_as_str+=x
    return letters_as_str

def bruteforce(charset, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
            for i in range(2, maxlength + 1)))



if __name__ == '__main__':
    global word_count
    global t_file
    print("Working...")
    posibilities = list(bruteforce(ask(), int(input('Max length of the words:'))))
    print(f'There are {len(posibilities)} possible word that will be searched.')
    word_count=0
    t_file=input("Wordlist name(don't type any extensions.):")
    for i in posibilities:
        ask_to_dictionary(i)
    print('\n',word_count,f"words was found and they was saved to {t_file}.txt")