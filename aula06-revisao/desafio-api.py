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

# LISTA DE REQUISIÇÕES DE 1 ENDPOINT
# [200, 200, 401, 200, 500]

def analisar_endpoint(codigos_endpoint):
    qtd_sucesso = 0

    for codigo in codigos_endpoint:
        if eh_sucesso(codigo):
            qtd_sucesso += 1

    qtd_total = len(codigos_endpoint)
    qtd_erros = qtd_total - qtd_sucesso
    porcentagem_sucesso = (qtd_sucesso / qtd_total) * 100

    tem_erros_seguidos = erros_seguidos(codigos_endpoint)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif porcentagem_sucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucesso, qtd_erros, porcentagem_sucesso, classificacao)

# PERCORRENDO A MATRIZ status
maior_erro = 0
endpoint_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    codigos_http = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(codigos_http)

    if erros > maior_erro:
        maior_erro = erros
        endpoint_maior_erro = nome_endpoint

    print(f"Endpoint: {nome_endpoint}")
    print(f"Requisições: {codigos_http}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual}")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()

print(f"Endpoint maior erro: {endpoint_maior_erro} ({maior_erro})")





