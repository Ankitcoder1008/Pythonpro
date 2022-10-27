lists=[1,2,3,4]
songs=['I should be allowed to think','Birdhouse in your soul']
hex=[[0,1,2,3,4,5,6,7,8,9,],['A','B','C','D','E','F']]
print(songs[0])
print(songs[1])
print('Numbers:',hex[0])
print('D:',hex[1][3])
print('A-c',hex[1][0:3])
print(hex[1]+lists)
print(len(hex))
songs += ['AKA Driver']
print(songs)
print(lists*2)
cubes = [x**3 for x in lists]
print(cubes)