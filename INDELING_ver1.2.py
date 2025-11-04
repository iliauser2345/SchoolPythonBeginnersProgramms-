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

whitelist=['Y','y','n','N']


#CREATING CUSTOM LIST(IF REQUESTED)-------------------------------------------------------
setting_custom_list=input("Want to fill in your own list?(Y/N):")
try:
    setting_custom_list_length=int(input("How many elements?:"))
except:
    print('Number required')
    setting_custom_list_length=int(input("How many elements?:"))
if setting_custom_list=="Y" or setting_custom_list=="y":
    BSD_O_AUG25B.clear()
    for k in range(setting_custom_list_length):
        BSD_O_AUG25B.append(input())
#CREATING CUSTOM LIST(IF REQUESTED)-------------------------------------------------------

#SETTINGS------------------------------------------------------------------------------
setting_stats=input("Show Stats?(Y/N):")
setting_distribution=input("Want to limit amount of groups?(Y/N):")
if setting_distribution=="Y" or setting_distribution=="y":
    setting_showcase=input("Showcase the leftovers?(Y/N):")
    amount=int(input("How many groups?:"))
size_group=int(input("How many person per group?:"))
#SETTINGS------------------------------------------------------------------------------



#PREPLANNING---------------------------------------------------------------------------
def spec_distribution():
    for j in range(amount):
        for a in range(size_group):
            summon=r.randint(0,len(BSD_O_AUG25B)-1)
            if setting_stats=="Y" or setting_stats=="y":
                print('length',len(BSD_O_AUG25B))
                print("random",summon)
            if summon not in group:
                group.append(BSD_O_AUG25B[summon])
                BSD_O_AUG25B.remove(BSD_O_AUG25B[summon])
        print(group)
        group.clear()
    if setting_showcase=="Y" or setting_showcase=="y":    
        print(BSD_O_AUG25B)
    
def unspec_distribution():
    while len(BSD_O_AUG25B)>=size_group:    
        for i in range(size_group):
            summon=r.randint(0,len(BSD_O_AUG25B)-1)
            if setting_stats=="Y" or setting_stats=="y":
                print('length',len(BSD_O_AUG25B))
                print("random",summon)
            if summon not in group:
                group.append(BSD_O_AUG25B[summon])
                BSD_O_AUG25B.remove(BSD_O_AUG25B[summon])
        print(group)
        group.clear()
    print(BSD_O_AUG25B)
#PREPLANNING----------------------------------------------------------------------------



#EXECUTION------------------------------------------------------------------------------
if setting_distribution=="Y" or setting_distribution=="y":
    spec_distribution()
elif setting_distribution=="N" or setting_distribution=="n":
    unspec_distribution()
else:
    print("invalid input. Distribution methods are defined by Y/N answer")
#EXECUTION------------------------------------------------------------------------------