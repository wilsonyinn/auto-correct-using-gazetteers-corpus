import nltk
import Levenshtein
from nltk.corpus import gazetteers

#maps words to number of occurences
freq_dict = {}      

word_count = 0

#map words to number of occurences
for word in gazetteers.words():
    word_count += 1
    if word not in freq_dict:
        freq_dict[word] = 1
    else:
        freq_dict[word] += 1

print("\nWELCOME TO GAZETTEERS CORPUS\n")

input = input("ENTER A STRING: ")

#word exists
if input in freq_dict:
    print("\n", input, "is a complete and correct word as per corpus gazetteers, and its probability is", freq_dict[input]/word_count)

#word does not exist
else:
    
    #maps words to distance from input string
    distance_map = {}

    #list for storing words of top 5 closest
    results = []

    #map word to distance
    for word in gazetteers.words():
        distance_map[word] = Levenshtein.distance(input, word)

    li = sorted(distance_map.items(), key=lambda kv: (kv[1], kv[0]))
    
    #takes the first 5 from sorted li
    for i in range(5):
        results.append(li.pop(0)[0])

    #output top 5 words closest words
    print("\nTOP 5 CLOSEST WORDS\n ")
    for word in results:
        print(word, " : ", freq_dict[word]/word_count)


