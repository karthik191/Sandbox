


data  =  [line.rstrip('\n') for line in open('mailList.txt')]
print(len(data))
for email in data:
    print(email.split('@')[0].replace('.',' '))