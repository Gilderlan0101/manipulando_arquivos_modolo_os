import os 

'''com essas duas linhas de codigo e posivel cria um caminho para salva arquivos em qualque maquina e cria a pasta sem 
erros '''
path = os.path.join('pasta', 'arquivo.txt') #criando um caminho para salva um arquivo em qualque sitema
os.makedirs(path, exist_ok=True)
print(path)

''' Podemos verifica qual e o arquivo base de uma pasta  '''
v = os.path.basename(path) # verificando qual é o arquivo base apos /
print(v)

''' Podemos verifica oque vem antes do arquivo base '''
var = os.path.dirname(path) # verificando qual pasta ou arquivo vem ates da /
print(var)

'''Verificando o caminho completo'''
caminho = os.path.split(path) # mostrado em uma tupla ('pasta', 'arquivo.txt')
print(caminho)

'''Tabem podemos mostra o caminho completo em forma de lista'''
completo = path.split(os.path.sep) # Mostra o caminho completo em forma de lista
print(completo)

# pegando o tamanho de um path completo
tamanho = os.path.getsize(path)
print(tamanho)