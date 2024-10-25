import pickle
f = open(r'11.txt', 'wb')
obj = ["Строка", (2, 3)]
pickle.dump(obj, f)
f.close()


f = open(r'11.txt', 'rb')
obj1 = pickle.load(f)

f.close()
pickle.dumps([1, 2])
