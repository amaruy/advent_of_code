import networkx as nx

G = nx.Graph([l.split('-') for l in open('2024/data/input23.txt').read().splitlines()])

# count triplets
print(sum(any(n.startswith('t') for n in tr) for tr in nx.enumerate_all_cliques(G) if len(tr) == 3))

# Find max clique
print(','.join(sorted(max(nx.find_cliques(G), key=len))))
