n : int
soma : float
maior : float
menor : float
media : float
cont : int

n = int(input("Quantos dias serão digitados: "))

vet : [float] = [0 for x in range (n)]

for i in range( n):
    vet[i] = float(input(f"Digite o faturamento do dia {i+1}: "))

menor = vet[0]
for i in range(n):
    if vet[i] < menor:
        if vet[i] != 0:
            menor = vet[i]

maior = vet[0]
for i in range(n):
    if vet[i] > maior:
        if vet[i] != 0:
            maior = vet[i]

soma = 0
for i in range(n):
    soma = soma + vet[i]

if vet[i] == 0:
    n = n - 1

media = 0
if vet[i] != 0:
    media = soma / n

cont = 0
if vet[i] > media:
    cont = cont + 1

print()
print(f"Menor valor do mês foi: {menor}")
print(f"Maior valor do mês foi: {maior}")
print(f"Dias no mês em que o valor de faturamento diário foi superior à média mensal: {cont}")


