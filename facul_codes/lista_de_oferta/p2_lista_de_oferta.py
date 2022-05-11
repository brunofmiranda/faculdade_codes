")
    carga = carga.replace("h", "")
    return int(carga)
# main
matriz = []
arquivos_abertos = []
while True:
    comando = input()
    if comando == "FIM":
        break
    elif comando[:4] == "leia":
        if os.path.isfile(comando[5:]): # confere se o arquivo existe
            if comando[5:] not in arquivos_abertos:
                arquivos_abertos.append(comando[5:])
                arquivo = open(comando[5:], "r", encoding="utf8")
                lista_arquivo = arquivo.readlines()

                #cria uma matriz que é uma tabela do arquivo
                for linha in lista_arquivo:
                    matriz.append(linha.split(","))
                arquivo.close()
        else:
            mensagem_erro(comando[5:])
    elif comando[:5] == "carga":
        if confere_arquivo_aberto():
            dict_carga = dict()
            docente = comando[6:]
            carga_t = 0
            alunos_t = 0

            # procura as disciplinas atreladas ao docente
            for linha in range(len(matriz)):  # cria uma tupla com a linha e a disciplina
                if docente in matriz[linha][4]:

                    # cria uma chave com nome + cod da disciplina e um valor (turma + carga + alunos)
                    carga_h = retira_parenteses((matriz[linha][4])[len(docente) + 1:])
                    alunos = int(matriz[linha][7])
                    chave_disciplina = f"{matriz[linha][1]} ({matriz[linha][0]})"
                    valor_disciplina = f"Turma {matriz[linha][2]}: {carga_h}h ({alunos} alunos)"

                    # se ja tiver aquela chave no dicionario, acrescenta ao valor outro +\n
                    if chave_disciplina in dict_carga.keys():
                        dict_carga[chave_disciplina].append(valor_disciplina)
                    else:
                        dict_carga[chave_disciplina] = [valor_disciplina]

                    if alunos > 6:
                        carga_t += carga_h
                        alunos_t += alunos

            # bota em ordem alfabética
            chave_ordenada = sorted(dict_carga.keys())

            # confere se achou o docente ou se não tem nada
            if dict_carga != {}:
                # impressao pro usuario
                print(f"{docente}:")
                for chave in chave_ordenada:
                    dict_carga[chave].sort()
                    print(f" * {chave}:")
                    for valor in dict_carga[chave]:
                        print(f"     {valor}")

                #confere se teve turmas consideradas
                if carga_t == 0:
                    print(f"[Carga total considerada: {carga_t}h (0.00h/aluno)]")
                else:
                    print(f"[Carga total considerada: {carga_t}h ({(carga_t / alunos_t):.2f}h/aluno)]")
            else:
                mensagem_erro(comando[6:])
        else:
            mensagem_erro(comando[6:])
    elif comando[:10] == "disciplina":
        if confere_arquivo_aberto():
            disciplinas_arq = dict()
            D = int(comando[11:])

            #cria dicionario{chave_p = disciplina, valor = dicionario{chave_s = turma, valor = [lista de professores]}}
            for linha in range(1, len(matriz)):
                chave_p = f"{matriz[linha][1]} ({matriz[linha][0]})"
                chave_s = matriz[linha][2]
                docente = f"{(matriz[linha][4])[:-6]}"
                if chave_p in disciplinas_arq.keys():
                    if chave_s in disciplinas_arq[chave_p].keys():
                        disciplinas_arq[chave_p][chave_s].append(docente)
                    else:
                        lista_temp = [f"{(matriz[linha][4])[:-6]}"]
                        dict_temp = {chave_s: lista_temp}
                        disciplinas_arq[chave_p].update(dict_temp)
                else:
                    lista_temp = [docente]
                    dict_temp = {chave_s: lista_temp}
                    disciplinas_arq[chave_p] = dict_temp

            #cria dicionario{chave_p = disciplina, valor = [lista de tuplas (turma, qtd de professores >= D)]}
            disciplinas_D = {}
            for chave_p in disciplinas_arq.keys():
                turmas_D = []
                for chave_s in disciplinas_arq[chave_p].keys():
                    if len(disciplinas_arq[chave_p][chave_s]) >= D:
                        tupla_temp = (chave_s, len(disciplinas_arq[chave_p][chave_s]))
                        turmas_D.append(tupla_temp)
                if turmas_D != []:
                    disciplinas_D[chave_p] = turmas_D

            #caso não houver nenhuma disciplina com qtd de professores >=D
            if disciplinas_D == {}:
                mensagem_erro(comando[11:])
            else:
                lista_chave_ordenada = sorted(disciplinas_D.keys()) #ordenando as disciplinas

                #impressão para o usuário
                print(f"Turmas com pelo menos {D} docentes:")
                for chave_p in lista_chave_ordenada:
                    print(f" * {chave_p}:", end="")
                    disciplinas_D[chave_p].sort(key = lambda tupla: tupla[0]) #ordenando a lista
                    mensagem = ""
                    for tupla in disciplinas_D[chave_p]:
                        mensagem = mensagem + (f" {tupla[0]} ({tupla[1]}),")
                    print(mensagem[:-1])
        else:
            mensagem_erro(comando[11:])
    elif comando[:10] == "matriculas":
        lista_cod = list(comando[11:].split(" "))
        if confere_arquivo_aberto():
            nome_disciplina = ""
            lista_matricula = []
            #cria lista de tupla(nome_disciplina, qtd total de alunos matriculados)
            for cod in lista_cod:
                achou = 0
                qtd_aluno = 0
                lista_turmas = []
                for linha in range(len(matriz)):
                    if matriz[linha][0] == cod:
                        achou = 1
                        nome_disciplina = matriz[linha][1]

                        #confere se a turma já foi contada
                        if matriz[linha][2] not in lista_turmas:
                            lista_turmas.append(matriz[linha][2])
                            qtd_aluno += int(matriz[linha][7])

                #cria tupla (nome da disciplina, qtd de alunos)
                tupla_temp = (nome_disciplina, cod, qtd_aluno, achou)
                lista_matricula.append(tupla_temp)

            #ordena em ordem alfabética e depois decrescente
            lista_matricula.sort(key=lambda tupla: tupla[0])
            lista_matricula.sort(key=lambda tupla: tupla[2], reverse=True)

            #impressão

            #ordena os cod não encontrado
            lista_erro = []
            for tupla in lista_matricula:
                if tupla[3] == 0:
                    lista_erro.append(tupla)
            lista_erro.sort(key=lambda tupla: tupla[1])
            for tupla in lista_erro:
                mensagem_erro(tupla[1])

            #impre os cod achado
            for tupla in lista_matricula:
                if tupla[3] == 1:
                    print(f"{tupla[2]} matriculados em {tupla[0]} ({tupla[1]})")
        else:
            for cod in lista_cod:
                mensagem_erro(cod)