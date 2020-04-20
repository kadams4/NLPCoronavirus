import pandas
import re
import numpy as np
import csv

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower() + " . "

reviews = pandas.read_csv("reviews.csv", index_col="id")
reviews.loc[:, "Text"] = reviews.loc[:, "Text"].apply(clean_str)
bad = reviews.loc[reviews['Positivity'] == 0, "Text"]
good = reviews.loc[reviews['Positivity'] == 1, "Text"]

print(reviews.iloc[0:20])

bad.to_csv('review-polarity.neg', header=False, index=False, sep='\n', mode='a')
good.to_csv('review-polarity.pos', header=False, index=False, sep='\n', mode='a')
