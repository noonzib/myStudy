import pickle

with open('list.txt', 'rb') as f:
    data = pickle.load(f)
print (data)