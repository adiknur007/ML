# Тапсырма 1: CSV Файлын Оқу және Тізімге Сақтау

data_rows = []
with open('Salaries.csv', 'r', encoding='utf-8') as f:
    for i in range (11):
        if i == 0:
            f.readline()
            continue
        data_rows.append(f.readline())
print (f"len(data_rows) = {len(data_rows)}")
print(data_rows)

# Тапсырма 2: Кортеж және Сөздік – Алғашқы 3 Адамның Атын Сақтау
first_three_names = tuple([data_rows[i].split(",")[1] for i in range(3)])

first_three_jobs = tuple([data_rows[i].split(",")[2]  for i in range(3)])

employee_titles = dict(zip(first_three_names, first_three_jobs))

print(f"first_three_names -> {first_three_names}")
print(f"employee_titles -> {employee_titles}")

# Тапсырма 3: Тізімдік Өрнектер (List Comprehension)

base_pays_str = [row.split(",")[3] if row.split(",")[3].replace(".", "").isdigit() else row.split(",")[4] for row in data_rows]
print(base_pays_str)

# Тапсырма 4: Жиын (Set) – Бірегей Атақтарды Табу

jobstitle = []
for row in data_rows:
  jobstitle.append(row.split(",")[2])
unique_titles = set(jobstitle)
print(*unique_titles, sep="\n")