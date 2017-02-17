fo=open("mytext.txt","w")
str=input("enter the data")
fo.write(str)
fo.close()
fo=open("mytext.txt","r")
for letters in fo:
    print("the data",letters)
#var=fo.read()
#print(var)
