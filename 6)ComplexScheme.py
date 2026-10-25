


plain="attackpostponeduntiltwoamxyz"
key="4312567"

dict={}
for k in key:
    dict[k]=""


for i in range(0,len(plain)):
    idx=i%len(key)
    dict[key[idx]]=dict[key[idx]]+plain[i]


print(dict)   
collect=""
key=list(key)
key.sort()

for k in key:
    collect=collect+dict[k]

print(collect)
    

