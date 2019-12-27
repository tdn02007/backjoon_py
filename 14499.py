map_data = input().split()
N, M, x, y, ncommand = list(map(int, map_data))
top = 0
bottom = 0
western = 0
east = 0
north = 0
south = 0

MAP = []
for i in range(N):
    N_data = input().split()
    N_data = list(map(int, N_data))
    MAP.append(N_data)

command = input().split()
command = list(map(int, command))

result = []
n_c = 0

while n_c < ncommand:
    for c in command:
        if c == 1:
            if y + 1 < M:
                y = y + 1
                temp = top
                top = western
                western = bottom
                bottom = east
                east = temp
                if MAP[x][y] == 0:
                    MAP[x][y] = bottom
                else:
                    bottom = MAP[x][y]
                    MAP[x][y] = 0
                result.append(top)
            n_c += 1

        elif c == 2:
            if y - 1 >= 0:
                y = y - 1
                temp = top
                top = east
                east = bottom
                bottom = western
                western = temp
                if MAP[x][y] == 0:
                    MAP[x][y] = bottom
                else:
                    bottom = MAP[x][y]
                    MAP[x][y] = 0
                result.append(top)
            n_c += 1

        elif c == 3:
            if x - 1 >= 0:
                x = x - 1
                temp = top
                top = south
                south = bottom
                bottom = north
                north = temp
                if MAP[x][y] == 0:
                    MAP[x][y] = bottom
                else:
                    bottom = MAP[x][y]
                    MAP[x][y] = 0

                result.append(top)
            n_c += 1

        else:
            if x + 1 < N:
                x = x + 1
                temp = top
                top = north
                north = bottom
                bottom = south
                south = temp
                if MAP[x][y] == 0:
                    MAP[x][y] = bottom
                else:
                    bottom = MAP[x][y]
                    MAP[x][y] = 0
                result.append(top)
            n_c += 1

for r in result:
    print(r)
