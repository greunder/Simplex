# =============================================================================
# Nom du fichier : SIMPLEX_PROJET_MARIETTE_Rayan.py
# Auteur : MARIETTE Rayan
# Année : 2021-2022
# Classe : ITS2
# Sujet : Methode Simplexe ' Linear Programming'
# Professeur : Thiago ABREU
# =============================================================================

import numpy as np
import warnings
from IHM_SIMPLEX_MARIETTE_Rayan.py import button_click

button_click()

def Fonction_Simplex(type, A, B, C, D, M):
    
    (m, n)= A.shape	#m = |Contraintes| , n = |variables|

    fZ = ''
    for j in range(0,n):
        fZ += '+'+str(C[j][0]) if (C[j][0])>0 else str(C[j][0]) 
        fZ += 'x'+str(j) + ' '
    print(' Fonction Objective: Z =',fZ)

    print(' Contraintes:', m)
    contrainte_ = ''
    for j in range (0, m):
        contrainte_ = ''
        Ri = '  C'+str(j+1)+':'
        for k in range (0,n):
            const = '+'+str(A[j][k]) if A[j][k] > 0  else str(A[j][k])
            contrainte_ += const+'x'+str(k)+' '
        contrainte_ += D[j][0] + str(B[j][0])
        print(Ri,contrainte_)

    Variables_basique = []
    
    
    Compteur = n
    

    #Matrice avec de nouvelles variables
    R = np.eye(m)

    Btemp = B

    tab= []	

    for i in range(m):
        if D[i] == '<=':	
            C = np.vstack((C, [[0]]))

            Compteur = Compteur + 1
            Variables_basique = Variables_basique + [Compteur-1]

            tab = [tab, 0]

        elif D[i] == '=':
            if type == 'min':
                C = np.vstack((C, [[M]]))
            else:
                C = np.vstack((C, [[-M]]))

            # colocar a var tab como basica
            Compteur = Compteur + 1
            Variables_basique = Variables_basique + [Compteur-1]

            tab = [tab, 1]
        elif D[i] == '>=':  # >=
         
            if type == 'min':
                C = np.vstack((C, [[0], [M]]))
            else:
                C = np.vstack((C, [[0], [-M]]))

            R = repeatColumnNegative(R, Compteur + 1 - n)
            Btemp = Col_to_col(Btemp, Compteur + 1 - n)

        
            Compteur = Compteur + 2
            Variables_basique = Variables_basique + [Compteur-1]

            tab = [tab, 0, 1]
      

    X = np.vstack((np.zeros((n, 1)), Btemp))

    A = np.hstack((A, R))
 
    st = np.vstack((np.hstack((-np.transpose(C), np.array([[0]]))), np.hstack((A, B))))

    (lignes, colonne) = st.shape

    # Variables_basique = ((n + 1):n+m)'

    z_optimal = np.matmul(np.transpose(C), X)
    print("\n",X)

    if z_optimal != 0:
        for i in range(m):
            if D[i] == '=' or D[i] == '>=':
                if type == 'min':
                    st[0,:]= st[0,:] + M * st[1+i,:]
                else:
                    st[0,:]= st[0,:] - M * st[1+i,:]


        print(st)

    iteration = 0
    while True:
        if type == 'min':
            w = np.amax(st[0, 0:colonne-1])
            iw = np.argmax(st[0, 0:colonne-1])
        else:
            w = np.amin(st[0, 0:colonne-1])
            iw = np.argmin(st[0, 0:colonne-1])

        if w <= 0 and type == 'min':
            break
        elif w >= 0 and type == 'max':
            break
        else:
            iteration = iteration + 1

         
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                
                b_ = st[1:lignes, colonne-1] 
                Colonne_Pivot = st[1: lignes, iw]
      
                tab1 = []
                for i in range(len(Colonne_Pivot)):
                    #print('Colonne_Pivot', i, '->', Colonne_Pivot[i])
                    if(Colonne_Pivot[i]) <=0:
                        tab1.append(np.inf)
                    else:
                        tab1.append(b_[i]/Colonne_Pivot[i])
                T = np.array(tab1)
            
            R = np.logical_and(T != np.inf, T >= 0)
            
            (k, ik) = minBlandWithMask(T, R)
            #print('k = ', k, ' ik =', ik)

            # Nouveau pivot
            Z_ = st[[0],:]

            pivot = st[ik+1, iw]

            # Ligne du pivot divisé par le pviot
            Ligne_pivot = st[ik+1,:] / pivot
            st = st - st[:, [iw]] * Ligne_pivot

            # Cas spécial
            st[ik+1,:]= Ligne_pivot

            # Nouvelle variable basique
            Variables_basique[ik] = iw

            print('\n', Variables_basique)

            basic = st[:, colonne-1]
            X = np.zeros((Compteur, 1))
            t = np.size(Variables_basique)

            for k in range(t):
                X[Variables_basique[k]] = basic[k+1]

            print(X)

            C = -np.transpose(Z_[[0], 0:Compteur])

            z_optimal = Z_[0, colonne-1] + np.matmul(np.transpose(C), X)
            st[0, colonne-1] = z_optimal
            print(z_optimal)


    t = np.size(tab)
    for i in range(t):
        if tab[i] == 1:
            if X[n + i] > 0:
                break

    return (z_optimal[0, 0], X)


def minBlandWithMask(x, mask):
    
    min = 0
    imin = 0

    n = np.size(x)

    for i in reversed(range(n)):
        if mask[i] == 1:
            if min == 0:
                min = x[i]
                imin = i
            else:
                if min > x[i]:
                    min = x[i]
                    imin = i
    return (min, imin)


def repeatColumnNegative(Mat, h):
    (r, c) = Mat.shape
    Mat = np.hstack((Mat[:, 0:h-1], -Mat[:, [h-1]], Mat[:, h-1:c]))

    return Mat


def Col_to_col(col, h):
    kpos = np.size(col)
    col = np.vstack((col[0:h-1, [0]], np.array([[0]]), col[h-1:kpos, [0]]))

    return col

if __name__ == '__main__':
    np.set_printoptions(suppress=True)#Maximisation ou Minimisation
    (z, x) = Fonction_Simplex('max', np.array([[1, 1, -2, 0], [0, 0, 1, 1], [1, 0,1, 0] , [0, 1,0, 1]]), #A,B,C,D
                            np.array([[200], [300], [400], [300]]),  #S                                          #b_
                            np.array([[30], [36], [25], [30]]),   # Fonction Objective Z                           
                            np.array([['='], ['='], ['<='], ['<=']]),  #Signe 
                  0)         

