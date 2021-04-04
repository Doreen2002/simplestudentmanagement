from getpass import *  #module allowing the input  password to be show in security character
from mysql.connector import * #module connecting to mysql
try:  #handling exception
    with connect(
        host = "localhost",
        user = input("enter username:"),
        password = getpass("enter password:"),  #details for connecting aspecifific database
        database = input("enter name of database:")
    )as connection:
        #if connection is succefull
        def insertStudentinfo(record):  #function for inserting in the Studentinfo table
            record = ( StudentID, Name, Contactinfo, AdmYear, Course)
            Insert_Query = 'Insert into Studentinfo (StudentID, Name, Contactinfo, AdmYear, Course) values (%s,%s,%s,%s,%s);'  #query for inserting
            with connection.cursor() as cursor:
                cursor.execute(Insert_Query,record)
                connection.commit()
        def insertAccountinfo(Accountinfo):   # function for inserting in the Account table
            Accountinfo = ( TotalFees, PaidFees, Balance,StudentID, Recieptno)
            Insert_Query = 'Insert into Accounts (TotalFees, PaidFees,Balance,StudentID, RecieptNo) values (%s,%s,%s,%s,%s);'   #query for inserting
            with connection.cursor() as cursor:
                cursor.execute(Insert_Query, Accountinfo)
                connection.commit()
        def insertMarkfile(Markfile):  # function for inserting in the Markfile table
            Markinfo = (StudentID, Monthlytest, Termlytest, TestNo )
            Insert_Query = 'Insert into Marksfile (StudentID, Monthlytest, Termlytest, TestNo) values (%s,%s,%s,%s);'  #query for inserting
            with connection.cursor() as cursor:
                cursor.execute(Insert_Query, Markinfo)
                connection.commit()
        def Studentrecord():  # function for retriving student number ,studentname, course, montly test, account balance from the tables using full join
            details_query = '''select Studentinfo.StudentID, Studentinfo.Name, Studentinfo.Course, Marksfile.TestNo, Accounts.Balance from Studentinfo inner 
            join Marksfile on Studentinfo.StudentID=Marksfile.StudentID inner join Accounts on Marksfile.StudentID=Accounts.StudentID;'''
            with connection.cursor() as cursor:
                cursor.execute(details_query)
                for details in cursor.fetchall():
                    print(details)
                connection.commit()
        print("enter 1 to register student")
        print("enter 2 make payments for student")
        print("enter 3 enter marks   for student")
        print("enter 4 view student details")
        ch = int(input("enter choice"))
        if ch == 1:
            StudentID = int(input("enter student number"))
            Name = input("enter student name")
            Contactinfo = input("enter phone number")
            AdmYear = input("enter admmited year")
            Course = input(" enter course")
            record = (StudentID, Name, Contactinfo, AdmYear, Course)
            insertStudentinfo(record)
        if ch == 2:
            StudentID = int(input("enter student number"))
            TotalFees= float(input("enter amount to be paid "))
            PaidFees = float(input("enter amount paid "))
            Balance = TotalFees - PaidFees
            Recieptno = int(input("enter receipt no "))
            Accountinfo = ( TotalFees, PaidFees, Balance,StudentID, Recieptno)
            insertAccountinfo(Accountinfo)
        if ch == 3:
            StudentID = int(input("enter student number"))
            Monthlytest = float(input("enter monthly mask"))
            Termlytest = float(input("enter termly test"))
            TestNo= int(input("enter  test number"))
            Markinfo = (StudentID, Monthlytest, Termlytest, TestNo)
            insertMarkfile(Markinfo)
        if ch == 4:
            Studentrecord()

except Error as e:
    print(e) #prints error that occurs in the database if any








