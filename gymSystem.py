import os
import shutil
import requests
from bs4 import BeautifulSoup
import platform
import subprocess
import ctypes
import datetime

def listar_arquivos_e_pastas():
    diretorio = os.path.dirname(os.path.abspath(__file__))
    arquivos = []
    pastas = []

    for item in os.listdir(diretorio):
        if os.path.isfile(os.path.join(diretorio, item)):
            arquivos.append(item)
        else:
            pastas.append(item)

    print("Arquivos:")
    for arquivo in arquivos:
        print(arquivo)

    print("\nPastas:")
    for pasta in pastas:
        print(pasta)

def criar_arquivo():
    localizacao = input("Onde o arquivo irá ser despejado? ")
    nome_arquivo = input("Qual será o nome do arquivo? ")
    conteudo = input("Por favor, escreva o conteudo que deseja nele, poderia? ")

    caminho_arquivo = os.path.join(localizacao, nome_arquivo)

    try:
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write(conteudo)
        print("Arquivo criado.")
    except PermissionError:
        print("Não é possível criar o arquivo. Você não possui permissões.")
    except OSError:
        print("Ocorreu um erro ao criar o arquivo.")

def apagar_arquivo():
    localizacao = input("Onde o arquivo irá ser removido? ")
    nome_arquivo = input("Qual será o nome do arquivo? ")
    caminho_arquivo = os.path.join(localizacao, nome_arquivo)

    if os.path.exists(caminho_arquivo):
        try:
            os.remove(caminho_arquivo)
            print("Arquivo apagado.")
        except PermissionError:
            print("Não é possível apagar o arquivo. Você não possui permissões.")
        except OSError:
            print("Ocorreu um erro ao apagar o arquivo.")
    else:
        print("Arquivo não se encontra onde requisitou.")

def editar_arquivo():
    localizacao = input("Onde o arquivo irá ser editado? ")
    nome_arquivo = input("Qual será o nome do arquivo? ")
    caminho_arquivo = os.path.join(localizacao, nome_arquivo)

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r+") as arquivo:
                conteudo = arquivo.read()
                print("Conteúdo atual:")
                print(conteudo)

                arquivo.seek(0)
                novo_conteudo = input("Qual será o novo conteúdo: ")
                arquivo.write(novo_conteudo)
                arquivo.truncate()

            print("Arquivo editado.")
        except PermissionError:
            print("Não é possível editar o arquivo. Você não possui permissões.")
        except OSError:
            print("Ocorreu um erro ao editar o arquivo.")
    else:
        print("Arquivo não se encontra onde requisitou.")

def mover_arquivo():
    localizacao_atual = input("Onde o arquivo se encontra? ")
    nome_arquivo = input("Qual a identificação dele? ")
    destino = input("Para onde o arquivo irá? ")

    caminho_arquivo_atual = os.path.join(localizacao_atual, nome_arquivo)
    caminho_destino = os.path.join(destino, nome_arquivo)

    if os.path.exists(caminho_arquivo_atual):
        try:
            shutil.move(caminho_arquivo_atual, caminho_destino)
            print("Arquivo movido.")
        except PermissionError:
            print("Não é possível mover o arquivo. Você não possui permissões.")
        except OSError:
            print("Ocorreu um erro ao mover o arquivo.")
    else:
        print("Arquivo não se encontra onde requisitou. ")

def pesquisar_na_rede():
    termo_pesquisa = input("O que deseja pesquisar? ")

    url = f"https://www.google.com/search?q={termo_pesquisa}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    resultado = soup.find('div', {'class': 'BNeawe s3v9rd AP7Wnd'})
    if resultado:
        print(resultado.get_text())
    else:
        print("Sem resultado. ")

def reiniciar_sistema():
    resposta = input("Deseja reiniciar o dispositivo? (s/n): ")

    if resposta.lower() == 's':
        sistema_operacional = platform.system()

        if sistema_operacional == 'Windows':
            os.system('shutdown /r /t 0')
        elif sistema_operacional == 'Linux':
            os.system('sudo shutdown -r now')
        elif sistema_operacional == 'Darwin':  # macOS
            os.system('sudo shutdown -r now')
        else:
            print("Não foi possível reiniciar o dispositivo.")
    else:
        print("Reinicialização cancelada.")

def bloquear_sistema():
    resposta = input("Deseja bloquear o dispositivo? (s/n): ")
    if resposta.lower() == 's':
        sistema_operacional = platform.system()

        if sistema_operacional == 'Windows':
            ctypes.windll.user32.LockWorkStation()
            print("Sistema bloqueado.")
        elif sistema_operacional == 'Linux':
            if shutil.which("xdg-screensaver"):
                subprocess.call(["xdg-screensaver", "lock"])
                print("Sistema bloqueado.")
            else:
                print("O comando 'xdg-screensaver' não está disponível no sistema.")
        elif sistema_operacional == 'Darwin': 
            subprocess.call(["/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession", "-suspend"])
            print("Sistema bloqueado.")
        else:
            print("Não é possível bloquear o dispositivo.")
    else:
        print("Bloqueio cancelado.")

def desligar_sistema():
    resposta = input("Deseja desligar a máquina? (s/n): ")

    if resposta.lower() == 's':
        sistema_operacional = platform.system()

        if sistema_operacional == 'Windows':
            os.system('shutdown /s /t 0')
        elif sistema_operacional == 'Linux':
            os.system('sudo shutdown now')
        elif sistema_operacional == 'Darwin': 
            os.system('sudo shutdown -h now')
        else:
            print("Não é possível desligar o dispositivo.")
    else:
        print("Desligamento cancelado.")

def admin_arquivos():
    while True:
        print("Administração de Arquivos")
        print("1 - Criar arquivo")
        print("2 - Editar arquivo")
        print("3 - Apagar arquivo")
        print("4 - Mover arquivo")
        print("5 - Listar os arquivos e pastar")
        print("0 - Voltar")

        opcao = input("O que deseja? ")

        if opcao == "1":
            criar_arquivo()
        elif opcao == "2":
            editar_arquivo()
        elif opcao == "3":
            apagar_arquivo()
        elif opcao == "4":
            mover_arquivo()
        elif opcao == "5":
            listar_arquivos_e_pastas()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def admin_sistema():
    while True:
        print("Administração do sistema")
        print("1 - Reiniciar sistema")
        print("2 - Bloquear sistema")
        print("3 - Desligar sistema")
        print("0 - Voltar")

        opcao = input("O que deseja efetuar? ")

        if opcao == "1":
            reiniciar_sistema()
        elif opcao == "2":
            bloquear_sistema()
        elif opcao == "3":
            desligar_sistema()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")
def registrar_ganhos():
    ganhos = float(input("Quanto ganhou? "))
    with open("Gastos.txt", "a") as arquivo:
        arquivo.write(f"Ganhos: {ganhos}\n")

def registrar_gastos():
    gastos = float(input("Quanto gastou? "))
    with open("Gastos.txt", "a") as arquivo:
        arquivo.write(f"Gastos: {gastos}\n")

def exibir_gastos():
    with open("Gastos.txt", "r") as arquivo:
        registros = arquivo.readlines()

    total_ganhos = sum(float(registro.strip().split(":")[1]) for registro in registros if "Ganhos" in registro)
    total_gastos = sum(float(registro.strip().split(":")[1]) for registro in registros if "Gastos" in registro)
    saldo_restante = total_ganhos - total_gastos

    print(f"Ganhos: R$ {total_ganhos:.2f}")
    print(f"Gastos: R$ {total_gastos:.2f}")
    print(f"Saldo: R$ {saldo_restante:.2f}")

    if saldo_restante < 0:
        print("Você está quebrado. Controle suas finanças")
    
def apagar_registros():
    with open("Gastos.txt", "r") as arquivo:
        registros = arquivo.readlines()
    
    if len(registros) == 0:
        print("Não há registros anteriores.")
        return

    print("Registros:")
    for i, registro in enumerate(registros):
        print(f"{i + 1}. {registro.strip()}")

    opcoes_validas = list(range(1, len(registros) + 1))
    opcoes_validas.append(0)

    while True:
        opcao = input("Digite a identificação do registro que deseja apagar (ou 0 para apagar todos os registros): ")
        if not opcao.isdigit() or int(opcao) not in opcoes_validas:
            print("Opção inválida, digite novamente.")
        else:
            opcao = int(opcao)
            break

    if opcao == 0:
        resposta = input("Tem certeza que deseja limpar os registros? (s/n): ")
        if resposta.lower() == 's':
            with open("Gastos.txt", "w") as arquivo:
                arquivo.write("")
            print("Registros limpos.")
        else:
            print("Limpeza cancelada.")
    else:
        del registros[opcao - 1]

        with open("Gastos.txt", "w") as arquivo:
            arquivo.writelines(registros)

        print("Registro limpos com exito.")

def gerenciador_financas():
    while True:
        print("Gerenciador Financeiro")
        print("1 - Registrar ganhos")
        print("2 - Registrar gastos")
        print("3 - Exibir registros anteriores")
        print("4 - Apagar registros anteriores")
        print("0 - Voltar")

        opcao = input("Selecione o que deseja: ")

        if opcao == "1":
            registrar_ganhos()
        elif opcao == "2":
            registrar_gastos()
        elif opcao == "3":
            exibir_gastos()
        elif opcao == "4":
            apagar_registros()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def registrar_peso():
    peso = float(input("Qual o seu peso atual? "))
    data = input("Digite a data (DD/MM/AAAA): ")

    with open("Fitness.txt", "a") as arquivo:
        arquivo.write(f"Peso: {peso} kg - Data: {data}\n")

def verificar_historico_peso():
    try:
        with open("Fitness.txt", "r") as arquivo:
            historico_peso = arquivo.read()
            print(historico_peso)
    except FileNotFoundError:
        print("Nenhum registro anterior.")

def exibir_atividades():
    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    
    dia_atual = datetime.datetime.today().weekday()
    
    if dia_atual < len(dias_semana):
        nome_arquivo = f"GYM{dia_atual + 1}.txt"
        try:
            with open(nome_arquivo, "r") as arquivo:
                atividades = arquivo.read()
                print(f"Atividades de {dias_semana[dia_atual]}:")
                print(atividades)
        except FileNotFoundError:
            print(f"Nenhuma atividade registrada para {dias_semana[dia_atual]}.")
    else:
        print("Dia inválido.")

def falar_com_professor():
    while True:
        print("Falar com o professor")
        print("1 - E-mail")
        print("2 - Telefone")
        print("3 - Rede social")
        print("0 - Voltar")

        opcao = input("Selecione como deseja entrar em contato: ")

        if opcao == "1":
            print("E-mail: matheuss.cirq@outlook.com")
        elif opcao == "2":
            print("Telefone: +55 071 98363-4696, consta WhatsApp para contato mais dinâmico.")
        elif opcao == "3":
            print("Rede social e registro como professor: @TeuHere - Instagram, 5687903 - CFEP")
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

def fitness_tracker():
    while True:
        print("Fitness Tracker")
        print("1 - Registrar peso")
        print("2 - Verificar histórico de peso")
        print("3 - Exibir atividades")
        print("4 - Falar com o professor")
        print("0 - Voltar")

        opcao = input("O que deseja? ")

        if opcao == "1":
            registrar_peso()
        elif opcao == "3":
            exibir_atividades()
        elif opcao == "4":
            falar_com_professor()
        elif opcao == "2":
            verificar_historico_peso()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")

while True:
    print("Opções")
    print("1 - Administração")
    print("2 - Pesquisar na rede")
    print("3 - Gerenciador de finanças")
    print("4 - Fitness tracker")
    print("0 - Sair")

    opcao = input("O que deseja? ")

    if opcao == "1":
        while True:
            print("Administração")
            print("1 - Arquivos")
            print("2 - Sistema")
            print("0 - Voltar")

            admin_opcao = input("O que deseja? ")

            if admin_opcao == "1":
                admin_arquivos()
            elif admin_opcao == "2":
                admin_sistema()
            elif admin_opcao == "0":
                break
            else:
                print("Opção inválida, tente novamente.")

    elif opcao == "2":
        pesquisar_na_rede()
    elif opcao == "3":
        gerenciador_financas()
    elif opcao == "4":
        fitness_tracker()
    elif opcao == "0":
        break
    else:
        print("Opção inválida, tente novamente.")
