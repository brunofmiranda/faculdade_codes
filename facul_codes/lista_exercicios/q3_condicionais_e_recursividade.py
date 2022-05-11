def aprendendo_IV():
    n = int(input())
    if (n>50):
        print(f'{n//3}')
    else:
        print(n)
def banner():
    def banner (n):
        if (n > 0) and ((n%2)==0):
            print('| | | | | | | | | |')
        elif (n > 0) and ((n%2)!=0):
            print('- - - - - - - - - -')
        elif (n < 0) and ((n%2)==0):
            print('. . . . . . . . . .')
        elif (n <0) and ((n%2)!=0):
            print('= = = = = = = = = =')
def triangulo_pitorestico():
    def pitorestico(a,b,c):
        if (a%2)==0 and (a%3)==0 and (a%5)==0:
            if (b%2)==0 and (b%3)==0 and (b%5)==0:
                if (c%2)==0 and (c%3)==0 and (c%5)==0:
                    print('Pitorestico!!!')
                else:
                    print('Nao foi dessa vez')
            else:
                print('Nao foi dessa vez')
        else:
            print('Nao foi dessa vez')
def recursao_e_condicao_simples():
    def simples(a):
        if a == 'repete':
            b = input('Olá! Vamos repetir!\n')
            simples(b)
    a = input()
    simples(a)
def multiplos():
    def multiple(a,b):
        if(a%b)==0 or (b%a)==0:
            if(a%b)==0:   
                print(f'{a} eh multiplo de {b}')
            if(b%a)==0:
                print(f'{b} eh multiplo de {a}')
        else:
            print('nao multiplos')
def complexo_B():
    def controle(n,c):
        if c==n:
            print(f'Parabens Julie! Voce tomou todos os {n} comprimidos!')
        elif c==0:
            c=1
            print(f'Voce ja tomou {c} comprimidos, restam {n-c}.')
            controle(n,c+1)
        else:
            print(f'Voce ja tomou {c} comprimidos, restam {n-c}.')
            controle(n,c+1)
def debugando_estruturas_de_desicao_2():
    lap, ipa, pag, dis = input().split()
    lap = int(lap)
    ipa = int(ipa)
    pag = int(pag)
    dis = int(dis)

    valor = (lap * 1500) + (ipa * 1000)
    #desconto por quantidade
    if ((lap + ipa) >= 3):
        valor = valor - 500
    #desconto por pagamento
    if (pag == 0):
        valor = valor - (valor * 0.03)
    elif(pag == 1):
        valor = valor - (valor * 0.10)
    #calculo de frete
    if(dis<=50):
        valor = valor + 100
    else:
        valor = valor + 200

    print(f'{valor:.2f}')
def domino():
    def dominos(N,M):
        qtd=(N*M)//2
        print(qtd)
def sequencia_de_pares_v2():
    def paresDeNumeros(n,m):
        if(n<=m):
            print(f'{n} {m}')
            paresDeNumeros(n+2,m-1)
def debugando_recursivo_1():
    def formaçãoDeVoo(offset, n):
        global N
        N = N + 1
        print(offset*" " + n*"V")
        if n <= 1:
            return print(" ");
        formaçãoDeVoo(offset+1, n-2)
        formaçãoDeVoo(offset+1, n-2)
