def cortadinhoinho():
    D = dict()
    n = int(input())
    for c1 in range(n):
        chave, valor = input().split(':')
        D[chave] = valor
    for chave1 in D.keys():
        print("{'" + f"{chave1}" + "':" + " '" + f"{D[chave1]}" + "'}")
    c1 = 0
    print("{", end="")
    for chave1 in D.keys():
        c1 += 1
        print("'" + f"{chave1}" + "':" + " '" + f"{D[chave1]}" + "'", end="")
        if c1 == n:
            continue
        else:
            print(", ", end="")
    print("}", end="")
def contando_consoantes_e_vogais():
    import unicodedata
    numeros = dict(consoantes=0, vogais=0)
    frase = input()
    frase = unicodedata.normalize('NFKD',frase.lower())
    for c1 in frase:
        if c1 in 'aeiou':
            numeros['vogais'] = numeros['vogais']+1
        elif c1 in 'bcdfghjklmnpqrstvwxyz':
            numeros['consoantes'] = numeros['consoantes'] + 1
        else:
            continue
    print("{'consoantes':", f"{numeros['consoantes']},", "'vogais':", f"{numeros['vogais']}" +"}")
def linguagem_do_gui():
    n = int(input())
    linguagem_gui = dict()
    for c1 in range(n):
        linha = []
        linha = input().split(" ")
        chave = linha[0]
        valor = ""
        for c2 in range(1, len(linha)):
            valor = valor + linha[c2] + " "
        linguagem_gui[chave] = valor
    texto = []
    texto = input().split(" ")
    for palavra in texto:
        print(f"{linguagem_gui[palavra]}", end="")
def aprendendo_zip_2():
    lista_1 = []
    lista_2 = []
    for c1 in range(10):
        if c1 < 5:
            lista_1.append(int(input()))
        else:
            lista_2.append(int(input()))
    list_tuple = []
    medias = []
    for tupla in zip(lista_1,lista_2):
        list_tuple.append(tupla)
        medias.append(sum(tupla)/2)
    print(list_tuple)
    print(medias)
def bons_pares():
    tam_lista = int(input())
    chaves = list(range(tam_lista))
    valores = list(map(int, input().split(" ")))
    dicionario = dict(zip(chaves, valores))
    bons_pares = 0
    for chave1 in range(tam_lista):
        if valores.count(dicionario[chave1]) > 1:
            for chave2 in range(chave1 + 1, tam_lista):
                if dicionario[chave2] == dicionario[chave1]:
                    bons_pares+= 1
    print(bons_pares)
def bolao():
    total_gatos = int(input())
    numeros_sorteados = list(map(int, input().split(" ")))
    numeros_gatos = dict()
    ganhador = ""
    for c1 in range(total_gatos):
        chave, valor = input().split("-")
        valor_inteiro = list(map(int, valor.split(" ")))
        numeros_gatos[chave] = valor_inteiro
    for chave in numeros_gatos.keys():
        if numeros_gatos[chave] == numeros_sorteados:
            ganhador = chave
    if ganhador != "":
        print(f"deu bom!\n{ganhador}")
    else:
        print("não foi dessa vez /:")
def pintando_o_seno():
   import math
    def TwoDSpace(deslocamento, amplitude, espaço):
        dicionario ={}
        for i in range(40):
            j = int(deslocamento - amplitude*math.sin(10*i*math.pi/180))
            dicionario[f"{i},{j}"] = "*"
        for j in range(20):
            for i in range(40):
                if dicionario.get(f"{i},{j}") != None:
                    print(dicionario[f"{i},{j}"], end="")
                else:
                    print(espaço, end="")
            print("") 
def consulfib():
    import sys
    sys.setrecursionlimit(10**6)
    def fibonacci(n, a = 1):
        if n == 1:
            return 0
        elif n == 2:
            return a
        return fibonacci(n - 1) + fibonacci(n - 2)
    n = int(input())
    lista = list(map(int, input().split(" ")))
    lista2 = []
    for c1 in range(len(lista)):
        lista2.append(fibonacci(lista[c1]))
    print(tuple(lista2))
def crud_sem_D():
    linhas = int(input())
    turma_g = {'João' : 10,
        'Maria' : 10,
        'Jorge' : 4,
        'Marta' : 5,
        'Mário' : 6,
        'Mikael' : 9}
    for c1 in range(linhas):
        instrucao = input()
        if instrucao[0] == 'C' or instrucao[0] == 'U':
            aluno, nota = instrucao[2:].split(" ")
            nota = int(nota)
            turma_g[aluno] = nota
        elif instrucao[0] == 'R':
            aluno = instrucao[2:]
            print(aluno, turma_g[aluno])
def falta_um():
    tam_lista = int(input())
    lista = list(map(int, input().split(" ")))
    lista.sort()
    repetido, falta = 0, 0
    for c1 in range(tam_lista):
        if c1+1 == tam_lista:
            break
        elif lista[c1] == lista[c1+1]:
            repetido = lista[c1]
            break
    for c1 in range(tam_lista+1):
        if c1+1 not in lista:
            falta = c1 + 1
            break
