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

    print("3/3 - Fechando programas pesados em segundo plano...")
    os.system("taskkill /f /im Discord.exe")

    print("Modo Gamer ativado! Pode jogar tranquilo, chefe!")



print("=" * 60)
print(" Olá pessoa que pegou o painel do Fe.403!")
print()
print(" Antes de tudo: crie um ponto de restauração (opção 1).")
print(" Algumas funções podem não funcionar pois nem todos os pc e notebooks são iguais")
print(" se funcionar bem, deixa seu feedback. Um abraço do mano Fe!")
print("=" * 60)
input("\nPressione ENTER para continuar...")


opcao = ""
while opcao != "0":
    print("=== Painel de Otimização ===")
    print("1 - Criando ponto de restauração")
    print("2 - Ver espaço em disco")
    print("3 - Ver informações do sistema")
    print("4 - Limpar cache DNS")
    print("5 - Verificar arquivos do sistema (sfc)")
    print("6 - Verificar imagem do WIN (DISM) ")
    print("7 - Limpando Disco Local  ")
    print("8 - Reorganiza os dados fisicamente no disco")
    print("9 - Abrir Gerenciador de tarefas")
    print("10 - Abrir Propriedades do sistema ")
    print("11 - Abir o Gerenciador de serviços")
    print("12 - Ativar Game mode")
    print("13 - Ativar modo de desempenho máximo")
    print("14 - Verificar atualizações de programas instalados")
    print("15 - Desativar modo turbo (voltar ao normal)")
    print("16 - Testar conexão com sua rede")
    print("17 - Resetar configuração de rede")
    print("18 - Verificar seu Ip")
    print("19 - Jogar lixo fora")
    print("20 - Limpar cache de navegador")
    print("21 - Programas que abrem com windows")
    print("22 - Relatório de bateria")
    print("23 - Limpar arquivos Temporarios")
    print("24 - Modo gamer (Ativa tudo de uma vez)")
    print("25 - Desativar efeitos visuais")
    print("26 - Desativar apps em segundo plano")
    print("27 - Desativar serviços inúteis")
    print("28 - Otimizar GameBar")
    print("29 - Desativar hibernação")
    print("30 - Desativar telemetria")
    print("31 - Aumentar prioridade de um jogo")
    print("32 - Reiniciar o Explorer")
    print("33 - Prioridade CPU/GPU geral pra jogos")
    print("34 - Desativar indexação de pesquisa")
    print("35 - Desativar Cortana")
    print("36 - Desativar Prefetch/Superfetch")
    print("0 - Sair")

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
        print("Estou Limpando seu disco heheheehehe lá ele....aguarde!")
        os.system("Cleanmgr")
        print("Feito chefe!")

    elif opcao == "8":
        print("Estou Reorganizando os dados do seu disco... aguarde!")
        os.system("defrag C: /O")
        print("Feito chefe!")

    elif opcao == "9":
        print("Estou abrindo o Gerenciador de tarefas...aguarde!")
        os.system("taskmgr")
        print("Feito chefe!")

    elif opcao == "10":
        print("Estou abrindo a propriedade do seu sistema...aguarde!")
        os.system("sysdm.cpl")
        print("Feito chefe!")

    elif opcao == "11":
        print("Estou abrindo o gerenciador de serviços...aguarde!")
        os.system("services.msc")
        print("Feito chefe!")

    elif opcao == "12":
        print("Estou ativando o Game mode...")
        os.system("start ms-settings:gaming-gamemode")
        print("Feito chefe!")

    elif opcao == "13":
        print("Ativando modo de desempenho máximo")
        resultado = os.popen("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61").read()
        guid_novo = resultado.split()[5]
        os.system(f"powercfg /setactive {guid_novo}")
        print("Modo turbo ativado, chefe")

    elif opcao == "14":
        print("Verificando atualizações de programas instalados por favor espere um pouco...")
        os.system("winget upgrade")
        print("Feito chefe!")

    elif opcao == "15":
        print("Desativando modo turbo, voltando ao normal...")
        os.system("powercfg /setactive 381b4222-f694-41f0-9685-ff5bb260df2e")
        print("Plano de energia normalizado, chefe!")

    elif opcao == "16":
        print("Testando sua rede com a internet agora.....aguarde")
        os.system("ping 8.8.8.8 -n 4")
        print("Ok feito!")

    elif opcao == "17":
        print("Resetando configurações de rede... Talvez precise reiniciar sua máquina")
        os.system("netsh winsock reset")
        print("Opa ta na mão! ")

    elif opcao == "18":
        print("Verificando agora seu Ip.... aguarde")
        os.system("ipconfig")
        print("achei hehehe !")

    elif opcao == "19":
        print("Jogando lixo fora...")
        os.system('powershell.exe -Command "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"')
        print("Ta feito chefe!")

    elif opcao == "20":
        print("Limpando cache do que você pesquisa no seu navegador")
        os.system('del /q /f /s "%LocalAppData%\\Google\\Chrome\\User Data\\Default\\Cache\\*.*"')
        os.system('del /q /f /s "%LocalAppData%\\Microsoft\\Edge\\User Data\\Default\\Cache\\*.*"')
        os.system('del /q /f /s "%LocalAppData%\\Mozilla\\Firefox\\Profiles\\*.default-release\\cache2\\*.*"')
        os.system('del /q /f /s "%AppData%\\Opera Software\\Opera Stable\\Cache\\*.*"')
        os.system('del /q /f /s "%LocalAppData%\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache\\*.*"')
        print("Cache limpo, chefe!")

    elif opcao == "21":
        print("Listando programas que abrem com o Windows...")
        os.system("wmic startup get caption,command")

    elif opcao == "22":
        print("Gerando relatório de bateria...")
        os.system("powercfg /batteryreport")
        print("Relatório salvo! Procure o arquivo battery-report.html na pasta onde você rodou o programa.")

    elif opcao == "23":
        print(" Estou limpando seu lixo...")
        os.system("del /q /f /s %TEMP%\\*.*")
        print("Ta feito meu chefe!")

    elif opcao == "24":
        modo_gamer()

    elif opcao == "25":
        print("Desativando efeitos visuais...")
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects" /v VisualFXSetting /t REG_DWORD /d 2 /f')
        print("Feito chefe!")

    elif opcao == "26":
        print("Desativando apps em segundo plano...")
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 1 /f')
        print("Feito chefe!")

    elif opcao == "27":
        print("Desativando serviços inúteis...")
        os.system("sc stop WerSvc")
        os.system("sc config WerSvc start= disabled")
        os.system("sc stop DiagTrack")
        os.system("sc config DiagTrack start= disabled")
        print("Feito chefe!")

    elif opcao == "28":
        print("Otimizando GameBar...")
        os.system('reg add "HKCU\\System\\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f')
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" /v AppCaptureEnabled /t REG_DWORD /d 0 /f')
        print("Feito chefe!")

    elif opcao == "29":
        print("Desativando hibernação (libera espaço em disco)...")
        os.system("powercfg /hibernate off")
        print("Feito chefe!")

    elif opcao == "30":
        print("Desativando telemetria...")
        os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f')
        print("Feito chefe!")

    elif opcao == "31":
        nome_jogo = input("Digite o nome do executável do jogo (ex: valorant.exe): ")
        print(f"Aumentando prioridade de {nome_jogo}...")
        os.system(f'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{nome_jogo}\\PerfOptions" /v CpuPriorityClass /t REG_DWORD /d 3 /f')
        print("Feito chefe!")

    elif opcao == "32":
        print("Reiniciando o Explorer...")
        os.system("taskkill /f /im explorer.exe")
        os.system("start explorer.exe")
        print("Feito chefe!")

    elif opcao == "33":
        print("Aumentando prioridade geral da CPU/GPU para jogos...")
        os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f')
        os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "GPU Priority" /t REG_DWORD /d 8 /f')
        os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games" /v "Priority" /t REG_DWORD /d 6 /f')
        print("Feito chefe!")

    elif opcao == "34":
        print("Desativando indexação de pesquisa...")
        os.system('net stop "Windows Search"')
        os.system('sc config "WSearch" start= disabled')
        print("Feito chefe!")

    elif opcao == "35":
        print("Desativando Cortana...")
        os.system('reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search" /v "AllowCortana" /t REG_DWORD /d 0 /f')
        print("Feito chefe!")

    elif opcao == "36":
        print("Desativando Prefetch e Superfetch (indicado pra HDD)...")
        os.system('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" /v EnablePrefetcher /t REG_DWORD /d 0 /f')
        os.system('sc config "SysMain" start=disabled')
        print("Feito chefe!")

    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opa parece que você errou o comando tente de novo bobão.")

print("Programa encerrado. Tchau tchau...")