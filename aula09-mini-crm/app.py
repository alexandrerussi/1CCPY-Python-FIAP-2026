from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    stage = input("Etapa no funil: ")

    # validar os dados
    # pegar os dados de name, email e stage e... MODELAR como DICT
    # model... lead como um dict
    print(model_lead(name, email, stage))

    # com meu lead modelado como dicionario...
    # posso enviar esse lead para o leads.json
    # para enviar, usaremos o control
    control.create_lead(model_lead(name, email, stage))

    print("leads adicionados (func)")

def list_leads():
    leads = control.read_leads()

    print(f"## | {"Nome":<12} | E-mail")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<12} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    # validar a query

    # com a query digitada (busca)... preciso enviar para o control
    # o control irá comparar a query com os dados do leads.json
    # e irá retornar os resultados da busca
    found_leads = control.read_leads_search(query)
    print(f"## | {"Nome":<12} | E-mail")
    for i, lead in found_leads:
        print(f"{i:02d} | {lead["name"]:<12} | {lead["email"]}")

def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possível exportar para csv")
    else:
        print(f"CSV exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[3] Buscar (nome/e-mail)")
        print("[4] Exportar CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()