from itertools import permutations, combinations

erres = ['R', 'r', '*r*']
aes = ['A', 'a']

for r_positions in combinations(range(5), 3):
    for r in permutations(erres):
        for a in permutations(aes):
            permutacion = [None] * 5

            permutacion[r_positions[0]] = r[0]
            permutacion[r_positions[1]] = r[1]
            permutacion[r_positions[2]] = r[2]

            a_positions = [i for i in range(5) if i not in r_positions]

            permutacion[a_positions[0]] = a[0]
            permutacion[a_positions[1]] = a[1]

            print("".join(permutacion))