#quadrangular de futebol

def inicia_times(lst):
    nomes = ["Real Madrid", "Bayern Munich", "Borussia Dortmund", "Paris Saint Germain"]
    for nome in nomes:
        lst.append(nome)
        lst.append(0) #vitorias
        lst.append(0) #empates
        lst.append(0) #derrotas
        lst.append(0) #saldo de gols

def define_partidas():
    nomes = ["Real Madrid", "Bayern Munich", "Borussia Dortmund", "Paris Saint Germain"]
    lista = [nomes[0], "", nomes[1], "",nomes[2], "", nomes[3], "",
             nomes[0], "", nomes[3], "",nomes[1], "", nomes[2], "",
             nomes[0], "", nomes[2], "",nomes[1], "", nomes[3]]
    return lista

times = []
inicia_times(times)
print(times)

partidas = define_partidas()
print(partidas)