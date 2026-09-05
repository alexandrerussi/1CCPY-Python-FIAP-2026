eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    "one": "uno",
    "two": "dos"
}

print(eng2sp)
print(len(eng2sp))

print('dos' in eng2sp)

valores = eng2sp.values()
print('dos' in valores)

print()

def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("Maçã")
print(dict_contagem)

print()

personagens_nomes = ["rick", "morty"]

personagens = [
    {
        "nome": "Rick",
        "idade": 70,
        "hobbies": ["xingar", "beber", "comer planetas"]
    },
    {
        "nome": "Morty",
        "idade": 14,
        "hobbies": ["jessica", "minecraft"]
    }
]

for personagem in personagens:
    # nome = personagem["nome"]
    # idade = personagem["idade"]

    for key, value in personagem.items():
        print(f"{key}: {value}")

    print()









