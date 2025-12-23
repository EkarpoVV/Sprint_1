# Если мое решение верное, но отличается от эталонного, просьба эталонное решение приложить в обратной связи, что бы я изучил его для развтия.

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 



def unic_func():
    seen = list()
    for key, value in tickets.items():
        unique_values = []
        for item in value:
            if item not in seen:
                seen.append(item)
                unique_values.append(item)
        tickets[key] = unique_values


    
def final_func():
    tickets_list = list(tickets.values()) # [['API_45', 'API_76', 'E2E_4'], ['UI_19', 'API_65', 'E2E_45'], ['E2E_2'], ['E2E_9'], ['API_61']]
    tickets_by_type = {}
    for key,value in types.items():
        tickets_by_type[value] = tickets_list[key-1]
    print(tickets_by_type)


unic_func()
final_func()