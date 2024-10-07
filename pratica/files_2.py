import os

def save_files():
    try:
        files_name = str(input('Nome do arquivo sem extensão(.txt): '))
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'my_resumo')

        os.makedirs(downloads_path, exist_ok=True) # Criando o caminho para ambos sistemas
        full_path = os.path.join(downloads_path, files_name + '.txt')

        diretorio = full_path

        with open(diretorio, 'a') as files:
            texto = str(input('Texto: '))
            files.write(texto)

            # verifica qual e o arquivo base apos a /
            base = os.path.basename(full_path)
        # verifica o tamanho do arquivo
        size = os.path.getsize(full_path)

            # mensagem de comfimação:
        if files:
            print(f'Arquivo: {base} Salvo com sucesso! Tamanho: {size} bytes ')

        else:
            print('Erro ao tenta escrever em seu aquivo tente novamente ou nos manda uma mensagem :(')
                
    except (FileNotFoundError or FileExistsError or ValueError) as e:
        print(f'Erro ao tenta cria e escreve no codigo M:{e}')
save_files()