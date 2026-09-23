Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers=["one","two","three","four","five"]
>>> numbers
['one', 'two', 'three', 'four', 'five']
>>> numbers[0]
'one'
>>> numbers[3]
'four'
>>> item.append("six")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    item.append("six")
NameError: name 'item' is not defined. Did you mean: 'iter'?
>>> numbers.append("six")
>>> numbers
['one', 'two', 'three', 'four', 'five', 'six']
>>> numbers.append("Seven24")
>>> numbers
['one', 'two', 'three', 'four', 'five', 'six', 'Seven24']
>>> numbers.reverse()
>>> numbers
['Seven24', 'six', 'five', 'four', 'three', 'two', 'one']
>>> numbers.remove("three")
>>> numbers
['Seven24', 'six', 'five', 'four', 'two', 'one']
>>> 
>>> car=[]
>>> type(bus)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    type(bus)
NameError: name 'bus' is not defined
>>> type(car)
<class 'list'>
>>> numbers1=numbers
>>> numbers1
['Seven24', 'six', 'five', 'four', 'two', 'one']
>>> numbers1.pop()
'one'
>>> numbers1.append("eight")
>>> numbers1
['Seven24', 'six', 'five', 'four', 'two', 'eight']
>>> numbers1
['Seven24', 'six', 'five', 'four', 'two', 'eight']
>>> #Looping
>>> [i for i in numbers]
['Seven24', 'six', 'five', 'four', 'two', 'eight']
numbers
['Seven24', 'six', 'five', 'four', 'two', 'eight']

#CORM process= check once & runs many times
#FOR loop-Checks the condition only once and runs the loop till the condition is satisfied (n-1) times
for in in range(10):
    
SyntaxError: invalid syntax
for s in range(10):
    print(s)

    
0
1
2
3
4
5
6
7
8
9
 #LIST
list=["apple","banana","cherry"]
list
['apple', 'banana', 'cherry']
#LIST LENGTH
print(len(list))
3
list2=["one","two","three")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
list2=["one","two","three"]
list2
['one', 'two', 'three']
#CONTAIN DIFF DATA TYPES
list=["abc",True,75,"female"]
list
['abc', True, 75, 'female']
print(type(list))
<class 'list'>
list1=list["one","two","three"]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    list1=list["one","two","three"]
TypeError: list indices must be integers or slices, not tuple
list1=list(("one","two","three"))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    list1=list(("one","two","three"))
TypeError: 'list' object is not callable
thislist = list(("apple", "banana", "cherry"))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    thislist = list(("apple", "banana", "cherry"))
TypeError: 'list' object is not callable
mylist = ["apple", "banana", "cherry"]
thislist = list(("apple", "banana", "cherry"))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    thislist = list(("apple", "banana", "cherry"))
TypeError: 'list' object is not callable
list = ["apple", "banana", "cherry"]
thislist = list(("apple", "banana", "cherry"))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    thislist = list(("apple", "banana", "cherry"))
TypeError: 'list' object is not callable
print(thislist)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(thislist)
NameError: name 'thislist' is not defined
thislist = ["apple", "banana", "cherry"]
thislist = list(("apple", "banana", "cherry"))
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    thislist = list(("apple", "banana", "cherry"))
TypeError: 'list' object is not callable
mylist=["app","phone","chat"]
print(mylist[1])
phone
