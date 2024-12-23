text = '''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''
text = open('2024/data/input23.txt').read()
e = [row.split('-') for row in text.splitlines()]

from collections import defaultdict

edges = defaultdict(set)

for node1, node2 in e:
    edges[node1].add(node2)
    edges[node2].add(node1)


triplets = set()
for node1, neighbors in edges.items():
    for node2 in neighbors:
        for node in edges[node1] & edges[node2]:
            triplets.add(tuple(sorted([node1, node2, node])))

tc = 0
for t in triplets:
    for n in t:
        if n.startswith('t'):
            tc += 1
            break
        

print(tc)

def bron_kerbosch(graph, R, P, X, cliques):
    if not P and not X:
        # Found a maximal clique
        cliques.append(R)
        return
    # Choose a pivot to reduce recursive calls
    pivot = max(P | X, key=lambda node: len(graph[node]))
    for v in P - graph[pivot]:
        bron_kerbosch(
            graph,
            R | {v},
            P & graph[v],
            X & graph[v],
            cliques
        )
        P.remove(v)
        X.add(v)

cliques = []
bron_kerbosch(edges, set(), set(edges.keys()), set(), cliques)

max_clique = max(cliques, key=len) 

print(",".join(sorted(max_clique)))