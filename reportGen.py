'''
Ivestment report generator 
@uthors : Oueslati Islem(islemoueslati), Ltifi Azer(azseza)
'''
import pylatex
import os 
import numpy
import requests
import matplotlib as mlt
import matplotlib.pyplot as plt

#inputOutput modules 
def greetings():
    print("")
    param = []
    print("press Enter after each input")
    try:
        param["adress"] = input("Enter the Property Adress (e.g XXXX Somthing Av , City , State , ZIP CODE ) ")
        param["propVal"] = int(input("Enter Property Value (no float) :"))
        param["rentEst"] = int(input("Enter Rent Estimation : "))
        param["taxRate"] = float(input("Enter The tax Rate (default 1.9%)"))
        param["annTaxRate"] = float(input("Enter Teh estimated anual Taxation(default .. )"))
    except ValueError:
        print("Wrong input Values")
    return parm
#api 

#formulas 


