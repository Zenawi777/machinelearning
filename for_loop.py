'''
for x in range(5):
    print(x)
    



for x in range(3,6):
    print(x)
    
for x in range(2,10,2):
    print(x)
    
'''

k=2
while(k<200):
    j=2
    while(j<= (k/j)):
        if not (k%j): break
        j=j+1
    if (j>k/j): print(k,'is prime')
    k=k+1
