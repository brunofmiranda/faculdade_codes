def lendo_ate_uma_linha():
    qtd_linhas = int(input())
    poema = open("poema.txt", "r")
    lista = poema.readlines()
    poema.close()

    for c1 in range(qtd_linhas):
        if c1 > len(lista)-1:
            break
        else:
            print(lista[c1], end="")
def csv_III():
    nome_arquivo = input()
    arquivo = open(nome_arquivo, "r")

    for linha in arquivo:
        linha = linha.replace(",",";")
        print(linha, end = "")
    arquivo.close()
def decifrando_cesar():
    nome_arquivo = input()
    arquivo = open(nome_arquivo, "r")
    lista_arquivo = arquivo.readlines()
    segredo = int(lista_arquivo[0])
    mensagem = lista_arquivo[1]
    for caractere in range(len(mensagem)):
        mensagem = mensagem.replace(mensagem[caractere], mensagem[caractere + segredo], 1)
    print(mensagem)
def caminhos():
    def caminho(nome_arquivo):
        try:
            f = open(nome_arquivo)
            print("Voce esta no " + nome_arquivo)
            f.close()
        except:
            print('Apaguei?')
def depurando_arquivos_1():
    import csv

    cursos = { '127' : 'Bacharelado em Ciência da Computação',
    '132' : 'Arquitetura e Urbanismo',
    '136' : 'Engenharia Civil',
    '137' : 'Engenharia Elétrica',
    '139' : 'Engenharia Florestal',
    '158' : 'Licenciatura em Física',
    '159' : 'Licenciatura em Química',
    '160' : 'Licenciatura em Ciências Biológicas',
    '161' : 'Licenciatura em Matemática',
    '162' : 'Licenciatura em Lígua Portuguesa'
    }

    filename = input()
    f = open(filename, 'r', encoding='latin_1', newline='')
    reader = csv.reader(f, delimiter=';')
    soma = 0.0
    cont = 0
    total = 0
    total_M = 0
    total_F = 0
    reader.__next__()
    for row in reader:
        total += 1
        if row[4]=="555": 
            curso = row[1]
            cont += 1
            soma += float(row[5].replace(",", "."))
        if row[3] == 'M':
            total_M += 1
        elif row[3] == 'F':
            total_F += 1
    media = soma / cont
    print(f'Relatório ENADE 2017')
    print(f'Curso: {cursos[curso]}')
    print(f'Total de alunos inscritos: {total}') #não conta a primeira linha que é o sigla dos campos
    print(f'Total de alunos que realizaram o Enade: {cont}')
    print(f'Quantidade de alunos do sexo masculino do curso inscritos no ENADE: {total_M}')
    print(f'Quantidade de alunos do sexo feminino do curso inscritos no ENADE: {total_F}')
    print(f'Média geral dos alunos que realizaram o ENADE: {media:.2f}')
def hackeando_o_moodles():
    import csv

    arquivo = open("/etc/passwd", "r")
    lista_arquivo = arquivo.readlines()

    index = int(input())
    linha_lida = lista_arquivo[index-1]

    for caractere in range(len(linha_lida)):
        if linha_lida[caractere] == ":":
            print(linha_lida[:caractere])
            break
def conta_palavras():
    def palavras_repetidas(nome_arquivo, palavra):
        arquivo = open(nome_arquivo, "r")
        qtd_palavra = 0
        for linha in arquivo:
            qtd_palavra += linha.count(palavra)
        return print(f"{palavra} aparece no arquivo {nome_arquivo} {qtd_palavra} vez(es).")
def agora_nao_ta_tao_facil():
    nome_arquivo = input()[22:]
    try:
        arquivo = open(nome_arquivo, "r")
        print("da pra abrir")
        lista_tuplas = []
        tupla_temp = ()
        for linha in arquivo:
            tupla_temp = linha.split(" ")
            tupla_temp[1] = int(tupla_temp[1].replace("\n", ""))
            lista_tuplas.append(tuple(tupla_temp))
        lista_tuplas.sort(key = lambda x: x[1], reverse = True)
        for tupla in lista_tuplas:
            print(tupla)
        arquivo.close()
    except:
        print('nao da pra abrir')
def simple_grep():
    p, c, n = input().split(" ")
    c = int(c)
    linhas_p = []
    arquivo = open(n, "r")
    lista_arquivo = arquivo.readlines()
    arquivo.close()
    for linha in range(len(lista_arquivo)):
        if p in lista_arquivo[linha]:
            print(f"{n}: {linha+1}")
            if c == 0:
                print(lista_arquivo[linha], end="")
                print("")
            elif linha == 0 and c ==1:
                print(lista_arquivo[linha], end="")
                print(lista_arquivo[linha+1], end="")
            elif c == 1:
                print(lista_arquivo[linha-1], end="")
                print(lista_arquivo[linha], end="")
                print(lista_arquivo[linha+1], end="")
            else:
                for linha_ant in range(linha-c, linha):
                    print(lista_arquivo[linha_ant], end="")
                print(lista_arquivo[linha], end="")
                for linha_post in range(linha+1, linha+c+1):
                    print(lista_arquivo[linha_post], end="")
                print("")
def onde_esta_o_wally():
    nome_arq = input()
    arq = open(nome_arq, "r")
    l_arq = arq.readlines()
    arq.close()
    qtd_l = len(l_arq)
    m_arq = []
    for linha in l_arq:
        m_arq.append(list(linha))
    qtd_c = len(m_arq[0])
    c_w = 0
    l_w = 0
    for l in range(qtd_l):
        if c_w != 0 and l_w != 0:
            print(f"{l_w} {c_w} horizontal")
            break
        for c in range(qtd_c):
            if c+5 <= qtd_c:
                if m_arq[l][c:c+5] == ["w", "a","l","l","y"]:
                    c_w = c+1
                    l_w = l+1
                    break
            else:
                break
    if c_w == 0 and l_w == 0:
        for c in range(qtd_c):
            c_temp = []
            for caractere in [x[c] for x in m_arq]:
                c_temp.append(caractere)
            for l in range(qtd_l):
                if l+5 <= qtd_l:
                    if c_temp[l:l+5] == ["w", "a","l","l","y"]:
                        c_w = c+1
                        l_w = l+1
                        break
                else:
                    break
            if c_w != 0 and l_w != 0:
                print(f"{l_w} {c_w} vertical")
                break
