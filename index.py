import sqlite3
connect=sqlite3.connect("Bank.db")
cursor=connect.cursor()

# cursor.execute("CREATE TABLE ACCOUNTS(acc_number number(16) primary key ,name varchar(32) not null,phone number(10) not null unique,email varchar(256) not null unique,balance number(8,2) default(1000),pin number(4) default(0),address varchar(256) not null );")

# cursor.execute("insert into ACCOUNTS(acc_number,name,phone,email,address) values (1234567891011121 , 'ratna sai' , 1234567890 , 'ratnasai@gmail.com' , 'panjagutta hyderabad telangana')")
# connect.commit()

def acc_creation(name,phone,email,address):
    data=cursor.execute("select acc_number from ACCOUNTS")
    a=data.fetchall()
    new_acc=(a[-1][-1])+1
    cursor.execute(f"insert into ACCOUNTS (acc_number,name,phone,email,address) values ({new_acc},'{name}',{phone},'{email}','{address}')")
    connect.commit()

def pin_gen(account, phone):
    data = cursor.execute(f"select * from ACCOUNTS where acc_number = {account}").fetchone()
    if data [2] == phone:
        pin = int(input("ENTER YOUR PIN"))
        cursor.execute(f"update ACCOUNTS set pin = {pin} where acc_number = {account}")
        connect.commit()
        print("pin generated successfully")
    else:
        print("MOBILE NUMBER DON'T MATCH")

def balance (acc,pin):
    data = cursor.execute(f"select * from ACCOUNTS where acc_number = {acc}").fetchone()
    if data [5] == pin:
        print(f"the available balance is {data[4]}")
    else:
        print("incorrect pin")

def withdrawl (acc,pin):
    data = cursor.execute(f"select * from ACCOUNTS where acc_number = {acc}").fetchone()
    if data [5] == pin:
        amt = int(input("ENTER THE AMOUT TO WITHDRAWL"))
        if amt <data [4] and amt> 0 and amt<=10000 :
            cursor.execute (f"update ACCOUNTS set balance = {data[4]-amt} where acc_number = {acc}")
            connect.commit()
            print (f"thanks for using BOB bank")
        else:
            print("invalid amt")
    else:
        print("incorrect pin")

def deposit (acc, pin):
    data= cursor.execute(f"select * from ACCOUNTS whereacc_number = {acc}").fetchone()
    if data [5] == pin:
        amt= int(input("ENTER THE AMOUT TO DEPOSIT"))
        if amt>= 500 and amt<=100000:
            cursor.execute(f"update ACCOUNTS set balance = {data[4]+amt} where acc_number = {acc}")
            connect.commit()
            print (f"thanks for using BOB bank")
        else:
            print("invalid amt")
    else:
        print("incorrect pin")

def acc_transfer (from_acc,to_acc, pin):
    data = cursor.execute(f"select * from ACCOUNTS where acc_number = {from_acc}").fetchone()
    if data[5] == pin:
        amt = float(input("ENTER THE AMT"))
        if amt <data[4] and amt>0.0 and amt<= 100000.0:
            cursor.execute(f"update ACCOUNTS set balance = {data[4]-amt } where acc_number = {from_acc}")
            connect.commit()
            data1= cursor.execute(f"select * from ACCOUNTS where acc_number = {to_acc}").fetchone()
            cursor.execute(f"update ACCOUNTS set balance = {data1 [4]+amt} where acc_number = {to_acc}")
            connect.commit()
        else:
            print("invlaid amt")
    else:
        print("incorrect pin")

print("*"*40)

user= int(input(''' WELCOME TO BOB Bank (Bank of Bihar)

1) ENTER 1 TO CREATE AN ACCOUNT
2) ENTER 2 TO GENERATE PIN
3) ENTER 3 FOR BALANCE ENQUIRY
4) ENTER 4 TO WITHDRAW
5) ENTER 5 FOR DEPOSIT
6) ENTER 6 FOR ACCOUNT TRANSFER \n :- '''))
if user == 1:
    name = input("ENTER YOUR NAME :")
    phone = int(input("ENTER YOUR MOBILE NUMBER: "))
    email =input("ENTER THE MAIL ID :")
    address = input("Address Pettuu :")
    acc_creation(name, phone, email, address)
elif user == 2:     
    account = int(input("ENTER YOUR ACCOUNT NUMBER"))
    phone= int(input("ENTER YOUR REGISTERED MOBILE NUMBER"))
    pin_gen(account, phone)
elif user == 3:
    acc = int(input("ENTER YOUR ACCOUNT NUMBER"))
    pin = int(input("ENTER YOUR PIN"))
    balance (acc, pin)
elif user == 4:
    acc =int(input("ENTER YOUR ACCOUNT NUMBER"))
    pin = int(input("ENTER YOUR PIN"))
    withdrawl (acc, pin)
elif user == 5:
    acc = int(input("ENTER YOUR ACCOUNT NUMBER"))
    pin = int(input("ENTER YOUR PIN"))
    deposit (acc, pin)
elif user == 6:
    from_acc= int(input("ENTER YOUR ACCOUNT NUMBER"))
    to_acc= int(input("ENTER THE ACCOUNT NUMBER TO WHOM U NEED TO TRANSFER MONEY"))
    pin=int(input("ENTER THE PIN"))
    acc_transfer(from_acc, to_acc,pin)