import string
import numpy as np


letters=string.ascii_lowercase   #abcdefghi........
plain=input("Enter plaintext: ") #"paymoremoney"

n=int(input(" Enter the number of rows/cols: "))

key=[

]

for i in range(n):
    row=[   ]
    for j in range(n):
        ele=int(input(" enter element "+str(i)+","+str(j)))
        row.append(ele)
    
    key.append(row)

n=len(key)

cipher=""
for i in range(0,len(plain),n):
    slice=plain[i:n+i]  
    
    temp=[]
    for letter in slice: 
        temp.append(letters.index(letter))
    
    temp=np.array(temp)
    key=np.array(key)
    
    result=np.dot(temp,key) % 26
    
    for r in result:
        cipher+=letters[r]

print(cipher)
