import pandas as pd
import numpy as np

data = {
    'Ученики': ['Виктор', 'Татьяна', 'Марина', 'Федор', 'Алексей', 'Павел', 'Кирилл', 'Вячеслав', 'Юлия', 'Валерия'],
    'Русский язык': np.random.randint(1, 6, size=10),
    'Математика': np.random.randint(1, 6, size=10),
    'Литература': np.random.randint(1, 6, size=10),
    'Физика': np.random.randint(1, 6, size=10),
    'Информатика': np.random.randint(1, 6, size=10)
}

df = pd.DataFrame(data)

print(df)

print("\nПервые несколько строк:")
print(df.head())

average_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(average_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"\nQ1 для Математики: {Q1_math}")
print(f"Q3 для Математики: {Q3_math}")

IQR_math = Q3_math - Q1_math
print(f"IQR для Математики: {IQR_math}")

std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)

