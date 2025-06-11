
#1
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo")
meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
estacoes_do_ano =  ("Verão", "Outono"," Inverno", "Primavera")
data = (dias_da_semana, meses_do_ano, estacoes_do_ano)
print("Data Tipo Tupla:")
def main(tupla):
    print("Dias da Semana: ", tupla[0])
    print("Meses do Ano: ", tupla[1])
    print("Estações do Ano: ", tupla[2])
main(data)
print("="*50)

#2
dias_da_semana2 = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo"]
meses_do_ano2 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
estacoes_do_ano2 = ["Verão", "Outono"," Inverno", "Primavera"]
data2 = [dias_da_semana2, meses_do_ano2, estacoes_do_ano2]
print("Data Tipo Lista:")   
def main2(lista2):
    print("Dias da Semana: ", lista2[0])
    print("Meses do Ano: ", lista2[1])
    print("Estações do Ano: ", lista2[2])
main2(data2)
print("="*50)

#3
dias_da_semana3 = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo"]
meses_do_ano3 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
estacoes_do_ano3 = ["Verão", "Outono","Inverno", "Primavera"]
data3 = [dias_da_semana3, meses_do_ano3, estacoes_do_ano3]
def imprimir(lista3):
    print(f"Quantos elementos: Há {len(lista3)} elementos nessa lista.")
    print(f"Dados: 1º - {lista3[0]}, 3º - {lista3[2]}, {len(lista3)}º - {lista3[-1]}")
imprimir(dias_da_semana3)
imprimir(meses_do_ano3)
imprimir(estacoes_do_ano3)
print("="*50)

#4 - 5
def questao4():
    lista4 = [ "Arroz", "Feijão", "Macarrão", "Frango", "Pão", "Leite", "Ovos", "Queijo", "Manteiga", "Açúcar", "Café", "Sal", "Óleo", "Alface", "Tomate"]

    def exibir_lista(lista):
        print("Aqui está sua lista atual: ")
        for i, lista in enumerate(lista, start= 1):
            print("- ", lista)
    def incluir_item():
        while True:
            novo_item = input("Digite o item que deseja incluir (ou digite 'PRONTO' para finalizar): ").strip().title()
            if novo_item.lower() == "pronto":
                break
            lista4.append(novo_item)
        exibir_lista(lista4)

    def remover_item():
        exibir_lista(lista4)
        item_para_remover = input("Digite o nome do item que deseja remover: ").strip().title()
        if item_para_remover in lista4:
            lista4.remove(item_para_remover)
            print(f"O item '{item_para_remover}' foi removido com sucesso!")
        else:
            print("Este item não está na lista.")
        exibir_lista(lista4)

    def atualizar_item():
        exibir_lista(lista4)
        item_para_atualizar = input("Digite o nome do item que deseja atualizar: ").strip().title()
        if item_para_atualizar in lista4:
            novo_valor = input(f"Digite o novo valor para o item '{item_para_atualizar}': ").strip().title()
            indice = lista4.index(item_para_atualizar)
            lista4[indice] = novo_valor
            print(f"O item '{item_para_atualizar}' foi atualizado para '{novo_valor}'.")
        else:
            print("Este item não está na lista.")
        exibir_lista(lista4)

    def menu():
        while True:
            print("\nEscolha uma das opções:")
            print("1 - Incluir um novo item")
            print("2 - Remover um item")
            print("3 - Atualizar um item existente")
            print("4 - Exibir lista")
            print("5 - Encerrar o programa")
            opcao = input("Digite o número da opção desejada: ").strip()
            if opcao == "1":
                incluir_item()
            elif opcao == "2":
                remover_item()
            elif opcao == "3":
                atualizar_item()
            elif opcao == "4":
                exibir_lista(lista4)
            elif opcao == "5":
                print("Programa encerrado. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    menu()
questao4()
print("=" * 50)

#6
linguagens_ocultas = ["C", "C++", "JavaScript", "Java", "Lua", "Python"]
def adivinhar_linguagem_oculta():
    print('Adivinhe as linguagens que constam na lista oculta! (Quando quiser encerrar digite "SAIR").')
    while True:
        tentativa = input("Sua tentativa: ").strip().title()
        if tentativa in linguagens_ocultas:
            print(f"A linguagem {tentativa} consta na lista!")
        elif tentativa.lower() == "sair":
            print("--- Programa encerrado ---")
            break
        else:
            print(f"A linguagem {tentativa} não consta na lista!")
adivinhar_linguagem_oculta()
print("="*50)

#7
lista_de_medicos = ["lucas", "joão", "ana", "júlia", "guilherme"]

def imprimir_lista_medicos():
    for i, medico in enumerate(lista_de_medicos, start=1):
        print(f"{i}. {medico.capitalize()}")

def escolher_medico():
    while True:
        imprimir_lista_medicos()
        escolha = input("Digite o número ou o nome do médico: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(lista_de_medicos):
                print(f"Consulta com o(a) médico(a) {lista_de_medicos[escolha-1].capitalize()} marcada!")
                break
            else:
                print("Número inválido! Tente novamente.")
        elif escolha.lower() in [medico.lower() for medico in lista_de_medicos]:
            print(f"Consulta com o(a) médico(a) {escolha.capitalize()} marcada!")
            break
        else:
            print("Digite um número ou nome válido!")
escolher_medico()