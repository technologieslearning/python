# -*- coding: utf-8 -*-
nombre_bonne_reponse = 0
nombre_mauvaise_reponse = 0

liste_mauvaise_reponse = [[],[],[]]
question = ["q1","q2","q3"]
reponse = ["r1","r2","r3"]

def quizz(question, reponse, numero):
    r = input(question)
    while r != reponse:
        liste_mauvaise_reponse[numero].append(r)
        print("Dommage, ce n'est pas la bonne réponse, réessayer encore")    
        r = input(question)
    if r == reponse:
        return False
    return True

for i in range(3):
    while quizz(question[i],reponse[i],i):
        quizz(question[i],reponse[i],i)

print("mauvaise reponse : ",liste_mauvaise_reponse)
print("bravo !")