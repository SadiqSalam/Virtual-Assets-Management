import os
import mysql.connector
import datetime
now = datetime.datetime.now()
import csv



def Stock_mgmt( ):
           while True :
                      print("\t\t\t 1. Add New Stock")
                      print("\t\t\t 2. List Stock")
                      print("\t\t\t 3. Update Stock")
                      print("\t\t\t 4. Delete Stock")
                      print("\t\t\t 5. Back (Main Menu)")
                      p=int (input("\t\tEnter Your Choice :"))
                      if p==1:
                                 add_Stock()
                      if p==2:
                                 search_Stock()
                      if p==3:
                                 update_Stock()
                      if p==4:
                                 delete_Stock()
                      if p== 5 :
                              break

def show_info():
          list_Stock()
          with open('records.csv', mode ='r') as file:
              b='y'
              while b=='y':
                  a=int(input("Enter the stock code for additional information: "))
                  csvFile = csv.reader(file)
                  #rows = list(csvFile)
                  print(rows[a-1])
                  b=input("Do you want to try again? y/n: ")

def invest_mgmt( ):
           while True :
                      print("\t\t\t 1. Add Investment")
                      print("\t\t\t 2. List Investment")
                      print("\t\t\t 3. Back (Main Menu)")
                      o=int (input("\t\tEnter Your Choice :"))
                      if o==1 :
                                 add_order()
                      if o==2 :
                                 list_order()
                      if o== 3 :
                                 break

def sales_mgmt( ):
           while True :
                      print("\t\t\t 1. Sale Items")
                      print("\t\t\t 2. List Sales")
                      print("\t\t\t 3. Delete Sales")
                      print("\t\t\t 4. Back (Main Menu)")
                      s=int (input("\t\tEnter Your Choice :"))
                      if s== 1 :
                                 sale_Stock()
                      if s== 2 :
                                 list_sale()
                      if s== 3 :
                                delete_sale()
                      if s== 4:
                                break
def delete_sale( ):
          mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
          mycursor=mydb.cursor()
          pcode=input("Enter Stock code: ")
          sql="DELETE from Sales WHERE pcode=%s;"
          mycursor.execute(sql,(pcode,))
          mydb.commit()
          print("SALES IS DELETED")
          
def user_mgmt( ):
           while True :
                      print("\t\t\t 1. Add user")
                      print("\t\t\t 2. List user")
                      print("\t\t\t 3. Delete user")
                      print("\t\t\t 4. Back (Main Menu)")
                      u=int (input("\t\tEnter Your Choice :"))
                      if u==1:
                                 add_user()
                      if u==2:
                                 list_user()
                      if u==3:
                                delete_user()
                      if u==4:
                                 break

def create_database():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")				#change as per system
           mycursor=mydb.cursor()
           print(" Creating Stock table")
           sql = "CREATE TABLE if not exists Stock (\
                  pcode int(4) PRIMARY KEY,\
                  pname char(30) NOT NULL,\
                  pprice float(8,2) ,\
                  pqty int(4) ,\
                  pcat char(30));"
           mycursor.execute(sql)
           print(" Creating ORDER table")
           sql = "CREATE TABLE if not exists orders (\
                  orderid int(4)PRIMARY KEY ,\
                  orderdate DATE ,\
                  pcode char(30) NOT NULL , \
                  pprice float(8,2) ,\
                  pqty int(4) ,\
                  supplier char(50),\
                  pcat char(30));"
           mycursor.execute(sql)
           print(" ORDER table created")

           print(" Creating SALES table")
           sql = "CREATE TABLE if not exists sales (\
                  salesid int(4) PRIMARY KEY ,\
                  salesdate DATE ,\
                  pcode char(30) references Stock(pcode), \
                  pprice float(8,2) ,\
                  pqty int(4) ,\
                  Total double(8,2)\
                  );"
           mycursor.execute(sql)
           print(" SALES table created")
           sql = "CREATE TABLE if not exists user (\
                  uid varchar(20) PRIMARY KEY,\
                  uname char(30) NOT NULL,\
                  upwd char(30));"
           mycursor.execute(sql)
           print(" USER table created")

def list_database():
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")   					#change as per system
        mycursor=mydb.cursor()
        sql="show tables;"
        mycursor.execute(sql)
        for i in mycursor:
                   print(i)

def add_order():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")				#change as per system
           mycursor=mydb.cursor()
           now = datetime.datetime.now()
           sql="INSERT INTO orders (orderid, orderdate, pcode, pprice, pqty, supplier, pcat) values (%s,%s,%s,%s,%s,%s,%s)"
           code=int(input("Enter Stock code :"))
           oid=now.year+now.month+now.day+now.hour+now.minute+now.second
           qty=int(input("Enter Stock quantity : "))
           price=float(input("Enter Stock unit price: "))
           cat=input("Enter Stock category: ")
           supplier=input("Enter Supplier details: ")           
           val=(oid,now,code,price,qty,supplier,cat)
           mycursor.execute(sql,val)
           mydb.commit()



def list_order():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI", database="stock")					#change as per system
           mycursor=mydb.cursor()
           sql="SELECT * from orders"
           mycursor.execute(sql)
           print("\t\t\t\t\t\t\t ORDER DETAILS")
           print("-"*85)
           print("orderid    Date    Stock code    price     quantity      Supplier      Category")
           print("-"*85)
           for i in mycursor:
                      print(i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t",i[4],"\t     ",i[5],"\t",i[6])
           print("-"*85)
                

def db_mgmt( ):
           while True :
                      print("\t\t\t 1. Database creation")
                      print("\t\t\t 2. List Database")
                      print("\t\t\t 3. Back (Main Menu)")
                      p=int (input("\t\tEnter Your Choice :"))
                      if p==1 :
                                 create_database()
                      if p==2 :
                                 list_database()
                      if p== 3 :
                                 break
def add_Stock():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")				#change as per system
           mycursor=mydb.cursor()
           sql="INSERT INTO Stock(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
           code=int(input("\t\tEnter Stock code :"))
           search="SELECT count(*) FROM Stock WHERE pcode=%s;"
           val=(code,)
           mycursor.execute(search,val)
           for x in mycursor:
                      cnt=x[0]
           if cnt==0:
                      name=input("\t\tEnter Stock name :")
                      qty=int(input("\t\tEnter Stock quantity :"))
                      price=float(input("\t\tEnter Stock unit price :"))
                      cat=input("\t\tEnter Stock category :")
                      val=(code,name,price,qty,cat)
                      mycursor.execute(sql,val)
                      mydb.commit()
           else:
                      print("\t\t Stock already exist")
def update_Stock():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
           mycursor=mydb.cursor()
           code=int(input("Enter the Stock code :"))
           qty=int(input("Enter the quantity :"))
           sql="UPDATE Stock SET pqty=pqty+%s WHERE pcode=%s;"
           val=(qty,code)
           mycursor.execute(sql,val)
           mydb.commit()
           print("\t\t Stock details updated")

def delete_Stock():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
           mycursor=mydb.cursor()
           code=int(input("Enter the Stock code :"))
           sql="DELETE FROM Stock WHERE pcode = %s;"
           val=(code,)
           mycursor.execute(sql,val)
           mydb.commit()
           print(mycursor.rowcount," record(s) deleted");
def search_Stock():
                    
           while True :
                      print("\t\t\t 1. List all Stock")
                      print("\t\t\t 2. List Stock code wise")
                      print("\t\t\t 3. List Stock category wise")
                      print("\t\t\t 4. Back (Main Menu)")
                      s=int (input("\t\tEnter Your Choice :"))
                      if s==1 :
                                 list_Stock()
                      if s==2 :
                                  code=int(input(" Enter Stock code :"))
                                  list_prcode(code)
                                  
                      if s==3 :
                                  cat=input("Enter category :")
                                  list_prcat(cat)
                                 
                      if s== 4 :
                                 break

def list_Stock():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * from Stock"
           mycursor.execute(sql)
           print("\t\t\t\t Stock DETAILS")
           print("\t\t","-"*58)
           print("\t\t code \t name\tprice\tquantity\tcategory")
           print("\t\t","-"*58)
           for i in mycursor:
                      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t",i[3],"\t",i[4])
           print("\t\t","-"*58)


def list_prcode(code):
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * from Stock WHERE pcode=%s"
           val=(code,)
           mycursor.execute(sql,val)
           print("\t\t\t\t Stock DETAILS")
           print("\t\t","-"*47)
           print("\t\t code    name    price   quantity      category")
           print("\t\t","-"*47)
           for i in mycursor:
                      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
           print("\t\t","-"*47)


def sale_Stock():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
           mycursor=mydb.cursor()
           pcode=input("Enter Stock code: ")
           sql="SELECT count(*) from Stock WHERE pcode=%s;"
           val=(pcode,)
           mycursor.execute(sql,val)
           for x in mycursor:
                      cnt=x[0]
           if cnt !=0 :
                      sql="SELECT * from Stock WHERE pcode=%s;"
                      val=(pcode,)
                      mycursor.execute(sql,val)
                      for x in mycursor:
                                 print(x)
                                 price=int(x[2])
                                 pqty=int(x[3])
                      qty=int(input("Enter no of quantity :"))
                      if qty <= pqty:
                                 total=qty*price;
                                 print ("Collect  Rs. ", total)
                                 sql="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
                                 val=(int(cnt)+1,datetime.datetime.now(),pcode,price,qty,total)
                                 mycursor.execute(sql,val)
                                 sql="UPDATE Stock SET pqty=pqty-%s WHERE pcode=%s"
                                 val=(qty,pcode)
                                 mycursor.execute(sql,val)
                                 mydb.commit()
                      else:
                                 print(" Quantity not Available")
           else:
                      print(" Stock is not avalaible")

def list_sale():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT * FROM sales"
           mycursor.execute(sql)
           print(" \t\t\t\tSALES DETAILS")
           print("-"*80)
           print("Sales id  Date    Stock Code     Price             Quantity           Total")
           print("-"*80)
           for x in mycursor:
                      print(x[0],"\t",x[1],"\t",x[2],"\t   ",x[3],"\t\t",x[4],"\t\t",x[5])
           print("-"*80)
                                 
                              
def list_prcat(cat):
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
           mycursor=mydb.cursor()
           print (cat)
           sql="SELECT * from Stock WHERE pcat =%s"
           val=(cat,)
           mycursor.execute(sql,val)
           clrscr()
           print("\t\t\t\t Stock DETAILS")
           print("\t\t","-"*47)
           print("\t\t code    name    price   quantity      category")
           print("\t\t","-"*47)
           for i in mycursor:
                      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
           print("\t\t","-"*47)

def add_user():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
           mycursor=mydb.cursor()
           uid=input("Enter emaid id :")
           name=input(" Enter Name :")
           paswd=input("Enter Password :")
           sql="INSERT INTO user values (%s,%s,%s);"
           val=(uid,name,paswd)
           mycursor.execute(sql,val)
           mydb.commit()
           print(mycursor.rowcount, " user created")


def list_user():
           mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
           mycursor=mydb.cursor()
           sql="SELECT uid,uname from user"
           mycursor.execute(sql)
           clrscr()
           print("\t\t\t\t USER DETAILS")
           print("\t\t","-"*27)
           print("\t\t UID        name    ")
           print("\t\t","-"*27)
           for i in mycursor:
                      print("\t\t",i[0],"\t",i[1])
           print("\t\t","-"*27)

def delete_user():
          mydb=mysql.connector.connect(host="localhost",user="root",passwd="AirJordan@IVXI",database="stock")
          mycursor=mydb.cursor()
          oid=input("Enter emaid id :")
          sql="DELETE FROM user WHERE uid=%s;"
          val=(oid,)
          mycursor.execute(sql,val)
          mydb.commit()
          print(mycursor.rowcount, " user deleted")

          
def clrscr():
            print("\n"*5)

fields=["INFORMATION"]
rows=[ ["Bitcoin: It is a decentralized digital currency, without a central bank or single administrator, that can be sent from user to user without the need for intermediaries. It was created in 2009 by Satoshi Nakamoto."],
    ["Dogecoin: It is a cryptocurrency created by software engineers Billy Markus and Jackson Palmer. It was created in 2013."],
    ["Ethereum: It is a decentralized, open-source blockchain with smart contract functionality. It was created in 2013 by programmer Vitalik Buterin."],
    ["Polkadot:  It is an open source, blockchain platform and cryptocurrency that allows for distributed computing. It was created in 2016 by Gavin Wood."],
    ["Binance: It is a cryptocurrency exchange which is the largest exchange in the world in terms of daily trading volume of cryptocurrencies. It was founded in 2017 by Changpeng Zhao."],
    ["Apple Inc.:  It is an American multinational technology company that specializes in consumer electronics, software and online services. As of January 2022, it is the world's most valuable company. It was created in 1976 by founders Steve Jobs, Steve Wozniak and Ronald Wayne"],
    ["Samsung: It is a South Korean multinational manufacturing conglomerate headquartered in Samsung Town, Seoul, South Korea.  It produces a wide range of products like clothing, automotive,  electronic components, medical equipment, telecommunications equipment and home appliances. It was created in 1938 by Lee Byung-chul."],
    ["Tesla Inc.: It is an American electric vehicle and clean energy company based in Austin, Texas. Tesla designs and manufactures electric cars, battery energy storage and related products and services. It was created in 2003 by  Martin Eberhard and Marc Tarpenning."],
    ["Google LLC: It is an American multinational technology company that specializes in Internet-related services and products, which include online advertising technologies, a search engine, cloud computing, software, and hardware. It was created in 1998 by Larry Page."],
    ["Microsoft Corporation: It is an American multinational technology corporation which produces computer software, consumer electronics, personal computers, and related services. It was created in 1975 by Bill Gates and Paul Allen."]]
filename="records.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    csvwriter.writerows(rows)

while True:
           clrscr()
           print("\t\t\t VIRTUAL ASSETS MANAGING TOOL")
           print("\t\t\t ***************************\n")
           print("\t\t 1. STOCK MANAGEMENT")
           print("\t\t 2. INVEST MANAGEMENT")
           print("\t\t 3. SALES MANAGEMENT")
           print("\t\t 4. USER MANAGEMENT")
           print("\t\t 5. DATABASE SETUP")
           print("\t\t 6. SHOW INFORMATION")
           print("\t\t 7. EXIT\n")
           n=int(input("Enter your choice :"))
           if n== 1:
                      Stock_mgmt()
           if n== 2:
                      os.system('cls')
                      invest_mgmt()
           if n== 3:
                      sales_mgmt()
           if n== 4:
                      user_mgmt()
           if n==5:
                      db_mgmt()
           if n==6:
                       show_info()
           if n== 7:
                     print("\n"
                              "      \n"
                              "          ##======================================================##\n"
                              "          ||                           THANK YOU                  ||\n"
                              "          ##======================================================##\n"
                              "\n")
                     print("***DEVELOPED BY SADIQ SALAM, YEYATI PRASHER, YASH BILTORIA XII-A 2021-22***")
                     break
