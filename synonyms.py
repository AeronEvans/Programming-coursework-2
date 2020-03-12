'''Semantic Similarity: starter code

'''

import math
import re


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 2.
    '''
    
    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    '''Return the cosine similarity of sparse vectors vec1 and vec2,
    stored as dictionaries as described in the handout for Project 2.
    '''
    
    dot_product = 0.0  # floating point to handle large numbers
    for x in vec1:
        if x in vec2:
            dot_product += vec1[x] * vec2[x]
    
    # Make sure empty vectors don't cause an error -- return -1 as
    # suggested in the handout for Project 2.
    norm_product = norm(vec1) * norm(vec2)
    if norm_product == 0.0:
        return -1.0
    else:
        return dot_product / norm_product









def get_sentence_lists(text):
    text = text.lower() #make every word lowercase
    sentences = []
    for i in re.split("\. *|\! *|\? *",text):
        if len(i)>0:
            sentences.append(i)

    

    words = []
    for i in sentences:
        a = re.split("; |, |\'|: |- ?|\' ?|\" ?|-- ?|\\n *| |\(|\) ?",i)
        
        b = []
        for j in a:
            if len(j)>0:
                b.append(j)
        words.append(b)

    
    return(words)


def get_sentence_lists_from_files(filenames):

    

    for i in filenames:
        a = open(i, "r")
        a = a.read()
        return (get_sentence_lists(a))
    
    


def build_semantic_descriptors(sentences):
    maindic = {}

    for i in sentences:
        for j in i:
            maindic.setdefault(j, {})
            selfdic = {}
            for k in i:
                if k != j:
                    selfdic.setdefault(k, 0)
                    selfdic[k] += 1
            for x in selfdic:
                maindic[j].setdefault(x,0)
                maindic[j][x]+=1
    return(maindic)


def most_similar_word(word, choices, semantic_descriptors):

    sd = semantic_descriptors
    highest_score = 0
    highest_word = choices[0]

    if word not in sd:
        return None
    
    
    for i in choices:
        if i not in sd:
            pass
        else:
            same = 0
            in_word = 0
            in_check = 0
            for x in sd[word]:
                in_word += (sd[word][x])**2

        
            for j in sd[i]:
                in_check += (sd[i][j])**2
                if j in sd[word]:
                    same += sd[i][j]*sd[word][j]
            score = (same/((in_word+in_check)**0.5))
            if score > highest_score:
                highest_score = score
                highest_word = i
    return(highest_word)
    pass


def run_similarity_test(filename, semantic_descriptors):
    
    a = open(filename, "r")
    a = a.read()

    sentences = []
    for i in re.split("\. *|\! *|\? *|\\n",a):
        if len(i)>0:
            sentences.append(i)

    

    words = []
    for i in sentences:
        a = re.split("; |, |\'|: |- ?|\' ?|\" ?|-- ?|\\n *| |\(|\) ?",i)
        
        b = []
        for j in a:
            if len(j)>0:
                b.append(j)
        words.append(b)

    correct = 0
    total = 0
    for i in words:
        print("word",i[0])
        print("guess", most_similar_word(i[0],[i[1],i[2]], semantic_descriptors))
        print("right",i[1])
        print()
        if most_similar_word(i[0],[i[1],i[2]], semantic_descriptors) == i[1]:
            correct += 1
            total += 1
        else:
            total += 1

    
    print((correct/total)*100)
    pass




a = get_sentence_lists_from_files(["wp.txt"])



b = build_semantic_descriptors(a)

c = most_similar_word('man',['am', 'i','believe','certain'],b)

run_similarity_test("test.txt", b)
