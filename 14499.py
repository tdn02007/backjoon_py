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

while(n_c < ncommand):
	for c in command:
		if c == 1:
			if x + 1 > M:
				continue
			if MAP[x+1][y] == 0:
				MAP[x+1][y] = east
				east = 0
			else:
				east = MAP[x+1][y]
				MAP[x+1][y] = 0
			temp = top
			top = western
			western = bottom
			bottom = east
			east = temp
			result.append(top)
			n_c += 1
			
		elif c == 2:
			if x - 1 < 0:
				continue
			if MAP[x-1][y] == 0:
				MAP[x-1][y] = western
				western = 0
			else:
				western = MAP[x-1][y]
				MAP[x-1][y] = 0
			temp = top
			top = east
			east = bottom
			bottom = western
			western = temp
			result.append(top)
			n_c += 1
		
		elif c == 3:
			if y - 1 < 0:
				continue
			if MAP[x][y-1] == 0:
				MAP[x][y-1] = north
				north = 0
			else:
				north = MAP[x][y-1]
				MAP[x][y-1] = 0
			temp = top
			top = south
			south = bottom
			bottom = north
			north = temp
			result.append(top)
			n_c += 1
		
		else:
			if y + 1 > N:
				continue
			if MAP[x][y+1] == 0:
				MAP[x][y+1] = south
				south = 0
			else:
				south = MAP[x][y+1]
				MAP[x][y+1] = 0
			temp = top
			top = north
			north = bottom
			bottom = south
			south = temp
			result.append(top)
			n_c += 1
			
for r in result:
	print(r)