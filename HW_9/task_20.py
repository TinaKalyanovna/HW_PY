Задание 1. Импортируйте библиотеку pandas. Считайте данные из csv-файла в датафрейм и сохраните в переменную data. Путь к файлу:
 
/datasets/data.csv
 
# импортируйте библиотеку pandas
import pandas as pd
# прочитайте csv-файл
data = pd.read_csv('/datasets/data.csv')
Задание 2. Выведите первые 20 строчек датафрейма data на экран.
 
print(data.head(20))
# ваш код здесь
print(data.head(20))
    children  days_employed  dob_years            education  education_id  \
0          1   -8437.673028         42               высшее             0   
1          1   -4024.803754         36              среднее             1   
2          0   -5623.422610         33              Среднее             1   
3          3   -4124.747207         32              среднее             1   
4          0  340266.072047         53              среднее             1   
5          0    -926.185831         27               высшее             0   
6          0   -2879.202052         43               высшее             0   
7          0    -152.779569         50              СРЕДНЕЕ             1   
8          2   -6929.865299         35               ВЫСШЕЕ             0   
9          0   -2188.756445         41              среднее             1   
10         2   -4171.483647         36               высшее             0   
11         0    -792.701887         40              среднее             1   
12         0            NaN         65              среднее             1   
13         0   -1846.641941         54  неоконченное высшее             2   
14         0   -1844.956182         56               высшее             0   
15         1    -972.364419         26              среднее             1   
16         0   -1719.934226         35              среднее             1   
17         0   -2369.999720         33               высшее             0   
18         0  400281.136913         53              среднее             1   
19         0  -10038.818549         48              СРЕДНЕЕ             1   
 
       family_status  family_status_id gender income_type  debt  \
0    женат / замужем                 0      F   сотрудник     0   
1    женат / замужем                 0      F   сотрудник     0   
2    женат / замужем                 0      M   сотрудник     0   
3    женат / замужем                 0      M   сотрудник     0   
4   гражданский брак                 1      F   пенсионер     0   
5   гражданский брак                 1      M   компаньон     0   
6    женат / замужем                 0      F   компаньон     0   
7    женат / замужем                 0      M   сотрудник     0   
8   гражданский брак                 1      F   сотрудник     0   
9    женат / замужем                 0      M   сотрудник     0   
10   женат / замужем                 0      M   компаньон     0   
11   женат / замужем                 0      F   сотрудник     0   
12  гражданский брак                 1      M   пенсионер     0   
13   женат / замужем                 0      F   сотрудник     0   
14  гражданский брак                 1      F   компаньон     1   
15   женат / замужем                 0      F   сотрудник     0   
16   женат / замужем                 0      F   сотрудник     0   
17  гражданский брак                 1      M   сотрудник     0   
18    вдовец / вдова                 2      F   пенсионер     0   
19         в разводе                 3      F   сотрудник     0   
 
     total_income                                 purpose  
0   253875.639453                           покупка жилья  
1   112080.014102                 приобретение автомобиля  
2   145885.952297                           покупка жилья  
3   267628.550329              дополнительное образование  
4   158616.077870                         сыграть свадьбу  
5   255763.565419                           покупка жилья  
6   240525.971920                       операции с жильем  
7   135823.934197                             образование  
8    95856.832424                   на проведение свадьбы  
9   144425.938277                 покупка жилья для семьи  
10  113943.491460                    покупка недвижимости  
11   77069.234271       покупка коммерческой недвижимости  
12            NaN                         сыграть свадьбу  
13  130458.228857                 приобретение автомобиля  
14  165127.911772              покупка жилой недвижимости  
15  116820.904450  строительство собственной недвижимости  
16  289202.704229                            недвижимость  
17   90410.586745              строительство недвижимости  
18   56823.777243      на покупку подержанного автомобиля  
19  242831.107982            на покупку своего автомобиля  
Задание 3. Выведите основную информацию о датафрейме с помощью метода info().
 
# ваш код здесь
data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21525 entries, 0 to 21524
Data columns (total 12 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   children          21525 non-null  int64  
 1   days_employed     19351 non-null  float64
 2   dob_years         21525 non-null  int64  
 3   education         21525 non-null  object 
 4   education_id      21525 non-null  int64  
 5   family_status     21525 non-null  object 
 6   family_status_id  21525 non-null  int64  
 7   gender            21525 non-null  object 
 8   income_type       21525 non-null  object 
 9   debt              21525 non-null  int64  
 10  total_income      19351 non-null  float64
 11  purpose           21525 non-null  object 
dtypes: float64(2), int64(5), object(5)
memory usage: 2.0+ MB
2  Предобработка данных
2.1  Удаление пропусков
Задание 4. Выведите количество пропущенных значений для каждого столбца. Используйте комбинацию двух методов.
 
data.isna().sum()
### Обнаружены пропуски в столбцах 'total_income', 'days_employed'
# определим, сколько таких пропущенных значений
data.isna().sum()
children               0
days_employed       2174
dob_years              0
education              0
education_id           0
family_status          0
family_status_id       0
gender                 0
income_type            0
debt                   0
total_income        2174
purpose                0
dtype: int64
Задание 5. В двух столбцах есть пропущенные значения. Один из них — days_employed. Пропуски в этом столбце вы обработаете на следующем этапе. Другой столбец с пропущенными значениями — total_income — хранит данные о доходах. На сумму дохода сильнее всего влияет тип занятости, поэтому заполнить пропуски в этом столбце нужно медианным значением по каждому типу из столбца income_type. Например, у человека с типом занятости сотрудник пропуск в столбце total_income должен быть заполнен медианным доходом среди всех записей с тем же типом.
 
data['total_income'] = data.groupby('income_type')['total_income'].transform(lambda x: x.fillna(x.median()))
 # ваш код здесь
2.2  Обработка аномальных значений
Задание 6. В данных могут встречаться артефакты (аномалии) — значения, которые не отражают действительность и появились по какой-то ошибке. Таким артефактом будет отрицательное количество дней трудового стажа в столбце days_employed. Для реальных данных это нормально. Обработайте значения в этом столбце: замените все отрицательные значения положительными с помощью метода abs().
 
data['days_employed'] = data['days_employed'].abs()
 # ваш код здесь
Задание 7. Для каждого типа занятости выведите медианное значение трудового стажа days_employed в днях.
 
table_4 = data.pivot_table(index='income_type', values= ['days_employed'], aggfunc='median')
print(table_4)
                 days_employed
income_type                   
безработный      366413.652744
в декрете          3296.759962
госслужащий        2689.368353
компаньон          1547.382223
пенсионер        365213.306266
предприниматель     520.848083
сотрудник          1574.202821
студент             578.751554