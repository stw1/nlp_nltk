from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


train = [
    ('draw', 'lvl_1'),
    ('define', 'lvl_1'),
    ('calculate', 'lvl_1'),
    ('arrange', 'lvl_1'),  
    ('repeat', 'lvl_1'),
    ('recall', 'lvl_1'), 
    ('recite', 'lvl_1'),
    ('tell', 'lvl_1'),  
    ('state', 'lvl_1'),
    ('who', 'lvl_1'), 
    ('what', 'lvl_1'),
    ('when', 'lvl_1'),  
    ('where', 'lvl_1'),
    ('why', 'lvl_1'), 
    ('name', 'lvl_1'),
    ('list', 'lvl_1'),  
    ('label', 'lvl_1'),
    ('illustrate', 'lvl_1'), 
    ('measure', 'lvl_1'),
    ('quote', 'lvl_1'),  
    ('match', 'lvl_1'),
    ('memorize', 'lvl_1'),  
    ('infer', 'lvl_2'),
    ('categorize', 'lvl_2'),
    ('collect', 'lvl_2'),
    ('display', 'lvl_2'),
    ('identify', 'lvl_2'),
    ('patterns', 'lvl_2'),
    ('organize', 'lvl_2'),
    ('construct', 'lvl_2'),
    ('modify', 'lvl_2'),
    ('perdict', 'lvl_2'),
    ('interpret', 'lvl_2'),
    ('distinguish', 'lvl_2'),
    ('context', 'lvl_2'),
    ('observation', 'lvl_2'),
    ('summarize', 'lvl_2'),
    ('show', 'lvl_2'),
    ('relate', 'lvl_2'),
    ('compare', 'lvl_2'),
    ('estimate', 'lvl_2'),
    ('cause', 'lvl_2'),
    ('effect', 'lvl_2'),
    ('separate', 'lvl_2'),
    ('graph', 'lvl_2'),
    ('classify', 'lvl_2'),
    ('assess', 'lvl_3'),
    ('revise', 'lvl_3'),
    ('apprise', 'lvl_3'),
    ('compare', 'lvl_3'),
    ('critique', 'lvl_3'),
    ('formulate', 'lvl_3'),
    ('hypothesize', 'lvl_3'),
    ('differentiate', 'lvl_3'),
    ('investigate', 'lvl_3'),
    ('construct', 'lvl_3'),
    ('prove', 'lvl_4'),
    ('design', 'lvl_4'), 
    ('connect', 'lvl_4'),
    ('synthesize', 'lvl_4'), 
    ('apply concepts', 'lvl_4'),
    ('critique', 'lvl_4'), 
    ('analyze', 'lvl_4'),
    ('create', 'lvl_4')
]

test = [
    ('why.', 'lvl_1'),
    ('critique', 'lvl_4')
]


cl = NaiveBayesClassifier(train)

# Classify a TextBlob
example_sentience = "Can you really experience anything objectively.  Formulate, critique, then investigate your answer?"

blob = TextBlob(example_sentience, classifier=cl)



for sentence in blob.sentences:
    print(sentence)
    if (sentence.classify() == "lvl_1"):
        print("Level One: Recall")
    elif (sentence.classify() == "lvl_2"):
        print("Level Two: Skill/Concept")
    elif (sentence.classify() == "lvl_3"):
        print("Level Three: Strategic Thinking")
    else:
        print("Level Four: Extended Thinking")

# Compute accuracy
accuracy = cl.accuracy(test)
print("Accuracy: {0}".format(accuracy))

prob_dist = cl.prob_classify(example_sentience)
print("Level 1: ", round(prob_dist.prob("lvl_1"), 2))
print("Level 2: ", round(prob_dist.prob("lvl_2"), 2))
print("Level 3: ", round(prob_dist.prob("lvl_3"), 2))
print("Level 4: ", round(prob_dist.prob("lvl_4"), 2))

cl.show_informative_features(5)