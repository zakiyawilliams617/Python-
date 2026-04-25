import networkx as nx

def read_input(filename):
    file = open(filename, "r")
    lines = file.read().split("\n")
    file.close()

    idx = 0
    n = int(lines[idx])
    idx = idx + 1

    team_names = []
    wins = []
    losses = []
    remaining = []
    games = []

    i = 0
    while i < n:
        parts = lines[idx].split()
        idx = idx + 1

        team_names.append(parts[0])
        wins.append(int(parts[1]))
        losses.append(int(parts[2]))
        remaining.append(int(parts[3]))

        row = []
        j = 4
        while j < 4 + n:
            row.append(int(parts[j]))
            j = j + 1
        games.append(row)
        i = i + 1

    return n, team_names, wins, losses, remaining, games

def check_trivial_elimination(x, n, team_names, wins, remaining):
    max_possible = wins[x] + remaining[x]
    i = 0
    while i < n:
        if i !=x:
            if wins[i] > max_possible:
                return True, team_names[i]
        i = i + 1
    return False, None

def build_flow_graph(x, n, wins, remaining, games):
    G = nx.DiGraph()
    G.add_node("s")
    G.add_node("t")

    i = 0 
    while i < n:
        if i != x:
            G.add_node(i)
        i = i + 1 

    i = 0
    while i < n:
        if i != x:
            j = i + 1
            while j < n:
                if j != x:
                    if games[i][j] > 0:
                        game_node = str(i) + "-" + str(j)
                        G.add_node(game_node)
                        G.add_edge("s", game_node, capacity=games[i][j])
                        G.add_edge(game_node, i, capacity=999999)
                        G.add_edge(game_node, j, capacity=999999)
                j = j + 1
        i = i + 1

    i = 0
    while i < n:
        if i != x:
            cap = wins[x] = remaining[x] - wins[i]
            if cap < 0:
                cap = 0
            G.add_edge(i, "t", capacity=cap)
        i = i + 1

    return G

def get_elimination_certificate(G, n, x, team_names):
    cut_value, partition = nx.minimum_cut(G, "s", "t")
    reachable = partition[0]

    certificate = []
    i = 0
    while i < n:
        if i != x:
            if i in reachable:
                certificate.append(team_names[i])
        i = i + 1
    return certificate

def total_games_from_source(x, n, games):
    total = 0
    i = 0
    while i < n:
        if i != x:
            j = i + 1
            while j < n:
                if j != x:
                    total = total + games[i][j]
                j = j + 1
        i = i + 1
    return total

def solve(filename):
    n, team_names, wins, losses, remaining, games = read_input(filename)

    x = 0
    while x < n:
        trivial, eliminator = check_trivial_elimination(x, n, team_names, wins, remaining)

        if trivial:
            print(team_names[x] + "has been trivially eliminated by " + eliminator + ".")
        else: 
            G = build_flow_graph(x, n, wins, remaining, games)
            flow_value, flow_duct = nx. maximum_flow(G, "s", "t")
            needed = total_games_from_source(x, n, games)

            if flow_value >= needed:
                print(team_names[x] + " is not eliminated.")
            else:
                certificate = get_elimination_certificate(G, n, x, team_names)
                if len(certificate) > 0:
                    print(team_names[x] + " is eliminated by " + str(certificate) + ".")
                else: 
                    print(team_names[x] + " is eliminated.")

        x = x + 1

solve("world_cup.txt")