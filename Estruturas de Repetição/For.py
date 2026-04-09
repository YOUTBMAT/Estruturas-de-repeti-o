# import time

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# for i in range (0, 11):
#     print (i)
#     time.sleep(1)


# for i in range(0,10):
#     if i % 2 == 0:
#         print (f"{i} é par")
#     else: 
#         print (f"{i} é impar")


# vogais = ['a','e','i','o','u']
# palavra = input("Digite uma palavra que começe com consoante: ")
# for letra in palavra:
#     primeiraLetra = palavra[0].lower()
#     if primeiraLetra in vogais:
#         break
#     print (letra)


for linha in range(3):
    for coluna in range(4):
        print("*", end=" ")
    print()