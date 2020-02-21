#1
#a)
a = 2**3*3
print(a)

#b)
b = 2**(3*3)
print(b) 

#c)
c = 3*5+2//7
print(c)

#d)
d = 3*5//2
print(d)

#e)
e = 5//2*3
print(e)

#f)
f = 22%8/4
print(f)

#g)
g = 22%(8/4)
print(g)

#h)
h = 34/8*3
print(h)

#2
#a
a2 = 'carro'+'casa'
print(a2)

#3
#a - V
#b - F
#c - F
#d - F
#e - F
#f - V
#g - V
#h - V
#i - F
#j - V

#4
print("Name?")
name = input()
print("Ano de Nascimento?")
birth_year = input()
print("Rua?")
street = input()
print("Postal Code?")
postal_code = input()
print(f'Boas {name} tens {2020 - int(birth_year)}, e vives na {street} {postal_code} e tem {len(street+postal_code)} caracteres!')
