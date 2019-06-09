# SMITH WATERMAN


from prettytable import PrettyTable

# creer la matrice
u = input("Entrez le premier mot : ")
u_len = len(u)
v = input("Entrez le deuxieme mot : ")
v_len = len(v)

# initialisation de la matrice
mat = [[0]*(u_len+1) for i in range(v_len+1)]

# define score and penalities
score_match = int(input("Score match:"))
score_mismatch = int(input("Score mismatch:"))
penal_ext = int(input("Penalite exterieur :"))


# remplire la matrice

for i in range(0, v_len):
    for j in range(0, u_len):
        if u[j] == v[i]:
            mat[i + 1][j + 1] = max(mat[i][j] + score_match, mat[i][j + 1] + penal_ext, mat[i + 1][j] + penal_ext)
        else:
            mat[i + 1][j + 1] = max(mat[i][j] + score_mismatch, mat[i][j + 1] + penal_ext, mat[i + 1][j] + penal_ext)

# exemple du cour u=gtcaggt, v=cagttag

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
