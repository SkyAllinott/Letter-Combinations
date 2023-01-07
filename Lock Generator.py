# All letters available
letters = [
    'cgflbptsmd',
    'earthiuoyl',
    'ealtoinsrm',
    'plyamdkesx'
]

# convert letters to uppercase
letters = [i.upper() for i in letters]

# Load the dictionary file into a dictionary object
def load_dict(path):
    with open(path) as f:
        # only look at words with the same number of letters as
        # we have character dials
        return { w.strip().upper():False for w in f if len(w.strip()) == len(letters)}

# Recursively build every word from letter list and check against
# dictionary
def check_word(word_so_far, remaining_dials, word_dict):
    # check completed word against dictionary
    if len(remaining_dials) == 0:
        return [word_so_far] if word_so_far in word_dict else []
    # build all words with next set of letters and recurse
    else:
        wordlist = []
        for c in remaining_dials[0]:
            wordlist += check_word(word_so_far + c, remaining_dials[1:], word_dict)
        return wordlist

def main():
    # load dictionary
    word_dict = load_dict("Dictionary.txt")

    # compare letters with dictionary
    matching_words = check_word("", letters, word_dict)
    print(matching_words)

    # build dictionary from word list (cuz speed)
    matching_words_dict = set(matching_words)

    # compare input against matched dictionary
    while True:
        x = input("Type a word and see if it can be spelled: ").upper()
        print(x in matching_words_dict)

if __name__ == '__main__':
    main()


