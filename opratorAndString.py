
'''logical operators
1.)And
2.)or
3.)not
'''
'logical operators\n1.)And\n2.)or\n3.)not\n'
not True

not int(bool(0))#typecasting

bool(1)

not 1

not 0

#EXAMPLE 1
zero=0
one=1
print(f"boolean of {zero} is {bool(zero)}")
print(f"boolean of {one} is {bool(one)}")
print(f"negation of {zero} is {not zero} and negation of {one} is {not one}")
print("\n............")



#EXAMPLE 2
negative_number=-5
positive_nume=5
print(f"boolean of {negative_number} is {bool(negative_number)}")
print(f"boolean of {positive_nume} is {bool(positive_nume)}")
print(f"negation of {negative_number} is {not negative_number} and negation of {positive_nume} is {not positive_nume}")
print("\n............")

#logical "and" operator

#EXAMPLE 1
#logical and
VEGETABLE=True
SALT=False
DISH=VEGETABLE and SALT
print(f"dish contains vegetables:{VEGETABLE}")
print(f"dish contains SALT:{SALT}")
print(f"hence dish prepared are good:{DISH}")


'''
EQUALITY OPERATORS:
1.)is   :-(a and b return true if variables /identifiers a and b points to the same object)
2.)is not   :-(a and b return true if variables /identifiers a and b points to te different objects)
3.)==    :-(a and b return true if variables /identifiers a and b has same value)
4.)!=   :-(a and b return true if variables /identifiers a and b has different value)
'''


list_a=[1,2,3,4]
list_b=[1,2,3,4]
print(id(list_a))# it give address where the list stored
print(id(list_b))





list_a == list_b


#same address 
str1="anu"
str2="anu"
print(id(str1))
print(id(str2))



#different address
str1="anu"
str2="anu1"
print(id(str1))
print(id(str2))

list_a
print(list_a)#it prints list a
list_a[0]#it print the elemen of list having index 0 i.e,1
list_a[0]=10 #it updates the value at index 0

print(list_a)

str1
print(str1)#it prints str1
print(str1[0])#it print the element of string having index 0 i.e,a
#str1[0]="b"  :-it is not possible in string it throws an error
#so we can say that the string are immutable/non mutable which means once you can define it you can
#you can replace the character but not change the


var=10
bin(10)
#0b indicates binarry
#bin() function is used for the binary conversion


'''
STRING:
 it define within single qoutes '' or within "" double qoutes
#string are immutable i.e, we cann't change its element which is present inside this
#string ha several in built function like "join,lower ,upper and so on"
"hi how are you?"


'''
str1="hi how do you do?"
print(str1)

str2="hi what are you doing now?"
print(str2)
print(str2[5])
print(str2[5:])
print(str2[5:11])
print(str2[-1])
print(str2[-1:])
print(str2[:-1])

print(str2[::-1])#it reverse the string
print(str2.find("o"))#it is used to find the index of "o"

len(str2)#length of str2

#count():it is function that returns th number of non-overlappng occurance of sustring in string S[start:end]
print(str2.count("o"))
print(str2.count(' '))#used to count empty space
print(str2.count(''))#count every element


#split function:-it returns substring in the strong ,using sep as a seperator string.
#"sep" is used to split the string
print(str2.split(' '))
print(str2.split('w'))
print(str2.split('o'))
print(str2.partition('w'))#string is only for 1st while partion for all w
print(str2.upper())






