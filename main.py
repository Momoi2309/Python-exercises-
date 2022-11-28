# ### EX 1 LOOPS
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(0, n):
#         print(i ** 2)
### EX 2 TUPLES
n=int(input())
a=tuple(map(int,input().split()))
print(hash(a))

# ### EX 3STRING FORMATTING


#nu am facut


### EX 4 CALENDAR


# from calendar import weekday,day_name
# import calendar
# print(calendar.TextCalendar(firstweekday=6).formatyear(2022))
#
# d,m,y = map(int, input().split())
#
# day = day_name[weekday(y, m, d)]
#
# print("The given date is:",day.upper())


### EX 5 SHAPE AND RESHAPE


# import numpy
#
# #shape
# change_array = numpy.array([1,2,3,4,5,6])
# change_array.shape = (3,2)
# print(change_array,"\n")
#
# ##reshape
# my_array = numpy.array([1,2,3,4,5,6,7,8])
# print(numpy.reshape(my_array,(2,4)))
#
#
# print(numpy.array(input().split(),int).reshape(3,3))




### EX 6 MERGE THE TOOLS

# def merge_the_tools(string, k):
#     # your code goes here
#     temp = []
#     len_temp = 0
#     for item in string:
#         len_temp += 1
#         if item not in temp:
#             temp.append(item)
#         if len_temp == k:
#             print (''.join(temp))
#             temp = []
#             len_temp = 0
# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)


### EX 7 TRIANGLE QUEST 2

#
# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print(((10**i)//9)**2)
#     ### the floor division // rounds the result down to the nearest whole number


### EX 8 COMPRESS THE STRING


##You are given a string . Suppose a character 'c' occurs consecutively X times in the string.
# Replace these consecutive occurrences of the character 'c' with (X,c)  in the string.

# from itertools import groupby
#
# for k, g in groupby(input()):
#   print((len([i for i in g]), int(k)), end=' ') ## stocheaza repetitiile de k intr o lista



# ### EX 9 DEALING WITH COMPLEX NUMBERS
#
#
# import math
# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary
#     def __add__(self, no):
#         return Complex((self.real+no.real), self.imaginary+no.imaginary)
#     def __sub__(self, no):
#         return Complex((self.real-no.real), (self.imaginary-no.imaginary))
#     def __mul__(self, no):
#         r = (self.real*no.real)-(self.imaginary*no.imaginary)
#         i = (self.real*no.imaginary+no.real*self.imaginary)
#         return Complex(r, i)
#     def __truediv__(self, no):
#         conjugate = Complex(no.real, (-no.imaginary))
#         num = self*conjugate
#         denom = no*conjugate
#         try:
#             return Complex((num.real/denom.real), (num.imaginary/denom.real))
#         except Exception as e:
#             print(e)
#     def mod(self):
#         m = math.sqrt(self.real**2+self.imaginary**2)
#         return Complex(m, 0) ## nu are parte reala mod nr complex = rad(a^2 + b^2) unde C=a+b*i
#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result
# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')