t = ('a', 'b')
print(t)

t = ('A',) + t[1:]
print(t)

a = 5
b = 10
a, b = b, a
print(a, b)

email = "joaozinho@gmail.com"
usuario, dominio = email.split("@")
print(usuario)
print(dominio)