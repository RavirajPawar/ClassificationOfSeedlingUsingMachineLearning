import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
db = pd.read_csv('path/fileName.csv')
db= db.sample(frac=1)
db
split_index = int(len(db)*.4)
x_train= db.iloc[:,:5][:-split_index]
x_test= db.iloc[:,:5][-split_index:]
y_train= db.iloc[:,5][:-split_index]
y_test= db.iloc[:,5][-split_index:]
# Create linear regression object
regr = RandomForestClassifier(max_depth=2,random_state=1)
# Train the model using the training sets
regr.fit(x_train,y_train
print("PLEASE READ INSTRUCTION")
lista=[]
print("""
Kindly enter 5 features in sequence
1.Number of leaves: (seedling has upto 15 leaves)
2.Height of seeding: (in centimeter upto 20cm)
3.Color of seedling: (white 100, Maroon 101, brown 102, green 103, faint green 104, yellow 105)
4.Texture of seedling: (choose smooth 0 rough 1)
5.Length of leaf: (in centimeter upto 20cm)""")
r=1
for x in range(0,5):

    print("Enter feature",r)
    a=int(input())
    r=r+1
    lista.append(a)
import numpy as np
dc=np.array(lista)
dc=dc[:,np.newaxis]
print("We got result as")
d=dc.reshape(1,5)
regr_pred = regr.predict(d)
if regr_pred==1:
    print("Mango Seedling")

elif regr_pred == 2:
    print("Tomato Seedling")
elif regr_pred == 3:
    print("Peanut Seedling")
elif regr_pred == 4:
    print("Almond Seedling")
elif regr_pred == 5:
    print("Mustard Seedling")
elif regr_pred == 6:
    print("Coconut Seedling")
else:
    print("error 404 not found")
