class SystemManager:
    '''A class for managing system operations.
    '''
    
    # We are not going to use an __init__ function. We'll just call the default
    # constructor.
    
    def check_username_password(self, users, username, password):
        '''
        Checks whether the username exists in the users dictionary and that the password matches the username.  Returns boolean.
        '''
        if username not in users or users[username] != password:
            return False
        return True

    
    def is_valid_password(self, password):
        '''
        Checks whether the given password is valid.  Returns boolean.
        The length of a valid password should be at least 8 characters and it should contain
        at least one lowercase character, one uppercase character, and one number.
        '''

        if password is None:
            return False
        
        if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password)):
            return True
        else:
            return False     

    
    def sign_up(self, users, logged_in, username, password):
        '''
        Allows users to sign up.
        If the username already exists in the users dictionary, prints a friendly message.
        If the password does not satisfy the rule(s) (not valid), prints a friendly message.
        Otherwise, saves the username and the corresponding password in the users dictionary, and prints a
        success message.

        Note(s):
        The user is not automatically logged in when he/she signs up.
        '''
        
        if username in users:
            print('Welcome, you have already opened an account.')
        elif not self.is_valid_password(password):
            print('Your password does not meet criteria')
        else:
            users[username] = password
            logged_in[username] = False
            print('You have successfully signed up')
            return True
        return False

       
    def log_in(self, users, logged_in, username, password):
        '''
        Allows users to log in.
        If the username does not exist in the users dictionary or the password is incorrect, prints an error message.
        Otherwise, saves the username and the value of True in the logged_in dictionary, and prints a welcome message.

        Note(s):
        Even if a user is already logged in, he/she can log in again.
        '''
        
        if not self.check_username_password(users, username, password):
            print('Error: Your account does not exist or Your password is incorrect.')
            
        else:
            logged_in[username] = True
            print(f"Welcome back {username} !!")
            return True
        
        return False

    def change_password(self, users, username, old_password, new_password):
        '''
        Allows users to change their password.
        If the username does not exist in the users dictionary, prints an error message.
        If the old_password is incorrect, prints an error message.
        If the new_password does not satisfy the rule(s) (not valid), prints an error message.
        Otherwise, changes the user's password in the users database, and prints a success message.
        '''
        if not self.check_username_password(users, username, old_password):
            print('Error: Invalid username or password.')
        elif not self.is_valid_password(new_password):
            print('Error: New password does not meet criteria.')
            return False
        else:
            users[username] = new_password
            print('Success: Your password has been successfully updated.')
            return True
    
    def delete_account(self, users, logged_in, username, password):
        '''
        Allows users to delete their account.
        If the username does not exist in the users database, prints an error message.
        If the password is incorrect, prints an error message.
        Otherwise, deletes the user's account from the users dictionary, and prints a success message.

        Note(s):
        Also deletes the user's information in the logged_in dictionary.
        '''
        
        if not self.check_username_password(users, username, password):
            print('Error: Username does not exist.')
        else:
            del users[username]
            if username in logged_in:
                del logged_in[username]
            print('Success: Your account has been successfully deleted.')
            return True
        return False
        

    def get_sign_ups(self, users):
        '''
        Returns a list of users who are signed up (in the users dictionary).
        '''
        return list(users.keys())

    def get_log_ins(self, logged_in):
        '''
        Returns a list of users who are logged in (in the logged_in dictionary).
        '''
        return [user for user, is_logged_in in logged_in.items() if is_logged_in]