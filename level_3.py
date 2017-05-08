"""
Elevator Maintenance
====================

You've been assigned the onerous task of elevator maintenance - ugh! It 
wouldn't be so bad, except that all the elevator documentation has been lying 
in a disorganized pile at the bottom of a filing cabinet for years, and you 
don't even know what elevator version numbers you'll be working on. 

Elevator versions are represented by a series of numbers, divided up into 
major, minor and revision integers. New versions of an elevator increase the 
major number, e.g. 1, 2, 3, and so on. When new features are added to an 
elevator without being a complete new version, a second number named "minor" 
can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small 
fixes or maintenance work can be represented by a third number named 
"revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used 
as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc 
(Commander Lambda is careful to always beta test her new technology, with her 
loyal henchmen as subjects!).

Given a list of elevator versions represented as strings, write a function 
answer(l) that returns the same list sorted in ascending order by major, minor, 
and revision number so that you can identify the current elevator version. 
The versions in list l will always contain major numbers, but minor and 
revision numbers are optional. If the version contains a revision number, 
then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], 
the function answer(l) would return the 
list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions 
are equivalent but one version contains more numbers than the others, then 
these versions must be sorted ascending based on how many numbers they have, 
e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at 
least 1 and will not exceed 100.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string list) l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
Output:
    (string list) ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]

Inputs:
    (string list) l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
Output:
    (string list) ["0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]

"""

def versionStr2Int(v_str):
    count = [1, 0, 0]
    split_v = [int(i) for i in v_str.split(".")]
    for i in range(len(split_v)):
        count[i] += split_v[i] + 1
    
    return 5**count[0] * 3**count[1] * 2**count[2]
              

def compareVersionStr(version_a, version_b):
    i, j = 0, 0
    n1, n2 = len(version_a), len(version_b)
    num1, num2 = 0, 0
    
    while (i < n1 or j < n2):
        while (i < n1 and version_a[i] != '.'):
            num1 = num1*10+(ord(version_a[i])-ord('0'))
            i += 1
        while (j < n2 and version_b[j] != '.'):
            num2 = num2*10+(ord(version_b[j])-ord('0'))
            j += 1

        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        
        num1 = 0
        num2 = 0
        i += 1
        j += 1

    unique_int_a = versionStr2Int(version_a)
    unique_int_b = versionStr2Int(version_b)
    if unique_int_a == unique_int_b:
        return 0
    else:
        if unique_int_a > unique_int_b:
            return 1
        else:
            return -1


def bubbleSort(orig_arr):
    arr = orig_arr[:]
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if compareVersionStr(arr[j], arr[j + 1]) == 1:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

def answer(l):
    return bubbleSort(l)
