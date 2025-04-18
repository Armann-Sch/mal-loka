# Libraries used
import numpy as np
from scipy import spatial

programname = "GloveAnalyzer"

# Global variables declared
modelA = {}
modelB = {}

distsA = {}
distsB = {}

# Accepts a filename as an argument and reads the file contents
# Glove vectors are assumed to have a dimension of 300
def load_glove_model(File):
    glove_model = {}

    with open(File, 'r') as f:
        for line in f:
            split_line = line.split()
            
            # Some tokens came out as two words sepearated by a space so
            # the systems checks to ensure it does not try to convert a
            # string to a float
            if (len(split_line) > 301):
                offset = len(split_line)-300
                word = " ".join(split_line[:offset])
                embedding = np.array(split_line[offset:], dtype=np.float64)            
            #if (len(split_line) == 302):
            #    word = split_line[0] + " " + split_line[1]
            #    embedding = np.array(split_line[2:], dtype=np.float64)
            else:
                word = split_line[0]
                embedding = np.array(split_line[1:], dtype=np.float64)
        
            glove_model[word] = embedding
        
        print(f"{len(glove_model)} words loaded!")
        return glove_model

###############################################################################
# Accepts a model object, a distance dict and a word                          #
# Updates the distance dictionary to to include an entry for the word that    # 
# contains a sorted list of tuples containing the other words and their       #
# euclidian distance from the original word.                                  #
###############################################################################
def make_sorted(model, word):
#    sort = {word: []}
    sort = []
    for k in model.keys():
        if k != word:
            if len(model[k]) == 302:
                print(k)
            sort.append((k, spatial.distance.euclidean(model[word], model[k])))
    sort = sorted(sort, key=lambda x: x[1])
    return sort

# Takes a model, main word string and integer n
# Returns the n closest words in terms of euclid
# distance from the main word along with the distance
def get_n_closest(model, main_word, n):
    return make_sorted(model, main_word)
    closest_words[:n]

# Takes a model, main word, float r as arguments
# Returns all the words with a euclid distance
# equal to or less than the provided range
# along with the distances
def get_within_range(model, main_word, r):
    in_range = []
    #search for words within range r

    return in_range

def print_resutls():
    return None

def save_results(ow):
    return None

def compare_word_n(word, n, wr):
    in_range_A = sorted(make_sorted(modelA, word)[:n])
    in_range_B = sorted(make_sorted(modelB, word)[:n])

    print(in_range_A)
    print(in_range_B)
    
    comparisons = {
        'average diff' : 0,
        'just A': [],
        'just B': [],
        'both': []
    }


    # wr determines whether results will be written over a file, appended to a file or printed int the terminal
    return word

#def compare_word_range(word, r, wr)

def prepare_models(A, B):
    global modelA
    global modelB
    modelA = load_glove_model(A)
    modelB = load_glove_model(B)
    #print(len(modelB['100']))
    #print(len(modelB['Sherlock']))
    compare_word_n('Sherlock', 30, True)

prepare_models("gloves/sherlock/vectors.txt", "gloves/14/model.txt")

# Dictionary for parsing commands
commands = {
    'help': ['h', 'help', 'commands'],
    'quit': ['q', 'quit', 'exit'],
    'compare': ['c', 'comp', 'compare'],
    'load': ['load'],
    'loadA': ['loada', 'la'],
    'loadB': ['loadb', 'lb'],
    'sizes': ['sizes'],
    'sizeA': ['sizeA'],
    'sizeB': ['sizeB'],
}

# Dictionary for holding descriptions for commands
commands_desc = {
    'help': 'h, help: List all commands and their descriptions\nh <cmd>, help <cmd>: Give the description of a specified command.',
    'load': 'load, l: '
}


print(f"Welcome to {programname}!\nInsert h for a list of commands")

# Loop that keeps the program running until the user tells it to quit
run = True
while run:
    # Input is read and parsed to see which action should be performed
    args = input("What would you like to do? ").split(" ")
    
    if len(args) != 0:
        args[0] = args[0].lower()
        
        if args[0] in commands['quit']:
            run = False
        
        elif args[0] in commands['compare']:
            print("comparing")
        
        elif args[0] in commands['load']:
            dists = {}
            if args[1].lower() == "a":
                modelA = load_glove_model(args[2])
            elif args[1].lower() == "b":
                modelB = load_glove_model(args[2])
            else:
                modelA = load_glove_model(args[1])
                modelB = load_glove_model(args[2])