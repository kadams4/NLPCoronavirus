import pandas as pd

root = "Split/"

types = ["train-70", "test-30"]

for type in types:
    filenames = ["2020-03-"+str(i)+"-Labels-"+type for i in range(12, 29)]

    for suffix in ["pos", "neg", "neu"]:

        data = []

        for filename in filenames:

            path = root + filename
            data += list(open(path+"."+suffix, "r", encoding='utf-8').readlines())

        print(len(data))
        with open('covid-tweets-'+type+'.'+suffix,'w') as f:
            f.write(''.join(data))
