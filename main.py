from tabulate import tabulate
import mysql.connector

con=mysql.connector.Connect(host="localhost",user="root",password="Prema@123",database="python_db")

if con:
    print("Connected")
else:
    print("No")


def insert(Name,age,city):
    res=con.cursor()
    sql="insert into users(Name,age,city)values(%s,%s,%s)"
    user=(Name,age,city)
    res.execute(sql,user)
    con.commit()
    print("Inserted Sucessfully")


def update(Name,age,city,id):
    res=con.cursor()
    sql="update users set Name=%s,age=%s,city=%s where id=%s"
    user = (Name,age,city,id)
    res.execute(sql,user)
    con.commit()
    print("Updated Sucessfully")

def select():
    res=con.cursor()
    sql = "SELECT ID,NAME,AGE,CITY from users"
    res.execute(sql)
    #result=res.fetchone()
    result = res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))


def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user = (id,)
    res.execute(sql,user)
    con.commit()
    print("Deleted Sucessfully")

while(True):
    print("1.Insert")
    print("2.Update")
    print("3.Select")
    print("4.Delete")
    print("5.Exit")

    choice = int(input("Enter your Choice"))
    if choice == 1:
        Name=input("Enter name")
        age =input("Enter age")
        city=input("Enter city")
        insert(Name,age,city)
    elif choice == 2:
        id=input("Enter Id")
        Name=input("Enter name")
        age =input("Enter age")
        city=input("Enter city")
        update(Name,age,city,id)
    elif choice == 3:
        select()

    elif choice == 4:
        id=input('Enter id')
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection.Please Try Again Later")
