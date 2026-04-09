# import time

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# for i in range (0, 11):
#     print (i)
#     time.sleep(1)

vogais = ['a','e','i','o','u']
palavra = input("Digite uma palavra que começe com consoante: ")
for letra in palavra:
    primeira_letra = palavra[0].lower()
    if primeira_letra in vogais:
        break
    print (letra)