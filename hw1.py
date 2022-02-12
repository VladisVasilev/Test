from ast import Assert


login = []
password = []
email = []
phone_number = []

def proverka_login():
    try:
        login = input()
        assert 4<len(login)<20
        print ('Correct login')
    except AssertionError:
        login = []
        print('Login should be >4 and <20')

def proverka_password():
    try:
        password = input()
        assert 8<=len(password)<=15
        print ('Correct password')
    except AssertionError:
        login = []
        print('Password should be >=8 and <=15')

def proverka_email():
    try:
        email = input()
        assert 5<=len(email) and email.find('@')!=-1 and email.find('.')!=-1
        print ('Correct email')
    except AssertionError:
        login = []
        print('Email should be >=5 and contain @ and .')

def proverka_number():
    try:
        phone_number = input()
        assert len(phone_number)==11 and phone_number.isdigit()==True 
        print ('Correct phone number')
    except AssertionError:
        login = []
        print('Phone number should have 11 digits')

print('Please, enter your login')
proverka_login()
print('Please, enter your password')
proverka_password()
print('Please, enter your email')
proverka_email()
print('Please, enter your phone number')
proverka_number()


#assert
#except
#try
#finally