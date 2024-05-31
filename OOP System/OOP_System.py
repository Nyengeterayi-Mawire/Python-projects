
class User:
    def __init__(self,username,password):
        self.username=username 
        self.password=password 

    def check_username(self,username):
        return self.username == username

    def check_password(self,password):
        return self.password == password

class Bank_account:
    def __init__(self,username,balance = 0): 
        self.username=username
        self.balance = balance 

    def check_balance(self):
        print(f'Currnet balance : {self.balance}') 

    def deposit(self,amount):
        self.balance += amount 
        print(f'Currnet Balance : {self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient funds') 
        else:
            self.balance -= amount 
            print(f'Currnet Balance : {self.balance}')

class User_Manager:
    def __init__(self):
         self.user_list = [] 

    def Create(self,username,password): 
         valid = True
         if self.user_list == []: 
                created_user = User(username,password) 
               
                user = {'user': created_user,'account':  Bank_account(username) }
                self.user_list.append(user) 
               
                return user
         else:
            for user in self.user_list: 
                object_user = user.get('user')
                if object_user.username == username:
                    print('username already taken') 
                    valid=False
                    break
            if valid:
                created_user = User(username,password)                
                user = {'user': created_user,'account':  Bank_account(username) }
                self.user_list.append(user)
                
                print(f'created user : {username}')  
                return user
            else:
                return False 

    def Login(self,username,password):
        for user in self.user_list:
            user_object = user.get('user') 
            if user_object.check_username(username):
                if user_object.check_password(password):
                    print('Successfully logged in')
                    return user 
                else:
                    print('Incorrect password')
                    return False
            print('Incorrect username')
            
        

    def __str__(self):
        print(f'list : {self.user_list}')


   
def main():
   user_list = User_Manager()  
   user_logged_in = {} 
   def Login_Logout_Page():
       print('Click one of the following\n 1.login\n 2.SignUp ')
       choice = int(input('What would you like to do '))
       if choice == 1 :
            while True:
              username=input('please enter your username')
              password = input('please enter your password')

              check = user_list.Login(username,password) 
              user_logged_in = check
              
              if check:
                  Home_Page(check) 
                  break 
              else:
                  continue
       elif choice == 2:
          while True:
              username=input('please enter your username')
              password = input('please enter your password')

              check = user_list.Create(username,password) 
              user_logged_in = check
             
              if check: 
                  Home_Page(check) 
              else:
                  continue 
       else:
           print('Invalid input : Please chose one of the specified options') 
           Login_Logout_Page()
   def Home_Page(user_logged_in):
       print('Select one of the options\n 1.Check Balance\n 2.Deposit\n 3.Withdraw\n 4. Logout') 
       while True:
            selection = int(input('What would you like to do ')) 
            account = user_logged_in.get('account')
            if selection == 1 :            
                account.check_balance()
            elif selection == 2: 
                amount = int(input('Enter amount to deposit'))
                account.deposit(amount)
            elif selection == 3:
                amount = int(input('Enter amount to withdraw'))
                account.withdraw(amount)
            elif selection == 4:
               Login_Logout_Page()
            else:
                print('TRY AGAIN : please enter the displayed option') 
                continue

   Login_Logout_Page()
    

    

if __name__ == "__main__":
    main()

