import numpy as np
from colorama import Fore, Style

def red_text(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

def d(a,b):
    """distance élémentaire"""
    if a != b:
        return 1
    else : 
        return 0

def dist(a,b):
    a = "  " + a  # l'algorithme a un prolème pour les deux premiers caractères par la forme même de matrice
    b = "  " + b
    tiret = "-"
    l = len(a)
    m = len(b)
    F = np.zeros((l,m))
    for i in range(0,l):
        F[i,0] = i
    for j in range(0,m):
        F[0,j] = j
    for i in range(1,l):
        for j in range(1,m):
            F[i, j] = min(F[i-1, j-1] + d(a[i],b[j]), F[i-1, j] + 1, F[i, j-1] + 1)
            
    AlignmentA = ""
    AlignmentB = ""
    i = l - 1
    j = m - 1
    while (i > 0 and j > 0):
        Score = F[i, j]
        ScoreDiag = F[i - 1, j - 1]
        ScoreUp = F[i - 1, j]
        ScoreLeft = F[i, j - 1]
        if (Score == ScoreDiag + d(a[i],b[j])):
            if a[i] != b[j]:
                AlignmentA = red_text(a[i]) + AlignmentA
                AlignmentB = red_text(b[j]) + AlignmentB
            else:
                AlignmentA = a[i] + AlignmentA
                AlignmentB = b[j] + AlignmentB
            i = i - 1
            j = j - 1
        elif (Score == ScoreUp + 1):
            AlignmentA = a[i] + AlignmentA
            AlignmentB = red_text(tiret) + AlignmentB
            i = i - 1
            
        elif (Score == ScoreLeft + 1):
            AlignmentA = red_text(tiret) + AlignmentA
            AlignmentB = b[j] + AlignmentB
            j = j - 1
            
 
    while (i >= 0 and j >= 0):
        if a[i] != b[j]:
            AlignmentA = red_text(a[i]) + AlignmentA
            AlignmentB = red_text(b[j]) + AlignmentB
        else:
            AlignmentA = a[i] + AlignmentA
            AlignmentB = b[j] + AlignmentB
        i = i - 1
        j = j - 1
        
    if i >= 0:
        while i >= 0:
            AlignmentA = red_text(a[i]) + AlignmentA
            AlignmentB = red_text(tiret) + AlignmentB
            i = i - 1
    elif j >= 0:
        while j >= 0:
            AlignmentA = red_text(tiret) + AlignmentA
            AlignmentB = red_text(b[j]) + AlignmentB
            j = j - 1
    
    
    return ([F[l-1,m-1], AlignmentA[2:], AlignmentB[2:]])
   
    
    
class Ruler:
    
    def __init__(self, a : str, b : str):
        self.a = a
        self.b = b
        
    def compute(self):
        self.distance = dist(self.a, self.b)[0] 
        
    def report(self):
        return (dist(self.a, self.b)[1], dist(self.a, self.b)[2])

        

    
    