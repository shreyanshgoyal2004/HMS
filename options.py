import pymysql as pym
import pandas as pd
from tabulate import tabulate
from datetime import *
import pywhatkit
import maskpass

db = pym.connect(host="localhost",user="root",password="shreyansh2004@IIIT",database="HospitalDb")

cursor = db.cursor()


#FUNCTION

def WriteHospital():
    print ("Enter Details::")
    name=input("Enter Patinet's Name:").capitalize()
    age=int(input("Enter Patinet's Age:"))
    sex=input("Enter Patinet's Sex (Male/Female):").capitalize()
    weight=int(input("Enter Patinet's Weight(In Kgs):"))
    height=int(input("Enter Patinet's Height:"))
    bgroup=input("Enter Patient's Blood Group:").upper()
    address=input("Enter Address:").capitalize()
    city=input("Enter City:").capitalize()
    pno=(input("Enter Phone number:"))
    email=input("Enter E-Mail:").lower()
    dname=input("Enter Symptoms:").capitalize()
    cursor.execute(f"INSERT INTO PatientDetail(nam,age,sex,Weight,Height,Bgroup,Adddress,City,Pno,Emial,Symptoms) VALUES('{name}', {age}, '{sex}', {weight}, {height}, '{bgroup}', '{address}', '{city}', '{pno}', '{email}', '{dname}')")
    db.commit()
    now = datetime.now()
    pywhatkit.sendwhatmsg(
    phone_no=f"+91-{pno}",
    message = f"Hi {name} this is system generated message to verify that your appointment has been confirmed",
    time_hour = now.hour,
    time_min = now.minute + 2,
    tab_close = True
)


    # db.close()

def convert_to_table(data,All=0):
    mydict={
        "Sno":[],
        "Name":[],
        "Age":[],
        "Sex":[],
        "Weight":[],
        "Height":[],
        "Blood_Group":[],
        "Address":[],
        "City":[],
        "Phone_Number":[],
        "Email":[],
        "Symptoms":[]
    }
    mydict_key=list(mydict.keys())
    for row in data:
       row1=list(row)
       for i in range(len(row1)):
        mylist=mydict[mydict_key[i]]
        mylist.append(row1[i])
    # print(mydict)
    df=pd.DataFrame(mydict)
    if(All==0):
        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    else:
        df.to_excel("ds.xls")
        print("\nExcel is Completely Downloaded")

def ReadHospital():
    cursor.execute("SELECT Sno, nam FROM PatientDetail")
    data = cursor.fetchall()
    
    mydic = {
        "SNo": [],
        "Name": []
    }
    mydic_key = list(mydic.keys())
    for row in data:
        row1 = list(row)
        for i in range(len(row1)):
            mydic[mydic_key[i]].append(row1[i])
    df = pd.DataFrame(mydic)
    print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
    

   
def SearchHospitalSno(n): 
    cursor.execute(f"SELECT * FROM PatientDetail WHERE Sno = {n}")
    data = cursor.fetchall()
    if(len(data)==0):
        print("No data found");
    else:
       convert_to_table(data)

def SearchHospitalCon(n): 
    cursor.execute(f"SELECT * FROM PatientDetail WHERE Pno = '{n}'")
    data = cursor.fetchall()
    if(len(data)==0):
        print("No data found");
    else:
        convert_to_table(data)
   
def SearchHospitalemail(n): 
    cursor.execute(f"SELECT * FROM PatientDetail WHERE Emial = '{n}'")
    data = cursor.fetchall()
    if(len(data)==0):
        print ("               ____________________________________________ ") 
        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    else:
        convert_to_table(data)

def SearchBloodgroup(n):

    cursor.execute(f"SELECT * FROM PatientDetail WHERE Bgroup = '{n}'")
    data = cursor.fetchall()
    if(len(data)==0):
        print("No data found");
    else:
        convert_to_table(data)
def SearchAge(n):
    cursor.execute(f"SELECT * FROM PatientDetail WHERE age = {n}")
    data = cursor.fetchall()
    if(len(data)==0):
        print ("               ____________________________________________ ") 
        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    else:
        convert_to_table(data)
    
            
def SearchSex(n): 
    cursor.execute(f"SELECT * FROM PatientDetail WHERE sex = '{n}'")
    data = cursor.fetchall()
    if(len(data)==0):
        print ("               ____________________________________________ ") 
        print ("               |  ... RECORD... DOES... NOT... EXIST ...  | ")
        print ("               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    else:
        convert_to_table(data)

password = "admin"
def ModiHospital(n):
        pas=maskpass.askpass("Enter the password to modify the records: ")
        if(pas==password):
            
            print("If you don't want to modify then enter the same value")
            cursor.execute(f"SELECT * FROM PatientDetail WHERE Sno = {n}")
            data = cursor.fetchall()
            if(len(data)==0):
                print("No data found");
            else:
                convert_to_table(data)
                print ("Enter Details::")
                name=input("Enter Patinet's Name:").capitalize()
                age=int(input("Enter Patinet's Age:"))
                sex=input("Enter Patinet's Sex (Male/Female):").capitalize()
                weight=int(input("Enter Patinet's Weight(In Kgs):"))
                height=int(input("Enter Patinet's Height:"))
                bgroup=input("Enter Patient's Blood Group:").upper()
                address=input("Enter Address:").capitalize()
                city=input("Enter City:").capitalize()
                pno=(input("Enter Phone number:"))
                email=input("Enter E-Mail:").lower()

                cursor.execute(f"UPDATE PatientDetail SET nam='{name}', age={age}, sex='{sex}', Weight={weight}, Height={height}, Bgroup='{bgroup}', Adddress='{address}', City = '{city}', Pno = '{pno}', Emial='{email}' WHERE Sno={n}")
                db.commit()
        else:
            print("Wrong Password")
        

def DelHospital():
    pas=maskpass.askpass("Enter the password to Delete the records: ")
    if(pas=="admin"):
        cursor.execute(f"SELECT * FROM PatientDetail")
        data = cursor.fetchall()
        if(len(data)==0):
            print("There are no appointements in the record right now")
        else:
            convert_to_table(data)
            n = int(input("Enter the serial number of record which you want to delete"))
            try:
                cursor.execute(f"DELETE FROM PatientDetail WHERE Sno={n}")
                db.commit(); 
            except:
                print("Wrong input") 
    else:
        print("Wrong Password")

def GetExcel():
    pas=maskpass.askpass("Enter the password to excel sheet of the records: ")
    if(pas=="admin"):
        # df=sql.read_sql('select * from 0patientdetail',db)
        cursor.execute("SELECT * FROM PatientDetail")
        data = cursor.fetchall()
        convert_to_table(data,All=1)
    # export the data into the excel sheet
        # df.to_excel('ds.xls')