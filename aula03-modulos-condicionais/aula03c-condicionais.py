# RELACIONAIS
idade = 17

maior_idade = idade >= 18
print(maior_idade)

if maior_idade:
    print("Maior de idade")

# OPERADORES LÓGICOS
# AND, OR, NOT
verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if not login:
    print("Tu é burro hein, tenta dnv ai")

# NOTAS....
print() # pular uma linha
nota_final = 10

if nota_final < 4:
    print("Reprovado")
elif nota_final < 6:
    print("Recuperação")
else:
    print("Aprovado")

print("FIM")



