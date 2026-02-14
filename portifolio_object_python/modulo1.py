# v Abaixo há as importações necessárias para otimizar o terminal usando uma função v 
import os 
def limpar_tela():
    os.system('cls')
# v Aqui há uma variável "vazia" na qual será utilizada mais tarde v
opcao = ""
# v Abaixo pode-se ver as classes de casa, apartamento e estúdio v
class casa:
    def __init__(self,quartos,garagem):
        self.quartos = quartos
        self.garagem = garagem
        self.valor_base = 900
    def calcular_valor(self):
        valor = self.valor_base
        if self.quartos == 2:
            valor += 200
        if self.garagem:
            valor += 300
        return valor

class apartamento:
    def __init__(self,quartos,garagem,sem_criancas):
        self.quartos = quartos
        self.garagem = garagem
        self.sem_criancas = sem_criancas
        self.valor_base = 700
    def calcular_valor(self):
        valor = self.valor_base
        if self.quartos == 2:
            valor += 200
        if self.garagem:
            valor += 300
        if self.sem_criancas:
            valor *= 0.95
        return valor
class estudio:
    def __init__(self, vagas):
        self.vagas = vagas
        self.valor_base = 1200
    def calcular_valor(self):
        valor = self.valor_base
        if self.vagas == 2:
            valor += 250
        elif self.vagas > 2:
            valor += 250 + (self.vagas - 2) * 60
        return valor
# v Aqui há uma função que servirá para os usuários escolherem qual tipo de conrato fazer v
def escolher_opcao(opcao):
    
    
    if (opcao == "1"):

        quartos = int(input("quantos quartos: "))
        garagem = input("Garagem: ").lower() == "s"
        valor_contrato = 2000
        parcelas = int(input("Quantas parcelas: "))
        while parcelas < 1 or parcelas > 5:
            print("Núemro inválido! Tente novamente.")
            parcelas = int(input("Digite novamente: "))
        parcela_contrato = valor_contrato / parcelas
        cas = casa(quartos = quartos, garagem = garagem, )
        valor_final = cas.calcular_valor()
        valor_com_contrato = valor_final + parcela_contrato
        print(f"Valor final:: {valor_com_contrato:.0f}")




    elif (opcao == "2"):

        quartos = int(input("quantos quartos: "))
        garagem = input("Garagem: ").lower() == "s"
        sem_criancas = input("Crianças: ").lower() == "n"
        valor_contrato = 2000
        parcelas = int(input("Quantas parcelas: "))
        while parcelas < 1 or parcelas > 5:
            print("Núemro inválido! Tente novamente.")
            parcelas = int(input("Digite novamente: "))
        parcela_contrato = valor_contrato / parcelas
        apart = apartamento(quartos = quartos, garagem = garagem,sem_criancas = sem_criancas )
        valor_final = apart.calcular_valor()
        valor_com_contrato = valor_final + parcela_contrato
        print(f"Valor final:: {valor_com_contrato:.0f}")

    elif (opcao == "3"):
        valor_contrato = 2000
        vagas = int(input("Quantidade de vagas: "))
        parcelas = int(input("Quantas parcelas: "))
        while parcelas < 1 or parcelas > 5:
            print("Núemro inválido! Tente novamente.")
            parcelas = int(input("Digite novamente: "))
        parcela_contrato = valor_contrato / parcelas
        estud = estudio(vagas = vagas)
        valor_final = estud.calcular_valor()
        valor_com_contrato = valor_final + parcela_contrato
        print(f"Valor final:: {valor_com_contrato:.0f}")


    elif (opcao == "0"):

        print("Sistema desligado")
    else:

        print("Opção inválida")
            

# v Abaixo há uma função para pausar o sistema v
def pausar_sistema():
    input("Digite ENTER para continuar ")
# Logo abaixo existe a função de mostrat o Menu v
def mostrar_menu():
    limpar_tela()
    print("==============OPÇÕES=============")
    print("Escolha entre as opções de imóveis:")
    print("1: Casa")
    print("2: Apartamento")
    print("3: Estúdio")
    print(" 4: Parar sistema")
  

# v Aqui é um loop para mostrar o menu, receber a escolha do usuário e depois pausar o sistema v
while (opcao != "0"):

    mostrar_menu()
   
    opcao = input("Escolha uma opcao: ")
    
    escolher_opcao(opcao)

    pausar_sistema()
    

