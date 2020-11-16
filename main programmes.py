import requests
import pickle

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
#print(data)

lst1 = data.split("\n")
print(lst1)

lst2 = [item.split(",") for item in lst1 if len(item)!=0]
print(lst2)

with open("myiris.pkl","wb") as f:
    pickle.dump(lst2, f)


############ This section of code is used to read the pickle file-------
# import pickle
# with open("myiris.pkl","rb") as f:
#     print(pickle.load(f))


