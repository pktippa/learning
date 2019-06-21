# Introduction to NLP

https://udemy.com/natural-language-processing/

## Environment Setup

* Anaconda installed
* Create new environment

```sh
$ conda create -y -n udemy_nlp python=3.6 anaconda
```

* Activate the Environment

```sh
$ source activate udemy_nlp
```

* Installing Dependencies
  * Python packages

    ```sh
    $ pip install -r requirements.txt
    ```
  * NLTK required downloads

    ```sh
    $ python nltk_downloads.py
    ```

## NLTK - Natural Language Toolkit

www.nltk.org

It is used to analyze the natural language in python. It is collection of Python modules and data sets that implement natural language processing techniques.

* Working on Word Count, see [Counting](Counting.ipynb)
* Average Words per sentence, per Year and plotting [here](Example_Words_Per_Sentence_Trends.ipynb)
* Frequency Distribution of Words [here](Frequency_Distribution.ipynb)
* Conditional Frequency Distribution of Words [here](Conditional_Frequency_Distribution.ipynb)
* Informative words by Example [here](Informative_Words_Example.ipynb)
* Bigrams, Trigrams, Ngrams [here](Bigrams_trigrams_ngrams.ipynb)
* Tokenization [here](Tokenization.ipynb)
* Normalizing [here](Normalizing.ipynb)
* Parts of Speech [here](09_Parts_of_Speech.ipynb)