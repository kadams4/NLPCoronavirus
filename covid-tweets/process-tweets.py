import pandas as pd
from sklearn.model_selection import train_test_split

root = "Labels/"

filenames = ["2020-03-"+str(i)+"-Labels" for i in range(12, 29)]

for filename in filenames:

    path = root + filename + ".csv"

    data = pd.read_csv(path)

    print(data.shape)

    #strings are already cleaned
    negative = data.loc[data['label'] == 1, "text"]
    neutral = data.loc[data['label'] == 0, "text"]
    positive = data.loc[data['label'] == 2, "text"]

    print(positive.shape)
    print(negative.shape)
    print(neutral.shape)

    #Shuffle in place
    positive = positive.sample(frac=1)
    neutral = neutral.sample(frac=1)
    negative = negative.sample(frac=1)

    def clean_and_write(data, filename, ):
        data = data.to_frame()
        data = data['text'].values.tolist()

        # remove duplicates
        data = list(set(data))

        # get rid of newlines
        data = [s.replace('\n', '\t') for s in data]

        f=open(filename,'w')
        s1='\n'.join(data)
        f.write(s1)
        f.close()

    for (df, suffix) in [(positive, 'pos'), (neutral, 'neu'), (negative, 'neg')]:
        train, test = train_test_split(df, test_size=0.2)

        clean_and_write(train, "Split/"+filename+'-train-70.'+suffix)
        clean_and_write(test, "Split/"+filename+'-test-30.'+suffix)
