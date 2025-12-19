myList = ['vasanth','kumar']
print(myList)
myList.append('Darshini')
print(myList)
myList2 = ['Darshini','Karthiga Menon']
myList.extend(myList2)
print(myList)
myList.remove('Darshini')
print(myList)
myList.pop(2)
print(myList)
print(myList.pop(2))
myList3 = ['Vasanth','Vasanth','Kumar','Vaganagar','Thiruthuraipoondai','Thanjavur','Chennai']
print(myList3.count('Vasanth'))
print(sorted(myList3))
print('****Replace Item****')
my_list = [10,20,30,40,50,60]
print(my_list)
my_list[1:2] = [60 , 66]
print(my_list)
print('****-List Comperhensive-***')
small_list = [item for item in range(0,16)]
print(small_list)
print('***-List Map function-***')
list1= [10,20,30]
result_list = list(map(lambda x:x+1,list1))
print(result_list)
print('***-Sum and average of all numbers in a list-***')
my_list1 = [10, 20, 30, 40, 50, 50]
total = 0
for x in my_list1:
        total +=x
print(f"Total --->",total)
print(f"Average --->",total/len(my_list1))
print('***-Reverse a list-***')
my_list2 = [10, 20, 30, 40, 50]
result_list = []
decrement = len(my_list2)
for x in my_list2:
    #result_list[decrement] = x
    decrement = decrement - 1
    if decrement < 0:
        result_list[decrement] = x
    
print(result_list)
print(my_list2[::-1])
print('***-Turn every item of a list into its square-***')
numbers = [1, 2, 3, 4, 5, 6, 7]
square_list = list(map (lambda x: x * x, numbers))
print(square_list)
print('***-Find Maximum and Minimum-***')
my_list3 = [8, 2, 15, 1, 9]
print(f"Maximum ",max(my_list3))
print(f"Minimum ",min(my_list3))
print('***-Count Occurrences-***')
sports1 = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
print(f"With Built-in function ", sports1.count('Football'))
print('***-List sort without build in function-***')
numbers = [5, 2, 8, 1, 9]
for index, num in enumerate(numbers):
        print(len(numbers))
        print(index+1)
        if (index+1) > len(numbers):
                print(numbers[index+1])
                
                


