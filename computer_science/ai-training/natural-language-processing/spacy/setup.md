# spacy setup

## v2

Windows

From Anaconda

Creating conda environment

```sh
$ conda create -y -n spacy2 python=3.6 anaconda
```

Activating

```sh
$ activate spacy2
```

Installing spacy

```sh
$ conda install -y spacy=2
```

Installing Language models

```sh
$ python -m spacy download en
```

the above command will give the information about which it is connecting to download the model.
Ex: https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.0.0/en_core_web_sm-2.0.0.tar.gz

If you face any issues from above command, we can manually download and install the same.

Install from the downloaded zip using pip

```
$ pip install en_core_web_sm-2.0.0.tar.gz
```

Now we can link the installed model with a language name, go to site-packages then run

Assuming Anaconda installed directory is lets say `D:\softs\anaconda\`.

Then the environment we created will be under `D:\softs\anaconda\envs\spacy2\`

Then the installed modules site-packages will be under `D:\softs\anaconda\envs\spacy2\Lib\site-packages\`

For Windows, make sure you run the below commands as `administrator`, if not the model linking may fail.

```sh
$ # changing directory
$ cd D:\softs\anaconda\envs\spacy2\Lib\site-packages\
$ python -m spacy link en_core_web_sm en
```

For running jupyter notebooks, update the `jupyter` module, assuming the conda environment is activated.

```sh
$ pip install jupyter
```