import os
import shutil
import platform
opcao = ""
while opcao != "0":
    print("=== Painel de Otimização ===")
    print("1 - Limpar arquivos Temporários")
    print("2 - Ver espaço em disco")
    print("3 - Ver informações do sistema")
    print("4 - Limpar cache DNS")
    print("5 - Verificar arquivos do sistema (sfc)")
    print("6 - Verificar imagem do WIN (DISM) ")
    print("7 - Limpando Disco Local  ")
    print("8 - Reorganiza os dados fisicamente no disco")
    print("9 - Abrir Gerenciador de tarefas")
    print("10 - Abrir Propriedades do sistema ")
    print("11 - Abir o Gerenciador de serviços...aguarde!")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(" Estou limpando seu lixo...")
        os.system("del /q /f /s %TEMP%\\*.*")
        print("Ta feito meu chefe!")

    elif opcao == "2":
        uso = shutil.disk_usage("C:\\")
        total_gb = uso.total / (1024**3)
        livre_gb = uso.free / (1024**3)
        usado_gb = uso.used / (1024**3)
        print(f"Disco C: — Total: {total_gb:.1f} GB | Usado: {usado_gb:.1f} GB | Livre: {livre_gb:.1f} GB")
        print ("Ta na mão!")

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
        print ("Estou reparando a imagem pra você sente e veja a mágica...(Isso pode demorar!)")
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
        
    elif opcao == "0":
        print("Saindo...")

    else:
        print("Opa parece que você errou o comando tente de novo bobão.")

print("Programa encerrado. Tchau tchau...")