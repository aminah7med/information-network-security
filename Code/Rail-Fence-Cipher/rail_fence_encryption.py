

plain="meetmeafterthetogaparty"
even=""
odd=""
for i in range(0,len(plain)):
    if i%2==0:
        even=even+plain[i]
    else:
        odd=odd+plain[i]


cipher=even+odd

print(cipher)

