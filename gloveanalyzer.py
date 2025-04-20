# Libraries used
import numpy as np
from scipy import spatial

programname = "GloveAnalyzer"

# Global variables declared
modelA = {}
modelB = {}

distsA = {}
distsB = {}

comparisons = {
        'word': '',
        'average diff' : 0,
        'just A': [],
        'just B': [],
        'both': []
    }

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
            else:
                word = split_line[0]
                embedding = np.array(split_line[1:], dtype=np.float64)
            
            if '@' not in word and '.com' not in word and '.org' not in word and '.net' not in word:
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

# Takes a model, main word, float r as arguments
# Returns all the words with a euclid distance
# equal to or less than the provided range
# along with the distances
def get_within_range(model, main_word, r):
    in_range = []
    #search for words within range r

    return in_range

def print_results(cmp):
    cmp_s1 = f"Comparison for \"{cmp['word']}\"\n"
    cmp_s2 = f"Nearby vectors only in A: {len(cmp['just A'])}\n"
    cmp_s3 = f"Nearby vectors only in B: {len(cmp['just B'])}\n"
    cmp_s4 = f"Nearby vectors in both: {len(cmp['both'])}\n"
    cmp_s5 = f"Average difference in vector distance: {cmp['average diff']}"
    cmp_string = cmp_s1+cmp_s2+cmp_s3+cmp_s4+cmp_s5
    print(cmp_string)
    while True:
        choice = input(f"To see the words in A , B or both, enter a, b or c. i for general info, To return to main menu enter blank. ").lower()
        c = ""
        if choice == 'a':
            c = 'just A'
        elif choice == 'b':
            c = 'just B'
        elif choice == 'c':
            c = 'both'
        elif choice == 'i':
            print(cmp_string)
        else:
            c = ''
        if c != '' and c != 'i':
            for w in cmp[c]:
                print(w)
        else:
            return


def save_results(ow):
    return None

def compare_word_n(word, n):
    compare = {
        'word': word,
        'average diff' : 0,
        'just A': [],
        'just B': [],
        'both': []
    }
    n = abs(n)

    if word not in modelA or word not in modelB:
        print("Word not found in or both models.")
        compare['word'] = ""
        return compare
    
    # List are sorted by distance in order to select the n closest
    # they are then sorted alphabetically to make comparing lists
    # simpler
    irA = sorted(make_sorted(modelA, word)[:n])
    irB = sorted(make_sorted(modelB, word)[:n])

    avr = 0
    i = 0
    j = 0
    total = 0
    count = 0
    
    while i < len(irA) and j < len(irB):
        # If the two words being compared are the same, add the word to the comparisons list both
        # in the form of a touple of the word and the difference in their eucledian distances
        if irA[i][0] == irB[j][0]:
            diff = irA[i][1]-irB[j][1]
            compare['both'].append((irA[i][0], diff))
            total += diff
            count += 1
            i += 1
            j += 1
        # If the word in model A is earlier alphabetically, add it to the comparisons list 'just A'
        # and increment i by 1
        elif irA[i][0] < irB[j][0]:
            compare['just A'].append(irA[i])
            i += 1
        # Conversely if the word in model B is earlier, add it to the comparisons list 'just B' and
        # increment j by 1
        else:
            compare['just B'].append(irB[j])
            j += 1
    
    if count != 0:
        avr = total/count
    compare['average diff'] = avr
    
    return compare

#def compare_word_range(word, r, wr)

def prepare_models(A, B):
    global modelA
    global modelB
    global comparisons
    modelA = load_glove_model(A)
    modelB = load_glove_model(B)
    
    comparisons = compare_word_n('Sherlock', 30)

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
    'print': ['print', 'p'],
    'save': ['save', 's']
}

# Dictionary for holding descriptions for commands
commands_desc = {
    'help': 'h, help <command>: List all commands and their descriptions\nh <cmd>, help <cmd>: Give the description of a specified command.',
    'quit': 'q, quit, exit: Exit the program.',
    'load': 'load, l <modelname1> <modelname2>: Load two models',
    'loada': 'loada, la <filename>: Load a model into the modelA object.',
    'loadb': 'loadb, lb <filename>: Load a model into the modelB object.',
    'sizes': 'sizes: Displays the number of entries in both models',
    'sizea': 'sizeA: Displays the number of entries in modelA.',
    'sizeb': 'sizeB: Displays the number of entries in modelB.',
    'print': 'print, p: Prints information about the last comparison in the terminal, enters a menu letting you see particular subsets of words using different commands.',
    'save': 'save, s <filename> <w|a>: Save the last comparison to a file, an optional parameter w or a to instruct it to overwrite or append to the file. It will append by default.'    
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
        
        elif args[0] in commands['help']:
            if len(args) >1:
                if args[1].lower() in commands:
                    print(commands_desc[args[1].lower()])
            else:
                for c in commands_desc:
                    print(commands_desc[c])

        elif args[0] in commands['compare']:
            n = 100
            if len(args) == 1:
                print("You must give a word to prefer, and optionally a number of nearest words.")
            else:
                w = args[1]
            if len(args) > 2:
                if args[2].isdigit():
                    n = int(args[2])
                else:
                    print("n must be a valid integer")
            comparisons = compare_word_n(w, n)
            print_results(comparisons)
        
        elif args[0] in commands['load']:
            if len(args) >= 3:
                modelA = load_glove_model(args[1])
                modelB = load_glove_model(args[2])
            else:
                print("You must enter two filenames")
        
        elif args[0] in commands['loadA']:
            if len(args) > 1:
                modelA = load_glove_model(args[1])
            else:
                print("You must enter file name.")
        
        elif args[0] in commands['loadB']:
            if len(args) > 1:
                modelB = load_glove_model(args[1])
            else:
                print("You must enter file name.")
        
        elif args[0] in commands['sizes']:
            print(f"ModelA: {len(modelA)} entries.\nModelB: {len(modelB)} entries.")

        elif args[0] in commands['sizeA']:
            print(f"ModelA: {len(modelA)} entries.")

        elif args[0] in commands['sizeB']:
            print(f"ModelB: {len(modelB)} entries.")

        elif args[0] in commands['print']:
            print_results(comparisons)