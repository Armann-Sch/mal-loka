import numpy as np

def load_glove_model(File):
    glove_model = {}
    with open(File, 'r') as f:
        for line in f:
            split_line = line.split()
            if (len(split_line) == 302):
                word = split_line[0] + " " + split_line[1]
                embedding = np.array(split_line[2:], dtype=np.float64)
            else:
                word = split_line[0]
                embedding = np.array(split_line[1:], dtype=np.float64)
            glove_model[word] = embedding
        print(f"{len(glove_model)} words loaded!")
        return glove_model

def get_n_closest(model, main_word, n):
    closest_words = []
    # Search for n closest vectors

    return closest_words

def get_within_range(model, main_word, r):
    in_range = []
    #search for words within range r

    return in_range

def get_distance(vecA, vecB):
    s = 0
    for i in range(len(vecA)):
        s += np.square(vecA[i]-vecB[i])
    return np.sqrt(s)

args = input().split(" ")
inA = args[0]
inB = args[1]

#modelA = load_glove_model(inA)
#modelB = load_glove_model(inB)
conversion_rules = []

if len(args) > 2:
    inC = args[2]


modelA = load_glove_model("gloves/sherlock/vectors.txt")
modelB = load_glove_model("gloves/14/model.txt")
print(modelA['Holmes'])
print(modelB['Holmes'])
print(modelA['Holmes']-modelB['Holmes'])
print(get_distance(modelA['Holmes'], modelB['Holmes']))