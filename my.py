

################# Program to connvert days into min || sec || hours
def days_to_units(days,unit):
    if days>0:
        if unit=='sec':
            return f"{days} days have {days*24*60*60} {unit}"
        elif unit=='min':
            return  f"{days} days have {days*24*60} {unit}"
        elif unit=='hours':
            return f"{days} days have {days*24} {unit}"
        else:
             return "Wrong input"
    else:
      return "days must > 0"



days=""
while days !='exit':
    days=input("Enter no of days like 10,20: Enter exit for close   : ")
    try:
        unit=input("Enter unit min sec hours: ")
        print(type(days))
        days_list=days.split(',')
        print(type(days_list))
        print(days_list)
        days_set=set(days_list)
        print(type(days_set))
        print(days_set)

        for item in days_set:
         
            result_string=days_to_units(int(item),unit)
            print(result_string)
    except  ValueError:
        print("Enter digits only")


'''
    Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
################ Loops ###################
## While:
'''
## Lists####
#list allows duplicates
name_list=['hamza','ali','daniyal']
print(type(name_list))
print(name_list)

for item in name_list:
    print(item)
    #accessing last item:
print(name_list[-1])
    #sort list
name_list.sort()
print(name_list)

'''

'''
    List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

'''

'''
######## Tuple ###
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))

    #update item to tuples
y=list(thistuple)
y[0]="banana"
thistuple=tuple(y)
print(type(thistuple))
print(thistuple)
'''

'''
#####     Sets
# unchangeable , unordered , dup val are not allowed    

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
thisset1 = {"apple", "banana", "daniyal"}
#union of sets
thisset.update(thisset1)

print(thisset)
'''

'''
Get a list of the keys:
x = thisdict.keys()

'''
####Python Dictionaries''''
    ##Dictionaries are used to store data values in key:value pairs.
    ##A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


