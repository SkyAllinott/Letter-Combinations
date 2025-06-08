# All letters available
LETTERS = [
    'cgflbptsmd',
    'earthiuoyl',
    'ealtoinsrm',
    'plyamdkesx'
]


# Load the dictionary file into a set
def load_dict(path, word_filter):
    with open(path) as f:
        # discard words not matching filter
        return set(i.strip().upper() for i in f if word_filter(i.strip().upper()))

# check word can be written on dial
def check_word(word, letter_matrix):
    return len(word) == len(letter_matrix) and all([c in letter_matrix[i] for i, c in enumerate(word)])

def main():
    # load uppercased letters into hash matrix
    letter_matrix = [set(i.upper()) for i in LETTERS]

    # load dictionary and compare entries
    matching_words = load_dict("Dictionary.txt", lambda w: check_word(w, letter_matrix))
    print(matching_words)

    # compare input against matched dictionary
    while True:
        x = input("Type a word and see if it can be spelled: ").upper().strip()
        print(x in matching_words)

if __name__ == '__main__':
    main()

