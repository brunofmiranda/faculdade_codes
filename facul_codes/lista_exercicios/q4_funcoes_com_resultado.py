def aprendendo_funcao_com_resultado_2():
    def subQuadrado(a,b):
        if b >= a:
            return print((b - a)**2)
        else:
            return print(a - b)

    a = int(input())
    b = int(input())
    subQuadrado(a,b)
def caixa():
    def parcelamento(valor_compra, qtd_parcelas):
        return valor_compra/qtd_parcelas
    def desconto(valor):
        return (valor*15)/100
    def caixa(valor_compra, qtd_parcelas):
        if qtd_parcelas == 1:
            return str(f"Voce ganhou um desconto de {desconto(valor_compra)} reais, volte sempre!")
        elif qtd_parcelas >=2:
            return str(f"Cada parcela é de {parcelamento(valor_compra, qtd_parcelas)} reais, volte sempre!")
def comparacao_I():
    def compara(n,m):
        if n > m:
            return True
        else:
            return False
def soma_harmonica():
    def soma_harmonica(X):
        if X == 1:
            return 1
        elif X > 1:
            return (1/X) + soma_harmonica(X-1)
def ano_bissexto():
    def anobissexto(a):
        if (a % 4 == 0 or a % 400 == 0) and not a % 100 == 0:
            return str('Sim')
        else:
            return str('Nao')
def e_multiplo_de_3_como_descobrir_usando_recursividade_mutua():
    def multiplo3(n):
        if n%3 == 0:
            return True
        else:
            return False

    def não_multiplo3(n):
        if n%3 != 0:
            return True
        else:
            return False
def segundo_grau():
    def calcula_f(a,b,c,x):
      return (a*(x*x)+b*x+c)

    def calcula_delta(a,b,c,x):
      delta = ((b*b) - (4*a*c))
      if(delta < 0):
        return "Equacao sem raizes reais"
      else:
        return "O resultado de f(" + str(x) + ") eh: " + str(calcula_f(a,b,c,x))
def estacionamento_no_shopping():
    import datetime
    import math
    def calcula_tiquete_estacionamento(hc, mc, hs, ms):
        h_chegada = datetime.timedelta(hours=hc, minutes=mc)
        h_saida = datetime.timedelta(hours=hs, minutes=ms)
        h_dentro = math.ceil(((h_saida-h_chegada).total_seconds())/3600) # converte em segundos depois em horas e depois arredonda pra cima (ceil())
        if h_dentro < 0:
            h_dentro = 24+h_dentro      
        if h_dentro == 0:
            return f"({(3.5*2)+(4.1*2)+(4.6*20)}, {24+h_dentro})"
        elif h_dentro <=2:
            return f"({(3.5*h_dentro)}, {h_dentro})"
        elif h_dentro <=4:
            return f"({(3.5*2)+(4.1*(h_dentro-2))}, {h_dentro})"
        else:
            return f"({(3.5*2)+(4.1*2)+(4.6*(h_dentro-4))}, {h_dentro})"
def pattern_mais_complicado():
    c = []
    def pattern(n):
        global c
        if n <= 0:
            c.append(n)
            c = c[::-1]
            return print("\n".join(map(str, c))), c.clear()
        elif n % 2 == 0:
            c.append(n)
            return print(f"{n}"), pattern(int(n-5))
        else:
            c.append(n)
            return print(f"{n}"), pattern(int(n-((n/2)+0.5)))
def mdc_metodo_da_forca_bruta():
    def mdc(x, y, contador, maximo): #máximo e contador começa com 1

        if x%contador == 0 and y%contador == 0:
            if contador == x and contador == y:
                return contador
            else:
                return mdc(x, y, contador+1, contador)
        else:
            if contador >= x or contador >= y:
                return maximo
            else:
                return mdc(x, y, contador+1, maximo)
