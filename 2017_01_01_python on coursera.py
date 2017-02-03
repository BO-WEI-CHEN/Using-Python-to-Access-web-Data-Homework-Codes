# 2017_01_01
import re
# Homework_regular_expression
# How to convert rtf into txt? Just use the combination of key "command+shift+t"
# open and read a text file
a = open('/Users/martinchen/PycharmProjects/2016_12_24_coursera/python_20170101_python.txt', 'r')
aread = a.read()  # read a for all words or lines
print aread
y = re.findall('[0-9]+', aread)  # application of regular expression of [0-9]+
print y
print type(y)  # check the type of y

y1 = map(int, y)  # convert the "strings" in the original list y into "integers" in the new list y1
print y1  # check the outcome: all strings convert into integers
print(sum(y1))  # sum up all the integers in the new list y1(the integers in a list can be summed up)

# tuple VS list
x = '12', '34'
print type(x)
print x
# use "in" to check if an element exists in the tuple
print(13 in x)  # false
print('12' in x)  # true
print('123' in x)  # false
print('34' in x)  # true
# You can't add elements to a tuple. Tuples have no append or extend method.
# You can't remove elements from a tuple. Tuples have no remove or pop method.
# You can find elements in a tuple, since this does not change the tuple.
# You can also use the in operator to check if an element exists in the tuple.
