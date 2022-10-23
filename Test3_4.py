#NE PAS MODIFIER LES FONCTIONS
#JUSTE LES VALEURS EN BAS SOUS LE if __name__ == '__main__':

#NE PAS VALIDER LES REPONSES EN 1 MINUTE SUR LE MOODLE ON VA ETRE GRILLER


#JE NE GARANTIS PAS LE 100% DE REUSSITE ET JE SUIS EN AUCUN CAS RESPONSABLE DE VOTRE ECHEC
#SI VOUS ETES PAS CONTENT APPRENEZ LE COURS ET FAITES LE POUR DE VRAI !
#CA MARCHE PAS FORCEMENT REGARDEZ LE SUJET
from math import exp
from math import log

def ex1(i,r1,r2,l,i2):
    eth = i*r1
    req=r1+r2
    q2= eth/req
    print(f'Q2 : {q2}')
    q3=(l)/req
    print(f'Q3 : {q3}')
    q4=q2
    print(f'Q4 : {q4}')
    q5=(1-exp(-1/2))*(eth/req)
    print(f'Q5 : {q5}')
    q6=-q3*(log(((-i2*req)/eth)+1))
    print(f'Q6 : {q6}')


def ex2(e,r1,r2,c,uc1,uc2):

    q7= (r1*c)/1000
    print(f'Q7 : {q7} ')
    q8=-q7*log((uc2-e)/(uc1-e))
    print(f'Q8 : {q8}')
    q9=(uc1-e)*exp(-q8/(2*q7))+e
    print(f'Q9 : {q9}')
    q10=(r2*c)/1000
    print(f'Q10 : {q10}')
    q11=-q10*log(uc1/uc2)+q8
    print(f'Q11 : {q11}')
    t2 = -(q11-q8)/2
    q12=uc2*exp(t2/q10)
    print(f'Q12 : {q12}')



if __name__ == '__main__':
    #Mettre les valeurs dans les mêmes unités que proposer par exemple
    # pour 11.4mH -> écrire 11.4
    #SI CHIFFRE A VIRGULE C'EST UN POINT A METTRE !!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Pour l'exo 1 mettre aussi I2 (valeur demandé en Q6 elle peut peut être varier)


    #ex1(I en A,R1 en ohm ,R2 en ohm,L en mH, I2 (Q6) en A )

    #ATTENTION AUX UNITES QUE JE DEMANDE
    #la réponse est toujours donnée dans l'unité demandé ex q7 en ms
    #ex2(E en V,r1 en kohm,r2 en kohm ,c en nF,uc1 en V,uc2 en V)
    ex2(12,1.2,2.7,575,2.6,8.4)