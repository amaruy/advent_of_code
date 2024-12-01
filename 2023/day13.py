text="""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

patterns = text.split('\n\n')


total = 0
for pattern in patterns:
    pattern = pattern.splitlines()
    m, n = len(pattern), len(pattern[0])
    for i in range(1, m-1):
        size = min(i, m-i) 
        for j in range(1, size+1): # grow reflection
            if pattern[i - j] != pattern[i+j]:
                break

    # check rows
    # check cols