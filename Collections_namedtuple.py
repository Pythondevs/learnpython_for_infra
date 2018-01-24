"""Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

Task

Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name .
Your task is to help Dr. Wesley calculate the average marks of the students.

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next  lines contains the marks, IDs, name  and class, under their respective column names.

Constraints
0 <= N >= 100

Output Format

Print the average marks of the list corrected to 2 decimal places.

"""
from collections import namedtuple as nt

def avg_function ():
    n = int(input())                        ## Input the number of students
    fields = input().split()                ## Creating Indexes through split command
    total=0
    for i in range(n):                      ## Looping for 5 times to input the values
        data = nt('data', fields)
        field1, field2, field3, field4 = input().split()               ## input values 5 times for differentt fields
        data = data(field1,field2,field3,field4)
        total+= int(data.MARKS)                                         ## Marks Total
    print (total/n)

if __name__ == '__main__':
    avg_function ()