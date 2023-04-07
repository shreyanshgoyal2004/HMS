import options as opt
import time
import art
from os import system

print("------------------------------------------------------------------------------------------------------------------------------------")
art.tprint("Hospital   Managment   System")
print("-------------------------------------------------------------------------------------------------------------------------------------")
while True:
    print("\n")
    print("1.WRITE RECORD\n2.SHOW ALL RECORDS\n3.SEARCH BY SERIAL NUMBER")
    print("4.SEARCH BY CONTACT NUMBER\n5.SEARCH BY BLOOD GROUP\n6.SEARCH BY AGE\n7.SEARCH BY SEX")
    print("8.SEARCH BY E-MAIL")
    print("9.MODIFY RECORD\n10.DELETE RECORD\n11.GET EXCEL SHEET OF ALL APPOINTMENT\n12.EXIT")
    ch=(input("\nPLEASE ENTER YOUR CHOICE:--"))
    # print("--------------------------------------------------------------------------------")

    if  int(ch)==1:
        opt.WriteHospital()
    elif  int(ch)==2:
        opt.ReadHospital()
        # system("cls")
    elif  int(ch)==3:
        n=int(input("PLEASE ENTER SERIAL NUMBER TO SEARCH:--"))
        opt.SearchHospitalSno(n)
    elif int(ch)==4:
        n=input("PLEASE ENTER CONTACT NUMBER TO SEARCH:--")
        opt.SearchHospitalCon(n)
    elif  int(ch)==5:
        n=input("PLEASE ENTER BLOOD GROUP TO SEARCH:--")
        opt.SearchBloodgroup(n)
    elif int(ch)==6:
        n=int(input("PLEASE ENTER AGE TO SEARCH:--"))
        opt.SearchAge(n)
    elif int(ch)==7:
        n=input("PLEASE ENTER SEX TO SEARCH:--")
        opt.SearchSex(n)
    
   
    elif int(ch)==8:
        n=input("PLEASE ENTER E-MAIL ADDRESS TO SEARCH:--")
        opt.SearchHospitalemail(n)
    elif int(ch)==9:
        n = input("Enter the serial number")
        opt.ModiHospital(n)
    elif int(ch)==10:
        opt.DelHospital()
    elif int(ch)==11:
        opt.GetExcel()
    elif int(ch)==12:
        print ("\n")
        print ("EXITING"),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print ("."),
        time.sleep(.8)
        print (".")
        break
    else:
        print ("Analysing your input."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print ("."),
        time.sleep(.6)
        print (".")
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~WRONG CHOICE!!!~~~~~~~~~~~~~~~~~~~\n\n\n")
        
    # system("cls")

        



        
        
