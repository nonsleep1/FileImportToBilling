#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import os
import sys
import time
import fnmatch
import re
#################################################################
if not os.path.exists("jauikelti.txt"): #imported files list
    file = open("jauikelti.txt","x")
else:
    print("Jau yra sukurtas")
    file=open("jauikelti.txt","w")

if not os.path.exists("sarasas.txt"):
    sarasasf = open("sarasas.txt","x")
else:
    print("Jau yra sukurtas")
    sarasasf=open("sarasas.txt","w") #list of files to import
##############################################################
def fileslistinfolder(folderis,sarasasf):
    for files in os.listdir(folderis):
        sarasasf.write(files+"\n")
################################################################
def listcreations_exit(file,sarasasf):
    file.close()
    sarasasf.close()
###################################################################
def compare_list():
    if not os.path.exists("reik_ikelti.txt"):
        reik_ikelti = open("reik_ikelti.txt","x")
    else:
        print("Jau yra sukurtas")
        reik_ikelti=open("reik_ikelti.txt","w")
        file = open("jauikelti.txt","r")
        sarasasf = open("sarasas.txt","r")
        file3 = set(sarasasf) - set(file)

        for list in file3:
            print(list)
        #    regex = re.compile(".xls")
            if not re.search(".xls",list):
                reik_ikelti.write(list)

        listcreations_exit(file,sarasasf)
####################################################################
#driver=webdriver.Chrome("./chromedriver")
print(sys.version)
folderis = "/home/nonsleep1/Documents/Bankai20190912/" #folder from where import files
reik_ikelti = "reik_ikelti.txt"
binary = FirefoxBinary('/usr/bin/firefox')
driver = webdriver.Firefox(firefox_binary=binary,executable_path="./geckodriver")
driver.get("") #Billing programs Url
username = driver.find_element_by_id("UserName")
password = driver.find_element_by_id("Password")
username.send_keys("") #username
password.send_keys(""+Keys.RETURN) #password
fileslistinfolder(folderis,sarasasf)
time.sleep(5)
driver.find_element_by_xpath("//body[contains(@class,'pace-done')]/div[contains(@class,'wrapper row-offcanvas row-offcanvas-left')]/aside[contains(@class,'right-side')]/section[@id='MainContent']/div[contains(@class,'row')]/div[contains(@class,'col-xs-12')]/div[contains(@class,'box box-primary')]/div[contains(@class,'box-body')]/div[contains(@role,'tabpanel')]/div[contains(@class,'tab-content')]/div[@id='PaymentImportTab']/div[contains(@class,'toolbar')]/div[2]").click()
time.sleep(5)
driver.find_element_by_xpath("(//button[@type='button'][contains(.,'< neparinkta >')])[1]").click()
time.sleep(5)
listas = driver.find_element_by_id("PaymentFile")
#print(listas.get_attribute("innerHTML"))
for option in listas.find_elements_by_tag_name('option'):
    #print(option.get_attribute("innerHTML"))
    if (option.get_attribute("innerHTML")) != "&lt; neparinkta &gt;":
        file.write(option.get_attribute("innerHTML")+"\n")
listcreations_exit(file,sarasasf)
compare_list()
time.sleep(10)
ikelimui_failas = open("reik_ikelti.txt","r")

### i loop
for ikelimui in ikelimui_failas.readlines():
    time.sleep(5)
    driver.execute_script("javascript:ImportPayments(); void(0)")
    popup = driver.switch_to_active_element()
    time.sleep(5)
    upload = popup.find_element_by_xpath("//input[@id='UploadedFile']")
    bankcodelist = popup.find_element_by_xpath("(//select[contains(@id,'BankCode')])[2]") 
    for option in bankcodelist.find_elements_by_tag_name('option'):
        #####Logic to find and import specific file to specific category ######
        #print(option.get_attribute("innerHTML"))
        if option.get_attribute("innerHTML") == "13. EMA" and re.search("EMA",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            print(nuoroda3)
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "5.Kredito unija su skaitikliais" and re.search("KU",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "6.Maxima su skaitikliais" and re.search("SL2019",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "12. Mokėjimo paslaugos" and re.search("VPO",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "9.Perlas su skaitikliais" and re.search("PP",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "2.SEB su skaitikliais" and re.search("seb",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "3.Luminor su skaitikliais" and re.search("Luminor",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "10.Šiaulių bankas" and re.search("SB",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "8.Paštas su skaitikliais" and re.search("Liet",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "11.Swedbank su skaitikliais" and re.search("swed",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
        if option.get_attribute("innerHTML") == "4.Butų ūkis su skaitikliais" and re.search("BV",ikelimui):
            print("JEGA as RADAU")
            nuoroda3 = folderis+ikelimui.strip()
            upload.send_keys(nuoroda3)
            option.click()
            popup.find_element_by_xpath("//input[contains(@class,'jid_submit_file_upload')]").click()
            break
ikelimui_failas.close()
driver.quit()