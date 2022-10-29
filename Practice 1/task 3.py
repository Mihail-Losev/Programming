line, row_count = input().split()
row_count = int(row_count)

interval = row_count - 2
z_count = (len(line) // (row_count + interval)) + 1
z_len = row_count + interval
z_diff = interval
'''for r in range(row_count):
    for z in range(r, z_count * row_count + 1, row_count + interval):
        print(line[z], end='')
        if 0 < r < row_count - 1:
            print(line[z + z_diff], end='')
    z_diff -= 1'''

matr = [line[i:i+z_len] for i in range(0, len(line), z_len)]
matr[-1] += ' ' * (z_len - len(matr[-1]))
s_res = ''
for i in range(len(matr)):
    s_res += matr[i][0]

for j in range(1, len(matr[0]) // 2):
    for i in range(len(matr) - 1):
        s_res += matr[i][j] + matr[i][z_len - j]
for i in range(len(matr)):
    s_res += matr[i][z_len // 2]
print(s_res)

