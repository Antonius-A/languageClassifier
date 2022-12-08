import json
import time

english_dictionary = {}
french_dictionary = {}
#the create_dictionary function converts a list of words into a dictionary object where every word becomes a key (for extremely fast referencing)
def create_dictionary(filename="english.txt", language="english"):
    # filename="words_alpha.txt" #contains non english words (total over 400k entries)
    dictionary = {}

    # Using readlines()
    file = open(filename, 'r')
    lines = file.readlines()

    count = 0
    # Strips the newline character
    for line in lines:
        print(count)
        dictionary[str(line.strip())] = [language, count]
        count += 1

    print(dictionary)

    # write dictionary to file
    with open(f'{language}_dictionary.json', 'w') as convert_file:
        convert_file.write(json.dumps(dictionary))

    return dictionary

#the load_dictionary function loads a dictionary object from file to the global variable [english_dictionary]
def load_dictionary(filename='dictionary.json', language_dictionary=english_dictionary):
    start_time = time.time()

    # Opening JSON file
    file = open(filename)

    # JSON object as a dictionary
    language_dictionary = json.load(file)

    return language_dictionary


#the check_english function checks if a word is found in the dictionary object (derived from dictionary.json)
def check_english(word, print_statements=False):
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

#this function accepts a list of words or sentence string and returns a boolean value based on a threshold (with a default % of 80% english words in list)
def if_english(words=None, threshold=0.8,remove_foreign=True):
    # start_time = time.time()
    def convert_list_to_percentage(word_list):

        answers = []
        for word in word_list:
            answers.append(check_english(word))
        print(sum(answers)/len(answers))
        if remove_foreign:
            updated_word_list = remove_foreigners(word_list, answers)
        else:
            updated_word_list = word_list
        percentage = sum(answers)/len(answers)

        return percentage > threshold, percentage, updated_word_list

    if words is None:
        return "invalid parameters, enter a string or list or words"
    if isinstance(words, str):
        words = words.split(" ")
    if isinstance(words, list):
        return convert_list_to_percentage(words)

    else:
        return "invalid parameters, enter a string or list or words"


#the check_english function checks if a word is found in the dictionary object (derived from dictionary.json)
def check_language(word: object, print_statements: object = False) -> object:
    global english_dictionary, french_dictionary

    if word in english_dictionary and word in french_dictionary:
        if print_statements:
            print("Word in both dictionaries")
        return "both"
    elif word in french_dictionary:
        if print_statements:
            print("Word in french dictionary")
        return "fr"
    elif word in english_dictionary:
        if print_statements:
            print("Word in english dictionary")
        return "en"
    else:
        if print_statements:
            print("Word not in dictionary")
        return None

#this function accepts a list of words or sentence string and returns a boolean value based on a threshold (with a default % of 80% english words in list)
def det_main_language(words=None, threshold=0.7):
    # start_time = time.time()
    def calc_language(word_list):
        answers = []
        for word in word_list:
            answers.append(check_language(word, print_statements=False))
            en_count = answers.count("en")
            fr_count = answers.count("fr")
            both_count = answers.count("both")
            none_count = answers.count(None)

        if both_count/len(answers) == 1:
            return "bilingual"

        if (en_count + both_count)/len(answers) >= 0.7:
            return "english"

        if (fr_count + both_count)/len(answers) >= 0.5:
            return "french"

        if none_count/len(answers) > 0.5:
            return "foreign"

        return "null"

    if words is None:
        return "invalid parameters, enter a string or list or words"
    if isinstance(words, str):
        words = words.split(" ")
    if isinstance(words, list):
        return calc_language(words)
    else:
        return "invalid parameters, enter a string or list or words"


def remove_foreigners(word_list, answer_list):
    if len(word_list) != len(answer_list):
        return "invalid inputs, both lists must be of equal length."
    for i, b in reversed(list(enumerate(answer_list))):
    #     print(i)
        if answer_list[i] == None:
            del word_list[i]
    return word_list



if __name__ == '__main__':
    start_time = time.time()
    #create dictionaries
    # english_dictionary = create_dictionary("Language_Files/english_MIT100K.txt", "english")
    # french_dictionary = create_dictionary("Language_Files/francais.txt", "french")

    #load dictionaries once jsons have been generated
    english_dictionary = load_dictionary("english_dictionary.json", english_dictionary)
    french_dictionary = load_dictionary("french_dictionary.json", french_dictionary)

    start_time = time.time()
    #
    # # sentence = ["hello", "there", "anthony", "my", "name", "is", "roger", "bonjour"]
    # sentence = "hallo mein friend"
    # sentence = "hola senior i love apples"
    #
    # print(if_english(sentence)) #returns True with an english score of 87.5%
    #
    # print("---Query Completed in %s seconds ---" % "{0:.7f}".format(time.time() - start_time))


    sentence = ["hello", "there", "anthony", "my", "name", "is", "roger", "bonjour"]
    # sentence = "hallo mein friend"
    # sentence = "bonjour je suis un stagiaire"
    print("Sentence is predominantly:",det_main_language(sentence))  # returns True with an english score of 87.5%

    print("---Query Completed in %s seconds ---" % "{0:.7f}".format(time.time() - start_time))



