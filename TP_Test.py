
def recherche_naive(m, t):
    len_n = len(t)
    len_m = len(m)
    i = 0
    while i < len_n - len_m + 1:
        j = 0
        while j < len_m and t[i + j] == m[j]:
            j = j + 1

        if j == len_m:
            return i
        i = i + 1

    return -1


def calcul_bords(m):
    len_m = len(m)
    bord = [-1]
    bord.extend([0] * len_m)
    i = -1
    for j in range(0, len_m - 1):
        while i >= 0 and m[i] != m[j]:
            i = bord[i]
        i = i + 1
        bord[j+1] = i

    return bord


def recherche_morris_prat_version1(m, t): #(Problème dans les résultats, je ne sais pas pourquoi)
    len_n = len(t)
    len_m = len(m)
    i = 0
    j = 0
    bord = calcul_bords(m)
    while i < len_n - len_m + 1 and j < len_m:
        if j >= 0 and t[i] != m[j]:
            j = bord[j]
        else:
            i = i + 1
            j = j + 1

    if j == len_m:
        return i - len_m
    else:
        return -1


def recherche_morris_prat_version2(m, t):
    len_n = len(t)
    len_m = len(m)
    i = 0
    j = 0
    bord = calcul_bords(m)
    while i < len_n - len_m + 1:
        while j < len_m and t[i + j] == m[j]:
            j = j + 1
        if j == len_m:
            return i
        i = i + j - bord[j]
        if bord[j] > 0:
            j = bord[j]
        else:
            j = 0

    return -1


def calcul_meilleur_bord(m):
    len_m = len(m)
    meilBord = [-1]
    meilBord.extend([0] * len_m)
    i = -1
    for j in range(0, len_m - 1):
        while i >= 0 and m[i] != m[j]:
            i = meilBord[i]
        i = i + 1
        if i == len_m - 1 or m[j+1] != m[i]:
            meilBord[j+1] = i
        else:
            meilBord[j+1] = meilBord[i]

    return meilBord


def prefixe_mot(m):
    len_m = len(m)
    prefixes = [0]; prefixes.extend([0] * (len_m-1))

    for i in range(0, len_m):
        prefixes[i] = m[0:i+1]

    return prefixes


def plus_long_prefixe(ch1, ch2):

    if len(ch1) > len(ch2):
        bigChaine = ch1
        littleChaine = ch2
    else:
        bigChaine = ch2
        littleChaine = ch1

    i = 1
    while littleChaine[0:i] in bigChaine[0:i]:
        i = i + 1
        if i >= len(littleChaine):
            break

    return littleChaine[0:i-1]


def suffixe_mot(m):
    len_m = len(m)
    suffixes = [0];
    suffixes.extend([0] * (len_m - 1))

    for i in range(0, len_m):
        suffixes[i] = m[-(i+1):len_m]

    return suffixes


def plus_long_suffixe(ch1, ch2):
    if len(ch1) > len(ch2):
        bigChaine = ch1
        littleChaine = ch2
    else:

        bigChaine = ch2
        littleChaine = ch1

    pluslongsuffixe = ''

    len_littleChaine = len(littleChaine)
    len_bigchaine = len(bigChaine)
    i = 0
    while littleChaine[-(i + 1):len_littleChaine] in bigChaine[-(i + 1):len_bigchaine]:
        pluslongsuffixe = littleChaine[-(i + 1):len_littleChaine]
        i = i + 1
        if i >= len_littleChaine:
            break

    return pluslongsuffixe


print(recherche_naive('a', 'ffffaaaaaa'))

print(recherche_morris_prat_version1('bbaa', 'aaabbababbaaba'))

print(recherche_morris_prat_version2('bbaa', 'aaabbababbaaba'))

print(prefixe_mot("cffffaaaaaad"))

print(plus_long_prefixe("aababba", "aabaaaabbaa"))

print(suffixe_mot("cffffaaaaaad"))

print("plus long suffixe entre : aababbada et aabaaaabbaada est : " + plus_long_suffixe("aababbada", "aabaaaabbaada"))
