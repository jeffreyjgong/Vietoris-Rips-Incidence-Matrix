n = int(input("Please enter n (the number of vertices on S1):\n"))
print(f'You entered {n}')
k = int(input("Please enter k (the number of connections on S1):\n"))
print(f'You entered {k}')
print(f'Here is the incidence matrix for {n} vertices on S1 with the {k}-th connection')

#n = 14 number of points on S1
#k = 6 number of connections (0 would be wedge of 0-spheres)


i_matrix = [[1]*n for i in range(n)]
for x in range(0,n):
  i_matrix[x][x] = 0

modmin = k+1
modmax = n-k

for a in range(0,n):
  for b in range(modmin, modmax):
    i_matrix[a][(a+b)%n] = 0

print(i_matrix)
