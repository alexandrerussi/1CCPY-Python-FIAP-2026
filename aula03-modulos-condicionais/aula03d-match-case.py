# imagina... um sistema que recolha escolha do usuario
# escolha_usuario
# se...
# 0 --> sair do programa
# 1 --> entrar no programa
# ----> erro!

escolha_usuario = 1234

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
        print("Erro!")