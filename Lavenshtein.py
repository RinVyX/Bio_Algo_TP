# LAVENSHTEIN

# linux : sudo pip3 install PTable
# windows : pip install PTable
from prettytable import PrettyTable


#creer la matrice
u = input("Entrez le premier mot : ")
u_len = len(u)
v = input("Entrez le deuxieme mot : ")
v_len = len(v)


mat = [[0]*(u_len+1) for i in range(v_len+1)]

#initialisation de la matrice
for i in range(0, u_len+1):
    mat[0][i] = i
for j in range(0, v_len+1):
    mat[j][0] = j


for i in range(1, v_len+1):
    for j in range(1, u_len+1):
        if u[j-1] == v[i-1]:
            mat[i][j] = min(mat[i-1][j-1], mat[i-1][j] + 1, mat[i][j-1] + 1)
        else:
            mat[i][j] = min(mat[i-1][j-1] + 1, mat[i-1][j] + 1, mat[i][j-1] + 1)

# Affichage de la matrice avec score
x = PrettyTable()

column_names = ['']
for i in range(0, u_len):
    column_names.append(u[i])

row_names = ['']
for i in range(0, v_len):
    row_names.append(v[i])

x.add_column('', column_names)
for i in range(0, v_len+1):
    x.add_column(row_names[i], mat[i])

print(x)

print("Score matrice[n][m]= ", mat[v_len][u_len])
