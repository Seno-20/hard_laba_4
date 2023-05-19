import pandas as pd
import csv
import re

with open('import_1.csv', 'r') as file:
    reader = csv.reader(file)
    
    # первое задание печатать первые строки из таблицы 
""" first_task = []
    for i, row in enumerate(reader):
        if i < 111:
            first_task.append(row)
        else:
            break
            
    for row in first_task:
       writer.writerow(row)"""

tabl = pd.read_csv('import copy.csv', sep='\t', encoding='utf-16')
tabl_c = tabl.copy()

address = tabl_c.pop("Address")
#tabl_c.to_csv("export.csv", sep='\t', index=False)
buffer = ""
for line in address:
    
    if line[0].isdigit() or line[1].isdigit():
        num = re.search(r'\d+', line).group()
        line = re.sub(r'in  Word', '', line)
        # Проверяем, попадает ли число в заданный промежуток
        if 8 <= int(num) <= 15:

            # Выполняем необходимые математические операции
            num = str(int(num) - 8)
            db_num = re.search(r'DB(\d+)', line).group(1)
            db_num = str(int(db_num) * 2)
            
            # Заменяем исходные значения на новые
            line = re.sub(r'\d+', '', line, count=1)  # Удаляем первое число из строки
            line = re.sub(r'DB\d+', 'D' + db_num, line)  # Изменяем формат строки
            line = re.sub(r'DW', 'D', line)  # Заменяем DW на D
            line = line + "." + num + "\t"
            buffer = buffer + line

        elif 0 <= int(num) <= 8:
            
            # Выполняем необходимые математические операции
            db_num = re.search(r'DB(\d+)', line).group(1)
            db_num = str(int(db_num) * 2 + 1)
            
            # Заменяем исходные значения на новые
            line = re.sub(r'\d+', '', line, count=1)  # Удаляем первое число из строки
            line = re.sub(r'DB\d+', 'D' + db_num, line)  # Изменяем формат строки
            line = re.sub(r'DW', 'D', line)  # Заменяем DW на D
            line = line + "." + num + "\t"
            buffer = buffer + line
        # Выводим результат
        #print(line.strip())
    elif line[0] == "D":
        line = "cool111111111" + "\t"
        buffer = buffer + line

    else:
        buffer = buffer + line
        
address_2 = pd.DataFrame({"Address" : [buffer] })
tabl_c.insert(7, "Address", (address_2))
tabl_c.to_csv("export5.csv", sep='\t', index=False)
print(buffer)


  
    # первое задание печатать первые строки из таблицы 
