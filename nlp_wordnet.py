from nltk.corpus import wordnet

syns = wordnet.synsets("program")

# synset
print(syns[0].name())

# just the word
print(syns[0].lemmas()[0].name())

# definition
print(syns[0].definition())

# example
print(syns[0].examples())

synonyms = []
antonyms =  []

for syn in wordnet.synsets("good"):
	for l in syn.lemmas():
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())

# Print synonyms and antonyms for the word "good"
# print(set(synonyms))
# print(set(antonyms))


# symantic similiarties
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("plane.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("bird.n.01")
print(w1.wup_similarity(w2))