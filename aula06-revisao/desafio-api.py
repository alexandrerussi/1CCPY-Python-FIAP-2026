endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# FUNÇÃO que verifica se UM código http de uma
# requisição é sucesso ou não
# 200 -> True
# 401 -> False
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# FUNÇÃO que verifica se tem 2 erros seguidos em
# uma lista de requisições (codigos) de UM endpoint
# [200, 200, 401, 200, 500] -> False
# [201, 500, 502, 201, 500] -> True
def erros_seguidos(codigos):
    for i in range(len(codigos) - 1):
        codigo_atual = codigos[i]
        prox_codigo = codigos[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

print(erros_seguidos(status[2]))







