from sqlalchemy.util import counter


def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


def Cloning(li1):
    li_copy = li1[:]
    return li_copy


def Reverse(lst):
    return [ele for ele in reversed (lst)]


def Second(lst):
    return lst.sort ( )

def EvenNum(lst):
    EvenNum = [num for num in lst if num % 2 == 0]
    return len(EvenNum)

def EvenRange(lst):
    Even = [num for num in lst if num % 2 == 0]
    return Even

def OddNum(lst):
    OddNum = [num for num in lst if num % 2 == 1]
    return len(OddNum)

def OddRange(lst):
    Odd = [num for num in lst if num % 2 == 1]
    return Odd

def NegNum(lst):
    num = [num for num in lst if num >= 0]
    return num

def LenNegNum(lst):
    num = [num for num in lst if num <= 0]
    return len(num)

def PosNum(lst):
    num = [num for num in lst if num <= 0]
    return num

def LenPosNum(lst):
    num = [num for num in lst if num >= 0]
    return len(num)

def Cumulative(lst):
    cu_list = []
    length = len(lst)
    cu_list = [sum(lst[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]



 # driver


# creating an empty list
lst = []
# number of elemetns as input
n = int (input ("Enter number of elements : "))
# iterating till the range
for i in range (0, n):
    ele = int (input ( ))
    lst.append (ele)  # adding the element

print ("Your list" + " = " + lst)
print (" ")
print ("Largest element is:", max (lst))
print ("Largest element is:", min (lst))
print (" ")
print ("Multiplication of your list from left to right" + " = " + str (multiplyList (lst)))
lst1 = Cloning (lst)
print (" ")
print ("Lenght of the list" + " = " + str (n))
print (" ")
print ("Original List:", lst)
print (" ")
print ("After Cloning:", lst1)
print (" ")
print ("Reverse List" + " = " + str(Reverse (lst)))
print (" ")
print("Second largest element is:", lst[-2])
print (" ")
print("Number of even numbers in list:" + " = " + str(EvenNum(lst)))
print("Even numbers in list:" + " = " + str(EvenRange(lst)))
print (" ")
print("Number of odd numbers in list:" + " = " + str(OddNum(lst)))
print("Odd numbers in list:" + " = " + str(OddRange(lst)))
print (" ")
print("Number of positive numbers in list:" + " = " + str(LenPosNum(lst)))
print("Positive numbers in list:" + " = " + str(NegNum(lst)))
print (" ")
print("Number of negative numbers in list:" + " = " + str(LenNegNum(lst)))
print("Negative numbers in list:" + " = " + str(PosNum(lst)))
print(" ")
print("Cumulative sum of the list  " + " = " + str(Cumulative(lst)))