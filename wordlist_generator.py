import itertools
import argparse
import os

def generate_combinations(word, max_upper, uppercase_letters):
    num_combinations = 0
    with open("output.txt", "w") as f:
        for i in range(max_upper + 1):
            for combination in itertools.combinations(uppercase_letters, i):
                for variation in itertools.product([False, True], repeat=len(word)):
                    new_word = ''
                    for j, letter in enumerate(word):
                        if letter.lower() in uppercase_letters:
                            if letter.lower() in combination:
                                new_word += letter.upper()
                            else:
                                new_word += letter.lower()
                        elif letter.lower() == 'o':
                            if variation[j]:
                                new_word += '0'
                            else:
                                new_word += 'o'
                        elif letter.lower() == 'a':
                            if variation[j]:
                                new_word += '@'
                            else:
                                new_word += 'a'
                        else:
                            new_word += letter
                        
                    f.write(new_word + '\n')
                    num_combinations += 1

    return num_combinations


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate combinations of a given string')
    parser.add_argument('-w', '--word', type=str, required=True, help='The input string to generate combinations from')
    parser.add_argument('--max-upper', type=int, default=2, help='The maximum number of uppercase letters to allow in the combinations')
    parser.add_argument('--uppercase', type=str, default='', help='Comma-separated list of letters that can be uppercase')
    args = parser.parse_args()

    if os.path.exists('output.txt'):
        response = input('Output file already exists. Do you want to continue and overwrite it? (y/n): ')
        if response.lower() != 'y' and response.lower() != 'yes':
            print('Exiting script...')
            exit()

    uppercase_letters = args.uppercase.lower().split(',')
    word = args.word.lower()

    num_combinations = generate_combinations(word, args.max_upper, uppercase_letters)
    print(f'{num_combinations} combinations written to output.txt')

