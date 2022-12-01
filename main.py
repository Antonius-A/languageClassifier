import json
import time

english_dictionary = {}

#filename="words_alpha.txt"
def create_dictionary(filename="wordlist_MIT100k.txt"):
    global english_dictionary
    dictionary = {}

    # Using readlines()
    file = open(filename, 'r')
    lines = file.readlines()

    count = 0
    # Strips the newline character
    for line in lines:
        print(count)
        dictionary[str(line.strip())] = ["english", count]
        count += 1

    print(dictionary)

    # write dictionary to file
    with open('dictionary.json', 'w') as convert_file:
        convert_file.write(json.dumps(dictionary))

    english_dictionary = dictionary

    return dictionary


def load_dictionary(filename='dictionary.json'):
    global english_dictionary

    start_time = time.time()

    # Opening JSON file
    file = open(filename)

    # returns JSON object as
    # a dictionary
    english_dictionary = json.load(file)


def check_english(word, print_statements=True):
    global english_dictionary

    start_time = time.time()

    if word in english_dictionary:
        if print_statements:
            print("English word")
            print("---Query Completed in %s seconds ---" % "{0:.7f}".format(time.time() - start_time))
        return True
    else:
        if print_statements:
            print("Not english word")
            print("---Query Completed in %s seconds ---" % "{0:.7f}".format(time.time() - start_time))
        return False




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_dictionary()
    load_dictionary()
    # check_english('hola')

    sentence = ["hello", "there", "anthony","my","name","is","roger"]
    answers = []
    for word in sentence:
        answers.append(check_english(word))
    print(answers)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
