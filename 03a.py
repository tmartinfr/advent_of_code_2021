lines = [line.strip() for line in open('03a_input').readlines()]
numlines = len(lines)
vstr = [''.join(s) for s in zip(*lines)]

gamma = [
    '1' if (len([b for b in s if b == '1']) > numlines / 2) else '0'
    for s in vstr
]
gamma = int(''.join(gamma), 2)

epsilon = [
    '1' if (len([b for b in s if b == '0']) > numlines / 2) else '0'
    for s in vstr
]
epsilon = int(''.join(epsilon), 2)

print(gamma * epsilon)

