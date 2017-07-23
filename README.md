## My Dictionary ![Travis-CI](https://travis-ci.org/zhcHoward/MyDictionary.svg?branch=master)

A small dictionanry program works in the console. In order to solve the problem that the dictionary I want to use does not have a Linux version, only Windows.

## Introduction

Now this program works for both English => Chinese and Chinese => English. Moreover, this program can display the pronouncation of a word if it is displayed in the website.

## How To Use

1. Clone this repo:

   `git clone https://github.com/zhcHoward/MyDictionary.git`

2. Enter the main directory:

   `cd MyDictionary`

3. Ensure you have Python3 and pip installed, then run command:

   `pip3 install -r requirements.txt`

   To install the necessary packages.

4. Run the program:

   `python3 dictionary.py <word-you-want-to-search> [dictionary]`

Make sure you use Python3, because this program is not tested under Python2, you may get unexpected errors with Python2.

Here are some examples of how it works:

**English => Chinese:**

```bash
python3 dictionary.py dictionary
英 [ˈdɪkʃənri], 美 [ˈdɪkʃəneri]
n. 词典，字典；[自]代码字典；
```

```shell
python3 dictionary.py "Erasure Code"
纠删码
```

**Chinese => English:**

```shell
python3 dictionary.py 词典
[cí diǎn]
释义 dictionary；lexicon；
```

By default, this program use `iciba` as the default dictionay, you can also use `youdao` if you prefer. Just add `youdao` to the command above:

```bash
python3 dictionary.py dictionary youdao
n. 字典；词典
```

More, if you prefer to use `youdao` dictionary by default, you can change settings in the `config.json` file.

## How It Works

This program simply send requests to the website and get the whole html content. Then it filters out the information that is needed. Last, this program formats all information and display it in the console.

## More Dictionaries

So far, this program has already full fill my requirements for an English-to-Chinese dictionary. So I may not keep develop it to support more dictionaies, but you can do that yourself.

To add support for new dictionary, you just need to implement a class that inherit from `DictionaryBase` and overwrite some functions in `DictionaryBase`. `youdao.py` and `iciba.py` under `Dictionary_APIs` folder are 2 examples.
