#Types of Arrays:
    #Single Demensional Array
        #there is only one row and multiple columns
    #Multi-Dementinal Array
        #there are multiple rows and multiple columns
            #you can not use the array package to do this, instead you will need to import from numpy

#by default, numpy is not a package that comes with Python
#we will need to install it by using PIP through the command prompt

#follow the steps listed in:  

# https://code.visualstudio.com/docs/python/python-tutorial#_install-and-use-packages



#1. Create a virtual environment to run the python rather than running it globally
# go to CMD and run:
# py -3 -m venv .venv
# .venv\scripts\activate

#2. Select python interpretor for .venv from command palette

#3. install packages from CMD:
# python -m pip install numpy

#4. Run import from Python Debug Console
from numpy import *




#Now we actually get to using Numpy
arr = array([1,2,3,2,5,4])

print(arr)