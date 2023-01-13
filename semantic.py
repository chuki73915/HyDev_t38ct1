import spacy

# Loading advanced English model
nlp = spacy.load("en_core_web_md")

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# It is interesting that although there are similarities between an apple and banana and between a cat and monkey,
# the scores of similarities are not similar to each other.

print("----------------------------------------------------------------")

# Loading basic English model
nlp = spacy.load("en_core_web_sm")

tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

"""The sm language model does not have the accuracy of the advanced md model. 
The results are vastly different from the first code, e.g the similarity between cat and apple is higher than 
monkey and banana in the second code."""
