import nltk
import csv
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


train = []

with open('dot_examples.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        train.append((row['Text'], row['Classification']))


test = [
    ('why.', 'lvl_1'),
    ('critique', 'lvl_4')
]


cl = NaiveBayesClassifier(train)

# Classify a TextBlob
# example_sentence = "Can you really experience anything objectively.  Formulate, critique, then investigate your answer?"
example_sentence = "How would you describe ants?  Gather information to develop alternative explanations for?"
#example_sentence = "Gather information to develop alternative explanations for"

# print(cl.classify(example_sentence))

blob = TextBlob(example_sentence, classifier=cl)



for sentence in blob.sentences:
    print("Sentence: ", sentence)

    prob_dist = cl.prob_classify(sentence)

    print("Probability of Level 1 : ", round(prob_dist.prob("1"), 2))
    print("Probability of Level 2: ", round(prob_dist.prob("2"), 2))
    print("Probability of Level 3: ", round(prob_dist.prob("3"), 2))
    print("Probability of Level 4: ", round(prob_dist.prob("4"), 2))
    

    if (sentence.classify() == "1"):
        print("Level One: Recall")
    elif (sentence.classify() == "2"):
        print("Level Two: Skill/Concept")
    elif (sentence.classify() == "3"):
        print("Level Three: Strategic Thinking")
    else:
        print("Level Four: Extended Thinking")

    print("")


    

