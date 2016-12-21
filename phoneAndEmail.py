## python3
## phoneAndEmail.py
## searches text in clipboard and extracts phone numbers and email addresses

import pyperclip, re


#phone number RegEx
phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #areacode
    (\s|-|\.)?          # separator
    (\d{3})             # first three digits
    (\s|-|\.)           # separator
    (\d{4})             # last three digits
    (\s*(ext|x|ext/)\s*(\d{2,5}))?  #extension
    )''', re.VERBOSE)
#email Regex
emailRegex=re.compile(r'''(
    [a-zA-Z0-9._%+-]+     #username
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

#collect matches and add to a string
text=str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
    phoneNum= "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum+=' x'+groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

#copy results to clipboard
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    
