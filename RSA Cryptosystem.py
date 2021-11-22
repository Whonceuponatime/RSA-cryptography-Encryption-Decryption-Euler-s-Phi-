#RSA Cryptosystem
#gcd and Euler's Phi function from https://www.geeksforgeeks.org/eulers-totient-function/
print("P value: ", end = "")
p = input()
print("Q value: ", end="")
q = input()
n = int(p)*int(q)

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)
phi_n = (phi_func(n))
print("Phi = ", end ="")
print(phi_n)
print("Public Key: ", end ="")
public_key = int(input())
print("Private Key: ", end ="")
private_key = int(input())
print("Message: ", end = "")
message = int(input())
def enc(public, m): 
    c = (m**public)%n
    print("Encrypted")
    print(c)
    return c
def dec(private, c):
    m = (c**private)%n
    print("Decrypted")
    print(m)
encrypted = enc(public_key, message)

dec(private_key, encrypted)
