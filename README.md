🖥️ Painel de Otimização — by Fe.403

Um painel de otimização para Windows, feito em Python, criado do zero por alguém que nunca tinha programado antes. Roda direto no terminal, com um menu simples, e ajuda a limpar, otimizar e configurar seu PC com poucos cliques.

💡 O que é isso?

É um programa que reúne, num só lugar, várias tarefas de manutenção e otimização do Windows que normalmente você precisaria abrir vários lugares diferentes pra fazer — Painel de Controle, PowerShell, Configurações, etc. Aqui é tudo num menu numerado, direto no terminal.

Feito pra quem quer:


Deixar o PC mais rápido e limpo
Melhorar o desempenho em jogos
Resolver pequenos problemas do Windows sem precisar procurar tutorial toda vez
🚀 Como usar (se você recebeu o .exe)


Baixe o arquivo painel.exe
Dê duplo clique nele
Vai aparecer uma tela pedindo permissão de Administrador → clique em Sim

Isso é necessário porque várias otimizações exigem esse nível de acesso



Se o Windows avisar "O SmartScreen protegeu seu PC" → clique em "Mais informações" → "Executar assim mesmo"

Isso acontece porque o programa não tem certificado digital pago, não significa que tem vírus



Vai aparecer uma mensagem de boas-vindas — aperte ENTER pra seguir
Escolha uma opção digitando o número e apertando ENTER


⚠️ Antes de usar, recomendo:

Use a opção 1 (Criar ponto de restauração) antes de qualquer outra coisa. Assim, se alguma otimização não agradar, dá pra voltar o Windows pro estado de antes.


📋 O que o painel faz

CategoriaO que temSistemaPonto de restauração, verificação de arquivos (sfc/DISM), espaço em disco, info do sistemaLimpezaArquivos temporários, cache de navegadores, LixeiraRedeTestar conexão, resetar rede, ver IP, limpar cache DNSJogosGame Mode, modo de desempenho máximo, prioridade de processo, Modo Gamer (ativa tudo de uma vez)Privacidade/PerformanceDesativar telemetria, apps em segundo plano, serviços desnecessários, CortanaFerramentas rápidasGerenciador de Tarefas, Propriedades do Sistema, Gerenciador de Serviços, relatório de bateria

29 opções no total, todas escolhidas por terem efeito real — nada de função "decorativa" que não faz diferença de verdade.


🛠️ Como rodar o código-fonte (pra quem tem Python)

Se você baixou o painel.py em vez do .exe:

bashpython painel.py

Requisitos: Python 3.x instalado (testado na versão 3.14), sistema Windows.


⚙️ Como gerar o .exe você mesmo

bashpip install pyinstaller
pyinstaller --onefile --console painel.py

O executável vai aparecer na pasta dist/.


⚠️ Avisos importantes


Esse programa modifica configurações do sistema, incluindo o Registro do Windows. Use com responsabilidade.
Testado em Windows 11. Pode ter comportamento diferente em versões mais antigas.
Algumas opções (como winget) dependem de componentes que nem todo Windows tem instalado por padrão — o painel avisa quando isso acontece.
Esse é um projeto pessoal e educacional. Não há garantias formais — use por sua conta e risco, e sempre crie um ponto de restauração antes de mexer em otimizações mais profundas.



❤️ Sobre o projeto

Esse painel nasceu de zero conhecimento em programação. Cada função aqui foi aprendida, testada, quebrada e corrigida até funcionar. Se você chegou até esse README, provavelmente é porque quer aprender também — e a mensagem é simples: dá pra fazer, com paciência e um erro por vez.

Feedbacks são muito bem-vindos. Se funcionou bem no seu PC, ou se algo travou, me conta!


Desenvolvido por Fe.403 — 2026
