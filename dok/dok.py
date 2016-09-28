import nltk
import csv
from textblob.classifiers import NaiveBayesClassifier
from nltk.tokenize import sent_tokenize


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
# example_sentence = "Can you really experience anything objectively."
# example_sentence2 = "Gather information to develop alternative explanations for"
example_sentence = "How would you describe ants?  Gather information to develop alternative explanations for?"

# This function prints the probability
def print_probability(sentence):
	print(sentence)
	prob_dist = cl.prob_classify(sentence)
	print("Probability of Level 1: ", (round(prob_dist.prob("1"), 2) * 100), "%")
	print("Probability of Level 2: ", (round(prob_dist.prob("2"), 2) * 100), "%")
	print("Probability of Level 3: ", (round(prob_dist.prob("3"), 2) * 100), "%")
	print("Probability of Level 4: ", (round(prob_dist.prob("4"), 2) * 100), "%")


	if (cl.classify(sentence) == "1"):
		print("Level One: Recall")
	elif (cl.classify(sentence) == "2"):
		print("Level Two: Skill/Concept")
	elif (cl.classify(sentence) == "3"):
		print("Level Three: Strategic Thinking")
	else:
		print("Level Four: Extended Thinking")


# Code to analysis each sentence.  One at a time.
sentence = sent_tokenize(example_sentence)
for i in sentence:
	print_probability(i)

    

