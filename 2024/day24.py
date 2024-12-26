text = open('2024/data/input24.txt').read()

AND = 'AND'
XOR = 'XOR'
OR = 'OR'

state, gates = text.split('\n\n')

state = [row.split(': ') for row in state.splitlines()]
state = {char:int(val) for char, val in state}

gates = [gate.split(' -> ') for gate in gates.splitlines()]


n = len(state) // 2
final = f'z45'

mixxed = set()
for exp, res in gates:
    a, op, b = exp.split(' ')

    if res.startswith('z') and op != XOR and res != final:
        mixxed.add(res)
    elif op == XOR and all(c not in exp+res for c in 'xyz'): 
        mixxed.add(res)

    elif op == AND and 'x00' not in exp:
        if any(res in sexp and OR not in sexp for sexp, _ in gates):
            mixxed.add(res)
            
    elif op == XOR and any(res in sexp and 'O' == sexp[4] for sexp, _ in gates):
        mixxed.add(res) 


gates = {res:exp for exp, res in gates}
def calculate(value):
    if value in state:
        return state[value]
    
    expression = gates[value]
    del gates[value]
    a, op, b = expression.split(' ')

    if value.startswith('z') and op != XOR and value != final:
        mixxed.add(value)

    if a not in state:
        calculate(a)
    if b not in state:
        calculate(b)
    
    a = state[a]
    b = state[b]

    if op == 'AND': state[value] = a & b
    elif op == 'OR': state[value] = a | b
    else: state[value] = a ^ b
    
    return state[value]

z = sorted([k for k in gates if k.startswith('z')], reverse=True)

sol = int("".join(map(str, map(calculate, z))), base=2)

print(sol)
print(','.join(sorted(mixxed)))





