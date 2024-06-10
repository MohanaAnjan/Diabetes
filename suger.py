import pandas as pd
import numpy as np 
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
#streamlit
import streamlit as st



df=pd.read_csv("D:/GUVI/DIABETIS/diabetes_prediction_dataset.csv")

# data cleaning
df.drop_duplicates(inplace=True)
encoder=LabelEncoder()
df.gender=encoder.fit_transform(df[["gender"]])
df.smoking_history=encoder.fit_transform(df[["smoking_history"]])


# dependent,independent fixing
x=df.drop('diabetes',axis=1)
y=df.diabetes


#train,test split
x_test,x_train,y_test,y_train=train_test_split(x,y,test_size=0.15)

#algorithm Selection 
# dependent is catagory so go for classifier algorithms

model = GradientBoostingClassifier().fit(x_train, y_train)
y_pred=model.predict(x_test)


