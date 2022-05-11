def algebra_linear_nao_matematica():
    dimensaoVetor = int(input())
    vet1 = list(map(int,input().strip().split()))[:dimensaoVetor]
    vet2 = list(map(int,input().strip().split()))[:dimensaoVetor]
    soma = 0
    for i in range(dimensaoVetor):
        soma += vet1[i]*vet2[i]
    if soma == 0:
        print("ortogonais")
    else:
        print(soma)
def listas_sao_mutaveis():
    lenList, numConsultas = map(int, input().split(" "))
    lista = list(map(int,input().strip().split()))[:lenList]
    for i in range(numConsultas):
        a, j = map(int, input().split(" "))
        lista[a] = j
        print(lista)
def depurando_listas_3():
    nomes = input().split()
    nomes.sort()
    repetido = 0
    for i in range(0, len(nomes)-1):
        if nomes[i] == nomes[i+1]:
            repetido += 1
        elif repetido >0 :
            print(nomes[i], repetido+1)
            repetido = 0
    if repetido == 1:
        print(nomes[i], repetido+1)
def modificando_a_lista():
    s = list(map(int, input().split(" ")))
    s.sort()
    n = int(input())
    repete = 0
    dif = 0
    for i in range(n):
        a, b = map(int, input().split(" "))
        if any(a == caractere for caractere in s):
            for c in range(len(s)):
                if a == s[c]:
                    repete += 1
            if repete == b:
                print("tudo ok")
            else:
                dif = b - (repete)
                while dif > 0:
                    s.append(a)
                    dif -= 1
                s.sort()
                print(*s)
            repete = 0
        else:
            print (f"{a} nao esta na lista")
def estatisticas_I():
    N = list(map(int, input().split(" ")))
    media = sum(N)/len(N)
    variancia = 0
    for i in range(len(N)):
        variancia += (N[i] - media)**2
    variancia = variancia/len(N)
    desvioP = variancia**0.5
    print(f"{variancia:.1f}\n{desvioP:.1f}")
def fibonacci_III():
    def fibonacci(n):
        f.append(n)
        if n<=1:
            return n
        else:
            return fibonacci(n-1)+fibonacci(n-2)

    f = []
    n = int(input())
    if n == 1:
        print("Termo:", fibonacci(n), "\nQuantidades:\nfibonacci(0) - 0")
    else:
        print("Termo:", fibonacci(n), "\nQuantidades:")
    repete = 1
    f.sort()
    for i in range(0, len(f)-1):
        if f[i] == f[i+1]:
            repete += 1
        else:
            print(f"fibonacci({f[i]}) - {repete}")
            repete = 1
    print(f"fibonacci({f[len(f)-1]}) - 1")
def debuggando_listas_4():
    def listaValoresUnicos(lista):
        l = []
        for item in lista:
             if item not in l:
                 l.append(item)
        return l

    lista = ['maçã', 'uva', 'abacate', 'uva', 'laranja', 'melancia', 'abacaxi', 'laranja']
    print(listaValoresUnicos(lista))
def escolha_premiada():
    from itertools import combinations
    v = list(map(int, input().split(" ")))
    s = int(input())
    combinacoes = []
    combinacao = []
    possibilidade = False
    for i in range(len(v)):
        combinacoes += combinations(v, i)
    for i in combinacoes: #aqui a gente pega uma das combinacoes, soma e ve se da s
        if sum(i) == s:
            possibilidade = True
            break
    if possibilidade:
        print("E possivel ganhar.")
    else:
        print("Impossivel ganhar.")
def sala_de_espera():
    m, n = map(int, input().split(" "))
    sala_espera = []
    distancias_maximas = []
    for fileira in range(m):
        distancias_maximas.append(1)
    for fileira in range(m):
        fileira_espera = list(map(int, input().split(" ")))
        for cadeira in range(n):
            if fileira_espera[cadeira] == 0:
                for cadeiras_restantes_direita in range(cadeira, n):
                    if fileira_espera[cadeiras_restantes_direita] == 1:
                        if distancias_maximas[fileira] < cadeiras_restantes_direita - cadeira:
                            distancias_maximas[fileira] = cadeiras_restantes_direita - cadeira
                            for cadeiras_restantes_esquerda in range (cadeira, -1, -1):
                                if fileira_espera[cadeiras_restantes_esquerda] == 1:
                                    if distancias_maximas[fileira] > cadeira - cadeiras_restantes_esquerda:
                                        distancias_maximas[fileira] = cadeira - cadeiras_restantes_esquerda
                                        break
                                    else:
                                        break
                            break
                        else:
                            break
    print (max(distancias_maximas))
