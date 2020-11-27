'''
Ivestment report generator 
@uthors : Oueslati Islem(islemoueslati), Ltifi Azer(azseza)
'''
import pylatex
import os 
import numpy
import matplotlib as mlt
import matplotlib.pyplot as plt
import re
import requests
from i18naddress import InvalidAddress, normalize_address
import googlemaps
import datetime
import google_streetview.api
#inputOutput modules

def greetings():
    print("")
    param = dict()
    adress=dict()
    print("####HELLO################git:$@/RentAnalyser#################################################################")
    print("###########################################################################################@azseza###########")
    print("##########################################################################################@islemoueslati#####")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Rent Balence Sheet Generator~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("")
    print("       >>>Press Enter after each input")
    try:
        adress['country_code'] = 'US'
        adress['city'] = input("Enter the Property Adress (e.g XXXX Somthing Av , City , State , ZIP CODE ),First The city :   ")
        adress['country_area'] = input("Enter the country area :   ")
        adress['postal_code'] = input("Enter The postal Code :   ")
        adress['street_address'] = input("Enter The Street Adress :   ")
        adress = normalize_address(adress)
        param['propVal'] = int(input("Enter Property Value (no float) :   "))
        param['rentEst'] = int(input("Enter Rent Estimation : "))
        param['taxRate'] = float(input("Enter The tax Rate (default 1.9%) :   "))
        param['annTaxRate'] = float(input("Enter Teh estimated anual Taxation(default .. ) :   "))
    except ValueError :
        print("Wrong input Values, Please relunch the program. ")
    except InvalidAddress :
        print("Wrong adress form, Please relunch the program. ") 
        print(InvalidAddress.errors)
    
    return param



#api 
def getting_imgz(adress : dict):
    gmaps = googlemaps.Client(key='#######################################') 
    geoloc_cord = gmaps.geocode(adress)
    params = [{
        'size': '600x300', # max 640x640 pixels
        'location': str(geoloc_cord[0]+';'+geoloc_cord[1]),
        'pitch': '0',
        'key': '#######################################'
            }]
    results = google_streetview.api.results(params)
    results.download_links('Images')
    


#formulas 


