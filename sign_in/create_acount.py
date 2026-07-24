import pandas as pd
df=pd.read_csv('identity.csv')
print(" hi i am, actually,  you don't need to know, but to sign in, it is nessacary to input your name, or at least, what youwant to be called")
print()
name=input()
print('now enter your username you want')
print()
username=input()
print('enter the password you want')
print()
password=input()
while len(password)<8:
  password=input('try again')
acount_data={"name":name,"email":username,"password":password}
dfinfo=pd.DataFrame([acount_data])
df=pd.concat([df, dfinfo], ignore_index=True)
df.to_csv("identity.csv", index=False)
