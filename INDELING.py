<<<<<<< HEAD
import random as r


BSD_O_AUG25B=[
    'Raad',
    'Josip',
    'Roan',
    'Cris',
    'Kourosh',
    'Sven F.',
    'Anas',
    'Jeffry',
    'Atilla',
    'Ammaar',
    'Ilia',
    'Lion',
    'Orhan',
    'Daniël',
    'Armin',
    'Jovan',
    'Ward',
    'Stefan',
    'Caelan',
    'Noah',
    'Kaydeon',
    'Sven W.',
    'Phoenix'
]
group=[]
counterloop=0
size_group=int(input("How many person per group?:"))
#amount=int(input("how many groups?:"))
while len(BSD_O_AUG25B)>=size_group:    
    for i in range(size_group):
         summon=r.randint(0,len(BSD_O_AUG25B)-1)
         #print('length',len(BSD_O_AUG25B))
         #print("random",summon)
         if summon not in group:
            group.append(BSD_O_AUG25B[summon])
            BSD_O_AUG25B.remove(BSD_O_AUG25B[summon])
    print(group)
    counterloop=+1
    group.clear()

print(BSD_O_AUG25B)
#print(group)
=======
import random as r


BSD_O_AUG25B=[
    'Raad',
    'Josip',
    'Roan',
    'Cris',
    'Kourosh',
    'Sven F.',
    'Anas',
    'Jeffry',
    'Atilla',
    'Ammaar',
    'Ilia',
    'Lion',
    'Orhan',
    'Daniël',
    'Armin',
    'Jovan',
    'Ward',
    'Stefan',
    'Caelan',
    'Noah',
    'Kaydeon',
    'Sven W.',
    'Phoenix'
]
group=[]
counterloop=0
size_group=int(input("How many person per group?:"))
amount=int(input("how many groups?:"))
while len(BSD_O_AUG25B)>=size_group:
    if counterloop<amount:
        for i in range(size_group):
            summon=r.randint(0,len(BSD_O_AUG25B)-1)
            #print('length',len(BSD_O_AUG25B))
            #print("random",summon)
            if summon not in group:
                group.append(BSD_O_AUG25B[summon])
                BSD_O_AUG25B.remove(BSD_O_AUG25B[summon])
        print(group)
        counterloop=+1
        group.clear()
    else:
        break

print(BSD_O_AUG25B)
#print(group)
>>>>>>> 15a1fb2824e5c4b2805f6c8bd7cb625f2eead2c9
