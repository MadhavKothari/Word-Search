inp = 'input.txt' 
'''
The input data contains the matrix in which the words have to be searched for 
with each line in the text file being a row in the word matrix. The words that 
have to be searched for are also inculded after the matrix by leaving a single 
blank line between them. Each word to be searched for is in its own line.
'''

with open (inp,'r') as f: # takes the file and splits them into the word matrix and the words to search for
    table2 = [] # this will hold the word matrix
    words2 = [] # this will hold the words to search for
    flag = 0 # the matrix is seperated from the words by a \n, this flag keeps track of that
    for line in f:
        if line != '\n' and flag == 0: 
            table2.append(line.strip('\n').split()) # Each element in this will be one row from the word matrix
        elif line == '\n': # flags when the new line appears
            flag += 1 
        elif line != '\n' and flag != 0: 
            words2.append(line.strip('\n')) # after the flag the new lines will be added to this list, each element is a word to search for


tab = table2 # reassigned variable cause to lazt to change the variable names in the rest of the code
wrd = words2
i = 0 # controls the row
j = 0 # controls the coloumn
pos = {} # this will hold the starting position of all the words being searched in the matrix
for w in wrd: #this assigns a default value to each word to [-1,-1]. Any word not found in the matrix will remain as [-1,-1]
    pos[w] = [-1,-1]
'''
This code will go over the entire matix only once letter by letter, at each letter 
it goes over all the words and if it matches the first letter of any word it goes 
for further analysis to see if the whole word is present.
'''
while i < len(tab): # loop that controls the rows
    j = 0 
    while j < len(tab[0]): # loop the controls the coloumns
        for w in wrd:  # this will go over all the words being search for at each position of the matrix           
            if w[0] == tab[i][j] and pos[w] == [-1,-1]: # if the first letter matches, and that the word hasnt been found already, this will check all 8 directions from that position
                pos[w] = [i,j] #saves the  current position 
                ti = i #takes the current row number to be modified
                tj = j #takes the current coloumn number to be modified
                tv = -1 # a flag for to check for the direction being checked for (To identify the direction the flag represents, t - temp, h - horizontal, v - vertical, d - diagonal top left to bottom right, d2 - diagonal top right to bottom left, r - reverse direction )
                t = 1 # temporary value to iterate over the word being searched for
                '''
                In each of the following loops, all the 8 directions are checked. 
                before each loop the t value is reset to 1 to go over the word being 
                checked for again. If a mismatch between the letter in the matrix and 
                the word being searched for occurs, the direction loop will break and 
                reset the value of the temp flag to -1. If t matches the word length 
                and the loop hasnt broken yet, the value of the temp flag will be changed.
                '''
                while t < len(w) and pos[w] != [-1,-1] and ti < len(tab)-1: # the condition on ti is to prevent the index out of range eror from occuring. If the loop would extend to the top or left edge of the word matrix, the condition is the temp value > 0
                    ti += 1
                    if w[t] != tab[ti][tj]:
                        tv = -1
                        break
                    elif w[t] == tab[ti][tj] and t == len(w)-1: # as t is controlling the index of the word being searched for it starts from 0, hence the len(w) - 1
                        tv = t
                    t+=1 # iterates over the word
                
                ti = i
                tj = j
                trv = -1
                t = 1
                while t < len(w) and pos[w] != [-1,-1] and ti > 0:
                    ti -= 1
                    if w[t] != tab[ti][tj]:
                        trv = -1
                        break
                    elif w[t] == tab[ti][tj] and t == len(w)-1:
                        trv = t
                    t+=1
                
                t = 1
                ti = i
                tj = j
                th = -1
                while t < len(w) and pos[w] != [-1,-1] and tj < len(tab[0])-1:
                    tj += 1
                    if w[t] != tab[ti][tj]:
                        th = -1
                        break
                    elif w[t] == tab[ti][tj] and t == len(w)-1:
                        th = t
                    t+=1
                    
                t = 1
                ti = i
                tj = j
                trh = -1
                while t < len(w) and pos[w] != [-1,-1] and tj > 0:
                    tj -= 1
                    if w[t] != tab[ti][tj]:
                        trh = -1
                        break
                    elif w[t] == tab[ti][tj] and t == len(w)-1:
                        trh = t
                    t+=1
                    
                ti = i
                tj = j
                td = -1
                t = 1
                while t < len(w) and pos[w] != [-1,-1] and tj < len(tab[0])-1 and ti < len(tab)-1:
                    tj += 1
                    ti += 1
                    if w[t] != tab[ti][tj]:
                        td = -1
                        break
                    elif w[t] == tab[ti][tj] and t == len(w)-1:
                        td = t
                    t+=1
                
                ti = i
                tj = j
                trd = -1
                t = 1                
                while t < len(w) and pos[w] != [-1,-1] and tj > 0 and ti > 0 :
                    tj -= 1
                    ti -= 1
                    if w[t] != tab[ti][tj]:
                        trd = -1
                        break
                    elif w[t] == tab[ti][tj] and t == len(w)-1:
                        trd = t
                    t+=1
                    
                ti = i
                tj = j
                td2 = -1
                t = 1
                while t < len(w) and pos[w] != [-1,-1] and tj > 0 and ti < len(tab)-1:
                    tj -= 1
                    ti += 1
                    if w[t] != tab[ti][tj]:
                        td2 = -1
                        break
                    elif w[t] == tab[ti][tj] and t == len(w)-1:
                        td2 = t
                    t+=1 
                    
                ti = i
                tj = j
                trd2 = -1
                t = 1
                while t < len(w) and pos[w] != [-1,-1] and tj < len(tab[0])-1 and ti > 0:
                    tj += 1
                    ti -= 1
                    if w[t] != tab[ti][tj]:
                        trd2 = -1
                        break
                    elif w[t] == tab[ti][tj] and t == len(w)-1:
                        trd2 = t
                    t+=1    
                if tv == -1 and th == -1 and td == -1 and trh == -1 and trv == -1 and trd == -1 and td2 == -1 and trd2 == -1 : # if none of the flags have been changed then the word was not found at the location in the matrix in any of the directions and the pos value is reset to default (ie. [-1,-1])
                    pos[w] = [-1,-1]
                else: #Saves the direction in which the word can be found in the word matrix, along with 1 based indexing for positions in the matrix
                    if tv > -1:
                        pos[w] = [i+1,j+1,'Down']
                    elif th > -1:
                        pos[w] = [i+1,j+1,'Right']
                    elif td > -1:
                        pos[w] = [i+1,j+1,'Down Right Diagonal']
                    elif trh > -1:
                        pos[w] = [i+1,j+1,'Left']
                    elif trv > -1:
                        pos[w] = [i+1,j+1,'Up']
                    elif trd > -1:
                        pos[w] = [i+1,j+1,'Up Left Diagonal']
                    elif td2 > -1:
                        pos[w] = [i+1,j+1,'Down Left Diagonal']
                    elif trd2 > -1:
                        pos[w] = [i+1,j+1,'Up Right Diagonal']
        j+=1
    i += 1
for key in pos:
    print('%15s : '%(key),pos[key]) #Printing the output


'''
Notes for future : simplify the code by trying to combine the loops and or by using functions and by trying to removing some conditions.
'''