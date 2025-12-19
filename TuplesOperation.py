myTuple = ("vasanthakumar",41,'MCA',"Vaganagar, Thiruthuraipoondai",'Thanjavur','Chennai')
print(myTuple)
print(list[myTuple])
name, age, qualification, native, study, rightNow = myTuple
print(age, native)
myTuples1 = ("vasanthakumar")
print(myTuples1 *3)
print('MCA' in myTuple)
t = (1, 2, 3, 4, 5,6)
a, b, *c = t
print(c)
print(t.index(4))
print(t[1:4])
d = {
    ('firstName', 'lastName'): "vasanthakumar",
    ('ug','pg') : ('B.sc','MCA')
     }
print(d)
      
