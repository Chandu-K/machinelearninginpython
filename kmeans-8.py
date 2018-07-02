#https://pythonprogramming.net/static/downloads/machine-learning-data/titanic.xls
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing, cross_validation
import pandas as pd


df=pd.read_excel('titanic.xls')
print(df.head())

df.drop(['body','name'],1,inplace=True)

df.convert_objects(convert_numeric=True)
df.fillna(0,inplace=True)
print(df.head())

def handle_non_numerical_data(df):
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1

            df[column] = list(map(convert_to_int, df[column]))

    return df

	
	
df=handle_non_numeric_data(df)
print(df.head())

df.drop(['sex','boat'], 1, inplace=True)

X = np.array(df.drop(['survived'], 1).astype(float))
X = preprocessing.scale(X)
y = np.array(df['survived'])

clf = KMeans(n_clusters=2)
clf.fit(X)

correct = 0
for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
	'''z.reshape(-1,1)
	array([[ 1],
   [ 2],
   [ 3],
   [ 4],
   [ 5],
   [ 6],
   [ 7],
   [ 8],
   [ 9],
   [10],
   [11],
   [12]])
   z.reshape(-1, 2)
	array([[ 1,  2],
   [ 3,  4],
   [ 5,  6],
   [ 7,  8],
   [ 9, 10],
   [11, 12]])'''
    prediction = clf.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print(correct/len(X))
