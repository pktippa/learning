# spaCy Linguistic Features

https://spacy.io/usage/linguistic-features

[IPython Notebook](Linguistic_features.ipynb)

## Rule-based Morphology

Inflectional morphology (can also have anogther forms, see [here](https://en.wikipedia.org/wiki/Inflection#Inflectional_morphology)) is the process by which a root form of a word is modified by adding prefixes or suffixes that specify its grammatical function but do not changes its part-of-speech. We say that a **lemma** (root form) is **inflected**(modified/combined) with one or more **morphological features** to create a surface form.

More [here](https://spacy.io/usage/linguistic-features#rule-based-morphology)

## Noun Chunks

Noun chunks are "base noun phrases" – flat phrases that have a noun as their head. You can think of noun chunks as a noun plus the words describing the noun – for example, "the lavish green grass" or "the world's largest tech fund". To get the noun chunks in a document, simply iterate over `Doc.noun_chunks`. More [here](https://spacy.io/usage/linguistic-features#noun-chunks)

```py
nlp = spacy.load('en')
doc = nlp(u'Autonomous cars shift insurance liability toward manufacturers')
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
          chunk.root.head.text)
```

TODO: till Tokenization, see the ipynb

https://spacy.io/usage/linguistic-features#how-tokenizer-works

TODO: Documentation contribution, add steps for suffix case algorithm summarization

## Hooking an arbitrary tokenizer into the pipeline

The tokenizer is the first component of the processing pipeline and the only one that can't be replaced by writing to `nlp.pipeline`. This is because it has a different signature from all the other components: it takes a text and returns a `Doc`, whereas all other components expect to already receive a tokenized `Doc`.