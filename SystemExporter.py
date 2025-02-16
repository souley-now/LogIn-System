class SystemExporter:
    '''A class for exporting user credentials to a file.
    '''
    
    # We are not going to use an __init__ function. We'll just call the default
    # constructor.
    
    def write_users_db(self, users, file):
        '''
        Writes all usernames and passwords in the users dictionary, to the given file.
        Each row is a comma-separated list including username and password.

        Example(s):
        lbrandon,My_Crazy_Password_1234
        tjones,4er3yw6rt5R
        dennisq,0987poiu1234QwEr
        '''

        with open(file, 'w') as stream:
            for username, password in users.items():
                stream.write(f"{username},{password}\n")
