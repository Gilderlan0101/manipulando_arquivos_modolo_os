import os

def creat_files():
    try:
        ''' criando um caminho de onde o path sera salvo e dando um nome '''
        files_name = str(input('Crie um nome para o arquivo sem extemsão: '))
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'automatizei')

        
        os.makedirs(download_path, exist_ok=True) # Criando o diretorio
        full_path = os.path.join(download_path, files_name + '.txt')   

        '''Criando um arquivo e escrevendo nele '''
        diretorio = full_path

        with open(diretorio, 'a') as files:
            date = str(input('Seu texto: '))
            files.write(date)
            name_file = os.path.basename(full_path) # pegando qual é o arquivo base do diretorio
            tamanho_file = os.path.getsize(download_path)
            print(f'Seu arquivo foi criado com sucesso: {name_file} Tamanho: {tamanho_file}')

        
            
    
    except ValueError as e:
        print(e)

creat_files()