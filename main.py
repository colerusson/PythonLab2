import json
import string
import argparse
import os


def main(inputString):
    # Write the code to count the number of words here
    # Remember to save the dictionary as a json file named "word-counts.json"
    string_input = inputString
    string_input.translate(str.maketrans('', '', string.punctuation))
    string_list = string_input.split()

    wordDict = {}

    for i in string_list:
        if i not in wordDict:
            wordDict[i.lower()] = string_list.count(i)

    json_object = json.dumps(wordDict, indent=4)

    return json_object


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s", "--string", type=str, required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)
