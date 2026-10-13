#Employee Profile Validator
email = 'alice.johnson@company.com' # Employee's email
print(f'Email: {email}') # output: Employee's email

at_position = email.find('@') # Find the position of @ in employee email
print(f'Position of @: {at_position}') # output: position of @ in email 

username = email[:at_position] # Slicing employee's email up to the @ position 
print(f'Username: {username}') # output: result of slicing employee email up to @ position to give username

has_at = '@' in email # Checking employees email to see if the @ is present
print(f'Has @ symbol: {has_at}') # output: returns true or false after checking for the @ symbol in email

has_com = '.com' in email # # Checking employees email to see if the .com is present
print(f'Has .com: {has_com}') # output: returns true or false after checking for the .com in email

messy_name = '  sARaH dAVis  ' # Employee's name but in untidy form
print(f"Original name: '{messy_name}'") # output: employee's name in untidy form

clean_name = messy_name.strip().title() # Removing leading and trailing space and capitalising first letter of words  
print(f"Cleaned name: '{clean_name}'") # output: employee's name cleaned with leading and trailing space removed and first letter of words capitalised

messy_email = '  SARAH.DAVIS@COMPANY.COM  ' # Employee's email in untidy form
clean_email = messy_email.strip().lower() # Removing leading and trailing space and lower casing employee's email
print(f"Original email: '{messy_email}'") # output: Employee's email in untidy form
print(f"Cleaned email: '{clean_email}'") # output: employee's email cleaned with leading and trailing space removed and in lowercase 

name_badge = clean_name.upper() # Employee's name badge all in upper case
print(f'Name badge: {name_badge}') # output: Employee's name badge in upper case

at_pos = clean_email.find('@') # Find the position of @ in employee email
email_user = clean_email[:at_pos] # Slicing employee's email up to the @ position 

print(f'Email: {clean_email}') # output: Employee email
print(f'Username: {email_user}') # output: result of slicing employee email up to @ position to give username

display_name = email_user.replace('.', ' ').title() # Employee display name replacing the . with a space
print(f'Display name: {display_name}') # output: Employee display name with space rather than .

phone = '123-456-7890' # Storing phone number in variable
phone_clean = phone.replace('-', '') # Replacing the dash in phone number so there is no space
print(f'Phone with dashes: {phone}') # output: number with dashes 
print(f'Phone without dashes: {phone_clean}') # output: number without dashes

full_address = '123 Main Street, Springfield, IL' # Storing address in variable
address_parts = full_address.split(', ') # Splitting address by commas and spaces
print(f'Address parts: {address_parts}') # output: address split with commas and spaces

rejoined = ' | '.join(address_parts) # Rejoining the address by | symbol
print(f'Rejoined: {rejoined}') # output: rejoined address by | symbol

employee_code = 'EMP-2024-SD' # Storing employee code in variable
starts_with_emp = employee_code.startswith('EMP') # Checking to see if the employee code starts with EMP
ends_with_com = clean_email.endswith('.com') # Checking to see if the employee email ends with .com 

print(f'Code: {employee_code}') # output: Employee code 
print(f'Starts with EMP: {starts_with_emp}') # output: result of checking if employee code starts with EMP as True or False 
print(f'Clean email: {clean_email}') # output: employee email
print(f'Ends with .com: {ends_with_com}') # output: result of checking if employee email ends with .com as True or False

dot_count = clean_email.count('.') # Counting how many dots in email
dash_count = employee_code.count('-') # Counting how many dashes in email

print(f'Dots in email: {dot_count}') # output: how many dots in email as a number
print(f'Dashes in code: {dash_count}') # output: how many dashes in email as a number