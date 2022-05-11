def strings_com_vogais_trocadas():
    string_a = input()
    string_e = string_a
    string_i = string_a
    string_o = string_a
    string_u = string_a
    for i in 'aeiou':
        string_a = string_a.replace(i, 'a')
        string_e = string_e.replace(i, 'e')
        string_i = string_i.replace(i, 'i')
        string_o = string_o.replace(i, 'o')
        string_u = string_u.replace(i, 'u')
    print(f'{string_a}\n{string_e}\n{string_i}\n{string_o}\n{string_u}')
def maior_string():
    n = int(input())
    maior_string = ""
    for i in range(n):
        string = input()
        if len(string) > len(maior_string):
            maior_string = string
    print(maior_string)
def regra_ortografica():
    redacao_str = input()
    redacao_list = list(redacao_str)
    for i in range(len(redacao_list)):
        if redacao_list[i] == 'n' and (redacao_list[i+1] == 'b' or redacao_list[i+1] == 'p'):
            redacao_list[i] = 'm'
    redacao_str = "".join(redacao_list)
    print(redacao_str)
def funcao_boolena_de_strings_5():
    import string
    def tem_letra_maiúscula(s):
        achei_maiuscula = 0
        for letra in s:
            if letra not in string.ascii_letters and letra not in string.digits:
                continue
            elif letra == letra.upper():
                return True
        return False
def tesouro():
    s = input()
    if s.find('X') == -1:
        print("Péricles, não tem tesouro")
    else:
        cont1 = 0
        cont2 = 0
        mensagem = ""
        for i in s:
            if mensagem != "":
                break
            cont1 += 1
            if i == 'P':
                for l in range(cont1, len(s)):
                    cont2 += 1
                    if s[l] == '#':
                        mensagem = "Péricles esse caminho não funciona"
                        break
                    elif s[l] == 'X':
                        mensagem = f"Péricles, {cont2} passos"
                        break
            elif i == 'X':
                for l in range(cont1, len(s)): 
                    cont2 -= 1
                    if s[l] == '#':
                        mensagem = "Péricles esse caminho não funciona"
                        break
                    elif s[l] == 'P':
                        mensagem = f"Péricles, {cont2} passos"
                        break
        print(mensagem)
def senha_valida():
    import string
    def eh_caractere_especial(s):
        for caractere in s:
            if caractere not in string.digits and caractere not in string.ascii_letters:
                return True
        return False

    s = input()
    num_requisitos = 0
    if len(s) > 6 and len(s) < 32:
        num_requisitos += 1
        if any(caractere == caractere.upper() and caractere not in string.digits for caractere in s):
            num_requisitos += 1
            if any (caractere == caractere.lower() and caractere not in string.digits for caractere in s):
                num_requisitos += 1
                if any(caractere in string.digits for caractere in s):
                    num_requisitos += 1
                    if eh_caractere_especial(s):
                        num_requisitos -= 1
    if num_requisitos == 4:
        print("Senha valida.")
    else:
        print("Senha invalida.")
def depurando_strings_4():
    import unicodedata
    def não_possui_a_letra_o(palavra):
        palavra = unicodedata.normalize('NFKD', palavra)
        for letra in palavra:
            if  letra == 'o':
                return False
        return True
def wubwubwub():
    s = input()
    musica_original = ""
    i = 0
    while i < len(s):
        if s[i:i+3] == 'WUB':
            i += 3
        else:
            musica_original = musica_original + musica_original.join(s[i])
            i += 1
            if s[i:i+3] == 'WUB':
                musica_original = musica_original + musica_original.join(' ')
            else:
                continue
    print(musica_original)
def batalha_naval_1D():
    s = input()
    qtd_disparos = s.count(".o")
    if s[0] == 'o':
        qtd_disparos += 1
    print(qtd_disparos)
def jogo_de_palavras_1():
    import unicodedata
    def não_possui_a_letra_u(palavra):
        palavra = unicodedata.normalize('NFKD', palavra)
        for letra in palavra:
            if letra == 'u' or letra == 'U':
                return False
        return True
