n1 : int
n2 : int
n3 : int
n : int

n1 = 0
n2 = 1
n3 = 0
n = 0

n = int(input("Digite um numero: "))

while n > n3:
    n3 = n1 + n2
    n1 = n2
    n2 = n3

if n1 == 0 or n2 == 1:
    print("O numero faz parte da sequencia de Fibonacci")
elif n == n3:
    print("O numero faz parte da sequencia de Fibonacci")
else:
    print("O numero digitado não faz parte da sequencia de Fibonacci.")





