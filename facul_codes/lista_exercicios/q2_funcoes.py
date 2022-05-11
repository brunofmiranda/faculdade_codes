def calculo_potencia_v2():
    from math import pow

    def powAPC(x,y):
        xy=pow(x,y)
        print(f'{xy:.1f}')
def hamburguer():
    def hamburguer(c,q,a,t,b):
        print(f'{c} carne(s)')
        print(f'{q} fatia(s) de queijo')
        print(f'{a} folha(s) de alface')
        print(f'{t} rodela(s) de tomate')
        print(f'{b} fatia(s) de bacon')
def calcule_o_diaI():
    #2
def fala_e_repete():
    def fala(nome):
        print(f'Oi, {nome}')
    def repete(nome):
        fala(nome)
        print('Repete, por favor! Não consigo te ouvir!')
        fala(nome)
def vestimentas_countryI():
    def vestimentas(x,y):
        if(x>y):
            m=y
        else:
            m=x
        print(m)
def modificador_de_numeros():
    def soma(x,y):
        print(f'{x+y}')
    def subtracao(x,y):
        print(f'{x-y}')
    n=int(input())
    soma(n,8)
    subtracao(n,7)
    soma(n,2)
    subtracao(n,9)
    soma(n,1)
    subtracao(n,3)
    soma(n,6)
    subtracao(n,5)
def pitagoras():
    def pitagoras(b, c):
        a = (b*b + c*c)**0.5
        print(int(a))

    b, c = input().split()
    pitagoras(int(b), int(c))
def piscina_da_mansao():
    def print_rectangle(a,b,c):
        print(a)
        print(f'{"+"*a}')
        print(f'+{" "*(a-2)}+')
        print(f'{"+"*a}')
        print(b)
        print(f'{"+"*b}')
        print(f'+{" "*(b-2)}+')
        print(f'{"+"*b}')
        print(c)
        print(f'{"+"*c}')
        print(f'+{" "*(c-2)}+')
        print(f'{"+"*c}')
    a,b,c = input().split()
    print_rectangle(int(a),int(b),int(c))
def pacotes_de_bolachaII():
    def pacotesDeBolacha(m,n,k):
        if int(m/n) >= k:
            print(f'{n*k}')
        elif int(m/n) < k:
            print(f'{(m//n)*n}')
def padroes_geometricos_2():
    s1, s2, s3, s4 = input().split()

    def duplica(f):
        f()
        f()
        f()

    def duplica_o_duplicado(f):
        duplica(f)
        duplica(f)
        
    def imprime_parte_linha1():
        print(f'{s1+s2}', end="")
        
    def imprime_parte_linha1_fim():
        print(s1)
        
    def imprime_parte_linha2():
        print(f'{s3+s4}', end="")
        
    def imprime_parte_linha2_fim():
        print(s3)
        
    def imprime_linha1():
        duplica_o_duplicado(imprime_parte_linha1)
        imprime_parte_linha1_fim()

    def imprime_linha2():
        duplica_o_duplicado(imprime_parte_linha2)
        imprime_parte_linha2_fim()
        
    def imprime_parte_padrao():
        imprime_linha1()
        imprime_linha2()
              
    def imprime_padrao():
        duplica_o_duplicado(imprime_parte_padrao)
        imprime_linha1()
        
    imprime_padrao()
