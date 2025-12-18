myDictionary = {
    "name" : "Vasanthakumar",
    2 : 41,
    156.6 : 'height'
    }
myDictionary1 = {
    76 : 'weight',
    'Qualification' : 'MCA',
    'native' : 'Vaganagar , ThiruthuraiPoondai'
    }
print(myDictionary)
print(myDictionary.get('city'))
print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary.items())
myDictionary.update(myDictionary1)
print(myDictionary)
print(myDictionary.pop(76))
print(myDictionary.popitem())
squares = {x: x*x for x in range(6)}
print(squares)
keys = ["name","age","qualification"]
print(dict.fromkeys(keys,"vasanthakumar"))
