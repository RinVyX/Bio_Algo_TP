# WUNCH NEEDLEMAN


from prettytable import PrettyTable

# exemple u="gtcaggt"
# v="cagttag"


# creer la matrice
u = input("Entrez le premier mot : ")
u_len = len(u)
v = input("Entrez le deuxieme mot : ")
v_len = len(v)


mat = [[0]*(u_len+1) for i in range(v_len+1)]


# definir les scores et indel
score_match = int(input("Donnez le score match : "))
score_mismatch = int(input("Donnez le score mismatch : "))
indel = int(input("Donnez l'indel : "))

# remplissage de la matrice
for i in range(1, u_len+1):
    mat[0][i] = mat[0][i-1] + indel
for j in range(1, v_len+1):
    mat[j][0] = mat[j-1][0] + indel

for i in range(0, v_len):
    for j in range(0, u_len):
        if u[j] == v[i]:
            mat[i + 1][j + 1] = max(mat[i][j] + score_match, mat[i][j + 1] + indel, mat[i + 1][j] + indel)
        else:
            mat[i + 1][j + 1] = max(mat[i][j] + score_mismatch, mat[i][j + 1] + indel, mat[i + 1][j] + indel)


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
