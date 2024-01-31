import re

def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+)\.[A-Z|a-z]{2,3}$\b'
    match = re.match(regex, email.lower())
    
    if match:
        return re.findall(r'@(.+?)\.', email.lower())[0]
    else:
        return None

def main():
    email = input('Enter email: ')
    webservice = check_email(email)

    if webservice:
        if webservice == 'gmail':
            print('You entered a Google mail :)')
        elif webservice == 'yahoo':
            print('You entered a Yahoo! mail :)')
        else:
            print('You entered a', webservice, 'mail :)')
    else:
        print('Invalid Email')

    check_for_second = input('Do you want to enter a 2nd email? (Y/N)').lower()
    
    if check_for_second == 'y':
        second_email = input('Enter 2nd email: ')
        webservice = check_email(second_email)

        if webservice:
            print('You entered a', webservice, 'mail as 2nd email :)')
        else:
            print('Invalid Email')

if __name__ == "__main__":
    main()
