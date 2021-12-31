# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:19:33 2021

@author: ameya
"""


def caesar_cipher(t,r):
    A="abcdefghijklmnopqrstuvwxyz"
    yc=''
    for i in range(len(t)):
        if not t[i].isalpha():yc+=t[i]
        else:
            j=0
            while t[i].lower()!=A[j]:
                j+=1
            if j + r > 25: k=j+r-26
            else: k = j+r
            if t[i].isupper(): yc+= A[k].upper()
            else:  yc+=A[k]
    return yc

def correct_caesar_cipher(s):
    M=[]
    N=[]
    m1=['a','e','i','o','u']
    
    for i4 in range(26):
        y=caesar_cipher(s,i4)
        w1=y.replace('.',' ').replace(',',' ').replace('?',' ')           
        z=w1.split()
        if '' in z:
            z.remove('')
        q=0
        
        for t1 in z:
            if len(t1)==1 and t1 in ['a','I']:
                q+=10
                
            if len(t1)==2:
                q2=['is','am','up','in', 'an', 'on','it','hi','by']
                if t1 in q2:
                    q+=20
          
            if len(t1)==3:
                t2=list(t1.lower())
                j=0
                for z1 in t2:
                    if z1 in m1:
                        j+=1
                if j==1:
                    q+=15
                if j==2:
                    q+=30
                                                               
            if len(t1)==4:
                t4=list(t1.lower())
                j7=0
                for z3 in t4:
                    if z3 in m1:
                        j7+=1
                if j7==2:
                    q+=40
    
            if len(t1)==5:
                t5=list(t1.lower())
                j2=0
                for z5 in t5:
                    if z5 in m1:
                        j2+=1
                if j2==3:
                    q+=50
                        
        M.append(i4)
        N.append(q)
    c3=M[N.index(max(N))]
    return caesar_cipher(s,c3)
    

print(correct_caesar_cipher("Lm,evi csy xlivi?"))
print(correct_caesar_cipher("Ohcl h upjl khf"))
print(correct_caesar_cipher("Szap jzf slo l ytnp etxp"))    
  


