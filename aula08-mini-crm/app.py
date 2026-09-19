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
    print(leads)

def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()