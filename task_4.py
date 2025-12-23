# Если мое решение верное, но отличается от эталонного, просьба эталонное решение приложить в обратной связи, что бы я изучил его для развтия.
# 1
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005'))) # Изменено после ревью
print(new_tasks)
print(completed_tasks)

# 2
new_tasks.remove('task_007') # Изменено после ревью
print(new_tasks)

# 3
print(new_tasks[-1])
