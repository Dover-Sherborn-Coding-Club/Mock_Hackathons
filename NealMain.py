import nltk     #Library import
nltk.download('wordnet')
nltk.download('punkt')
from nltk.corpus import wordnet
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
# from nltk.lm import Vocabulary

tokenizer = RegexpTokenizer(r'[\w]+')   #Regex
ps = PorterStemmer()

Letter = 0     #Setup
Scannedwords = []
Filter = input("Enter Filter (All if All, N for Noun, V for Verb, ect..):  ").casefold()
input_words = (input("Enter a Sentence:  ")).casefold()

words = tokenizer.tokenize(input_words)   #Regex implementation

# vocab = Vocabulary(words, unk_cutoff=2)
# print (vocab)

# print (words)

tokens = [i for i in words]      #FreqDist
freqs = nltk.FreqDist(tokens)
Occurence = [(wrd, freq) for wrd, freq in freqs.items()]
print (Occurence)

# tokens = nltk.tokenize.word_tokenize(words)
# fdist=FreqDist(tokens)
# print (fdist)

Input_Roots = input("Specific Roots?  ").casefold()  #Input for roots

if Input_Roots == "no" or "none":
    Input_Roots = False

for word in words:       #Mainpy
    try:
        type = wordnet.synsets(word)[0].pos()
        if word in Scannedwords:
            continue
        else:
            Scannedwords.append (word)  #Duplicates
    except IndexError:    #ignore
        continue
    # print (word, ":", type) 
    roots = ps.stem(word)   #Roots
    for i in word:
       Letter += 1  #Letter Count

    if Letter >= 6 and (type == Filter or Filter == "all") and (roots == Input_Roots or Input_Roots == False):   #Filter
        Letter = 0
        syn = wordnet.synsets(word)
        print ("---------------\n---------------")
        print (word, ":", type) 
        print ("---------------")
        print (word, "Definition:  ", syn[0].definition())
        print ("---------------")
        if input("Synonym? (T for True, F for False):  ").casefold() == "t":
            print ("---------------")
            print (word, "Synonym:  ", syn[0].lemmas()[0].name())
        else:
            continue
    else:
        Letter = 0
