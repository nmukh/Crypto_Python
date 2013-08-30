# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 17:44:29 2013

@author: nmukh
"""
from numpy import *
from numpy.linalg import det
from numpy.linalg import inv   
from numpy.random import *

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sentence = 'Some random, thxat! sentence here or theres.'
blocks = 2

def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b
 
 
def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1
    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime       
    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def hill():
    A = random_integers(-10,10,(blocks,blocks))
    determinant = int(round(det(A),0))%26
    print determinant
    while (gcd(determinant,len(LETTERS))!=1):
        A = random_integers(-10,10,(blocks,blocks))
        determinant = int(round(det(A),0))%26
    return A

def adj(A):
    return array([[A[1][1],-1*A[0][1]],[-1*A[1][0],A[0][0]]])

A = hill()
d = int(round(det(A),0))%26
d_inv = findModInverse(d,26)
A_inv = adj(A)*d_inv

def chunk(sentence):
    sentence = sentence.upper()
    lettersOnly = []
    for symbol in sentence:
        if symbol in LETTERS:
            lettersOnly.append(symbol)
    string = ''.join(lettersOnly)
    if (len(string)%blocks)!=0:
        string = string +(len(string)%blocks)*'X'
    string = array(map(LETTERS.find,string))
    nums = string.reshape(len(string)/blocks,2,1)
    return nums
    #return [string[i:i+blocks] for i in range(0, len(string), blocks)]
    
def encode(sentence):
    translated = ''
    encoded_list = []
    for obj in chunk(sentence):
        encoded = dot(A, obj) % len(LETTERS)
        encoded_list.append(encoded.tolist())
    coded = [item for sublist in encoded_list for item in sublist for item in item]
    for number in coded:
        translated+=LETTERS[number]
    return translated
    
def decode(sentence):
    translated=''
    decoded_list=[]
    for obj in chunk(sentence):
        decoded = dot(A_inv, obj) % len(LETTERS)
        decoded_list.append(decoded.tolist())
    uncoded = [item for sublist in decoded_list for item in sublist for item in item]
    for number in uncoded:
        translated+=LETTERS[number]
    return translated

       


