import argparse
import itertools
import os

def generate_combinations(word, max_upper, uppercase_letters, uppercase_positions):
    # Convert uppercase letters to lowercase in word
    lowercase_word = word.lower()

    # Create a list to store the final combinations
    combinations = []

    # Create a list of all possible combinations of uppercase and lowercase letters
    for num_upper in range(min(max_upper, len(word)) + 1):
        for positions in itertools.combinations(range(len(word)), num_upper):
            # Create a copy of lowercase_word to modify
            current_word = list(lowercase_word)

            # Convert the selected positions to uppercase
            for pos in positions:
                if pos in uppercase_positions:
                    current_word[pos] = current_word[pos].upper()
                elif current_word[pos] in uppercase_letters:
                    current_word[pos] = current_word[pos].upper()

            # Append the current combination to the list
            combinations.append("".join(current_word))

    return combinations

if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Add the arguments
    parser.add_argument("-w", "--word", type=str, help="the word to generate combinations from")
    parser.add_argument("-mu", "--max-upper", type=int, default=1, help="the maximum number of uppercase letters allowed")
    parser.add_argument("-up", "--uppercase-letters", type=str, default="", help="comma-separated list of uppercase letters")
    parser.add_argument("-upp", "--uppercase-positions", type=str, default="", help="comma-separated list of positions where uppercase letters can be used")
    parser.add_argument("-o", "--output", type=str, default="output.txt", help="the name of the output file")

    # Parse the arguments
    args = parser.parse_args()

    # Get the word
    word = args.word

    # Get the maximum number of uppercase letters allowed
    max_upper = args.max_upper

    # Get the uppercase letters
    uppercase_letters = args.uppercase_letters.split(",")

    # Get the uppercase positions
    uppercase_positions = [int(p.strip()) - 1 for p in args.uppercase_positions.split(",") if p.strip().isdigit()]

    # Generate the combinations
    combinations = generate_combinations(word, max_upper, uppercase_letters, uppercase_positions)

    # Check if the output file already exists
    if os.path.isfile(args.output):
        overwrite = input("The output file already exists. Do you want to overwrite it? (y/n) ")
        if overwrite.lower() not in ["y", "yes"]:
            exit()

    # Write the combinations to the output file
    with open(args.output, "w") as f:
        for combination in combinations:
            f.write(combination + "\n")

    print(f"{len(combinations)} combinations generated and written to {args.output}")

