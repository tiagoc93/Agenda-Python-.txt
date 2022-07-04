"""
Pequeno projeto de agenda em python, utilizando leitura de arquivos txt.
"""

# Menu
def iniciar():
    #Cria o arquivo txt se ele não existir.
    open('catalogo.txt','a+')
    
    # Gera um loop com um menu e as opções de chamada de função.
    while True:
        menu = int(input("""
            ============================================================
            |               Bem-vindo(a) a Agenda Python               |
            |            Escolha a ação que deseja realizar            |
            |                1- Consultar Contado                      |
            |                2- Cadastrar Contato                      |
            |                3- Deletar Contato                        |
            |                4- Sair                                   |
            ============================================================                                                                
        """))
        if menu == 1:
            mostrarAgenda()
        elif menu == 2:
            cadastrarContato()
        elif menu == 3:
            apagarContato()
        elif menu == 4:
            print('Saindo do Programa...')
            break
        

# Mostra todos os contatos cadastrados
def mostrarAgenda():
    while True:
        filtrar = int(input('1- Filtrar por nome\n2- Lista Completa\n3- Voltar para o menu principal\n'))
        if filtrar == 1:
            filtro = input('Digite o nome do contato a ser filtrado: ')
            with open('catalogo.txt') as arq:
                for line in arq:
                    if filtro in line:
                        print('========================================================')
                        print(line, end='')
                        print('========================================================\n')
        elif filtrar == 2:
            borda = print('===============Lista de Contatos Completa===============')
            with open('catalogo.txt') as arq:
                for item in arq.readlines():
                    print(item, end='')
                    print('='*56)
        
        elif filtrar == 3:
            break
        
        
        else:
            print('Digite opção válida.\n')
            continue
            
# Cadastro de Contato
def cadastrarContato():
    
    while True:
        nome = input('Digite o nome do contado: ')
        telefone = input('Digite o telefone do contato: ') 
        with open('catalogo.txt', 'a') as arq: # Abre o arquivo no modo append.
            arq.write(f'Nome: {nome}, Telefone: {telefone}\n')
            print('Contato cadastrado com sucesso!\n')
            retornar = input('Deseja cadastrar mais um contato (s/n)? ')
            if retornar == 'n':
                break
            else:
                continue
            

def apagarContato():
    contato = input('Qual contato deseja apagar?')
    with open('catalogo.txt', 'r') as arq: # Abre no modo leitura
        lines = arq.readlines()
        with open('catalogo.txt', 'w') as arqw: # subscreve o arquivo com as alterações
            for line in lines:
                if line.find(contato) == -1: # find sempre devolve -1 quando localiza o que foi especificado.
                    arqw.write(line)
    print('Contato Deletado.')


    
            

if __name__ == '__main__':
    iniciar()    


