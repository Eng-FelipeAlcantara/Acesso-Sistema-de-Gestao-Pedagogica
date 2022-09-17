#Programa que gera acesso a um sistema de gestão pedagógica para professores, pais e estudantes
resposta="SIM"
while resposta=="SIM":
    nivel=input("Digite o nível de acesso: ").upper()
    if nivel=="PRO" or nivel=="ALU":
        genero=input("Digite o seu gênero: ").upper()
        if nivel=="PRO":
            if genero=="FEMININO":
                print("Olá professora")
            else:
                print("Olá professor")
        else:
            if genero=="FEMININO":
                print("Olá aluna")
            else:
                print("Olá aluno")
    elif nivel=="responsável":
        print("Olá pai/mãe")
    else:
        print("Olá pai/mãe")
    resposta=input("Digite SIM para continuar: ").upper()