numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers)

numbers.extend([7, 8, 9])
print(numbers)

numbers.insert(0, 0)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.pop(0)
print(numbers)

# -----------------

item = ["Maçã", "Banana", "Laranja"]
utem= ["comprar", "trocar"]

for u in utem:
    for i in item:
        print(f"{u}: {i}") 

#------------------

# secret = 2
# guess = 0

# while guess != secret:
#     guess = int(input("Tente: "))
#     if guess != secret:
#         print("NOOOO")

# print("SIIIIIIIUUUUUU")

#------------------

# words = ["sky", "sun", "msdvn", "star", "svsvv", "earth"]

# for word in words:
#     for letter in word:
#         if letter in 'aeiou':
#             print(f"{word} tem vogal")
#             break

#     else:
#         print(f"{word} não tem vogal")


#-----------------

# numeros = [1, 2, 3, 4, 5]

# for n in numeros:
#     if n == 3:
#         continue
#     print(n)

# for n in numeros:
#     if n == 3:
#         break
#     print(n)

#-----------------

# for n in range(0, 11, 2):
#     print(n)

#-----------------

developer = ["Alfa", "Papa", "Charlie", "Delta", "Mike"]

codes = ["A", "P", "C", "D", "M"]

for name, code in zip(developer, codes):
    print(f"{name} - {code}")

#-----------------

numeros = [1, 2, 3, 4, 5]

def sum(a):
    return a + 2

sum = list(map(sum, numeros))
print(sum)

#-----------------

