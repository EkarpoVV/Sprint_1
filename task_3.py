# Если мое решение верное, но отличается от эталонного, просьба эталонное решение приложить в обратной связи, что бы я изучил его для развтия.
world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022]='Аргентина'
for key, value in world_champions.items():
    print(key, '-', value)

country = 'Италия'

list_land = list(world_champions.values())
if country in list_land:
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')


'''ДОП РЕШЕНИЕ
is_champion_italy = False
for value in world_champions.items():
    if country in value:
        is_champion_italy = True
        break
        
if is_champion_italy == True:
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
'''





    