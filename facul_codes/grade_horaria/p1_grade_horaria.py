def analisa_retirada(f_grade, f_hora_materia):
    linha_vazia = False
    for c1 in f_hora_materia:
        for c2 in range(1,7):
            if f_grade[c1][2] != "          ":
                linha_vazia = True
                return linha_vazia


def mensagem_erro(f_grade):
    print(f"!({entrada})")
    return f_grade


def imprime_grade(f_grade):
    print("+---------------+", end="")
    print("----------+" * 6)
    for coluna in range(7):
        print(f"{f_grade[0][coluna]}|", end="")
    print("")
    print("+---------------+", end="")
    print("----------+" * 6)
    for linha in range(1, 16):
        if any(espaco != "          " and espaco != "|               " and espaco != "               " for espaco in f_grade[linha]):
            for coluna in range(7):
                print(f"{f_grade[linha][coluna]}|", end="")
            print("")
            print("+---------------+", end="")
            print("----------+"*6)


def desmembra_dth(f_dth):
    f_dia_materia = []
    f_turno_materia = ""
    f_hora_materia = []
    f_dth = str(f_dth).strip("[']")
    for caractere in range(len(f_dth)):
        if f_dth[caractere] in "234567":
            f_dia_materia.append(f_dth[caractere])
        elif f_dth[caractere] in 'MNT':
            f_turno_materia = f_dth[caractere]
            f_hora_materia = list(map(int, f_dth[caractere+1:]))
            break
        else:
            return 0, 0, 0
    for f_horario in range(len(f_hora_materia)):
        if f_turno_materia == 'M':
            if f_hora_materia[f_horario] > 5 or f_hora_materia[f_horario] < 1:
                return 0, 0, 0
        elif f_turno_materia == "T":
            if f_hora_materia[f_horario] > 6 or f_hora_materia[f_horario] < 1:
                return 0, 0, 0
        elif f_turno_materia == "N":
            if f_hora_materia[f_horario] > 4 or f_hora_materia[f_horario] < 1:
                return 0, 0, 0
    f_dia_materia = list(map(int, f_dia_materia))
    return f_dia_materia, f_turno_materia, f_hora_materia


def altera_grade(f_tipo, f_dia_materia, f_turno_materia, f_hora_materia, f_grade, f_nome_materia):
    f_horario_lista = lista_horario(f_hora_materia, f_turno_materia)
    f_acrescimo_linha = corrige_horario_linha(f_turno_materia)
    for c1 in range(len(f_hora_materia)):
        for dia in f_dia_materia:
            if f_tipo == "+":
                if f_grade[f_hora_materia[c1] + f_acrescimo_linha][dia - 1] != "          ":
                    return mensagem_erro(f_grade)
                else:
                    f_grade[f_hora_materia[c1] + f_acrescimo_linha][dia-1] = " " + f_nome_materia + " "
            elif f_tipo == "-":
                if f_grade[f_hora_materia[c1] + f_acrescimo_linha][dia - 1] == (" " + f_nome_materia + " "):
                    f_grade[f_hora_materia[c1] + f_acrescimo_linha][dia-1] = "          "
                else:
                    return mensagem_erro(f_grade)
        if f_tipo == "+":
            f_grade[f_hora_materia[c1] + f_acrescimo_linha][0] = "| " + f_horario_lista[c1] + " "
        elif f_tipo == "-":
            if analisa_retirada(f_grade, f_hora_materia):
                f_grade[f_hora_materia[c1] + f_acrescimo_linha][0] = "|               "
    return f_grade


def corrige_horario_linha(f_turno_materia):
    f_acrescimo_linha = 0
    if f_turno_materia == "M":
        f_acrescimo_linha = 0
    elif f_turno_materia == "T":
        f_acrescimo_linha = 5
    elif f_turno_materia == "N":
        f_acrescimo_linha = 11
    return f_acrescimo_linha


def cria_grade():
    f_grade = [["|               ", " Seg      ", " Ter      ", " Qua      ", " Qui      ", " Sex      ", " Sab      "]]
    for linha in range(1, 16):
        f_grade.append(["               "])
        for coluna in range(6):
            f_grade[linha].append("          ")
    return f_grade


def lista_horario(f_hora_materia, f_turno_materia):
    relacao_hora_num = []
    if f_turno_materia == "M":
        relacao_hora_num = ['08:00 - 08:55', '08:55 - 09:50', '10:00 - 10:55', '10:55 - 11:50', '12:00 - 12:55']
    elif f_turno_materia == "T":
        relacao_hora_num = ['12:55 - 13:50', '14:00 - 14:55', '14:55 - 15:50', '16:00 - 16:55', '16:55 - 17:50', '18:00 - 18:55']
    elif f_turno_materia == "N":
        relacao_hora_num = ['19:00 - 19:50', '19:50 - 20:40', '20:50 - 21:40', '21:40 - 22:30']
    f_horario_lista = []
    for f_horario in f_hora_materia:
        f_horario_lista.append(relacao_hora_num[f_horario-1])
    return f_horario_lista


global entrada
dia_materia = []
turno_materia = ""
hora_materia = []
grade = cria_grade()
while True:
    entrada = input()
    if entrada == "Hasta la vista, beibe!":
        break
    elif entrada == "?":
        imprime_grade(grade)
    else:
        lista_dth = entrada[11:].split(' ')
        for dth in lista_dth:
            dia_materia, turno_materia, hora_materia = desmembra_dth(dth)
            if dia_materia == 0 and turno_materia == 0 and hora_materia == 0:
                print(f"!({entrada})")
            else:
                grade = altera_grade(entrada[0], dia_materia, turno_materia, hora_materia, grade, entrada[2:10])