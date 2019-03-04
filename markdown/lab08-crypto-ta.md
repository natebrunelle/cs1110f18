---
title: "Lab 8: Crypto"
...


# Review Office Hours

It appears that many students don't know about office hours.
Start by reviewing how the OH link on the homepage works.


# Purpose of this lab

This lab has three goals

1.	Help them see cases where both `for element in thing:`{.python} and `for i in range(len(thing)):`{.python} are useful
2.	Have them write simple loops
3.	Provide an introduction to an important topic that we won't get to in lecture

# Pairing + Approach

If necessary in your lab, remind the students about good pairing:

1.	Two minds, one focus -- they should be working together
2.	Diver + Navigator roles, swapped from time to time

Also remind them that if you can't do something on paper, you can't tell the computer how to do it either.
Always start working off of the computer.

# Overview

Help them understand the example code on the student view of the lab:

````python
def encrypt_chunk(chunk, key):
    ...
    return transformed_version_of_chunk


def encrypt(plain_text, key):
    cipher_text = '' # accumulator pattern: start with no encrypted test
    for i in range(0, len(plain_text), chunk_size): # look one chunk at a time
        chunk = plain_text[i:i+chunk_size]          # all chunks the same size
        cipher_text += encrypt_chunk(chunk, key)    # the real work is in another function
    return cipher_text
````

Discuss how this works, and then show them a pair-swap encryption:

````python
def pair_swap_chunk(chunk):
    """Swaps the order of letters in a 2-letter string"""
    if len(chunk) < 2:
    	return chunk
    return chunk[1] + chunk[0]


def pair_swap(text):
    ans = ''
    for i in range(0, len(text), 2):
        chunk = text[i:i+2]
        ans += pair_swap_chunk(chunk)
    return ans
````

(see also this [pre-populated PythonTutor instance](https://goo.gl/VnwXGH))

Pair swap does not need a key, and it is its own inverse.
Other ciphers in this lab are more complicated...

# Contextualize

There's a reason we said "Code up at least two of the following ciphers."
Programming all 6 is unlikely to be doable by most pairs.
Depending on which one you start with, even doing 2 might be out of scope for lab.

Point out the Application section and encourage them to try it out after getting a cipher implemented.

# Example Solutions

## Character to/from Integer

There are other ways, but by far the easiest (and also showing how to use some collections methods) is

````python
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(letter)
letter = alphabet[index % len(alphabet)]
````
## Shift

Here's a version that uses alphabet-based indices, with cases, in a separate function:

````python
def shift(c, key):
    l = c.lower()
    n = alphabet.find(l)
    if n < 0: return c
    l2 = alphabet[(n+key)%26]
    if l == c: return l2
    return l2.upper()
    
def encrypt_shift(text, key):
    ans = ''
    for c in text:
        ans += shift(c, key)
    return ans

def decrypt_shift(text, key):
    return encrypt_shift(text, 26-key)
````


## Vignère

Re-using the `shift` function from the Shift cipher...

````python
def encrypt_vignere(text, key):
    ans = ''
    for i in range(len(text)):
        ans += shift(text[i], alphabet.find(key[i%len(key)]))
    return ans

def decrypt_vignere(text, key):
    ans = ''
    for i in range(len(text)):
        ans += shift(text[i], 26-alphabet.find(key[i%len(key)]))
    return ans
````

This can also be done by chunks instead of character-by-character.

## Autokey

This solution uses things we've never taught, like inline `if` expressions...

````python
def encrypt_autokey(text, key):
    ans = ''
    for i in range(len(text)):
        ans += shift(text[i], alphabet.find(key[i] if i < len(key) else text[i-len(key)]))
    return ans

def decrypt_autokey(text, key):
    ans = ''
    for i in range(len(text)):
        ans += shift(text[i], 26-alphabet.find(key[i] if i < len(key) else ans[i-len(key)]))
    return ans
````

## Ubbi Dubbi

Note that the decryption function is not much like the encryption...

````
def encrypt_ubbi(text):
    ans = ''
    for c in text:
        if c in 'aeiouAEIOU':
            ans += 'ub'
        ans += c
    return ans

def decrypt_ubbi(text):
    ans = ''
    i = 0
    while i < len(text):
        if text[i:i+2] == 'ub':
            ans += text[i+2]
            i += 3
        else:
            ans += text[i]
            i += 1
    return ans
````


## Permutation

This cipher begs by-chunk solution:

````
def encrypt_perm(text, key):
    text += ' '*(len(text) - (len(text)//len(key))*len(key))
    ans = ''
    for i in range(0, len(text), len(key)):
        chunk = text[i:i+len(key)]
        for j in key:
            ans += chunk[j]
    return ans

def decrypt_perm(text, key):
    inv = [0]*len(key)
    for i in range(len(key)):
        inv[key[i]] = i
    print(key, inv)
    return encrypt_perm(text, inv)
````

## Zombie

There's no pretty way to do this one...

````python
def encrypt_zombie(text):
    ans = ''
    for c in text.lower():
        i = alphabet.find(c)
        if i < 0: ans += c
        else: ans += 'bghmnz'[i%6] + ['', 'r', 'a', 'ra'][i//6]
    return ans

def decrypt_zombie(text):
    ans = ''
    i = 0
    while i < len(text):
        c = 'bghmnz'.find(text[i])
        if c < 0:
            ans += text[i]
            i += 1
            continue
        elif text[i+1:i+3] == 'ra': 
            c += 18
            i += 3
        elif text[i+1:i+2] == 'a': 
            c += 12
            i += 2
        elif text[i+1:i+2] == 'r': 
            c += 6
            i += 2
        else: 
            i += 1
        ans += 'abcdefghijkmnopqrstuvwyz'[c]
    return ans
````
