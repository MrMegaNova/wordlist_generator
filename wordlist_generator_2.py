import argparse

def generate_wordlist(word, uppercase_positions):
    """
    Generates all possible combinations of a given word, with uppercase letters at specific positions
    """
    uppercase_positions = set(uppercase_positions) # convert to set for faster membership testing
    replacements = {'a': '@', 'o': '0'} # define replacements as a dictionary
    wordlist = [word] # add the original word to the wordlist
    for i in range(2**len(uppercase_positions)): # loop over all possible combinations of uppercase letters
        new_word = ''
        for j, char in enumerate(word):
            if j in uppercase_positions:
                if i & (1 << len(uppercase_positions) - 1 - list(uppercase_positions).index(j)): # check if the j-th position should be uppercase
                    char = char.upper()
            if char.lower() in replacements:
                char = replacements[char.lower()]
            new_word += char
        wordlist.append(new_word)
    return wordlist

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate all possible combinations of a word with uppercase letters at specific positions')
    parser.add_argument('-w', '--word', type=str, required=True, help='the word to generate combinations for')
    parser.add_argument('-up', '--uppercase-positions', type=int, nargs='+', required=True, help='the positions of uppercase letters in the word')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='the file to write the generated wordlist to (default: output.txt)')
    args = parser.parse_args()

    wordlist = generate_wordlist(args.word, args.uppercase_positions)

    with open(args.output, 'w') as f:
        for word in wordlist:
            f.write(word + '\n')

