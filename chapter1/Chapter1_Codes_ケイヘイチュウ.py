# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:46:08 2022

@author: ケイ　ヘイチュウ
"""
import urllib.request as ur
import random

# 00. Reversed string
Reversed_str="stressed"
Reversed_str_list=list(Reversed_str)
flag=True
index=0
while flag:
    imp=Reversed_str_list[index]
    Reversed_str_list[index]=Reversed_str_list[(len(Reversed_str)-index-1)]
    Reversed_str_list[len(Reversed_str)-index-1]=imp
    index=index+1
    if index ==len(Reversed_str)/2:
        break
Reversed_str=''.join(Reversed_str_list)
print(Reversed_str)

'''
#The standard solution of 00.Reversed string.

str="stressed"
new_str=str[::-1]
print(new_str)
'''

#01."パタトクカシーー"
str="パタトクカシーー"
str2=""
for i in range(len(str)):
    if i%2==0:
        str2=str2+str[i]
print(str2) 

'''
#The standard solution of 01."パタトクカシーー".
s = 'パタトクカシーー'
print (s[::2])  
'''

#02."パトカー" + "タクシー" = "パタトクカシーー"
str="パトカー"
str2="タクシー"
new_str=""
if len(str)==len(str2):
    for i in range(len(str)):
        new_str=new_str+str[i]
        new_str=new_str+str2[i]
if len(str)<len(str2):
    for i in range(len(str)):
        new_str=new_str+str[i]
        new_str=new_str+str2[i]
    for i in range(len(str),len(str2)):
        new_str=new_str+str2[i] 
if len(str)>len(str2):
    for i in range(len(str2)):
        new_str=new_str+str[i]
        new_str=new_str+str2[i]
    for i in range(len(str2),len(str)):
        new_str=new_str+str[i] 
print(new_str)
       
'''
#The standard solution of 01."パタトクカシーー".
text1="パトカー"
text2="タクシー"
new_text=[s1+s2 for s1,s2 in zip(text1,text2)]
new_text="".join(new_text)
print(new_text)
'''


PI="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
normalized_str=PI.replace(",", "").replace(".", "")
words=normalized_str.split(" ")
print(words)
pi_list = [len(w) for w in words]
print(pi_list)

'''
txt = "Google#Runoob#Taobao#Facebook"
x = txt.split("#", 5)
print(x)
'''  

Element="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
normalized_str=Element.replace(",", "").replace(".", "")
words=normalized_str.split(" ")

Map_char=[1,5,6,7,8,9,15,16,10]

Element_result={}

for i,word in  enumerate(words):
     if i+1 in Map_char:
         Element_result[i]=word[0]
     else:
         Element_result[i]=word[:2]
print(Element_result) 


def ngram(S, n):
    r = []
    for i in range(len(S) - n + 1):
        r.append(S[i:i+n])#The process range is [i,i+n)
    return r
s = 'I am an NLPer'
print (ngram(s.split(),2))
print (ngram(s,2))


SetX=ngram('paraparaparadise',2)
SetX=set(SetX)
SetY=ngram('paragraph',2)
SetY=set(SetY)
Intersection_Set=SetX & SetY
print(Intersection_Set)
Union_Set=SetX.union(SetY)
print(Union_Set)
Difference_Set=SetX.difference(SetY)
print(Difference_Set)
print('se' in SetX)
print('se' in SetY)

'''
def sentence_generation(x,y,z):
    return   str(y) + ' is ' + str(x) + ' at ' + str(z)
print(sentence_generation(12, 'temperature', 22.4))
'''

def cipher(str):
    new = []
    for i in str:
        if 97 <= ord(i) <= 122:
           i = chr(219 - ord(i))
        new.append(i)
    return ''.join(new)

print(cipher(s))   
            
s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
ans = []
text = s.split()
for word in text:
    if (len(word)>4):
        mid = list(word[1:-1])
        random.shuffle(mid)
        word = word[0] + ''.join(mid) + word[-1]
        ans.append(word)
    else:
        ans.append(word)
print (' '.join(ans))
            
    

    
    
    
    
         

    
    
        
        
