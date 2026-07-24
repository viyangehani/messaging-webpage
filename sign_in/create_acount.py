import pandas as pd
df=pd.read_csv('identity.csv')
print(" hi i am, actually,  you don't need to know, but to sign in, it is nessacary to input your name, or at least, what youwant to be called")
print()
name=input()
print('now enter your username you want')
print()
username=input()
print('enter the oassword you want')
print()
password=input()
while len(password)<8:
  password=input('try again')

