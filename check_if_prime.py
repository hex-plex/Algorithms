def is_prime(a):
    x = True
    for j in range(2,int(a/2)):
        if(a%j==0):
            x=False
            break
    if x:
        print("Its a Prime")
    else: 
        print("Its not a Prime")
