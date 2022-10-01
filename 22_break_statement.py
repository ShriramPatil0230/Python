from traceback import print_tb
from turtle import position
from setuptools import SetuptoolsDeprecationWarning


Student = ["Shriram","Jay","Roy","Jen"]

position = 1

for name in Student:
    if name == "Shriram":
       break
    position = position + 1
print(position)