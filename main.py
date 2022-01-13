import mysql.connector as mysql


db=mysql.connect(host="localhost", user="root", password="", database="college")
command_handler=db.cursor(buffered=True) 


def admin_session():
    print("logged in")
    while True:

        print("admin menu")
        print("1.Register new student")
        print("2.Register new teacher")
        print("3.Delete Student")
        print("4.Delete teacher")
        print("5.logout")
        user_option=input("option:")
        if user_option=="1":
            print('registering new student')
            username_new=input("Enter new student username ")
            password_new=input("Enter new student password ")
            query_values=(username_new,password_new)
            command_handler.execute("Insert into users (username,password,privilege) values (%s,%s,'student')",query_values)
            db.commit()
            print(username_new+"has been registered as a student")
        elif user_option=="2":
            print('registering new teacher')
            username_new=input("Enter new student username ")
            password_new=input("Enter new student password ")
            query_values=(username_new,password_new)
            command_handler.execute("Insert into users (username,password,privilege) values (%s,%s,'teacher')",query_values)
            db.commit()
            print(username_new+"has been registered as a teacher")
        elif user_option=="3":
            print("deleting student account ")
            username=input("input username ")
            query_values=(username,"student")
            command_handler.execute("DELETE FROM users WHERE username = %s and privilege =%s ",query_values)
            db.commit()
            if command_handler.rowcount<1:
                print("user not found")
            else:
                print("user deleted")
        elif user_option=="4":
            print("deleting student account ")
            username=input("input username ")
            query_values=(username,"teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s and privilege =%s ",query_values)
            db.commit()
            if command_handler.rowcount<1:
                print("user not found")
            else:
                print("user deleted")
        elif user_option=="5":
            break






def auth_admin():
    print("admin login")
    username=input("Enter username ")
    password=input("Enter password ")
    if username=="admin":
        if password=="admin":
            admin_session()
        else:
            print("wrong password")




def main():
    while True:
        print("Welcome")
        print('')
        print('1. Login as student')
        print('2. Login as teacher')
        print('3. Login as admin')
        user_option = input("Option: ")

        if user_option == "1":
            print("Student Login")

        elif user_option == "2":
            print("Teacher Login")

        elif user_option == "3":
            auth_admin()

        elif user_option == "4":
            break
        
main()
