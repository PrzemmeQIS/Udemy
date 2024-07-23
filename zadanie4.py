x = '123abc'
s = '123asbcs'

l1 = ['kupa']
counter = 0

for letter in x:
    if letter == s[counter]:
        l1.append(letter)
        counter = counter + 1
    else:
        break
    
print(l1)