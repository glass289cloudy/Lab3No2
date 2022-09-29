e = {
'1' : ['A', 'E','I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
'2' : ['D', 'G'],
'3' : ['B', 'C', 'M', 'P'],
'4' : ['F', 'H', 'V', 'W', 'Y'],
'5' : ['K'],
'8' : ['J', 'X'],
'10' : ['Q', 'Z']
}
a = input("Введите слово \n")
a = a.upper()
k = 0
for i in a:
    for j in e.items():
        if i in j[1]:
            k += int(j[0])
print(k)