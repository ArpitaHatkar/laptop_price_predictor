import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from pickle import dump

data = pd.read_csv("laptop.csv")
print(data.shape)
print(data.isnull().sum())

data["price"] = data["price"].str.replace(",","")

features = data.drop(["Timestamp","price"],axis=1)
target = data["price"]
print(features)
print(target)

nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

nfeatures.to_csv("features.csv")

x_train,x_test,y_train,y_test = train_test_split(nfeatures.values,target)

model1 = LinearRegression()
model1.fit(x_train,y_train)
score1 = model1.score(x_test,y_test)
print("Linear Regression --> score = ", round(score1 * 100,2),"%")


model2 = DecisionTreeRegressor()
model2.fit(x_train,y_train)
score2 = model2.score(x_test,y_test)
print("Decision Tree Regressor --> score = ",round(score2 * 100,2),"%")

model3 = RandomForestRegressor()
model3.fit(x_train,y_train)
score3 = model3.score(x_test,y_test)
print("Random Forest Regressor --> score = ",round(score3 * 100,2),"%")

with open("laptop_model.pkl","wb") as f:
	dump(model3,f)



