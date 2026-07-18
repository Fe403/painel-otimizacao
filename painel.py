import os
import shutil
import platform
import sys
import ctypes
import datetime

def registrar_log(acao):
    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("log.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{agora} - {acao}\n")

def eh_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def rodar_como_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )

if not eh_admin():
    rodar_como_admin()
    sys.exit()

def modo_gamer():
    print("Ativando Modo Gamer completo...")

    print("1/3 - Ativando Game Mode...")
    os.system("start ms-settings:gaming-gamemode")

    print("2/3 - Ativando desempenho máximo...")
    resultado = os.popen("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61").read()
    guid_novo = resultado.split()[5]
    os.system(f"powercfg /setactive {guid_novo}")

    print("3/3 - Otimizando GameBar...")
    os.system('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f')
    os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v AppCaptureEnabled /t REG_DWORD /d 0 /f')

    print("Modo Gamer ativado! Pode jogar tranquilo, chefe!")


def winget_disponivel():
    resultado = os.system("where winget >nul 2>nul")
    return resultado == 0



print("=" * 60)
print(" Olá pessoa que pegou o painel do Fe.403!")
print()
print(" Antes de tudo: crie um ponto de restauração (opção 1).")
print(" Algumas funções podem não funcionar que nem em outros Pcs ou Notebooks —")
print(" se funcionar bem, deixa seu feedback. Um abraço do mano Fe!")
print("=" * 60)
input("\nPressione ENTER para continuar...")


opcao = ""
while opcao != "0":
    print("=== Painel de Otimização — Fe.403 ===")
    print("1  - Criar ponto de restauração")
    print("2  - Ver espaço em disco")
    print("3  - Ver informações do sistema")
    print("4  - Limpar cache DNS")
    print("5  - Verificar arquivos do sistema (sfc)")
    print("6  - Verificar imagem do Windows (DISM)")
    print("7  - Abrir Gerenciador de Tarefas")
    print("8 - Abrir Propriedades do Sistema")
    print("9 - Abrir Gerenciador de Serviços")
    print("10 - Ativar Game Mode")
    print("11 - Ativar modo de desempenho máximo")
    print("12 - Verificar atualizações de programas (winget)")
    print("13 - Desativar modo turbo (voltar ao normal)")
    print("14 - Testar conexão com a internet")
    print("15 - Resetar configuração de rede")
    print("16 - Verificar seu IP")
    print("17 - Esvaziar a Lixeira")
    print("18 - Limpar cache de navegadores")
    print("19 - Programas que abrem com o Windows")
    print("20 - Relatório de bateria")
    print("21 - Limpar arquivos temporários")
    print("22 - MODO GAMER (ativa tudo de uma vez)")
    print("23 - Desativar apps em segundo plano")
    print("24 - Desativar serviços inúteis")
    print("25 - Otimizar GameBar")
    print("26 - Desativar telemetria")
    print("27 - Aumentar prioridade de um jogo")
    print("28 - Reiniciar o Explorer")
    print("29 - Desativar Cortana")
    print("0  - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Criando ponto de restauração... (pode demorar um pouco)")
        os.system('powershell.exe -Command "Checkpoint-Computer -Description \'Painel de Otimizacao\' -RestorePointType MODIFY_SETTINGS"')
        print("Ponto de restauração criado, chefe! Se algo der errado, dá pra voltar aqui.")

    elif opcao == "2":
        uso = shutil.disk_usage("C:\\")
        total_gb = uso.total / (1024**3)
        livre_gb = uso.free / (1024**3)
        usado_gb = uso.used / (1024**3)
        print(f"Disco C: — Total: {total_gb:.1f} GB | Usado: {usado_gb:.1f} GB | Livre: {livre_gb:.1f} GB")
        print("Ta na mão!")

    elif opcao == "3":
        print(f"Sistema: {platform.system()} {platform.release()}")
        print(f"Versão: {platform.version()}")
        print(f"Processador: {platform.processor()}")
        print(f"Nome da máquina: {platform.node()}")
        print("Ta na mão!")

    elif opcao == "4":
        print(" Estou limpando cache DNS...")
        os.system("ipconfig /flushdns")
        print("Feito chefe!")

    elif opcao == "5":
        print(" Estou verificando arquivos do sistema... (Isso pode demorar!)")
        os.system("sfc /scannow")
        print("Feito chefe!")

    elif opcao == "6":
        print("Estou reparando a imagem pra você sente e veja a mágica...(Isso pode demorar!)")
        os.system("DISM /Online /Cleanup-Image /RestoreHealth")
        print("Feito chefe!")

    elif opcao == "7":
        print("Estou abrindo o Gerenciador de tarefas...aguarde!")
        os.system("taskmgr")
        print("Feito chefe!")

    elif opcao == "8":
        print("Estou abrindo a propriedade do seu sistema...aguarde!")
        os.system("sysdm.cpl")
        print("Feito chefe!")

    elif opcao == "9":
        print("Estou abrindo o gerenciador de serviços...aguarde!")
        os.system("services.msc")
        print("Feito chefe!")

    elif opcao == "10":
        print("Estou ativando o Game mode...")
        os.system("start ms-settings:gaming-gamemode")
        print("Feito chefe!")

    elif opcao == "11":
        print("Ativando modo de desempenho máximo")
        resultado = os.popen("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61").read()
        guid_novo = resultado.split()[5]
        os.system(f"powercfg /setactive {guid_novo}")
        print("Modo turbo ativado, chefe")

    elif opcao == "12":
        if winget_disponivel():
            print("Verificando atualizações de programas instalados por favor espere um pouco...")
            os.system("winget upgrade")
            print("Feito chefe!")
        else:
            print("O winget não está disponível nesse PC.")
            print("Pra resolver: abre a Microsoft Store, procura por 'App Installer' e atualiza/instala.")
            print("Depois disso essa opção passa a funcionar normalmente.")

    elif opcao == "13":
        print("Desativando modo turbo, voltando ao normal...")
        os.system("powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e")
        print("Plano de energia normalizado, chefe!")

    elif opcao == "14":
        print("Testando sua rede com a internet agora.....aguarde")
        os.system("ping 8.8.8.8 -n 4")
        print("Ok feito!")

    elif opcao == "15":
        print("Resetando configurações de rede... Talvez precise reiniciar sua máquina")
        os.system("netsh winsock reset")
        print("Opa ta na mão! ")

    elif opcao == "16":
        print("Verificando agora seu Ip.... aguarde")
        os.system("ipconfig")
        print("achei hehehe !")

    elif opcao == "17":
        print("Jogando lixo fora...")
        os.system('powershell.exe -Command "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"')
        print("Ta feito chefe!")

    elif opcao == "18":
        print("Limpando cache do que você pesquisa no seu navegador")
        os.system('del /q /f /s "%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Cache\\*.*"')
        os.system('del /q /f /s "%LocalAppData%\\Microsoft\\Edge\\User Data\\Default\\Cache\\*.*"')
        os.system('del /q /f /s "%LocalAppData%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cache2\\*.*"')
        os.system('del /q /f /s "%AppData%\\Opera Software\\Opera Stable\\Cache\\*.*"')
        os.system('del /q /f /s "%LocalAppData%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache\\*.*"')
        print("Cache limpo, chefe!")

    elif opcao == "19":
        print("Listando programas que abrem com o Windows...")
        os.system("wmic startup get caption,command")

    elif opcao == "20":
        print("Gerando relatório de bateria...")
        os.system("powercfg /batteryreport")
        print("Relatório salvo! Procure o arquivo battery-report.html na pasta onde você rodou o programa.")

    elif opcao == "21":
        print(" Estou limpando seu lixo...")
        os.system("del /q /f /s %TEMP%\\*.*")
        print("Ta feito meu chefe!")

    elif opcao == "22":
        modo_gamer()

    elif opcao == "23":
        print("Desativando apps em segundo plano...")
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 1 /f')
        print("Feito chefe!")

    elif opcao == "24":
        print("Desativando serviços inúteis...")
        os.system("sc stop WerSvc")
        os.system("sc config WerSvc start= disabled")
        os.system("sc stop DiagTrack")
        os.system("sc config DiagTrack start= disabled")
        print("Feito chefe!")

    elif opcao == "25":
        print("Otimizando GameBar...")
        os.system('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f')
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v AppCaptureEnabled /t REG_DWORD /d 0 /f')
        print("Feito chefe!")

    elif opcao == "26":
        print("Desativando telemetria...")
        os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f')
        print("Feito chefe!")

    elif opcao == "27":
        nome_jogo = input("Digite o nome do executável do jogo (ex: valorant.exe): ")
        print(f"Aumentando prioridade de {nome_jogo}...")
        os.system(f'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{nome_jogo}\\PerfOptions" /v CpuPriorityClass /t REG_DWORD /d 3 /f')
        print("Feito chefe!")

    elif opcao == "28":
        print("Reiniciando o Explorer...")
        os.system("taskkill /f /im explorer.exe")
        os.system("start explorer.exe")
        print("Feito chefe!")

    elif opcao == "29":
        print("Desativando Cortana...")
        os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search" /v "AllowCortana" /t REG_DWORD /d 0 /f')
        print("Feito chefe!")

    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opa parece que você errou o comando tente de novo bobão.")

print("Programa encerrado. Tchau tchau...")