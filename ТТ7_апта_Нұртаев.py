# 1) Жеңіл деңгей (Basic)
# Деректерді зерттеу
# 1.1) Titanic деректер жинағын жүктеп, оның өлшемін (shape) және бағандарын (columns) қараңыз.
# 1.2)Әр бағандағы бос мәндердің санын анықтаңыз.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("/tested.csv")
print(df.columns)
print(df.shape)

# 2) Сандық бағандарды сипаттау
# 2.1)age және fare бағандарының орташа мәнін, минимумы, максимумы және стандартты ауытқуын есептеңіз
print("Age статистикасы: ")
print("Орташа мән: ", df['Age'].mean())
print("Минимум мән: ", df['Age'].min())
print("Максимум мән: ", df['Age'].max())
print("Стандартты ауытқу: ", df['Age'].std())

print("\nFare статистикасы: ")
print("Орташа мән: ", df['Fare'].mean())
print("Минимум мән: ", df['Fare'].min())
print("Максимум мән: ", df['Fare'].max())
print("Стандартты ауытқу: ", df['Fare'].std())

# 3) Гистограмма
# 3.1 age бағанын гистограмма түрінде бейнелеңіз.
# 3.2) KDE қисығын қосып көріңіз.
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=25, kde=True)
plt.title('Жас бойынша таралу')
plt.xlabel('Жас')
plt.ylabel('Саны')
plt.show()

# 2. Орташа деңгей (Intermediate)
# Boxplot
# 2.1 pclass бойынша fare бағанын Boxplot арқылы бейнелеңіз.
# 2.2 Қорапшадан көрініп тұрған ауытқуларды анықтаңыз.
plt.figure(figsize=(8,5))
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title("Билет классы және билет құны бойынша Boxplot")
plt.show()
# 2.3 Scatter plot
# 2.4 age және fare бағандарын нүктелік диаграммада бейнелеңіз.
# 2.5 survived бағанына қарай түсін өзгертіңіз.
plt.figure(figsize=(8,5))
sns.scatterplot(x='Age', y='Fare', hue='Survived',data=df)
plt.title("Жас және билет құны бойынша нүктелік диаграмма")
plt.show()

# 2.6 Heatmap
# 2.7 Сандық бағандардың корреляциясын анықтап, оны Seaborn heatmap арқылы визуализациялаңыз.
# 2.8 Бос мәндерді өңдеу
# 2.9 age бағанындағы бос мәндерді бағанның медианасымен толтырыңыз.
# 3.0 embarked бағанындағы бос мәндерді ең жиі кездесетін мәнмен толтырыңыз.
a_df = df.select_dtypes(include=['int64', 'float64'])
plt.figure(figsize=(8,5))
sns.heatmap(a_df.corr(), annot=True, cmap='coolwarm')
plt.title("Сандық бағдардың коррелияциясы")
plt.show()

df['Age'] =df['Age'].fillna(df['Age'].mean())
df['Cabin'] =df['Cabin'].fillna(df['Cabin'].mode()[0])
print(df.isnull().sum())

# Санаттық белгілерді кодтау
# sex бағанын Label Encoding арқылы түрлендіріңіз.
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
print(df[['Sex']].head())

# embarked бағанын One-Hot Encoding арқылы түрлендіріңіз.
embarked_dummies = pd.get_dummies(df['Embarked'], prefix='Embarked')
df = pd.concat([df, embarked_dummies], axis=1)
print(df.head())
#  Сақтау
df.to_csv("/home/elmadmin/PycharmProjects/ML/Titanic.csv", index=False)

