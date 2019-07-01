import pickle

a = ['a', 'b', 'c']
with open ('list.txt','wb') as f:
    pickle.dump(a, f)