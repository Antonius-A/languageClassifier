import json
import time

english_dictionary = {}

#the create_dictionary function converts a list of words into a dictionary object where every word becomes a key (for extremely fast referencing)
def create_dictionary(filename="wordlist_MIT100k.txt"):
    # filename="words_alpha.txt" #contains non english words (total over 400k entries)
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

#the load_dictionary function loads a dictionary object from file to the global variable [english_dictionary]
def load_dictionary(filename='dictionary.json'):
    global english_dictionary

    start_time = time.time()

    # Opening JSON file
    file = open(filename)

    # returns JSON object as
    # a dictionary
    english_dictionary = json.load(file)

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
def if_english(words=None, threshold=0.8):
    start_time = time.time()
    def convert_list_to_percentage(word_list):

        answers = []
        for word in word_list:
            answers.append(check_english(word))
        #print(sum(answers)/len(answers))
        return sum(answers)/len(answers) > threshold

    if words is None:
        return "invalid parameters, enter a string or list or words"
    if isinstance(words, str):
        words = words.split(" ")
    if isinstance(words, list):
        result =  convert_list_to_percentage(words)
        print("---Query Completed in %s seconds ---" % "{0:.7f}".format(time.time() - start_time))
        return
    else:
        return "invalid parameters, enter a string or list or words"



if __name__ == '__main__':
    # create_dictionary()
    load_dictionary()
    # check_english('hola')

    sentence = ["hello", "there", "anthony", "my", "name", "is", "roger", "bonjour"]
    print(if_english(sentence)) #returns True with an english score of 87.5%

