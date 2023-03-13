import argparse
import itertools
import os


def generate_combinations(word, uppercase, max_upper):
    possible_cases = []
    for letter in word:
        if letter.lower() in uppercase:
            possible_cases.append([letter.lower(), letter.upper()])
        elif letter.lower() == 'o':
            possible_cases.append(['o', 'O', '0'])
        elif letter.lower() == 'a':
            possible_cases.append(['a', 'A', '@'])
        else:
            possible_cases.append([letter.lower()])

    combinations = list(itertools.product(*possible_cases))
    filtered_combinations = []
    for combination in combinations:
        if max_upper >= combination.count(''.join(filter(str.isupper, combination))):
            filtered_combinations.append(''.join(combination))
    return filtered_combinations


def write_to_file(file_path, contents):
    with open(file_path, 'w') as f:
        f.write(contents)


def main():
    parser = argparse.ArgumentParser(description='Générer toutes les combinaisons possibles de la chaine de caractère donnée.')
    parser.add_argument('-w', '--word', type=str, help='la chaine de caractère pour générer les combinaisons', required=True)
    parser.add_argument('-u', '--uppercase', type=str, help='les lettres qui peuvent être en majuscule', default='')
    parser.add_argument('-m', '--max-upper', type=int, help='le nombre maximum de lettres en majuscule', default=0)
    parser.add_argument('-o', '--output', type=str, help='le fichier de destination pour écrire les combinaisons', default='output.txt')

    args = parser.parse_args()

    if os.path.exists(args.output):
        while True:
            answer = input(f"Le fichier {args.output} existe déjà. Voulez-vous continuer et supprimer le fichier existant ? (y/n) ")
            if answer.lower() in ['y', 'yes']:
                os.remove(args.output)
                break
            elif answer.lower() in ['n', 'no']:
                print("Opération annulée.")
                return
            else:
                print("Répondez par y (oui) ou n (non).")

    combinations = generate_combinations(args.word, args.uppercase, args.max_upper)
    contents = '\n'.join(combinations)
    write_to_file(args.output, contents)


if __name__ == '__main__':
    main()

