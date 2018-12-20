#Sreeraj Karpe roll no.28 Gr no.11810158
#Akaash More roll no.41 Gr no.1181082
#Vineet Kumbhar roll no.32 Gr no.11811198
#Rishikesh Mishra roll no.40 Gr no.11811272
#Ankit Lanjekar roll no.34 gr no.11810639
#Nikhar Jain roll no.44 gr no.11810255
from easygui import *
import sys
import Tkinter
import tkMessageBox
msgbox("Welcome to online payment service")
while 1:
 a = choicebox("Recharge your ...",choices=["Mobile","D2H Box","Telephone"])
 if a == "Mobile":
    a0 = ccbox("You have opted for Mobile Recharge")
    a6 = choicebox("Please chosse your carrier",choices= ["Idea","Jio","Vodafone","Airtel"])
    msg = "Enter your personal information"
    title = "ONLINE PAYMENT SERVICES"
    fieldNames = ["Name","Street Address","City","State","ZipCode"]
    fieldValues = []  
    fieldValues = multenterbox(msg,title, fieldNames)
    while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
              errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": break # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    print "Reply was:", fieldValues
    a11 = enterbox("Enter cvv")
    a12 = enterbox("Enter amount of recharge")
    a2 =  enterbox("Enter the otp sent by bank on your registered number.Never share this with anyone")
    a13 = ccbox("Congratulations Recharge done sucessfully!!")
    sys.exit(0)
 elif a == "D2H Box":
      b0 = ccbox("You have opted for D2H Recharge")
      b6 = choicebox("Please chosse your service provider",choices= ["Videocon","Tata Sky","DEN"])
      msg = "Enter your personal information"
      title = "ONLINE PAYMENT SERVICES"
      fieldNames = ["Name","Street Address","City","State","ZipCode","Card holder's name","CVV","Recharge amt."]
      fieldValues = []  
      fieldValues = multenterbox(msg,title, fieldNames)
      while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
              errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": break # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
      print "Reply was:", fieldValues
      b2 =  enterbox("Enter the otp sent by bank on your registered number.Never share this with anyone")
      b13 = ccbox("Congratulations Recharge done sucessfully!!")
      sys.exit(0)
 if a == "Telephone":
   c0 = ccbox("You have opted for Telephone Recharge") 
   c6 = choicebox("Please chosse your carrier",choices= ["BSNL","Tata Docomo"])
   msg = "Enter your personal information"
      title = "ONLINE PAYMENT SERVICES"
      fieldNames = ["Name","Street Address","City","State","ZipCode","Card holder's name","CVV","Recharge amt."]
      fieldValues = []  
      fieldValues = multenterbox(msg,title, fieldNames)
      while 1:
        if fieldValues == None: break
        errmsg = ""
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
              errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "": break # no problems found
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
      print "Reply was:", fieldValues
   c2 =  enterbox("Enter the otp sent by bank on your registered number.Never share this with anyone")
   c13 = ccbox("Congratulations Recharge done sucessfully!!")
else:
     sys.exit(0)
