import mysql.connector as  sql
conn=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'admin@123', database='courier_service_system' )
cust1=conn.cursor()
print('WELCOME TO ULTRA COURIER SERVICE:')
o=input('Press enter to begin your courier surfing')
print('1.CREATE YOUR COURIER SERVICE ACCOUNT')
print('2.LOGIN')
choose=int(input('ENTER (1) FOR NEW ACCOUNT OR (2) FOR LOGIN:'))
if choose==1:
     name=input('Enter your user name: ')
     passwd=input('Set your password here: ')
     passwd1=input('Confirm password: ')
     cust1.execute("INSERT INTO login (user_name, password) VALUES ('"+name+"','"+passwd+"')")
     conn.commit()
     print('Congratulation, Your account has been successfully created.')
     move_in=input('Press enter to login')
     import B_COURIER_MENU
elif choose==2:
     email=input('Enter your user name: ')
     passd=input('Enter your password: ')
     cust1.execute('select * from login where user_name="'+email+'" and password="'+passd+'"')
     if cust1.fetchone() is None:
          print('Sorry, your username or password is incorrect.Please try again.')
     else:
         import B_COURIER_MENU
