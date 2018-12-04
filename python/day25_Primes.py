N=int("3")
for _ in range(N):

"""
int isPrime(int n, int i){
    if(n%i==0 && n!=2 && n!=i){
      return(0);
    } else {
       if (i < sqrt(n)) {
            return( isPrime(n,i+1) );
        } else
         return 1;
    }
}

"""

def isPrime(num):
    if num == 1:
        print("Not prime")
        return
    if num == 2:
        print("Prime")
        return
    if num%2 == 0:
        print("Not prime")
        return
    for i in range(3,round(num**0.5)+1):
        if num%i == 0:
            print("Not prime")
            return
    print("Prime")



isPrime(12)
isPrime(5)
isPrime(7)
isPrime(1)
isPrime(2)

1000000007**0.5

isPrime(1000000007)
isPrime(100000003)
isPrime(1000003)


isPrime(1000000000)
isPrime(1000000001)
isPrime(1000000002)
isPrime(1000000003)
isPrime(1000000004)
isPrime(1000000005)
isPrime(1000000006)
isPrime(1000000007)
isPrime(1000000008)
isPrime(1000000009)


isPrime(1)
isPrime(4)
isPrime(9)
isPrime(16)
isPrime(25)
isPrime(36)
isPrime(49)
isPrime(64)
isPrime(81)
isPrime(100)
isPrime(121)
isPrime(144)
isPrime(169)
isPrime(196)
isPrime(225)
isPrime(256)
isPrime(289)
isPrime(324)
isPrime(361)
isPrime(400)
isPrime(441)
isPrime(484)
isPrime(529)
isPrime(576)
isPrime(625)
isPrime(676)
isPrime(729)
isPrime(784)
isPrime(841)
isPrime(907)
