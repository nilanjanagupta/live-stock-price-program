import requests
import bs4
from bs4 import BeautifulSoup
def tcs() :
    urltcs =requests.get('https://www.moneycontrol.com/india/stockpricequote/computerssoftware/tataconsultancyservices/TCS')
    datatcs = bs4.BeautifulSoup(urltcs.text, "lxml")
    datatcs = datatcs.find('div', {"class":'inprice1 nsecp'}).text
    return  datatcs
def reliance():
    urlreliance = requests.get('https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI')
    datareliance = bs4.BeautifulSoup(urlreliance.text,"lxml")
    datareliance = datareliance.find('div',{"class":'inprice1 nsecp'}).text
    return datareliance
def hdfc():
    urlhdfc = requests.get('https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/hdfcbank/HDF01')
    datahdfc = bs4.BeautifulSoup(urlhdfc.text,"lxml")
    datahdfc = datahdfc.find('div', {"class":'inprice1 nsecp'}).text
    return datahdfc
def infosys():
    urlinfosys = requests.get('https://www.moneycontrol.com/india/stockpricequote/computerssoftware/infosys/IT')
    datainfosys = bs4.BeautifulSoup(urlinfosys.text,"lxml")
    datainfosys = datainfosys.find('div', {"class":'inprice1 nsecp'}).text
    return datainfosys
def kotak():
    urlkotak = requests.get('https://www.moneycontrol.com/india/stockpricequote/banksprivatesector/kotakmahindrabank/KMB')
    datakotak = bs4.BeautifulSoup(urlkotak.text,"lxml")
    datakotak=datakotak.find('div', {"class":'inprice1 nsecp'}).text
    return datakotak
while True:
    print('the current price for TCS is ' +str(tcs()))
    print('the current price for Reliance is ' + str(reliance()))
    print('the current price for HDFC bank is ' + str(hdfc()))
    print('the current price for Infosys is ' + str(infosys()))
    print('the current price for Kotak Mahindra Bank is ' + str(kotak()))
