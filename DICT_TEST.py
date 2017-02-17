dict = {'Name': 'Zara', 'Age': '7', 'Class': 'First'}
dict1={'sal':'20000','email':'xyz@com'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
x=dict.copy()
x.update(dict1)
print(x)
#print(dict.items())