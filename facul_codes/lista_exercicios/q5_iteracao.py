def jovem_fisico():
    qtd_vetores = int(input())
    contador = 0
    soma_forças = 0
    while qtd_vetores > contador:
        x, y, z = input().split(" ")
        x = int(x)
        y = int(y)
        z = int(z)
        soma_forças = soma_forças + x + y + z
        contador +=1
    if soma_forças == 0:
        print("YES")
    else:
        print("NO")
def conversao_real_para_dolar():
    cotacao = float(input())
    tam_lote = int(input())
    qtd_lote = int(input())
    valor_lote = (cotacao * tam_lote)
    valor_lote = valor_lote + (valor_lote*0.025)
    contador = 1
    while qtd_lote >= contador:
        print(f'Lote: {contador} - Total da venda: R$ {valor_lote:.2f}')
        contador += 1 
def pescaria():
    n = int(input())
    peixe = input()
    if peixe == 'atum':
        while n > 0:
            print("Nossa, pesquei um atum gigante!")
            n -=1
    elif peixe == 'salmão':
        n = n*2
        while n > 0:
            print("Que salmão bonito que pesquei!")
            n -=1
    else:
        print("Nem sabia que esse peixe existia")
def loop_infinito():
    while True:
        numero = int(input())
        if numero <= 0:
            break
        elif numero > 10**9:
            print("isso ai tem cara de loop infinito")
        else:
            print("nossa o programa foi rapido")
def fugitivo():
    N, M = input().split(" ")
    M = int(M)
    N = int(N)
    mensagem = ""
    p_c = [0,0] #p_c = plano cartesiano
    while N > 0:
        C, D = input().split(" ")
        D = int(D)
        if C == 'N':
            p_c[1] = p_c[1] + D
        elif C == 'S':
            p_c[1] = p_c[1] - D
        elif C == 'L':
            p_c[0] = p_c[0] + D
        elif C == 'O':
            p_c[0] = p_c[0] - D
        distancia_percorrida = (abs((p_c[0])**2)+(abs(p_c[1])**2))**0.5
        if distancia_percorrida > M:
            mensagem = 'sim'  
        N -= 1
    if mensagem == 'sim':
        print("sim")
    else:
        print("nao")
def looPA():
    a1, r, n = input().split(" ")
    a1 = int(a1)
    r = int(r)
    n = int(n)
    contador = 0
    soma_termos = 0
    while contador != n:
        an = a1 + contador*r
        print(an)
        soma_termos = soma_termos + an
        contador +=1
    print(soma_termos)
def debugando_iteracao_5():
    soma = 0
    x = 0
    while True:
        x = int(input())
        if x >= 0:
            soma = soma + x
        else:
            print(soma)
            break
def objetos_voadores_nao_identificados_II():
    l, r = input().split(" ")
    l = int(l)
    r = int(r)
    min_ovni = 1
    min_ovni_ant = 0
    dif = 0
    c = 0
    while min_ovni <= r:
        min_ovni = min_ovni + (3 + c)
        if min_ovni >= l and min_ovni_ant >= l and min_ovni <= r:
            dif = min_ovni - min_ovni_ant - 1
        min_ovni_ant = min_ovni
        c += 2
    print(dif)
def numero_de_armstrong_formatado():
    n = input()
    c = len(n)
    n = int(n)
    mensagem = ""
    alg = 0
    armstrong = 0
    linha1 = ""
    linha2 = ""
    n2 = n
    while n > 0:
        alg = n % 10
        armstrong = armstrong + (alg**c)
        linha1 = linha1 + f"{alg}^{c} + "
        linha2 = linha2 + f"{alg**c} + "
        n = n // 10
    linha1 = linha1[:-2] + "="
    if armstrong == n2:
        linha2 = linha2[:-2] + f"= {n2}"
        print(f"{linha1}\n{linha2}\n{n2} é um número de Armstrong de {c} ordem.")
    else:
        linha2 = linha2[:-2] + f"!= {n2}"
        print(f"{linha1}\n{linha2}\n{n2} não é um número de Armstrong de {c} ordem.")
def depurando_codigo_python_5():
    def digito(c):
        if c=="0" or c=="1" or c=="2" or c=="3" or c=="4" or c=="5" or c=="6" or c=="7" or c=="8" or c=="9":
            return True
        else:
            return False

    x = input()
    concatenador = ""
    cont = 0
    acumulador = 0
    while x != "*":
        if digito(x):
            x = int(x)
            cont += 1
            acumulador += x
        else:
            concatenador = concatenador + x
        x = input()
    if acumulador == 0:
        media_digitos = 0.0
    else:
        media_digitos = acumulador/cont
    print(concatenador, media_digitos)
