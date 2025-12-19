import copy
myList = [[1,2,3],[4,5,6]]
shallowCopy = myList.copy()
deepCopty = copy.deepcopy(myList)
print(myList)
print(shallowCopy)
print(deepCopty)
print("***After Changes***")
myList[1][0] = 6
print(f"Ordiginal -->", myList)
print(f"Shallow Copy--->", shallowCopy)
print(f"Deep Copy---->", deepCopty)
