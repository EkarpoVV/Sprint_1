# Если мое решение верное, но отличается от эталонного, просьба эталонное решение приложить в обратной связи, что бы я изучил его для развтия.
list_empty = []
string_1 = '1h 45m,360s,25m,30m 120s,2h 60s'
string_mod = string_1.replace(',', ' ')
list_mod = string_mod.split()
for i in list_mod:
    if 'h' in i:
        x = int(i.replace('h', '')) 
        y = x * 60
        list_empty.append(y)
    elif 's' in i:
        x = int(i.replace('s', '')) 
        y = x // 60
        list_empty.append(y)

    elif 'm' in i:
        x = int(i.replace('m', '')) 
        list_empty.append(x)

all_time = sum(list_empty)
print(all_time)