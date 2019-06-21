# spacy NLP Learning

Must read of https://spacy.io/

Note: Make sure you followed the [setup](setup.md) document properly.

## spacy-101

Available ipython notebook [here](spacy-101.ipynb)

```py
import spacy

nlp = spacy.load('en')
doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
```

During text processing, spacy does

1. Tokenization i.e. segments it into words, punctuation and so on. More [here](https://spacy.io/usage/spacy-101#annotations-token)

```py
for token in doc:
    print(token.text)
```

2. Part-of-speech tags and dependencies

After tokenization, spaCy can **parse** and **tag** a given Doc. This is where the statistical **model** comes in, which enables spaCy to make a **prediction** of which **tag** or label most likely applies in this context. More [here](https://spacy.io/usage/spacy-101#annotations-pos-deps)

```py
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
```

3. Named Entities

A named entity is a "real-world object" that's assigned a name – for example, a person, a country, a product or a book title. More [here](https://spacy.io/usage/spacy-101#annotations-ner)

Named entities are available as the `ents` property of a `Doc`:

```py
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

4. Word Vectors and Similarity

spaCy is able to compare two objects, and make a prediction of **how similar they are**.
More [here](https://spacy.io/usage/spacy-101#vectors-similarity)

```py
tokens = nlp(u'dog cat banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.similarity(token2))
```

TODO: More from spacy-101, is pending

* [Linguistic Feautres](linguistic_feautures.md)