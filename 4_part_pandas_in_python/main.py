import sys
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# 33. Прочитать файл CSV и перевести его в DataFrame
df = pd.read_csv('data.csv')
print(df.to_string())
print("\t33--"*20)

# 34. Прочитать файл CSV (определенные столбцы и определенное кол-во строк) и перевести его в DataFrame
df = pd.read_csv('data.csv', nrows=10,usecols=['Name', 'Sex', 'Survived'])
print(df.to_string())
print("\t34--"*20)

# 35. Прочитать файл CSV и перевести каждую 100-ую строку в DataFrame
df = pd.read_csv('data.csv', chunksize=100)
df_each = pd.DataFrame()
for chunk in df:
    df_each = df_each.append(chunk.iloc[0, :])
print(df_each.head().to_string())
print("\t35--"*20)

# 36. Преобразовать индексы объекта Series в столбец DataFrame
test_list = 'abcedf'
test_arr = np.arange(len(test_list))
test_dict = dict(zip(test_list, test_arr))
s = pd.Series(test_dict)

# сбрасываем индексы
df = s.to_frame().reset_index()
# присвоение имёен столбцам
df.columns = ['letter', 'number']
print(df.to_string())
print("\t36--"*20)

# 37. Посмотреть информацию объекта DataFrame
df = pd.read_csv('data.csv', nrows=10)
# Формат каждого столбца
print('\n', 'Формат столбцов:')
print(df.dtypes)
print("\t37-1--"*20)

# Размерность DataFrame
print('\n', 'Размерность:')
print(df.shape)
print("\t37-2--"*20)

# Общая статистика
print('\n', 'Общая статистика')
print(df.describe().to_string())
print("\t37-3--"*20)

# 38. Получить данные из DataFrame по условию
s = 'abcdefghijklmnopqrstuvwxyz'
# создаем DataFrame из рандомных цифр
df = pd.DataFrame(np.random.randint(low=1, high=10, size=[3, 5]))
# добавляем столбец букв
df = pd.concat([df, pd.DataFrame({'letter': ['a', 'b', 'c']})], axis=1)
# добавляем столбец рандомных букв
df = pd.concat([df, pd.DataFrame({'r_letter': [random.choice(s) for i in range(len(df))]})], axis=1)
print('сформированный DataFrame:')
print(df)
print("\t38-1--"*20)

# получаем номер строки и столбца (индексацию) по условию
row, col = np.where(df.values == 5)
print('индексы строк и столбцов:')
print(row)
print(col)
print("\t38-2--"*20)

# получаем данные по индексации (подобно индексации в матрице)
if (row.size != 0) and (col.size != 0):
    print('данные по индексации (строка, столбец):')
    print(df.iat[row[0], col[0]])
    print(df.iloc[row[0], col[0]])
    print("\t38-3--"*20)

# получаем данные по индексации и именованому объекту (смешанный тип)
if (row.size != 0) and (col.size != 0):
    print('данные по индексации и наименованию:')
    print(df.at[row[0], 1])
    print(df.at[row[0], 'letter'])
    print("\t38-4--"*20)

# получаем по условию столбцы и строки DataFrame
# (loc;at - принимают строки(столбцы) с определенными метками из индекса (именованные метки))
# (iloc, iat) - принимают номера строк и столбцов
ans1 = df.loc[df['letter'] == 'a']
print('данные по условию:')
print(ans1)
print("\t38-5--"*20)

# 39. Изменить данные столбца DataFrame по условию (по многим условиям)
# загружаем данные (только 10 строк)
df = pd.read_csv('data.csv', nrows=10)
# определим функцию для изменения значений в столбце
def change_values(val):
    """ тестовая функция измененения значений """
    # проверка на числовой тип входящей переменной
    try:
        float(val)
    except Exception as e:
        return val
    # условия изменения значений
    if val > 25:
        return 'High'
    elif val < 25:
        return 'Low'

col_df = df['Age'].apply(change_values)
print(col_df)
print("\t39--"*20)

# 40. Переименовать столбец(-ы) в DataFrame(df)
df = pd.read_csv('data.csv', nrows=10)
# меняем наименование одного столбца
df = df.rename(columns={'Name': 'FullName'})
# изменяем наименования всех столбцов
df.columns = df.columns.map(lambda x: x + '_')
print(df.to_string())
print("\t40--"*20)

# 41. Проверить имеет ли df пропущенные значения
df = pd.read_csv('data.csv', nrows=10)
# проверка на пропущенные значения
print(df.isnull().values.any())
print("\t41--"*20)

# 42. Получить наименование столбцов и сумму пропущенных значений DF
df = pd.read_csv('data.csv', nrows=20)
# получаем Series суммы пропущенных значений
# вариант 1
missing = df.isnull().sum()
# вариант 2
missing = df.apply(lambda x: x.isnull().sum())
print(missing[missing != 0])
print("\t42--"*20)

# 43. Заменить пропущенные значения поля "Age" в зависимости от поля "Name"
# данный фрагмент встречается в популярной задаче на kaggle.com о Титанике.
# Решение всей задаче вы можете посмотреть по ссылке:
# у поля "Name" есть Титулы (Mr, Miss, Mrs и т.д.). Нужно проставить пропущенные значения "Age"
# медианой по титулам
df = pd.read_csv('data.csv')
# смотрим на пропущенные значения
print(df.isnull().sum())
print("\t43-1--"*20)

# смотрим на первые строки поля "Name"
print(df['Name'].head(10))
print("\t43-2--"*20)

# добавляем столбец "Title" (извлекаем из поля "Name" титулы)
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

# смотрим на частоту встречаемости Титулов
print(df['Title'].value_counts())
print("\t43-2--"*20)
# заполняем пропуски "age" в зависимости от "титулов"
df['Age'].fillna(df.groupby('Title')['Age'].transform('median'), inplace=True)

#output
     PassengerId  Survived  Pclass                                                                                Name     Sex    Age  SibSp  Parch              Ticket      Fare            Cabin Embarked
0              1         0       3                                                             Braund, Mr. Owen Harris    male  22.00      1      0           A/5 21171    7.2500              NaN        S
1              2         1       1                                 Cumings, Mrs. John Bradley (Florence Briggs Thayer)  female  38.00      1      0            PC 17599   71.2833              C85        C
2              3         1       3                                                              Heikkinen, Miss. Laina  female  26.00      0      0    STON/O2. 3101282    7.9250              NaN        S
3              4         1       1                                        Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.00      1      0              113803   53.1000             C123        S
4              5         0       3                                                            Allen, Mr. William Henry    male  35.00      0      0              373450    8.0500              NaN        S
5              6         0       3                                                                    Moran, Mr. James    male    NaN      0      0              330877    8.4583              NaN        Q
6              7         0       1                                                             McCarthy, Mr. Timothy J    male  54.00      0      0               17463   51.8625              E46        S
7              8         0       3                                                      Palsson, Master. Gosta Leonard    male   2.00      3      1              349909   21.0750              NaN        S
8              9         1       3                                   Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)  female  27.00      0      2              347742   11.1333              NaN        S
9             10         1       2                                                 Nasser, Mrs. Nicholas (Adele Achem)  female  14.00      1      0              237736   30.0708              NaN        C
10            11         1       3                                                     Sandstrom, Miss. Marguerite Rut  female   4.00      1      1             PP 9549   16.7000               G6        S
11            12         1       1                                                            Bonnell, Miss. Elizabeth  female  58.00      0      0              113783   26.5500             C103        S
12            13         0       3                                                      Saundercock, Mr. William Henry    male  20.00      0      0           A/5. 2151    8.0500              NaN        S
13            14         0       3                                                         Andersson, Mr. Anders Johan    male  39.00      1      5              347082   31.2750              NaN        S
14            15         0       3                                                Vestrom, Miss. Hulda Amanda Adolfina  female  14.00      0      0              350406    7.8542              NaN        S
15            16         1       2                                                    Hewlett, Mrs. (Mary D Kingcome)   female  55.00      0      0              248706   16.0000              NaN        S
16            17         0       3                                                                Rice, Master. Eugene    male   2.00      4      1              382652   29.1250              NaN        Q
17            18         1       2                                                        Williams, Mr. Charles Eugene    male    NaN      0      0              244373   13.0000              NaN        S
18            19         0       3                             Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)  female  31.00      1      0              345763   18.0000              NaN        S
19            20         1       3                                                             Masselmani, Mrs. Fatima  female    NaN      0      0                2649    7.2250              NaN        C
20            21         0       2                                                                Fynney, Mr. Joseph J    male  35.00      0      0              239865   26.0000              NaN        S
21            22         1       2                                                               Beesley, Mr. Lawrence    male  34.00      0      0              248698   13.0000              D56        S
22            23         1       3                                                         McGowan, Miss. Anna "Annie"  female  15.00      0      0              330923    8.0292              NaN        Q
23            24         1       1                                                        Sloper, Mr. William Thompson    male  28.00      0      0              113788   35.5000               A6        S
24            25         0       3                                                       Palsson, Miss. Torborg Danira  female   8.00      3      1              349909   21.0750              NaN        S
25            26         1       3                           Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)  female  38.00      1      5              347077   31.3875              NaN        S
26            27         0       3                                                             Emir, Mr. Farred Chehab    male    NaN      0      0                2631    7.2250              NaN        C
27            28         0       1                                                      Fortune, Mr. Charles Alexander    male  19.00      3      2               19950  263.0000      C23 C25 C27        S
28            29         1       3                                                       O'Dwyer, Miss. Ellen "Nellie"  female    NaN      0      0              330959    7.8792              NaN        Q
29            30         0       3                                                                 Todoroff, Mr. Lalio    male    NaN      0      0              349216    7.8958              NaN        S
30            31         0       1                                                            Uruchurtu, Don. Manuel E    male  40.00      0      0            PC 17601   27.7208              NaN        C
31            32         1       1                                      Spencer, Mrs. William Augustus (Marie Eugenie)  female    NaN      1      0            PC 17569  146.5208              B78        C
32            33         1       3                                                            Glynn, Miss. Mary Agatha  female    NaN      0      0              335677    7.7500              NaN        Q
33            34         0       2                                                               Wheadon, Mr. Edward H    male  66.00      0      0          C.A. 24579   10.5000              NaN        S
34            35         0       1                                                             Meyer, Mr. Edgar Joseph    male  28.00      1      0            PC 17604   82.1708              NaN        C
35            36         0       1                                                      Holverson, Mr. Alexander Oskar    male  42.00      1      0              113789   52.0000              NaN        S
36            37         1       3                                                                    Mamee, Mr. Hanna    male    NaN      0      0                2677    7.2292              NaN        C
37            38         0       3                                                            Cann, Mr. Ernest Charles    male  21.00      0      0          A./5. 2152    8.0500              NaN        S
38            39         0       3                                                  Vander Planke, Miss. Augusta Maria  female  18.00      2      0              345764   18.0000              NaN        S
39            40         1       3                                                         Nicola-Yarred, Miss. Jamila  female  14.00      1      0                2651   11.2417              NaN        C
40            41         0       3                                      Ahlin, Mrs. Johan (Johanna Persdotter Larsson)  female  40.00      1      0                7546    9.4750              NaN        S
41            42         0       2                            Turpin, Mrs. William John Robert (Dorothy Ann Wonnacott)  female  27.00      1      0               11668   21.0000              NaN        S
42            43         0       3                                                                 Kraeff, Mr. Theodor    male    NaN      0      0              349253    7.8958              NaN        C
43            44         1       2                                            Laroche, Miss. Simonne Marie Anne Andree  female   3.00      1      2       SC/Paris 2123   41.5792              NaN        C
44            45         1       3                                                       Devaney, Miss. Margaret Delia  female  19.00      0      0              330958    7.8792              NaN        Q
45            46         0       3                                                            Rogers, Mr. William John    male    NaN      0      0     S.C./A.4. 23567    8.0500              NaN        S
46            47         0       3                                                                   Lennon, Mr. Denis    male    NaN      1      0              370371   15.5000              NaN        Q
47            48         1       3                                                           O'Driscoll, Miss. Bridget  female    NaN      0      0               14311    7.7500              NaN        Q
48            49         0       3                                                                 Samaan, Mr. Youssef    male    NaN      2      0                2662   21.6792              NaN        C
49            50         0       3                                       Arnold-Franchi, Mrs. Josef (Josefine Franchi)  female  18.00      1      0              349237   17.8000              NaN        S
50            51         0       3                                                          Panula, Master. Juha Niilo    male   7.00      4      1             3101295   39.6875              NaN        S
51            52         0       3                                                        Nosworthy, Mr. Richard Cater    male  21.00      0      0          A/4. 39886    7.8000              NaN        S
52            53         1       1                                            Harper, Mrs. Henry Sleeper (Myna Haxtun)  female  49.00      1      0            PC 17572   76.7292              D33        C
53            54         1       2                                  Faunthorpe, Mrs. Lizzie (Elizabeth Anne Wilkinson)  female  29.00      1      0                2926   26.0000              NaN        S
54            55         0       1                                                      Ostby, Mr. Engelhart Cornelius    male  65.00      0      1              113509   61.9792              B30        C
55            56         1       1                                                                   Woolner, Mr. Hugh    male    NaN      0      0               19947   35.5000              C52        S
56            57         1       2                                                                   Rugg, Miss. Emily  female  21.00      0      0          C.A. 31026   10.5000              NaN        S
57            58         0       3                                                                 Novel, Mr. Mansouer    male  28.50      0      0                2697    7.2292              NaN        C
58            59         1       2                                                        West, Miss. Constance Mirium  female   5.00      1      2          C.A. 34651   27.7500              NaN        S
59            60         0       3                                                  Goodwin, Master. William Frederick    male  11.00      5      2             CA 2144   46.9000              NaN        S
60            61         0       3                                                               Sirayanian, Mr. Orsen    male  22.00      0      0                2669    7.2292              NaN        C
61            62         1       1                                                                 Icard, Miss. Amelie  female  38.00      0      0              113572   80.0000              B28      NaN
62            63         0       1                                                         Harris, Mr. Henry Birkhardt    male  45.00      1      0               36973   83.4750              C83        S
63            64         0       3                                                               Skoog, Master. Harald    male   4.00      3      2              347088   27.9000              NaN        S
64            65         0       1                                                               Stewart, Mr. Albert A    male    NaN      0      0            PC 17605   27.7208              NaN        C
65            66         1       3                                                            Moubarek, Master. Gerios    male    NaN      1      1                2661   15.2458              NaN        C
66            67         1       2                                                        Nye, Mrs. (Elizabeth Ramell)  female  29.00      0      0          C.A. 29395   10.5000              F33        S
67            68         0       3                                                            Crease, Mr. Ernest James    male  19.00      0      0           S.P. 3464    8.1583              NaN        S
68            69         1       3                                                     Andersson, Miss. Erna Alexandra  female  17.00      4      2             3101281    7.9250              NaN        S
69            70         0       3                                                                   Kink, Mr. Vincenz    male  26.00      2      0              315151    8.6625              NaN        S
70            71         0       2                                                          Jenkin, Mr. Stephen Curnow    male  32.00      0      0          C.A. 33111   10.5000              NaN        S
71            72         0       3                                                          Goodwin, Miss. Lillian Amy  female  16.00      5      2             CA 2144   46.9000              NaN        S
72            73         0       2                                                                Hood, Mr. Ambrose Jr    male  21.00      0      0        S.O.C. 14879   73.5000              NaN        S
73            74         0       3                                                         Chronopoulos, Mr. Apostolos    male  26.00      1      0                2680   14.4542              NaN        C
74            75         1       3                                                                       Bing, Mr. Lee    male  32.00      0      0                1601   56.4958              NaN        S
75            76         0       3                                                             Moen, Mr. Sigurd Hansen    male  25.00      0      0              348123    7.6500            F G73        S
76            77         0       3                                                                   Staneff, Mr. Ivan    male    NaN      0      0              349208    7.8958              NaN        S
77            78         0       3                                                            Moutal, Mr. Rahamin Haim    male    NaN      0      0              374746    8.0500              NaN        S
78            79         1       2                                                       Caldwell, Master. Alden Gates    male   0.83      0      2              248738   29.0000              NaN        S
79            80         1       3                                                            Dowdell, Miss. Elizabeth  female  30.00      0      0              364516   12.4750              NaN        S
80            81         0       3                                                                Waelens, Mr. Achille    male  22.00      0      0              345767    9.0000              NaN        S
81            82         1       3                                                         Sheerlinck, Mr. Jan Baptist    male  29.00      0      0              345779    9.5000              NaN        S
82            83         1       3                                                      McDermott, Miss. Brigdet Delia  female    NaN      0      0              330932    7.7875              NaN        Q
83            84         0       1                                                             Carrau, Mr. Francisco M    male  28.00      0      0              113059   47.1000              NaN        S
84            85         1       2                                                                 Ilett, Miss. Bertha  female  17.00      0      0          SO/C 14885   10.5000              NaN        S
85            86         1       3                             Backstrom, Mrs. Karl Alfred (Maria Mathilda Gustafsson)  female  33.00      3      0             3101278   15.8500              NaN        S
86            87         0       3                                                              Ford, Mr. William Neal    male  16.00      1      3          W./C. 6608   34.3750              NaN        S
87            88         0       3                                                       Slocovski, Mr. Selman Francis    male    NaN      0      0     SOTON/OQ 392086    8.0500              NaN        S
88            89         1       1                                                          Fortune, Miss. Mabel Helen  female  23.00      3      2               19950  263.0000      C23 C25 C27        S
89            90         0       3                                                              Celotti, Mr. Francesco    male  24.00      0      0              343275    8.0500              NaN        S
90            91         0       3                                                                Christmann, Mr. Emil    male  29.00      0      0              343276    8.0500              NaN        S
91            92         0       3                                                          Andreasson, Mr. Paul Edvin    male  20.00      0      0              347466    7.8542              NaN        S
92            93         0       1                                                         Chaffee, Mr. Herbert Fuller    male  46.00      1      0         W.E.P. 5734   61.1750              E31        S
93            94         0       3                                                             Dean, Mr. Bertram Frank    male  26.00      1      2           C.A. 2315   20.5750              NaN        S
94            95         0       3                                                                   Coxon, Mr. Daniel    male  59.00      0      0              364500    7.2500              NaN        S
95            96         0       3                                                         Shorney, Mr. Charles Joseph    male    NaN      0      0              374910    8.0500              NaN        S
96            97         0       1                                                           Goldschmidt, Mr. George B    male  71.00      0      0            PC 17754   34.6542               A5        C
97            98         1       1                                                     Greenfield, Mr. William Bertram    male  23.00      0      1            PC 17759   63.3583          D10 D12        C
98            99         1       2                                                Doling, Mrs. John T (Ada Julia Bone)  female  34.00      0      1              231919   23.0000              NaN        S
99           100         0       2                                                                   Kantor, Mr. Sinai    male  34.00      1      0              244367   26.0000              NaN        S
100          101         0       3                                                             Petranec, Miss. Matilda  female  28.00      0      0              349245    7.8958              NaN        S
101          102         0       3                                                    Petroff, Mr. Pastcho ("Pentcho")    male    NaN      0      0              349215    7.8958              NaN        S
102          103         0       1                                                           White, Mr. Richard Frasar    male  21.00      0      1               35281   77.2875              D26        S
103          104         0       3                                                          Johansson, Mr. Gustaf Joel    male  33.00      0      0                7540    8.6542              NaN        S
104          105         0       3                                                      Gustafsson, Mr. Anders Vilhelm    male  37.00      2      0             3101276    7.9250              NaN        S
105          106         0       3                                                               Mionoff, Mr. Stoytcho    male  28.00      0      0              349207    7.8958              NaN        S
106          107         1       3                                                    Salkjelsvik, Miss. Anna Kristine  female  21.00      0      0              343120    7.6500              NaN        S
107          108         1       3                                                              Moss, Mr. Albert Johan    male    NaN      0      0              312991    7.7750              NaN        S
108          109         0       3                                                                     Rekic, Mr. Tido    male  38.00      0      0              349249    7.8958              NaN        S
109          110         1       3                                                                 Moran, Miss. Bertha  female    NaN      1      0              371110   24.1500              NaN        Q
110          111         0       1                                                      Porter, Mr. Walter Chamberlain    male  47.00      0      0              110465   52.0000             C110        S
111          112         0       3                                                                Zabour, Miss. Hileni  female  14.50      1      0                2665   14.4542              NaN        C
112          113         0       3                                                              Barton, Mr. David John    male  22.00      0      0              324669    8.0500              NaN        S
113          114         0       3                                                             Jussila, Miss. Katriina  female  20.00      1      0                4136    9.8250              NaN        S
114          115         0       3                                                               Attalah, Miss. Malake  female  17.00      0      0                2627   14.4583              NaN        C
115          116         0       3                                                               Pekoniemi, Mr. Edvard    male  21.00      0      0   STON/O 2. 3101294    7.9250              NaN        S
116          117         0       3                                                                Connors, Mr. Patrick    male  70.50      0      0              370369    7.7500              NaN        Q
117          118         0       2                                                     Turpin, Mr. William John Robert    male  29.00      1      0               11668   21.0000              NaN        S
118          119         0       1                                                            Baxter, Mr. Quigg Edmond    male  24.00      0      1            PC 17558  247.5208          B58 B60        C
119          120         0       3                                                   Andersson, Miss. Ellis Anna Maria  female   2.00      4      2              347082   31.2750              NaN        S
120          121         0       2                                                         Hickman, Mr. Stanley George    male  21.00      2      0        S.O.C. 14879   73.5000              NaN        S
121          122         0       3                                                          Moore, Mr. Leonard Charles    male    NaN      0      0           A4. 54510    8.0500              NaN        S
122          123         0       2                                                                Nasser, Mr. Nicholas    male  32.50      1      0              237736   30.0708              NaN        C
123          124         1       2                                                                 Webber, Miss. Susan  female  32.50      0      0               27267   13.0000             E101        S
124          125         0       1                                                         White, Mr. Percival Wayland    male  54.00      0      1               35281   77.2875              D26        S
125          126         1       3                                                        Nicola-Yarred, Master. Elias    male  12.00      1      0                2651   11.2417              NaN        C
126          127         0       3                                                                 McMahon, Mr. Martin    male    NaN      0      0              370372    7.7500              NaN        Q
127          128         1       3                                                           Madsen, Mr. Fridtjof Arne    male  24.00      0      0             C 17369    7.1417              NaN        S
128          129         1       3                                                                   Peter, Miss. Anna  female    NaN      1      1                2668   22.3583            F E69        C
129          130         0       3                                                                  Ekstrom, Mr. Johan    male  45.00      0      0              347061    6.9750              NaN        S
130          131         0       3                                                                Drazenoic, Mr. Jozef    male  33.00      0      0              349241    7.8958              NaN        C
131          132         0       3                                                      Coelho, Mr. Domingos Fernandeo    male  20.00      0      0  SOTON/O.Q. 3101307    7.0500              NaN        S
132          133         0       3                                      Robins, Mrs. Alexander A (Grace Charity Laury)  female  47.00      1      0           A/5. 3337   14.5000              NaN        S
133          134         1       2                                       Weisz, Mrs. Leopold (Mathilde Francoise Pede)  female  29.00      1      0              228414   26.0000              NaN        S
134          135         0       2                                                      Sobey, Mr. Samuel James Hayden    male  25.00      0      0          C.A. 29178   13.0000              NaN        S
135          136         0       2                                                                  Richard, Mr. Emile    male  23.00      0      0       SC/PARIS 2133   15.0458              NaN        C
136          137         1       1                                                        Newsom, Miss. Helen Monypeny  female  19.00      0      2               11752   26.2833              D47        S
137          138         0       1                                                         Futrelle, Mr. Jacques Heath    male  37.00      1      0              113803   53.1000             C123        S
138          139         0       3                                                                 Osen, Mr. Olaf Elon    male  16.00      0      0                7534    9.2167              NaN        S
139          140         0       1                                                                  Giglio, Mr. Victor    male  24.00      0      0            PC 17593   79.2000              B86        C
140          141         0       3                                                       Boulos, Mrs. Joseph (Sultana)  female    NaN      0      2                2678   15.2458              NaN        C
141          142         1       3                                                            Nysten, Miss. Anna Sofia  female  22.00      0      0              347081    7.7500              NaN        S
142          143         1       3                                Hakkarainen, Mrs. Pekka Pietari (Elin Matilda Dolck)  female  24.00      1      0    STON/O2. 3101279   15.8500              NaN        S
143          144         0       3                                                                 Burke, Mr. Jeremiah    male  19.00      0      0              365222    6.7500              NaN        Q
144          145         0       2                                                          Andrew, Mr. Edgardo Samuel    male  18.00      0      0              231945   11.5000              NaN        S
145          146         0       2                                                        Nicholls, Mr. Joseph Charles    male  19.00      1      1          C.A. 33112   36.7500              NaN        S
146          147         1       3                                        Andersson, Mr. August Edvard ("Wennerstrom")    male  27.00      0      0              350043    7.7958              NaN        S
147          148         0       3                                                    Ford, Miss. Robina Maggie "Ruby"  female   9.00      2      2          W./C. 6608   34.3750              NaN        S
148          149         0       2                                            Navratil, Mr. Michel ("Louis M Hoffman")    male  36.50      0      2              230080   26.0000               F2        S
149          150         0       2                                                   Byles, Rev. Thomas Roussel Davids    male  42.00      0      0              244310   13.0000              NaN        S
150          151         0       2                                                          Bateman, Rev. Robert James    male  51.00      0      0         S.O.P. 1166   12.5250              NaN        S
151          152         1       1                                                   Pears, Mrs. Thomas (Edith Wearne)  female  22.00      1      0              113776   66.6000               C2        S
152          153         0       3                                                                    Meo, Mr. Alfonzo    male  55.50      0      0          A.5. 11206    8.0500              NaN        S
153          154         0       3                                                     van Billiard, Mr. Austin Blyler    male  40.50      0      2            A/5. 851   14.5000              NaN        S
154          155         0       3                                                               Olsen, Mr. Ole Martin    male    NaN      0      0           Fa 265302    7.3125              NaN        S
155          156         0       1                                                         Williams, Mr. Charles Duane    male  51.00      0      1            PC 17597   61.3792              NaN        C
156          157         1       3                                                    Gilnagh, Miss. Katherine "Katie"  female  16.00      0      0               35851    7.7333              NaN        Q
157          158         0       3                                                                     Corn, Mr. Harry    male  30.00      0      0     SOTON/OQ 392090    8.0500              NaN        S
158          159         0       3                                                                 Smiljanic, Mr. Mile    male    NaN      0      0              315037    8.6625              NaN        S
159          160         0       3                                                          Sage, Master. Thomas Henry    male    NaN      8      2            CA. 2343   69.5500              NaN        S
160          161         0       3                                                            Cribb, Mr. John Hatfield    male  44.00      0      1              371362   16.1000              NaN        S
161          162         1       2                                  Watt, Mrs. James (Elizabeth "Bessie" Inglis Milne)  female  40.00      0      0          C.A. 33595   15.7500              NaN        S
162          163         0       3                                                          Bengtsson, Mr. John Viktor    male  26.00      0      0              347068    7.7750              NaN        S
163          164         0       3                                                                     Calic, Mr. Jovo    male  17.00      0      0              315093    8.6625              NaN        S
164          165         0       3                                                        Panula, Master. Eino Viljami    male   1.00      4      1             3101295   39.6875              NaN        S
165          166         1       3                                     Goldsmith, Master. Frank John William "Frankie"    male   9.00      0      2              363291   20.5250              NaN        S
166          167         1       1                                              Chibnall, Mrs. (Edith Martha Bowerman)  female    NaN      0      1              113505   55.0000              E33        S
167          168         0       3                                     Skoog, Mrs. William (Anna Bernhardina Karlsson)  female  45.00      1      4              347088   27.9000              NaN        S
168          169         0       1                                                                 Baumann, Mr. John D    male    NaN      0      0            PC 17318   25.9250              NaN        S
169          170         0       3                                                                       Ling, Mr. Lee    male  28.00      0      0                1601   56.4958              NaN        S
170          171         0       1                                                           Van der hoef, Mr. Wyckoff    male  61.00      0      0              111240   33.5000              B19        S
171          172         0       3                                                                Rice, Master. Arthur    male   4.00      4      1              382652   29.1250              NaN        Q
172          173         1       3                                                        Johnson, Miss. Eleanor Ileen  female   1.00      1      1              347742   11.1333              NaN        S
173          174         0       3                                                           Sivola, Mr. Antti Wilhelm    male  21.00      0      0   STON/O 2. 3101280    7.9250              NaN        S
174          175         0       1                                                             Smith, Mr. James Clinch    male  56.00      0      0               17764   30.6958               A7        C
175          176         0       3                                                              Klasen, Mr. Klas Albin    male  18.00      1      1              350404    7.8542              NaN        S
176          177         0       3                                                       Lefebre, Master. Henry Forbes    male    NaN      3      1                4133   25.4667              NaN        S
177          178         0       1                                                          Isham, Miss. Ann Elizabeth  female  50.00      0      0            PC 17595   28.7125              C49        C
178          179         0       2                                                                  Hale, Mr. Reginald    male  30.00      0      0              250653   13.0000              NaN        S
179          180         0       3                                                                 Leonard, Mr. Lionel    male  36.00      0      0                LINE    0.0000              NaN        S
180          181         0       3                                                        Sage, Miss. Constance Gladys  female    NaN      8      2            CA. 2343   69.5500              NaN        S
181          182         0       2                                                                    Pernot, Mr. Rene    male    NaN      0      0       SC/PARIS 2131   15.0500              NaN        C
182          183         0       3                                               Asplund, Master. Clarence Gustaf Hugo    male   9.00      4      2              347077   31.3875              NaN        S
183          184         1       2                                                           Becker, Master. Richard F    male   1.00      2      1              230136   39.0000               F4        S
184          185         1       3                                                 Kink-Heilmann, Miss. Luise Gretchen  female   4.00      0      2              315153   22.0250              NaN        S
185          186         0       1                                                               Rood, Mr. Hugh Roscoe    male    NaN      0      0              113767   50.0000              A32        S
186          187         1       3                                     O'Brien, Mrs. Thomas (Johanna "Hannah" Godfrey)  female    NaN      1      0              370365   15.5000              NaN        Q
187          188         1       1                                       Romaine, Mr. Charles Hallace ("Mr C Rolmane")    male  45.00      0      0              111428   26.5500              NaN        S
188          189         0       3                                                                    Bourke, Mr. John    male  40.00      1      1              364849   15.5000              NaN        Q
189          190         0       3                                                                 Turcin, Mr. Stjepan    male  36.00      0      0              349247    7.8958              NaN        S
190          191         1       2                                                                 Pinsky, Mrs. (Rosa)  female  32.00      0      0              234604   13.0000              NaN        S
191          192         0       2                                                               Carbines, Mr. William    male  19.00      0      0               28424   13.0000              NaN        S
192          193         1       3                                     Andersen-Jensen, Miss. Carla Christine Nielsine  female  19.00      1      0              350046    7.8542              NaN        S
193          194         1       2                                                          Navratil, Master. Michel M    male   3.00      1      1              230080   26.0000               F2        S
194          195         1       1                                           Brown, Mrs. James Joseph (Margaret Tobin)  female  44.00      0      0            PC 17610   27.7208               B4        C
195          196         1       1                                                                Lurette, Miss. Elise  female  58.00      0      0            PC 17569  146.5208              B80        C
196          197         0       3                                                                 Mernagh, Mr. Robert    male    NaN      0      0              368703    7.7500              NaN        Q
197          198         0       3                                                    Olsen, Mr. Karl Siegwart Andreas    male  42.00      0      1                4579    8.4042              NaN        S
198          199         1       3                                                    Madigan, Miss. Margaret "Maggie"  female    NaN      0      0              370370    7.7500              NaN        Q
199          200         0       2                                              Yrois, Miss. Henriette ("Mrs Harbeck")  female  24.00      0      0              248747   13.0000              NaN        S
200          201         0       3                                                      Vande Walle, Mr. Nestor Cyriel    male  28.00      0      0              345770    9.5000              NaN        S
201          202         0       3                                                                 Sage, Mr. Frederick    male    NaN      8      2            CA. 2343   69.5500              NaN        S
202          203         0       3                                                          Johanson, Mr. Jakob Alfred    male  34.00      0      0             3101264    6.4958              NaN        S
203          204         0       3                                                                Youseff, Mr. Gerious    male  45.50      0      0                2628    7.2250              NaN        C
204          205         1       3                                                            Cohen, Mr. Gurshon "Gus"    male  18.00      0      0            A/5 3540    8.0500              NaN        S
205          206         0       3                                                          Strom, Miss. Telma Matilda  female   2.00      0      1              347054   10.4625               G6        S
206          207         0       3                                                          Backstrom, Mr. Karl Alfred    male  32.00      1      0             3101278   15.8500              NaN        S
207          208         1       3                                                         Albimona, Mr. Nassef Cassem    male  26.00      0      0                2699   18.7875              NaN        C
208          209         1       3                                                           Carr, Miss. Helen "Ellen"  female  16.00      0      0              367231    7.7500              NaN        Q
209          210         1       1                                                                    Blank, Mr. Henry    male  40.00      0      0              112277   31.0000              A31        C
210          211         0       3                                                                      Ali, Mr. Ahmed    male  24.00      0      0  SOTON/O.Q. 3101311    7.0500              NaN        S
211          212         1       2                                                          Cameron, Miss. Clear Annie  female  35.00      0      0        F.C.C. 13528   21.0000              NaN        S
212          213         0       3                                                              Perkin, Mr. John Henry    male  22.00      0      0           A/5 21174    7.2500              NaN        S
213          214         0       2                                                         Givard, Mr. Hans Kristensen    male  30.00      0      0              250646   13.0000              NaN        S
214          215         0       3                                                                 Kiernan, Mr. Philip    male    NaN      1      0              367229    7.7500              NaN        Q
215          216         1       1                                                             Newell, Miss. Madeleine  female  31.00      1      0               35273  113.2750              D36        C
216          217         1       3                                                              Honkanen, Miss. Eliina  female  27.00      0      0    STON/O2. 3101283    7.9250              NaN        S
217          218         0       2                                                        Jacobsohn, Mr. Sidney Samuel    male  42.00      1      0              243847   27.0000              NaN        S
218          219         1       1                                                               Bazzani, Miss. Albina  female  32.00      0      0               11813   76.2917              D15        C
219          220         0       2                                                                  Harris, Mr. Walter    male  30.00      0      0           W/C 14208   10.5000              NaN        S
220          221         1       3                                                      Sunderland, Mr. Victor Francis    male  16.00      0      0     SOTON/OQ 392089    8.0500              NaN        S
221          222         0       2                                                                Bracken, Mr. James H    male  27.00      0      0              220367   13.0000              NaN        S
222          223         0       3                                                             Green, Mr. George Henry    male  51.00      0      0               21440    8.0500              NaN        S
223          224         0       3                                                                Nenkoff, Mr. Christo    male    NaN      0      0              349234    7.8958              NaN        S
224          225         1       1                                                        Hoyt, Mr. Frederick Maxfield    male  38.00      1      0               19943   90.0000              C93        S
225          226         0       3                                                        Berglund, Mr. Karl Ivar Sven    male  22.00      0      0             PP 4348    9.3500              NaN        S
226          227         1       2                                                           Mellors, Mr. William John    male  19.00      0      0           SW/PP 751   10.5000              NaN        S
227          228         0       3                                                     Lovell, Mr. John Hall ("Henry")    male  20.50      0      0           A/5 21173    7.2500              NaN        S
228          229         0       2                                                           Fahlstrom, Mr. Arne Jonas    male  18.00      0      0              236171   13.0000              NaN        S
229          230         0       3                                                             Lefebre, Miss. Mathilde  female    NaN      3      1                4133   25.4667              NaN        S
230          231         1       1                                        Harris, Mrs. Henry Birkhardt (Irene Wallach)  female  35.00      1      0               36973   83.4750              C83        S
231          232         0       3                                                            Larsson, Mr. Bengt Edvin    male  29.00      0      0              347067    7.7750              NaN        S
232          233         0       2                                                           Sjostedt, Mr. Ernst Adolf    male  59.00      0      0              237442   13.5000              NaN        S
233          234         1       3                                                      Asplund, Miss. Lillian Gertrud  female   5.00      4      2              347077   31.3875              NaN        S
234          235         0       2                                                   Leyson, Mr. Robert William Norman    male  24.00      0      0          C.A. 29566   10.5000              NaN        S
235          236         0       3                                                        Harknett, Miss. Alice Phoebe  female    NaN      0      0          W./C. 6609    7.5500              NaN        S
236          237         0       2                                                                   Hold, Mr. Stephen    male  44.00      1      0               26707   26.0000              NaN        S
237          238         1       2                                                    Collyer, Miss. Marjorie "Lottie"  female   8.00      0      2          C.A. 31921   26.2500              NaN        S
238          239         0       2                                                     Pengelly, Mr. Frederick William    male  19.00      0      0               28665   10.5000              NaN        S
239          240         0       2                                                              Hunt, Mr. George Henry    male  33.00      0      0          SCO/W 1585   12.2750              NaN        S
240          241         0       3                                                               Zabour, Miss. Thamine  female    NaN      1      0                2665   14.4542              NaN        C
241          242         1       3                                                      Murphy, Miss. Katherine "Kate"  female    NaN      1      0              367230   15.5000              NaN        Q
242          243         0       2                                                     Coleridge, Mr. Reginald Charles    male  29.00      0      0         W./C. 14263   10.5000              NaN        S
243          244         0       3                                                       Maenpaa, Mr. Matti Alexanteri    male  22.00      0      0   STON/O 2. 3101275    7.1250              NaN        S
244          245         0       3                                                                Attalah, Mr. Sleiman    male  30.00      0      0                2694    7.2250              NaN        C
245          246         0       1                                                         Minahan, Dr. William Edward    male  44.00      2      0               19928   90.0000              C78        Q
246          247         0       3                                               Lindahl, Miss. Agda Thorilda Viktoria  female  25.00      0      0              347071    7.7750              NaN        S
247          248         1       2                                                     Hamalainen, Mrs. William (Anna)  female  24.00      0      2              250649   14.5000              NaN        S
248          249         1       1                                                       Beckwith, Mr. Richard Leonard    male  37.00      1      1               11751   52.5542              D35        S
249          250         0       2                                                       Carter, Rev. Ernest Courtenay    male  54.00      1      0              244252   26.0000              NaN        S
250          251         0       3                                                              Reed, Mr. James George    male    NaN      0      0              362316    7.2500              NaN        S
251          252         0       3                                          Strom, Mrs. Wilhelm (Elna Matilda Persson)  female  29.00      1      1              347054   10.4625               G6        S
252          253         0       1                                                           Stead, Mr. William Thomas    male  62.00      0      0              113514   26.5500              C87        S
253          254         0       3                                                            Lobb, Mr. William Arthur    male  30.00      1      0           A/5. 3336   16.1000              NaN        S
254          255         0       3                                            Rosblom, Mrs. Viktor (Helena Wilhelmina)  female  41.00      0      2              370129   20.2125              NaN        S
255          256         1       3                                             Touma, Mrs. Darwis (Hanne Youssef Razi)  female  29.00      0      2                2650   15.2458              NaN        C
256          257         1       1                                                      Thorne, Mrs. Gertrude Maybelle  female    NaN      0      0            PC 17585   79.2000              NaN        C
257          258         1       1                                                                Cherry, Miss. Gladys  female  30.00      0      0              110152   86.5000              B77        S
258          259         1       1                                                                    Ward, Miss. Anna  female  35.00      0      0            PC 17755  512.3292              NaN        C
259          260         1       2                                                         Parrish, Mrs. (Lutie Davis)  female  50.00      0      1              230433   26.0000              NaN        S
260          261         0       3                                                                   Smith, Mr. Thomas    male    NaN      0      0              384461    7.7500              NaN        Q
261          262         1       3                                                   Asplund, Master. Edvin Rojj Felix    male   3.00      4      2              347077   31.3875              NaN        S
262          263         0       1                                                                   Taussig, Mr. Emil    male  52.00      1      1              110413   79.6500              E67        S
263          264         0       1                                                               Harrison, Mr. William    male  40.00      0      0              112059    0.0000              B94        S
264          265         0       3                                                                  Henry, Miss. Delia  female    NaN      0      0              382649    7.7500              NaN        Q
265          266         0       2                                                                   Reeves, Mr. David    male  36.00      0      0          C.A. 17248   10.5000              NaN        S
266          267         0       3                                                           Panula, Mr. Ernesti Arvid    male  16.00      4      1             3101295   39.6875              NaN        S
267          268         1       3                                                            Persson, Mr. Ernst Ulrik    male  25.00      1      0              347083    7.7750              NaN        S
268          269         1       1                                       Graham, Mrs. William Thompson (Edith Junkins)  female  58.00      0      1            PC 17582  153.4625             C125        S
269          270         1       1                                                              Bissette, Miss. Amelia  female  35.00      0      0            PC 17760  135.6333              C99        S
270          271         0       1                                                               Cairns, Mr. Alexander    male    NaN      0      0              113798   31.0000              NaN        S
271          272         1       3                                                        Tornquist, Mr. William Henry    male  25.00      0      0                LINE    0.0000              NaN        S
272          273         1       2                                           Mellinger, Mrs. (Elizabeth Anne Maidment)  female  41.00      0      1              250644   19.5000              NaN        S
273          274         0       1                                                               Natsch, Mr. Charles H    male  37.00      0      1            PC 17596   29.7000             C118        C
274          275         1       3                                                          Healy, Miss. Hanora "Nora"  female    NaN      0      0              370375    7.7500              NaN        Q
275          276         1       1                                                   Andrews, Miss. Kornelia Theodosia  female  63.00      1      0               13502   77.9583               D7        S
276          277         0       3                                                   Lindblom, Miss. Augusta Charlotta  female  45.00      0      0              347073    7.7500              NaN        S
277          278         0       2                                                         Parkes, Mr. Francis "Frank"    male    NaN      0      0              239853    0.0000              NaN        S
278          279         0       3                                                                  Rice, Master. Eric    male   7.00      4      1              382652   29.1250              NaN        Q
279          280         1       3                                                    Abbott, Mrs. Stanton (Rosa Hunt)  female  35.00      1      1           C.A. 2673   20.2500              NaN        S
280          281         0       3                                                                    Duane, Mr. Frank    male  65.00      0      0              336439    7.7500              NaN        Q
281          282         0       3                                                    Olsson, Mr. Nils Johan Goransson    male  28.00      0      0              347464    7.8542              NaN        S
282          283         0       3                                                           de Pelsmaeker, Mr. Alfons    male  16.00      0      0              345778    9.5000              NaN        S
283          284         1       3                                                          Dorking, Mr. Edward Arthur    male  19.00      0      0          A/5. 10482    8.0500              NaN        S
284          285         0       1                                                          Smith, Mr. Richard William    male    NaN      0      0              113056   26.0000              A19        S
285          286         0       3                                                                 Stankovic, Mr. Ivan    male  33.00      0      0              349239    8.6625              NaN        C
286          287         1       3                                                             de Mulder, Mr. Theodore    male  30.00      0      0              345774    9.5000              NaN        S
287          288         0       3                                                                Naidenoff, Mr. Penko    male  22.00      0      0              349206    7.8958              NaN        S
288          289         1       2                                                                Hosono, Mr. Masabumi    male  42.00      0      0              237798   13.0000              NaN        S
289          290         1       3                                                                Connolly, Miss. Kate  female  22.00      0      0              370373    7.7500              NaN        Q
290          291         1       1                                                        Barber, Miss. Ellen "Nellie"  female  26.00      0      0               19877   78.8500              NaN        S
291          292         1       1                                             Bishop, Mrs. Dickinson H (Helen Walton)  female  19.00      1      0               11967   91.0792              B49        C
292          293         0       2                                                              Levy, Mr. Rene Jacques    male  36.00      0      0       SC/Paris 2163   12.8750                D        C
293          294         0       3                                                                 Haas, Miss. Aloisia  female  24.00      0      0              349236    8.8500              NaN        S
294          295         0       3                                                                    Mineff, Mr. Ivan    male  24.00      0      0              349233    7.8958              NaN        S
295          296         0       1                                                                   Lewy, Mr. Ervin G    male    NaN      0      0            PC 17612   27.7208              NaN        C
296          297         0       3                                                                  Hanna, Mr. Mansour    male  23.50      0      0                2693    7.2292              NaN        C
297          298         0       1                                                        Allison, Miss. Helen Loraine  female   2.00      1      2              113781  151.5500          C22 C26        S
298          299         1       1                                                               Saalfeld, Mr. Adolphe    male    NaN      0      0               19988   30.5000             C106        S
299          300         1       1                                     Baxter, Mrs. James (Helene DeLaudeniere Chaput)  female  50.00      0      1            PC 17558  247.5208          B58 B60        C
300          301         1       3                                            Kelly, Miss. Anna Katherine "Annie Kate"  female    NaN      0      0                9234    7.7500              NaN        Q
301          302         1       3                                                                  McCoy, Mr. Bernard    male    NaN      2      0              367226   23.2500              NaN        Q
302          303         0       3                                                     Johnson, Mr. William Cahoone Jr    male  19.00      0      0                LINE    0.0000              NaN        S
303          304         1       2                                                                 Keane, Miss. Nora A  female    NaN      0      0              226593   12.3500             E101        Q
304          305         0       3                                                   Williams, Mr. Howard Hugh "Harry"    male    NaN      0      0            A/5 2466    8.0500              NaN        S
305          306         1       1                                                      Allison, Master. Hudson Trevor    male   0.92      1      2              113781  151.5500          C22 C26        S
306          307         1       1                                                             Fleming, Miss. Margaret  female    NaN      0      0               17421  110.8833              NaN        C
307          308         1       1  Penasco y Castellana, Mrs. Victor de Satode (Maria Josefa Perez de Soto y Vallejo)  female  17.00      1      0            PC 17758  108.9000              C65        C
308          309         0       2                                                                 Abelson, Mr. Samuel    male  30.00      1      0           P/PP 3381   24.0000              NaN        C
309          310         1       1                                                      Francatelli, Miss. Laura Mabel  female  30.00      0      0            PC 17485   56.9292              E36        C
310          311         1       1                                                      Hays, Miss. Margaret Bechstein  female  24.00      0      0               11767   83.1583              C54        C
311          312         1       1                                                          Ryerson, Miss. Emily Borie  female  18.00      2      2            PC 17608  262.3750  B57 B59 B63 B66        C
312          313         0       2                                               Lahtinen, Mrs. William (Anna Sylfven)  female  26.00      1      1              250651   26.0000              NaN        S
313          314         0       3                                                              Hendekovic, Mr. Ignjac    male  28.00      0      0              349243    7.8958              NaN        S
314          315         0       2                                                                  Hart, Mr. Benjamin    male  43.00      1      1        F.C.C. 13529   26.2500              NaN        S
315          316         1       3                                                     Nilsson, Miss. Helmina Josefina  female  26.00      0      0              347470    7.8542              NaN        S
316          317         1       2                                                 Kantor, Mrs. Sinai (Miriam Sternin)  female  24.00      1      0              244367   26.0000              NaN        S
317          318         0       2                                                                Moraweck, Dr. Ernest    male  54.00      0      0               29011   14.0000              NaN        S
318          319         1       1                                                            Wick, Miss. Mary Natalie  female  31.00      0      2               36928  164.8667               C7        S
319          320         1       1                            Spedden, Mrs. Frederic Oakley (Margaretta Corning Stone)  female  40.00      1      1               16966  134.5000              E34        C
320          321         0       3                                                                  Dennis, Mr. Samuel    male  22.00      0      0           A/5 21172    7.2500              NaN        S
321          322         0       3                                                                    Danoff, Mr. Yoto    male  27.00      0      0              349219    7.8958              NaN        S
322          323         1       2                                                           Slayter, Miss. Hilda Mary  female  30.00      0      0              234818   12.3500              NaN        Q
323          324         1       2                                 Caldwell, Mrs. Albert Francis (Sylvia Mae Harbaugh)  female  22.00      1      1              248738   29.0000              NaN        S
324          325         0       3                                                            Sage, Mr. George John Jr    male    NaN      8      2            CA. 2343   69.5500              NaN        S
325          326         1       1                                                            Young, Miss. Marie Grice  female  36.00      0      0            PC 17760  135.6333              C32        C
326          327         0       3                                                           Nysveen, Mr. Johan Hansen    male  61.00      0      0              345364    6.2375              NaN        S
327          328         1       2                                                             Ball, Mrs. (Ada E Hall)  female  36.00      0      0               28551   13.0000                D        S
328          329         1       3                                      Goldsmith, Mrs. Frank John (Emily Alice Brown)  female  31.00      1      1              363291   20.5250              NaN        S
329          330         1       1                                                        Hippach, Miss. Jean Gertrude  female  16.00      0      1              111361   57.9792              B18        C
330          331         1       3                                                                  McCoy, Miss. Agnes  female    NaN      2      0              367226   23.2500              NaN        Q
331          332         0       1                                                                 Partner, Mr. Austen    male  45.50      0      0              113043   28.5000             C124        S
332          333         0       1                                                           Graham, Mr. George Edward    male  38.00      0      1            PC 17582  153.4625              C91        S
333          334         0       3                                                     Vander Planke, Mr. Leo Edmondus    male  16.00      2      0              345764   18.0000              NaN        S
334          335         1       1                                  Frauenthal, Mrs. Henry William (Clara Heinsheimer)  female    NaN      1      0            PC 17611  133.6500              NaN        S
335          336         0       3                                                                  Denkoff, Mr. Mitto    male    NaN      0      0              349225    7.8958              NaN        S
336          337         0       1                                                           Pears, Mr. Thomas Clinton    male  29.00      1      0              113776   66.6000               C2        S
337          338         1       1                                                     Burns, Miss. Elizabeth Margaret  female  41.00      0      0               16966  134.5000              E40        C
338          339         1       3                                                               Dahl, Mr. Karl Edwart    male  45.00      0      0                7598    8.0500              NaN        S
339          340         0       1                                                        Blackwell, Mr. Stephen Weart    male  45.00      0      0              113784   35.5000                T        S
340          341         1       2                                                      Navratil, Master. Edmond Roger    male   2.00      1      1              230080   26.0000               F2        S
341          342         1       1                                                      Fortune, Miss. Alice Elizabeth  female  24.00      3      2               19950  263.0000      C23 C25 C27        S
342          343         0       2                                                          Collander, Mr. Erik Gustaf    male  28.00      0      0              248740   13.0000              NaN        S
343          344         0       2                                          Sedgwick, Mr. Charles Frederick Waddington    male  25.00      0      0              244361   13.0000              NaN        S
344          345         0       2                                                             Fox, Mr. Stanley Hubert    male  36.00      0      0              229236   13.0000              NaN        S
345          346         1       2                                                       Brown, Miss. Amelia "Mildred"  female  24.00      0      0              248733   13.0000              F33        S
346          347         1       2                                                           Smith, Miss. Marion Elsie  female  40.00      0      0               31418   13.0000              NaN        S
347          348         1       3                                           Davison, Mrs. Thomas Henry (Mary E Finck)  female    NaN      1      0              386525   16.1000              NaN        S
348          349         1       3                                              Coutts, Master. William Loch "William"    male   3.00      1      1          C.A. 37671   15.9000              NaN        S
349          350         0       3                                                                    Dimic, Mr. Jovan    male  42.00      0      0              315088    8.6625              NaN        S
350          351         0       3                                                              Odahl, Mr. Nils Martin    male  23.00      0      0                7267    9.2250              NaN        S
351          352         0       1                                              Williams-Lambert, Mr. Fletcher Fellows    male    NaN      0      0              113510   35.0000             C128        S
352          353         0       3                                                                  Elias, Mr. Tannous    male  15.00      1      1                2695    7.2292              NaN        C
353          354         0       3                                                           Arnold-Franchi, Mr. Josef    male  25.00      1      0              349237   17.8000              NaN        S
354          355         0       3                                                                   Yousif, Mr. Wazli    male    NaN      0      0                2647    7.2250              NaN        C
355          356         0       3                                                         Vanden Steen, Mr. Leo Peter    male  28.00      0      0              345783    9.5000              NaN        S
356          357         1       1                                                         Bowerman, Miss. Elsie Edith  female  22.00      0      1              113505   55.0000              E33        S
357          358         0       2                                                           Funk, Miss. Annie Clemmer  female  38.00      0      0              237671   13.0000              NaN        S
358          359         1       3                                                                McGovern, Miss. Mary  female    NaN      0      0              330931    7.8792              NaN        Q
359          360         1       3                                                   Mockler, Miss. Helen Mary "Ellie"  female    NaN      0      0              330980    7.8792              NaN        Q
360          361         0       3                                                                  Skoog, Mr. Wilhelm    male  40.00      1      4              347088   27.9000              NaN        S
361          362         0       2                                                           del Carlo, Mr. Sebastiano    male  29.00      1      0       SC/PARIS 2167   27.7208              NaN        C
362          363         0       3                                                     Barbara, Mrs. (Catherine David)  female  45.00      0      1                2691   14.4542              NaN        C
363          364         0       3                                                                     Asim, Mr. Adola    male  35.00      0      0  SOTON/O.Q. 3101310    7.0500              NaN        S
364          365         0       3                                                                 O'Brien, Mr. Thomas    male    NaN      1      0              370365   15.5000              NaN        Q
365          366         0       3                                                      Adahl, Mr. Mauritz Nils Martin    male  30.00      0      0              C 7076    7.2500              NaN        S
366          367         1       1                                    Warren, Mrs. Frank Manley (Anna Sophia Atkinson)  female  60.00      1      0              110813   75.2500              D37        C
367          368         1       3                                                      Moussa, Mrs. (Mantoura Boulos)  female    NaN      0      0                2626    7.2292              NaN        C
368          369         1       3                                                                 Jermyn, Miss. Annie  female    NaN      0      0               14313    7.7500              NaN        Q
369          370         1       1                                                       Aubart, Mme. Leontine Pauline  female  24.00      0      0            PC 17477   69.3000              B35        C
370          371         1       1                                                         Harder, Mr. George Achilles    male  25.00      1      0               11765   55.4417              E50        C
371          372         0       3                                                           Wiklund, Mr. Jakob Alfred    male  18.00      1      0             3101267    6.4958              NaN        S
372          373         0       3                                                          Beavan, Mr. William Thomas    male  19.00      0      0              323951    8.0500              NaN        S
373          374         0       1                                                                 Ringhini, Mr. Sante    male  22.00      0      0            PC 17760  135.6333              NaN        C
374          375         0       3                                                          Palsson, Miss. Stina Viola  female   3.00      3      1              349909   21.0750              NaN        S
375          376         1       1                                               Meyer, Mrs. Edgar Joseph (Leila Saks)  female    NaN      1      0            PC 17604   82.1708              NaN        C
376          377         1       3                                                     Landergren, Miss. Aurora Adelia  female  22.00      0      0              C 7077    7.2500              NaN        S
377          378         0       1                                                           Widener, Mr. Harry Elkins    male  27.00      0      2              113503  211.5000              C82        C
378          379         0       3                                                                 Betros, Mr. Tannous    male  20.00      0      0                2648    4.0125              NaN        C
379          380         0       3                                                         Gustafsson, Mr. Karl Gideon    male  19.00      0      0              347069    7.7750              NaN        S
380          381         1       1                                                               Bidois, Miss. Rosalie  female  42.00      0      0            PC 17757  227.5250              NaN        C
381          382         1       3                                                         Nakid, Miss. Maria ("Mary")  female   1.00      0      2                2653   15.7417              NaN        C
382          383         0       3                                                                  Tikkanen, Mr. Juho    male  32.00      0      0   STON/O 2. 3101293    7.9250              NaN        S
383          384         1       1                                 Holverson, Mrs. Alexander Oskar (Mary Aline Towner)  female  35.00      1      0              113789   52.0000              NaN        S
384          385         0       3                                                              Plotcharsky, Mr. Vasil    male    NaN      0      0              349227    7.8958              NaN        S
385          386         0       2                                                           Davies, Mr. Charles Henry    male  18.00      0      0        S.O.C. 14879   73.5000              NaN        S
386          387         0       3                                                     Goodwin, Master. Sidney Leonard    male   1.00      5      2             CA 2144   46.9000              NaN        S
387          388         1       2                                                                    Buss, Miss. Kate  female  36.00      0      0               27849   13.0000              NaN        S
388          389         0       3                                                                Sadlier, Mr. Matthew    male    NaN      0      0              367655    7.7292              NaN        Q
389          390         1       2                                                               Lehmann, Miss. Bertha  female  17.00      0      0             SC 1748   12.0000              NaN        C
390          391         1       1                                                          Carter, Mr. William Ernest    male  36.00      1      2              113760  120.0000          B96 B98        S
391          392         1       3                                                              Jansson, Mr. Carl Olof    male  21.00      0      0              350034    7.7958              NaN        S
392          393         0       3                                                        Gustafsson, Mr. Johan Birger    male  28.00      2      0             3101277    7.9250              NaN        S
393          394         1       1                                                              Newell, Miss. Marjorie  female  23.00      1      0               35273  113.2750              D36        C
394          395         1       3                                 Sandstrom, Mrs. Hjalmar (Agnes Charlotta Bengtsson)  female  24.00      0      2             PP 9549   16.7000               G6        S
395          396         0       3                                                                 Johansson, Mr. Erik    male  22.00      0      0              350052    7.7958              NaN        S
396          397         0       3                                                                 Olsson, Miss. Elina  female  31.00      0      0              350407    7.8542              NaN        S
397          398         0       2                                                             McKane, Mr. Peter David    male  46.00      0      0               28403   26.0000              NaN        S
398          399         0       2                                                                    Pain, Dr. Alfred    male  23.00      0      0              244278   10.5000              NaN        S
399          400         1       2                                                    Trout, Mrs. William H (Jessie L)  female  28.00      0      0              240929   12.6500              NaN        S
400          401         1       3                                                                  Niskanen, Mr. Juha    male  39.00      0      0   STON/O 2. 3101289    7.9250              NaN        S
401          402         0       3                                                                     Adams, Mr. John    male  26.00      0      0              341826    8.0500              NaN        S
402          403         0       3                                                            Jussila, Miss. Mari Aina  female  21.00      1      0                4137    9.8250              NaN        S
403          404         0       3                                                      Hakkarainen, Mr. Pekka Pietari    male  28.00      1      0    STON/O2. 3101279   15.8500              NaN        S
404          405         0       3                                                             Oreskovic, Miss. Marija  female  20.00      0      0              315096    8.6625              NaN        S
405          406         0       2                                                                  Gale, Mr. Shadrach    male  34.00      1      0               28664   21.0000              NaN        S
406          407         0       3                                                    Widegren, Mr. Carl/Charles Peter    male  51.00      0      0              347064    7.7500              NaN        S
407          408         1       2                                                      Richards, Master. William Rowe    male   3.00      1      1               29106   18.7500              NaN        S
408          409         0       3                                                   Birkeland, Mr. Hans Martin Monsen    male  21.00      0      0              312992    7.7750              NaN        S
409          410         0       3                                                                  Lefebre, Miss. Ida  female    NaN      3      1                4133   25.4667              NaN        S
410          411         0       3                                                                  Sdycoff, Mr. Todor    male    NaN      0      0              349222    7.8958              NaN        S
411          412         0       3                                                                     Hart, Mr. Henry    male    NaN      0      0              394140    6.8583              NaN        Q
412          413         1       1                                                              Minahan, Miss. Daisy E  female  33.00      1      0               19928   90.0000              C78        Q
413          414         0       2                                                      Cunningham, Mr. Alfred Fleming    male    NaN      0      0              239853    0.0000              NaN        S
414          415         1       3                                                           Sundman, Mr. Johan Julian    male  44.00      0      0   STON/O 2. 3101269    7.9250              NaN        S
415          416         0       3                                             Meek, Mrs. Thomas (Annie Louise Rowley)  female    NaN      0      0              343095    8.0500              NaN        S
416          417         1       2                                     Drew, Mrs. James Vivian (Lulu Thorne Christian)  female  34.00      1      1               28220   32.5000              NaN        S
417          418         1       2                                                       Silven, Miss. Lyyli Karoliina  female  18.00      0      2              250652   13.0000              NaN        S
418          419         0       2                                                          Matthews, Mr. William John    male  30.00      0      0               28228   13.0000              NaN        S
419          420         0       3                                                           Van Impe, Miss. Catharina  female  10.00      0      2              345773   24.1500              NaN        S
420          421         0       3                                                              Gheorgheff, Mr. Stanio    male    NaN      0      0              349254    7.8958              NaN        C
421          422         0       3                                                                 Charters, Mr. David    male  21.00      0      0          A/5. 13032    7.7333              NaN        Q
422          423         0       3                                                                  Zimmerman, Mr. Leo    male  29.00      0      0              315082    7.8750              NaN        S
423          424         0       3                              Danbom, Mrs. Ernst Gilbert (Anna Sigrid Maria Brogren)  female  28.00      1      1              347080   14.4000              NaN        S
424          425         0       3                                                         Rosblom, Mr. Viktor Richard    male  18.00      1      1              370129   20.2125              NaN        S
425          426         0       3                                                              Wiseman, Mr. Phillippe    male    NaN      0      0          A/4. 34244    7.2500              NaN        S
426          427         1       2                                         Clarke, Mrs. Charles V (Ada Maria Winfield)  female  28.00      1      0                2003   26.0000              NaN        S
427          428         1       2                 Phillips, Miss. Kate Florence ("Mrs Kate Louise Phillips Marshall")  female  19.00      0      0              250655   26.0000              NaN        S
428          429         0       3                                                                    Flynn, Mr. James    male    NaN      0      0              364851    7.7500              NaN        Q
429          430         1       3                                                  Pickard, Mr. Berk (Berk Trembisky)    male  32.00      0      0   SOTON/O.Q. 392078    8.0500              E10        S
430          431         1       1                                           Bjornstrom-Steffansson, Mr. Mauritz Hakan    male  28.00      0      0              110564   26.5500              C52        S
431          432         1       3                                   Thorneycroft, Mrs. Percival (Florence Kate White)  female    NaN      1      0              376564   16.1000              NaN        S
432          433         1       2                                 Louch, Mrs. Charles Alexander (Alice Adelaide Slow)  female  42.00      1      0          SC/AH 3085   26.0000              NaN        S
433          434         0       3                                                          Kallio, Mr. Nikolai Erland    male  17.00      0      0   STON/O 2. 3101274    7.1250              NaN        S
434          435         0       1                                                           Silvey, Mr. William Baird    male  50.00      1      0               13507   55.9000              E44        S
435          436         1       1                                                           Carter, Miss. Lucile Polk  female  14.00      1      2              113760  120.0000          B96 B98        S
436          437         0       3                                                Ford, Miss. Doolina Margaret "Daisy"  female  21.00      2      2          W./C. 6608   34.3750              NaN        S
437          438         1       2                                               Richards, Mrs. Sidney (Emily Hocking)  female  24.00      2      3               29106   18.7500              NaN        S
438          439         0       1                                                                   Fortune, Mr. Mark    male  64.00      1      4               19950  263.0000      C23 C25 C27        S
439          440         0       2                                              Kvillner, Mr. Johan Henrik Johannesson    male  31.00      0      0          C.A. 18723   10.5000              NaN        S
440          441         1       2                                         Hart, Mrs. Benjamin (Esther Ada Bloomfield)  female  45.00      1      1        F.C.C. 13529   26.2500              NaN        S
441          442         0       3                                                                     Hampe, Mr. Leon    male  20.00      0      0              345769    9.5000              NaN        S
442          443         0       3                                                           Petterson, Mr. Johan Emil    male  25.00      1      0              347076    7.7750              NaN        S
443          444         1       2                                                           Reynaldo, Ms. Encarnacion  female  28.00      0      0              230434   13.0000              NaN        S
444          445         1       3                                                   Johannesen-Bratthammer, Mr. Bernt    male    NaN      0      0               65306    8.1125              NaN        S
445          446         1       1                                                           Dodge, Master. Washington    male   4.00      0      2               33638   81.8583              A34        S
446          447         1       2                                                   Mellinger, Miss. Madeleine Violet  female  13.00      0      1              250644   19.5000              NaN        S
447          448         1       1                                                         Seward, Mr. Frederic Kimber    male  34.00      0      0              113794   26.5500              NaN        S
448          449         1       3                                                      Baclini, Miss. Marie Catherine  female   5.00      2      1                2666   19.2583              NaN        C
449          450         1       1                                                      Peuchen, Major. Arthur Godfrey    male  52.00      0      0              113786   30.5000             C104        S
450          451         0       2                                                               West, Mr. Edwy Arthur    male  36.00      1      2          C.A. 34651   27.7500              NaN        S
451          452         0       3                                                     Hagland, Mr. Ingvald Olai Olsen    male    NaN      1      0               65303   19.9667              NaN        S
452          453         0       1                                                     Foreman, Mr. Benjamin Laventall    male  30.00      0      0              113051   27.7500             C111        C
453          454         1       1                                                            Goldenberg, Mr. Samuel L    male  49.00      1      0               17453   89.1042              C92        C
454          455         0       3                                                                 Peduzzi, Mr. Joseph    male    NaN      0      0            A/5 2817    8.0500              NaN        S
455          456         1       3                                                                  Jalsevac, Mr. Ivan    male  29.00      0      0              349240    7.8958              NaN        C
456          457         0       1                                                           Millet, Mr. Francis Davis    male  65.00      0      0               13509   26.5500              E38        S
457          458         1       1                                                   Kenyon, Mrs. Frederick R (Marion)  female    NaN      1      0               17464   51.8625              D21        S
458          459         1       2                                                                 Toomey, Miss. Ellen  female  50.00      0      0        F.C.C. 13531   10.5000              NaN        S
459          460         0       3                                                               O'Connor, Mr. Maurice    male    NaN      0      0              371060    7.7500              NaN        Q
460          461         1       1                                                                 Anderson, Mr. Harry    male  48.00      0      0               19952   26.5500              E12        S
461          462         0       3                                                                 Morley, Mr. William    male  34.00      0      0              364506    8.0500              NaN        S
462          463         0       1                                                                   Gee, Mr. Arthur H    male  47.00      0      0              111320   38.5000              E63        S
463          464         0       2                                                        Milling, Mr. Jacob Christian    male  48.00      0      0              234360   13.0000              NaN        S
464          465         0       3                                                                  Maisner, Mr. Simon    male    NaN      0      0            A/S 2816    8.0500              NaN        S
465          466         0       3                                                     Goncalves, Mr. Manuel Estanslas    male  38.00      0      0  SOTON/O.Q. 3101306    7.0500              NaN        S
466          467         0       2                                                               Campbell, Mr. William    male    NaN      0      0              239853    0.0000              NaN        S
467          468         0       1                                                          Smart, Mr. John Montgomery    male  56.00      0      0              113792   26.5500              NaN        S
468          469         0       3                                                                  Scanlan, Mr. James    male    NaN      0      0               36209    7.7250              NaN        Q
469          470         1       3                                                       Baclini, Miss. Helene Barbara  female   0.75      2      1                2666   19.2583              NaN        C
470          471         0       3                                                                   Keefe, Mr. Arthur    male    NaN      0      0              323592    7.2500              NaN        S
471          472         0       3                                                                     Cacic, Mr. Luka    male  38.00      0      0              315089    8.6625              NaN        S
472          473         1       2                                             West, Mrs. Edwy Arthur (Ada Mary Worth)  female  33.00      1      2          C.A. 34651   27.7500              NaN        S
473          474         1       2                                        Jerwan, Mrs. Amin S (Marie Marthe Thuillard)  female  23.00      0      0     SC/AH Basle 541   13.7917                D        C
474          475         0       3                                                         Strandberg, Miss. Ida Sofia  female  22.00      0      0                7553    9.8375              NaN        S
475          476         0       1                                                         Clifford, Mr. George Quincy    male    NaN      0      0              110465   52.0000              A14        S
476          477         0       2                                                             Renouf, Mr. Peter Henry    male  34.00      1      0               31027   21.0000              NaN        S
477          478         0       3                                                           Braund, Mr. Lewis Richard    male  29.00      1      0                3460    7.0458              NaN        S
478          479         0       3                                                           Karlsson, Mr. Nils August    male  22.00      0      0              350060    7.5208              NaN        S
479          480         1       3                                                            Hirvonen, Miss. Hildur E  female   2.00      0      1             3101298   12.2875              NaN        S
480          481         0       3                                                      Goodwin, Master. Harold Victor    male   9.00      5      2             CA 2144   46.9000              NaN        S
481          482         0       2                                                    Frost, Mr. Anthony Wood "Archie"    male    NaN      0      0              239854    0.0000              NaN        S
482          483         0       3                                                            Rouse, Mr. Richard Henry    male  50.00      0      0            A/5 3594    8.0500              NaN        S
483          484         1       3                                                              Turkula, Mrs. (Hedwig)  female  63.00      0      0                4134    9.5875              NaN        S
484          485         1       1                                                             Bishop, Mr. Dickinson H    male  25.00      1      0               11967   91.0792              B49        C
485          486         0       3                                                              Lefebre, Miss. Jeannie  female    NaN      3      1                4133   25.4667              NaN        S
486          487         1       1                                     Hoyt, Mrs. Frederick Maxfield (Jane Anne Forby)  female  35.00      1      0               19943   90.0000              C93        S
487          488         0       1                                                             Kent, Mr. Edward Austin    male  58.00      0      0               11771   29.7000              B37        C
488          489         0       3                                                       Somerton, Mr. Francis William    male  30.00      0      0          A.5. 18509    8.0500              NaN        S
489          490         1       3                                               Coutts, Master. Eden Leslie "Neville"    male   9.00      1      1          C.A. 37671   15.9000              NaN        S
490          491         0       3                                                Hagland, Mr. Konrad Mathias Reiersen    male    NaN      1      0               65304   19.9667              NaN        S
491          492         0       3                                                                 Windelov, Mr. Einar    male  21.00      0      0    SOTON/OQ 3101317    7.2500              NaN        S
492          493         0       1                                                          Molson, Mr. Harry Markland    male  55.00      0      0              113787   30.5000              C30        S
493          494         0       1                                                             Artagaveytia, Mr. Ramon    male  71.00      0      0            PC 17609   49.5042              NaN        C
494          495         0       3                                                          Stanley, Mr. Edward Roland    male  21.00      0      0           A/4 45380    8.0500              NaN        S
495          496         0       3                                                               Yousseff, Mr. Gerious    male    NaN      0      0                2627   14.4583              NaN        C
496          497         1       1                                                      Eustis, Miss. Elizabeth Mussey  female  54.00      1      0               36947   78.2667              D20        C
497          498         0       3                                                     Shellard, Mr. Frederick William    male    NaN      0      0           C.A. 6212   15.1000              NaN        S
498          499         0       1                                     Allison, Mrs. Hudson J C (Bessie Waldo Daniels)  female  25.00      1      2              113781  151.5500          C22 C26        S
499          500         0       3                                                                  Svensson, Mr. Olof    male  24.00      0      0              350035    7.7958              NaN        S
500          501         0       3                                                                    Calic, Mr. Petar    male  17.00      0      0              315086    8.6625              NaN        S
501          502         0       3                                                                 Canavan, Miss. Mary  female  21.00      0      0              364846    7.7500              NaN        Q
502          503         0       3                                                      O'Sullivan, Miss. Bridget Mary  female    NaN      0      0              330909    7.6292              NaN        Q
503          504         0       3                                                      Laitinen, Miss. Kristina Sofia  female  37.00      0      0                4135    9.5875              NaN        S
504          505         1       1                                                               Maioni, Miss. Roberta  female  16.00      0      0              110152   86.5000              B79        S
505          506         0       1                                          Penasco y Castellana, Mr. Victor de Satode    male  18.00      1      0            PC 17758  108.9000              C65        C
506          507         1       2                                       Quick, Mrs. Frederick Charles (Jane Richards)  female  33.00      0      2               26360   26.0000              NaN        S
507          508         1       1                                       Bradley, Mr. George ("George Arthur Brayton")    male    NaN      0      0              111427   26.5500              NaN        S
508          509         0       3                                                            Olsen, Mr. Henry Margido    male  28.00      0      0              C 4001   22.5250              NaN        S
509          510         1       3                                                                      Lang, Mr. Fang    male  26.00      0      0                1601   56.4958              NaN        S
510          511         1       3                                                            Daly, Mr. Eugene Patrick    male  29.00      0      0              382651    7.7500              NaN        Q
511          512         0       3                                                                   Webber, Mr. James    male    NaN      0      0    SOTON/OQ 3101316    8.0500              NaN        S
512          513         1       1                                                           McGough, Mr. James Robert    male  36.00      0      0            PC 17473   26.2875              E25        S
513          514         1       1                                      Rothschild, Mrs. Martin (Elizabeth L. Barrett)  female  54.00      1      0            PC 17603   59.4000              NaN        C
514          515         0       3                                                                   Coleff, Mr. Satio    male  24.00      0      0              349209    7.4958              NaN        S
515          516         0       1                                                        Walker, Mr. William Anderson    male  47.00      0      0               36967   34.0208              D46        S
516          517         1       2                                                        Lemore, Mrs. (Amelia Milley)  female  34.00      0      0          C.A. 34260   10.5000              F33        S
517          518         0       3                                                                   Ryan, Mr. Patrick    male    NaN      0      0              371110   24.1500              NaN        Q
518          519         1       2                                Angle, Mrs. William A (Florence "Mary" Agnes Hughes)  female  36.00      1      0              226875   26.0000              NaN        S
519          520         0       3                                                                 Pavlovic, Mr. Stefo    male  32.00      0      0              349242    7.8958              NaN        S
520          521         1       1                                                               Perreault, Miss. Anne  female  30.00      0      0               12749   93.5000              B73        S
521          522         0       3                                                                     Vovk, Mr. Janko    male  22.00      0      0              349252    7.8958              NaN        S
522          523         0       3                                                                  Lahoud, Mr. Sarkis    male    NaN      0      0                2624    7.2250              NaN        C
523          524         1       1                                     Hippach, Mrs. Louis Albert (Ida Sophia Fischer)  female  44.00      0      1              111361   57.9792              B18        C
524          525         0       3                                                                   Kassem, Mr. Fared    male    NaN      0      0                2700    7.2292              NaN        C
525          526         0       3                                                                  Farrell, Mr. James    male  40.50      0      0              367232    7.7500              NaN        Q
526          527         1       2                                                                Ridsdale, Miss. Lucy  female  50.00      0      0         W./C. 14258   10.5000              NaN        S
527          528         0       1                                                                  Farthing, Mr. John    male    NaN      0      0            PC 17483  221.7792              C95        S
528          529         0       3                                                           Salonen, Mr. Johan Werner    male  39.00      0      0             3101296    7.9250              NaN        S
529          530         0       2                                                         Hocking, Mr. Richard George    male  23.00      2      1               29104   11.5000              NaN        S
530          531         1       2                                                            Quick, Miss. Phyllis May  female   2.00      1      1               26360   26.0000              NaN        S
531          532         0       3                                                                   Toufik, Mr. Nakli    male    NaN      0      0                2641    7.2292              NaN        C
532          533         0       3                                                                Elias, Mr. Joseph Jr    male  17.00      1      1                2690    7.2292              NaN        C
533          534         1       3                                              Peter, Mrs. Catherine (Catherine Rizk)  female    NaN      0      2                2668   22.3583              NaN        C
534          535         0       3                                                                 Cacic, Miss. Marija  female  30.00      0      0              315084    8.6625              NaN        S
535          536         1       2                                                              Hart, Miss. Eva Miriam  female   7.00      0      2        F.C.C. 13529   26.2500              NaN        S
536          537         0       1                                                   Butt, Major. Archibald Willingham    male  45.00      0      0              113050   26.5500              B38        S
537          538         1       1                                                                 LeRoy, Miss. Bertha  female  30.00      0      0            PC 17761  106.4250              NaN        C
538          539         0       3                                                            Risien, Mr. Samuel Beard    male    NaN      0      0              364498   14.5000              NaN        S
539          540         1       1                                                  Frolicher, Miss. Hedwig Margaritha  female  22.00      0      2               13568   49.5000              B39        C
540          541         1       1                                                             Crosby, Miss. Harriet R  female  36.00      0      2           WE/P 5735   71.0000              B22        S
541          542         0       3                                                Andersson, Miss. Ingeborg Constanzia  female   9.00      4      2              347082   31.2750              NaN        S
542          543         0       3                                                   Andersson, Miss. Sigrid Elisabeth  female  11.00      4      2              347082   31.2750              NaN        S
543          544         1       2                                                                   Beane, Mr. Edward    male  32.00      1      0                2908   26.0000              NaN        S
544          545         0       1                                                          Douglas, Mr. Walter Donald    male  50.00      1      0            PC 17761  106.4250              C86        C
545          546         0       1                                                        Nicholson, Mr. Arthur Ernest    male  64.00      0      0                 693   26.0000              NaN        S
546          547         1       2                                                   Beane, Mrs. Edward (Ethel Clarke)  female  19.00      1      0                2908   26.0000              NaN        S
547          548         1       2                                                          Padro y Manent, Mr. Julian    male    NaN      0      0       SC/PARIS 2146   13.8625              NaN        C
548          549         0       3                                                           Goldsmith, Mr. Frank John    male  33.00      1      1              363291   20.5250              NaN        S
549          550         1       2                                                      Davies, Master. John Morgan Jr    male   8.00      1      1          C.A. 33112   36.7500              NaN        S
550          551         1       1                                                         Thayer, Mr. John Borland Jr    male  17.00      0      2               17421  110.8833              C70        C
551          552         0       2                                                         Sharp, Mr. Percival James R    male  27.00      0      0              244358   26.0000              NaN        S
552          553         0       3                                                                O'Brien, Mr. Timothy    male    NaN      0      0              330979    7.8292              NaN        Q
553          554         1       3                                                   Leeni, Mr. Fahim ("Philip Zenni")    male  22.00      0      0                2620    7.2250              NaN        C
554          555         1       3                                                                  Ohman, Miss. Velin  female  22.00      0      0              347085    7.7750              NaN        S
555          556         0       1                                                                  Wright, Mr. George    male  62.00      0      0              113807   26.5500              NaN        S
556          557         1       1                   Duff Gordon, Lady. (Lucille Christiana Sutherland) ("Mrs Morgan")  female  48.00      1      0               11755   39.6000              A16        C
557          558         0       1                                                                 Robbins, Mr. Victor    male    NaN      0      0            PC 17757  227.5250              NaN        C
558          559         1       1                                              Taussig, Mrs. Emil (Tillie Mandelbaum)  female  39.00      1      1              110413   79.6500              E67        S
559          560         1       3                                        de Messemaeker, Mrs. Guillaume Joseph (Emma)  female  36.00      1      0              345572   17.4000              NaN        S
560          561         0       3                                                            Morrow, Mr. Thomas Rowan    male    NaN      0      0              372622    7.7500              NaN        Q
561          562         0       3                                                                   Sivic, Mr. Husein    male  40.00      0      0              349251    7.8958              NaN        S
562          563         0       2                                                          Norman, Mr. Robert Douglas    male  28.00      0      0              218629   13.5000              NaN        S
563          564         0       3                                                                   Simmons, Mr. John    male    NaN      0      0     SOTON/OQ 392082    8.0500              NaN        S
564          565         0       3                                                      Meanwell, Miss. (Marion Ogden)  female    NaN      0      0   SOTON/O.Q. 392087    8.0500              NaN        S
565          566         0       3                                                                Davies, Mr. Alfred J    male  24.00      2      0           A/4 48871   24.1500              NaN        S
566          567         0       3                                                                Stoytcheff, Mr. Ilia    male  19.00      0      0              349205    7.8958              NaN        S
567          568         0       3                                         Palsson, Mrs. Nils (Alma Cornelia Berglund)  female  29.00      0      4              349909   21.0750              NaN        S
568          569         0       3                                                                 Doharr, Mr. Tannous    male    NaN      0      0                2686    7.2292              NaN        C
569          570         1       3                                                                   Jonsson, Mr. Carl    male  32.00      0      0              350417    7.8542              NaN        S
570          571         1       2                                                                  Harris, Mr. George    male  62.00      0      0         S.W./PP 752   10.5000              NaN        S
571          572         1       1                                       Appleton, Mrs. Edward Dale (Charlotte Lamson)  female  53.00      2      0               11769   51.4792             C101        S
572          573         1       1                                                    Flynn, Mr. John Irwin ("Irving")    male  36.00      0      0            PC 17474   26.3875              E25        S
573          574         1       3                                                                   Kelly, Miss. Mary  female    NaN      0      0               14312    7.7500              NaN        Q
574          575         0       3                                                        Rush, Mr. Alfred George John    male  16.00      0      0          A/4. 20589    8.0500              NaN        S
575          576         0       3                                                                Patchett, Mr. George    male  19.00      0      0              358585   14.5000              NaN        S
576          577         1       2                                                                Garside, Miss. Ethel  female  34.00      0      0              243880   13.0000              NaN        S
577          578         1       1                                           Silvey, Mrs. William Baird (Alice Munger)  female  39.00      1      0               13507   55.9000              E44        S
578          579         0       3                                                    Caram, Mrs. Joseph (Maria Elias)  female    NaN      1      0                2689   14.4583              NaN        C
579          580         1       3                                                                 Jussila, Mr. Eiriik    male  32.00      0      0   STON/O 2. 3101286    7.9250              NaN        S
580          581         1       2                                                         Christy, Miss. Julie Rachel  female  25.00      1      1              237789   30.0000              NaN        S
581          582         1       1                                Thayer, Mrs. John Borland (Marian Longstreth Morris)  female  39.00      1      1               17421  110.8833              C68        C
582          583         0       2                                                          Downton, Mr. William James    male  54.00      0      0               28403   26.0000              NaN        S
583          584         0       1                                                                 Ross, Mr. John Hugo    male  36.00      0      0               13049   40.1250              A10        C
584          585         0       3                                                                 Paulner, Mr. Uscher    male    NaN      0      0                3411    8.7125              NaN        C
585          586         1       1                                                                 Taussig, Miss. Ruth  female  18.00      0      2              110413   79.6500              E68        S
586          587         0       2                                                             Jarvis, Mr. John Denzil    male  47.00      0      0              237565   15.0000              NaN        S
587          588         1       1                                                    Frolicher-Stehli, Mr. Maxmillian    male  60.00      1      1               13567   79.2000              B41        C
588          589         0       3                                                               Gilinski, Mr. Eliezer    male  22.00      0      0               14973    8.0500              NaN        S
589          590         0       3                                                                 Murdlin, Mr. Joseph    male    NaN      0      0          A./5. 3235    8.0500              NaN        S
590          591         0       3                                                                Rintamaki, Mr. Matti    male  35.00      0      0   STON/O 2. 3101273    7.1250              NaN        S
591          592         1       1                                     Stephenson, Mrs. Walter Bertram (Martha Eustis)  female  52.00      1      0               36947   78.2667              D20        C
592          593         0       3                                                          Elsbury, Mr. William James    male  47.00      0      0            A/5 3902    7.2500              NaN        S
593          594         0       3                                                                  Bourke, Miss. Mary  female    NaN      0      2              364848    7.7500              NaN        Q
594          595         0       2                                                             Chapman, Mr. John Henry    male  37.00      1      0         SC/AH 29037   26.0000              NaN        S
595          596         0       3                                                         Van Impe, Mr. Jean Baptiste    male  36.00      1      1              345773   24.1500              NaN        S
596          597         1       2                                                          Leitch, Miss. Jessie Wills  female    NaN      0      0              248727   33.0000              NaN        S
597          598         0       3                                                                 Johnson, Mr. Alfred    male  49.00      0      0                LINE    0.0000              NaN        S
598          599         0       3                                                                   Boulos, Mr. Hanna    male    NaN      0      0                2664    7.2250              NaN        C
599          600         1       1                                        Duff Gordon, Sir. Cosmo Edmund ("Mr Morgan")    male  49.00      1      0            PC 17485   56.9292              A20        C
600          601         1       2                                 Jacobsohn, Mrs. Sidney Samuel (Amy Frances Christy)  female  24.00      2      1              243847   27.0000              NaN        S
601          602         0       3                                                                Slabenoff, Mr. Petco    male    NaN      0      0              349214    7.8958              NaN        S
602          603         0       1                                                           Harrington, Mr. Charles H    male    NaN      0      0              113796   42.4000              NaN        S
603          604         0       3                                                           Torber, Mr. Ernst William    male  44.00      0      0              364511    8.0500              NaN        S
604          605         1       1                                                     Homer, Mr. Harry ("Mr E Haven")    male  35.00      0      0              111426   26.5500              NaN        C
605          606         0       3                                                       Lindell, Mr. Edvard Bengtsson    male  36.00      1      0              349910   15.5500              NaN        S
606          607         0       3                                                                   Karaic, Mr. Milan    male  30.00      0      0              349246    7.8958              NaN        S
607          608         1       1                                                         Daniel, Mr. Robert Williams    male  27.00      0      0              113804   30.5000              NaN        S
608          609         1       2                               Laroche, Mrs. Joseph (Juliette Marie Louise Lafargue)  female  22.00      1      2       SC/Paris 2123   41.5792              NaN        C
609          610         1       1                                                           Shutes, Miss. Elizabeth W  female  40.00      0      0            PC 17582  153.4625             C125        S
610          611         0       3                           Andersson, Mrs. Anders Johan (Alfrida Konstantia Brogren)  female  39.00      1      5              347082   31.2750              NaN        S
611          612         0       3                                                               Jardin, Mr. Jose Neto    male    NaN      0      0  SOTON/O.Q. 3101305    7.0500              NaN        S
612          613         1       3                                                         Murphy, Miss. Margaret Jane  female    NaN      1      0              367230   15.5000              NaN        Q
613          614         0       3                                                                    Horgan, Mr. John    male    NaN      0      0              370377    7.7500              NaN        Q
614          615         0       3                                                     Brocklebank, Mr. William Alfred    male  35.00      0      0              364512    8.0500              NaN        S
615          616         1       2                                                                 Herman, Miss. Alice  female  24.00      1      2              220845   65.0000              NaN        S
616          617         0       3                                                           Danbom, Mr. Ernst Gilbert    male  34.00      1      1              347080   14.4000              NaN        S
617          618         0       3                                     Lobb, Mrs. William Arthur (Cordelia K Stanlick)  female  26.00      1      0           A/5. 3336   16.1000              NaN        S
618          619         1       2                                                         Becker, Miss. Marion Louise  female   4.00      2      1              230136   39.0000               F4        S
619          620         0       2                                                                 Gavey, Mr. Lawrence    male  26.00      0      0               31028   10.5000              NaN        S
620          621         0       3                                                                 Yasbeck, Mr. Antoni    male  27.00      1      0                2659   14.4542              NaN        C
621          622         1       1                                                        Kimball, Mr. Edwin Nelson Jr    male  42.00      1      0               11753   52.5542              D19        S
622          623         1       3                                                                    Nakid, Mr. Sahid    male  20.00      1      1                2653   15.7417              NaN        C
623          624         0       3                                                         Hansen, Mr. Henry Damsgaard    male  21.00      0      0              350029    7.8542              NaN        S
624          625         0       3                                                         Bowen, Mr. David John "Dai"    male  21.00      0      0               54636   16.1000              NaN        S
625          626         0       1                                                               Sutton, Mr. Frederick    male  61.00      0      0               36963   32.3208              D50        S
626          627         0       2                                                      Kirkland, Rev. Charles Leonard    male  57.00      0      0              219533   12.3500              NaN        Q
627          628         1       1                                                       Longley, Miss. Gretchen Fiske  female  21.00      0      0               13502   77.9583               D9        S
628          629         0       3                                                           Bostandyeff, Mr. Guentcho    male  26.00      0      0              349224    7.8958              NaN        S
629          630         0       3                                                            O'Connell, Mr. Patrick D    male    NaN      0      0              334912    7.7333              NaN        Q
630          631         1       1                                                Barkworth, Mr. Algernon Henry Wilson    male  80.00      0      0               27042   30.0000              A23        S
631          632         0       3                                                         Lundahl, Mr. Johan Svensson    male  51.00      0      0              347743    7.0542              NaN        S
632          633         1       1                                                           Stahelin-Maeglin, Dr. Max    male  32.00      0      0               13214   30.5000              B50        C
633          634         0       1                                                       Parr, Mr. William Henry Marsh    male    NaN      0      0              112052    0.0000              NaN        S
634          635         0       3                                                                  Skoog, Miss. Mabel  female   9.00      3      2              347088   27.9000              NaN        S
635          636         1       2                                                                   Davis, Miss. Mary  female  28.00      0      0              237668   13.0000              NaN        S
636          637         0       3                                                          Leinonen, Mr. Antti Gustaf    male  32.00      0      0   STON/O 2. 3101292    7.9250              NaN        S
637          638         0       2                                                                 Collyer, Mr. Harvey    male  31.00      1      1          C.A. 31921   26.2500              NaN        S
638          639         0       3                                              Panula, Mrs. Juha (Maria Emilia Ojala)  female  41.00      0      5             3101295   39.6875              NaN        S
639          640         0       3                                                          Thorneycroft, Mr. Percival    male    NaN      1      0              376564   16.1000              NaN        S
640          641         0       3                                                              Jensen, Mr. Hans Peder    male  20.00      0      0              350050    7.8542              NaN        S
641          642         1       1                                                                Sagesser, Mlle. Emma  female  24.00      0      0            PC 17477   69.3000              B35        C
642          643         0       3                                                       Skoog, Miss. Margit Elizabeth  female   2.00      3      2              347088   27.9000              NaN        S
643          644         1       3                                                                     Foo, Mr. Choong    male    NaN      0      0                1601   56.4958              NaN        S
644          645         1       3                                                              Baclini, Miss. Eugenie  female   0.75      2      1                2666   19.2583              NaN        C
645          646         1       1                                                           Harper, Mr. Henry Sleeper    male  48.00      1      0            PC 17572   76.7292              D33        C
646          647         0       3                                                                   Cor, Mr. Liudevit    male  19.00      0      0              349231    7.8958              NaN        S
647          648         1       1                                                 Simonius-Blumer, Col. Oberst Alfons    male  56.00      0      0               13213   35.5000              A26        C
648          649         0       3                                                                  Willey, Mr. Edward    male    NaN      0      0       S.O./P.P. 751    7.5500              NaN        S
649          650         1       3                                                     Stanley, Miss. Amy Zillah Elsie  female  23.00      0      0            CA. 2314    7.5500              NaN        S
650          651         0       3                                                                   Mitkoff, Mr. Mito    male    NaN      0      0              349221    7.8958              NaN        S
651          652         1       2                                                                 Doling, Miss. Elsie  female  18.00      0      1              231919   23.0000              NaN        S
652          653         0       3                                                      Kalvik, Mr. Johannes Halvorsen    male  21.00      0      0                8475    8.4333              NaN        S
653          654         1       3                                                       O'Leary, Miss. Hanora "Norah"  female    NaN      0      0              330919    7.8292              NaN        Q
654          655         0       3                                                        Hegarty, Miss. Hanora "Nora"  female  18.00      0      0              365226    6.7500              NaN        Q
655          656         0       2                                                           Hickman, Mr. Leonard Mark    male  24.00      2      0        S.O.C. 14879   73.5000              NaN        S
656          657         0       3                                                               Radeff, Mr. Alexander    male    NaN      0      0              349223    7.8958              NaN        S
657          658         0       3                                                       Bourke, Mrs. John (Catherine)  female  32.00      1      1              364849   15.5000              NaN        Q
658          659         0       2                                                        Eitemiller, Mr. George Floyd    male  23.00      0      0               29751   13.0000              NaN        S
659          660         0       1                                                          Newell, Mr. Arthur Webster    male  58.00      0      2               35273  113.2750              D48        C
660          661         1       1                                                       Frauenthal, Dr. Henry William    male  50.00      2      0            PC 17611  133.6500              NaN        S
661          662         0       3                                                                   Badt, Mr. Mohamed    male  40.00      0      0                2623    7.2250              NaN        C
662          663         0       1                                                          Colley, Mr. Edward Pomeroy    male  47.00      0      0                5727   25.5875              E58        S
663          664         0       3                                                                    Coleff, Mr. Peju    male  36.00      0      0              349210    7.4958              NaN        S
664          665         1       3                                                         Lindqvist, Mr. Eino William    male  20.00      1      0   STON/O 2. 3101285    7.9250              NaN        S
665          666         0       2                                                                  Hickman, Mr. Lewis    male  32.00      2      0        S.O.C. 14879   73.5000              NaN        S
666          667         0       2                                                         Butler, Mr. Reginald Fenton    male  25.00      0      0              234686   13.0000              NaN        S
667          668         0       3                                                          Rommetvedt, Mr. Knud Paust    male    NaN      0      0              312993    7.7750              NaN        S
668          669         0       3                                                                     Cook, Mr. Jacob    male  43.00      0      0            A/5 3536    8.0500              NaN        S
669          670         1       1                                   Taylor, Mrs. Elmer Zebley (Juliet Cummins Wright)  female    NaN      1      0               19996   52.0000             C126        S
670          671         1       2                       Brown, Mrs. Thomas William Solomon (Elizabeth Catherine Ford)  female  40.00      1      1               29750   39.0000              NaN        S
671          672         0       1                                                              Davidson, Mr. Thornton    male  31.00      1      0          F.C. 12750   52.0000              B71        S
672          673         0       2                                                         Mitchell, Mr. Henry Michael    male  70.00      0      0          C.A. 24580   10.5000              NaN        S
673          674         1       2                                                               Wilhelms, Mr. Charles    male  31.00      0      0              244270   13.0000              NaN        S
674          675         0       2                                                          Watson, Mr. Ennis Hastings    male    NaN      0      0              239856    0.0000              NaN        S
675          676         0       3                                                      Edvardsson, Mr. Gustaf Hjalmar    male  18.00      0      0              349912    7.7750              NaN        S
676          677         0       3                                                       Sawyer, Mr. Frederick Charles    male  24.50      0      0              342826    8.0500              NaN        S
677          678         1       3                                                             Turja, Miss. Anna Sofia  female  18.00      0      0                4138    9.8417              NaN        S
678          679         0       3                                             Goodwin, Mrs. Frederick (Augusta Tyler)  female  43.00      1      6             CA 2144   46.9000              NaN        S
679          680         1       1                                                  Cardeza, Mr. Thomas Drake Martinez    male  36.00      0      1            PC 17755  512.3292      B51 B53 B55        C
680          681         0       3                                                                 Peters, Miss. Katie  female    NaN      0      0              330935    8.1375              NaN        Q
681          682         1       1                                                                  Hassab, Mr. Hammad    male  27.00      0      0            PC 17572   76.7292              D49        C
682          683         0       3                                                         Olsvigen, Mr. Thor Anderson    male  20.00      0      0                6563    9.2250              NaN        S
683          684         0       3                                                         Goodwin, Mr. Charles Edward    male  14.00      5      2             CA 2144   46.9000              NaN        S
684          685         0       2                                                   Brown, Mr. Thomas William Solomon    male  60.00      1      1               29750   39.0000              NaN        S
685          686         0       2                                              Laroche, Mr. Joseph Philippe Lemercier    male  25.00      1      2       SC/Paris 2123   41.5792              NaN        C
686          687         0       3                                                            Panula, Mr. Jaako Arnold    male  14.00      4      1             3101295   39.6875              NaN        S
687          688         0       3                                                                   Dakic, Mr. Branko    male  19.00      0      0              349228   10.1708              NaN        S
688          689         0       3                                                     Fischer, Mr. Eberhard Thelander    male  18.00      0      0              350036    7.7958              NaN        S
689          690         1       1                                                   Madill, Miss. Georgette Alexandra  female  15.00      0      1               24160  211.3375               B5        S
690          691         1       1                                                             Dick, Mr. Albert Adrian    male  31.00      1      0               17474   57.0000              B20        S
691          692         1       3                                                                  Karun, Miss. Manca  female   4.00      0      1              349256   13.4167              NaN        C
692          693         1       3                                                                        Lam, Mr. Ali    male    NaN      0      0                1601   56.4958              NaN        S
693          694         0       3                                                                    Saad, Mr. Khalil    male  25.00      0      0                2672    7.2250              NaN        C
694          695         0       1                                                                     Weir, Col. John    male  60.00      0      0              113800   26.5500              NaN        S
695          696         0       2                                                          Chapman, Mr. Charles Henry    male  52.00      0      0              248731   13.5000              NaN        S
696          697         0       3                                                                    Kelly, Mr. James    male  44.00      0      0              363592    8.0500              NaN        S
697          698         1       3                                                    Mullens, Miss. Katherine "Katie"  female    NaN      0      0               35852    7.7333              NaN        Q
698          699         0       1                                                            Thayer, Mr. John Borland    male  49.00      1      1               17421  110.8833              C68        C
699          700         0       3                                            Humblen, Mr. Adolf Mathias Nicolai Olsen    male  42.00      0      0              348121    7.6500            F G63        S
700          701         1       1                                   Astor, Mrs. John Jacob (Madeleine Talmadge Force)  female  18.00      1      0            PC 17757  227.5250          C62 C64        C
701          702         1       1                                                    Silverthorne, Mr. Spencer Victor    male  35.00      0      0            PC 17475   26.2875              E24        S
702          703         0       3                                                               Barbara, Miss. Saiide  female  18.00      0      1                2691   14.4542              NaN        C
703          704         0       3                                                               Gallagher, Mr. Martin    male  25.00      0      0               36864    7.7417              NaN        Q
704          705         0       3                                                             Hansen, Mr. Henrik Juul    male  26.00      1      0              350025    7.8542              NaN        S
705          706         0       2                                      Morley, Mr. Henry Samuel ("Mr Henry Marshall")    male  39.00      0      0              250655   26.0000              NaN        S
706          707         1       2                                                       Kelly, Mrs. Florence "Fannie"  female  45.00      0      0              223596   13.5000              NaN        S
707          708         1       1                                                   Calderhead, Mr. Edward Pennington    male  42.00      0      0            PC 17476   26.2875              E24        S
708          709         1       1                                                                Cleaver, Miss. Alice  female  22.00      0      0              113781  151.5500              NaN        S
709          710         1       3                                   Moubarek, Master. Halim Gonios ("William George")    male    NaN      1      1                2661   15.2458              NaN        C
710          711         1       1                                    Mayne, Mlle. Berthe Antonine ("Mrs de Villiers")  female  24.00      0      0            PC 17482   49.5042              C90        C
711          712         0       1                                                                  Klaber, Mr. Herman    male    NaN      0      0              113028   26.5500             C124        S
712          713         1       1                                                            Taylor, Mr. Elmer Zebley    male  48.00      1      0               19996   52.0000             C126        S
713          714         0       3                                                          Larsson, Mr. August Viktor    male  29.00      0      0                7545    9.4833              NaN        S
714          715         0       2                                                               Greenberg, Mr. Samuel    male  52.00      0      0              250647   13.0000              NaN        S
715          716         0       3                                          Soholt, Mr. Peter Andreas Lauritz Andersen    male  19.00      0      0              348124    7.6500            F G73        S
716          717         1       1                                                       Endres, Miss. Caroline Louise  female  38.00      0      0            PC 17757  227.5250              C45        C
717          718         1       2                                                 Troutt, Miss. Edwina Celia "Winnie"  female  27.00      0      0               34218   10.5000             E101        S
718          719         0       3                                                                 McEvoy, Mr. Michael    male    NaN      0      0               36568   15.5000              NaN        Q
719          720         0       3                                                        Johnson, Mr. Malkolm Joackim    male  33.00      0      0              347062    7.7750              NaN        S
720          721         1       2                                                   Harper, Miss. Annie Jessie "Nina"  female   6.00      0      1              248727   33.0000              NaN        S
721          722         0       3                                                           Jensen, Mr. Svend Lauritz    male  17.00      1      0              350048    7.0542              NaN        S
722          723         0       2                                                        Gillespie, Mr. William Henry    male  34.00      0      0               12233   13.0000              NaN        S
723          724         0       2                                                             Hodges, Mr. Henry Price    male  50.00      0      0              250643   13.0000              NaN        S
724          725         1       1                                                       Chambers, Mr. Norman Campbell    male  27.00      1      0              113806   53.1000               E8        S
725          726         0       3                                                                 Oreskovic, Mr. Luka    male  20.00      0      0              315094    8.6625              NaN        S
726          727         1       2                                         Renouf, Mrs. Peter Henry (Lillian Jefferys)  female  30.00      3      0               31027   21.0000              NaN        S
727          728         1       3                                                            Mannion, Miss. Margareth  female    NaN      0      0               36866    7.7375              NaN        Q
728          729         0       2                                                     Bryhl, Mr. Kurt Arnold Gottfrid    male  25.00      1      0              236853   26.0000              NaN        S
729          730         0       3                                                       Ilmakangas, Miss. Pieta Sofia  female  25.00      1      0    STON/O2. 3101271    7.9250              NaN        S
730          731         1       1                                                       Allen, Miss. Elisabeth Walton  female  29.00      0      0               24160  211.3375               B5        S
731          732         0       3                                                            Hassan, Mr. Houssein G N    male  11.00      0      0                2699   18.7875              NaN        C
732          733         0       2                                                                Knight, Mr. Robert J    male    NaN      0      0              239855    0.0000              NaN        S
733          734         0       2                                                          Berriman, Mr. William John    male  23.00      0      0               28425   13.0000              NaN        S
734          735         0       2                                                        Troupiansky, Mr. Moses Aaron    male  23.00      0      0              233639   13.0000              NaN        S
735          736         0       3                                                                Williams, Mr. Leslie    male  28.50      0      0               54636   16.1000              NaN        S
736          737         0       3                                             Ford, Mrs. Edward (Margaret Ann Watson)  female  48.00      1      3          W./C. 6608   34.3750              NaN        S
737          738         1       1                                                              Lesurer, Mr. Gustave J    male  35.00      0      0            PC 17755  512.3292             B101        C
738          739         0       3                                                                  Ivanoff, Mr. Kanio    male    NaN      0      0              349201    7.8958              NaN        S
739          740         0       3                                                                  Nankoff, Mr. Minko    male    NaN      0      0              349218    7.8958              NaN        S
740          741         1       1                                                         Hawksford, Mr. Walter James    male    NaN      0      0               16988   30.0000              D45        S
741          742         0       1                                                       Cavendish, Mr. Tyrell William    male  36.00      1      0               19877   78.8500              C46        S
742          743         1       1                                               Ryerson, Miss. Susan Parker "Suzette"  female  21.00      2      2            PC 17608  262.3750  B57 B59 B63 B66        C
743          744         0       3                                                                   McNamee, Mr. Neal    male  24.00      1      0              376566   16.1000              NaN        S
744          745         1       3                                                                  Stranden, Mr. Juho    male  31.00      0      0   STON/O 2. 3101288    7.9250              NaN        S
745          746         0       1                                                        Crosby, Capt. Edward Gifford    male  70.00      1      1           WE/P 5735   71.0000              B22        S
746          747         0       3                                                         Abbott, Mr. Rossmore Edward    male  16.00      1      1           C.A. 2673   20.2500              NaN        S
747          748         1       2                                                               Sinkkonen, Miss. Anna  female  30.00      0      0              250648   13.0000              NaN        S
748          749         0       1                                                           Marvin, Mr. Daniel Warner    male  19.00      1      0              113773   53.1000              D30        S
749          750         0       3                                                             Connaghton, Mr. Michael    male  31.00      0      0              335097    7.7500              NaN        Q
750          751         1       2                                                                   Wells, Miss. Joan  female   4.00      1      1               29103   23.0000              NaN        S
751          752         1       3                                                                 Moor, Master. Meier    male   6.00      0      1              392096   12.4750             E121        S
752          753         0       3                                                    Vande Velde, Mr. Johannes Joseph    male  33.00      0      0              345780    9.5000              NaN        S
753          754         0       3                                                                  Jonkoff, Mr. Lalio    male  23.00      0      0              349204    7.8958              NaN        S
754          755         1       2                                                    Herman, Mrs. Samuel (Jane Laver)  female  48.00      1      2              220845   65.0000              NaN        S
755          756         1       2                                                           Hamalainen, Master. Viljo    male   0.67      1      1              250649   14.5000              NaN        S
756          757         0       3                                                        Carlsson, Mr. August Sigfrid    male  28.00      0      0              350042    7.7958              NaN        S
757          758         0       2                                                            Bailey, Mr. Percy Andrew    male  18.00      0      0               29108   11.5000              NaN        S
758          759         0       3                                                        Theobald, Mr. Thomas Leonard    male  34.00      0      0              363294    8.0500              NaN        S
759          760         1       1                            Rothes, the Countess. of (Lucy Noel Martha Dyer-Edwards)  female  33.00      0      0              110152   86.5000              B77        S
760          761         0       3                                                                  Garfirth, Mr. John    male    NaN      0      0              358585   14.5000              NaN        S
761          762         0       3                                                      Nirva, Mr. Iisakki Antino Aijo    male  41.00      0      0    SOTON/O2 3101272    7.1250              NaN        S
762          763         1       3                                                               Barah, Mr. Hanna Assi    male  20.00      0      0                2663    7.2292              NaN        C
763          764         1       1                                           Carter, Mrs. William Ernest (Lucile Polk)  female  36.00      1      2              113760  120.0000          B96 B98        S
764          765         0       3                                                              Eklund, Mr. Hans Linus    male  16.00      0      0              347074    7.7750              NaN        S
765          766         1       1                                                Hogeboom, Mrs. John C (Anna Andrews)  female  51.00      1      0               13502   77.9583              D11        S
766          767         0       1                                                           Brewe, Dr. Arthur Jackson    male    NaN      0      0              112379   39.6000              NaN        C
767          768         0       3                                                                  Mangan, Miss. Mary  female  30.50      0      0              364850    7.7500              NaN        Q
768          769         0       3                                                                 Moran, Mr. Daniel J    male    NaN      1      0              371110   24.1500              NaN        Q
769          770         0       3                                                    Gronnestad, Mr. Daniel Danielsen    male  32.00      0      0                8471    8.3625              NaN        S
770          771         0       3                                                              Lievens, Mr. Rene Aime    male  24.00      0      0              345781    9.5000              NaN        S
771          772         0       3                                                             Jensen, Mr. Niels Peder    male  48.00      0      0              350047    7.8542              NaN        S
772          773         0       2                                                                   Mack, Mrs. (Mary)  female  57.00      0      0         S.O./P.P. 3   10.5000              E77        S
773          774         0       3                                                                     Elias, Mr. Dibo    male    NaN      0      0                2674    7.2250              NaN        C
774          775         1       2                                               Hocking, Mrs. Elizabeth (Eliza Needs)  female  54.00      1      3               29105   23.0000              NaN        S
775          776         0       3                                             Myhrman, Mr. Pehr Fabian Oliver Malkolm    male  18.00      0      0              347078    7.7500              NaN        S
776          777         0       3                                                                    Tobin, Mr. Roger    male    NaN      0      0              383121    7.7500              F38        Q
777          778         1       3                                                       Emanuel, Miss. Virginia Ethel  female   5.00      0      0              364516   12.4750              NaN        S
778          779         0       3                                                             Kilgannon, Mr. Thomas J    male    NaN      0      0               36865    7.7375              NaN        Q
779          780         1       1                               Robert, Mrs. Edward Scott (Elisabeth Walton McMillan)  female  43.00      0      1               24160  211.3375               B3        S
780          781         1       3                                                                Ayoub, Miss. Banoura  female  13.00      0      0                2687    7.2292              NaN        C
781          782         1       1                                           Dick, Mrs. Albert Adrian (Vera Gillespie)  female  17.00      1      0               17474   57.0000              B20        S
782          783         0       1                                                              Long, Mr. Milton Clyde    male  29.00      0      0              113501   30.0000               D6        S
783          784         0       3                                                              Johnston, Mr. Andrew G    male    NaN      1      2          W./C. 6607   23.4500              NaN        S
784          785         0       3                                                                    Ali, Mr. William    male  25.00      0      0  SOTON/O.Q. 3101312    7.0500              NaN        S
785          786         0       3                                                  Harmer, Mr. Abraham (David Lishin)    male  25.00      0      0              374887    7.2500              NaN        S
786          787         1       3                                                           Sjoblom, Miss. Anna Sofia  female  18.00      0      0             3101265    7.4958              NaN        S
787          788         0       3                                                           Rice, Master. George Hugh    male   8.00      4      1              382652   29.1250              NaN        Q
788          789         1       3                                                          Dean, Master. Bertram Vere    male   1.00      1      2           C.A. 2315   20.5750              NaN        S
789          790         0       1                                                            Guggenheim, Mr. Benjamin    male  46.00      0      0            PC 17593   79.2000          B82 B84        C
790          791         0       3                                                            Keane, Mr. Andrew "Andy"    male    NaN      0      0               12460    7.7500              NaN        Q
791          792         0       2                                                                 Gaskell, Mr. Alfred    male  16.00      0      0              239865   26.0000              NaN        S
792          793         0       3                                                             Sage, Miss. Stella Anna  female    NaN      8      2            CA. 2343   69.5500              NaN        S
793          794         0       1                                                            Hoyt, Mr. William Fisher    male    NaN      0      0            PC 17600   30.6958              NaN        C
794          795         0       3                                                               Dantcheff, Mr. Ristiu    male  25.00      0      0              349203    7.8958              NaN        S
795          796         0       2                                                                  Otter, Mr. Richard    male  39.00      0      0               28213   13.0000              NaN        S
796          797         1       1                                                         Leader, Dr. Alice (Farnham)  female  49.00      0      0               17465   25.9292              D17        S
797          798         1       3                                                                    Osman, Mrs. Mara  female  31.00      0      0              349244    8.6833              NaN        S
798          799         0       3                                                        Ibrahim Shawah, Mr. Yousseff    male  30.00      0      0                2685    7.2292              NaN        C
799          800         0       3                                Van Impe, Mrs. Jean Baptiste (Rosalie Paula Govaert)  female  30.00      1      1              345773   24.1500              NaN        S
800          801         0       2                                                                Ponesell, Mr. Martin    male  34.00      0      0              250647   13.0000              NaN        S
801          802         1       2                                         Collyer, Mrs. Harvey (Charlotte Annie Tate)  female  31.00      1      1          C.A. 31921   26.2500              NaN        S
802          803         1       1                                                 Carter, Master. William Thornton II    male  11.00      1      2              113760  120.0000          B96 B98        S
803          804         1       3                                                     Thomas, Master. Assad Alexander    male   0.42      0      1                2625    8.5167              NaN        C
804          805         1       3                                                             Hedman, Mr. Oskar Arvid    male  27.00      0      0              347089    6.9750              NaN        S
805          806         0       3                                                           Johansson, Mr. Karl Johan    male  31.00      0      0              347063    7.7750              NaN        S
806          807         0       1                                                              Andrews, Mr. Thomas Jr    male  39.00      0      0              112050    0.0000              A36        S
807          808         0       3                                                     Pettersson, Miss. Ellen Natalia  female  18.00      0      0              347087    7.7750              NaN        S
808          809         0       2                                                                   Meyer, Mr. August    male  39.00      0      0              248723   13.0000              NaN        S
809          810         1       1                                      Chambers, Mrs. Norman Campbell (Bertha Griggs)  female  33.00      1      0              113806   53.1000               E8        S
810          811         0       3                                                              Alexander, Mr. William    male  26.00      0      0                3474    7.8875              NaN        S
811          812         0       3                                                                   Lester, Mr. James    male  39.00      0      0           A/4 48871   24.1500              NaN        S
812          813         0       2                                                           Slemen, Mr. Richard James    male  35.00      0      0               28206   10.5000              NaN        S
813          814         0       3                                                  Andersson, Miss. Ebba Iris Alfrida  female   6.00      4      2              347082   31.2750              NaN        S
814          815         0       3                                                          Tomlin, Mr. Ernest Portage    male  30.50      0      0              364499    8.0500              NaN        S
815          816         0       1                                                                    Fry, Mr. Richard    male    NaN      0      0              112058    0.0000             B102        S
816          817         0       3                                                        Heininen, Miss. Wendla Maria  female  23.00      0      0    STON/O2. 3101290    7.9250              NaN        S
817          818         0       2                                                                  Mallet, Mr. Albert    male  31.00      1      1     S.C./PARIS 2079   37.0042              NaN        C
818          819         0       3                                                    Holm, Mr. John Fredrik Alexander    male  43.00      0      0              C 7075    6.4500              NaN        S
819          820         0       3                                                        Skoog, Master. Karl Thorsten    male  10.00      3      2              347088   27.9000              NaN        S
820          821         1       1                                  Hays, Mrs. Charles Melville (Clara Jennings Gregg)  female  52.00      1      1               12749   93.5000              B69        S
821          822         1       3                                                                   Lulic, Mr. Nikola    male  27.00      0      0              315098    8.6625              NaN        S
822          823         0       1                                                     Reuchlin, Jonkheer. John George    male  38.00      0      0               19972    0.0000              NaN        S
823          824         1       3                                                                  Moor, Mrs. (Beila)  female  27.00      0      1              392096   12.4750             E121        S
824          825         0       3                                                        Panula, Master. Urho Abraham    male   2.00      4      1             3101295   39.6875              NaN        S
825          826         0       3                                                                     Flynn, Mr. John    male    NaN      0      0              368323    6.9500              NaN        Q
826          827         0       3                                                                        Lam, Mr. Len    male    NaN      0      0                1601   56.4958              NaN        S
827          828         1       2                                                               Mallet, Master. Andre    male   1.00      0      2     S.C./PARIS 2079   37.0042              NaN        C
828          829         1       3                                                        McCormack, Mr. Thomas Joseph    male    NaN      0      0              367228    7.7500              NaN        Q
829          830         1       1                                           Stone, Mrs. George Nelson (Martha Evelyn)  female  62.00      0      0              113572   80.0000              B28      NaN
830          831         1       3                                             Yasbeck, Mrs. Antoni (Selini Alexander)  female  15.00      1      0                2659   14.4542              NaN        C
831          832         1       2                                                     Richards, Master. George Sibley    male   0.83      1      1               29106   18.7500              NaN        S
832          833         0       3                                                                      Saad, Mr. Amin    male    NaN      0      0                2671    7.2292              NaN        C
833          834         0       3                                                              Augustsson, Mr. Albert    male  23.00      0      0              347468    7.8542              NaN        S
834          835         0       3                                                              Allum, Mr. Owen George    male  18.00      0      0                2223    8.3000              NaN        S
835          836         1       1                                                         Compton, Miss. Sara Rebecca  female  39.00      1      1            PC 17756   83.1583              E49        C
836          837         0       3                                                                    Pasic, Mr. Jakob    male  21.00      0      0              315097    8.6625              NaN        S
837          838         0       3                                                                 Sirota, Mr. Maurice    male    NaN      0      0              392092    8.0500              NaN        S
838          839         1       3                                                                     Chip, Mr. Chang    male  32.00      0      0                1601   56.4958              NaN        S
839          840         1       1                                                                Marechal, Mr. Pierre    male    NaN      0      0               11774   29.7000              C47        C
840          841         0       3                                                         Alhomaki, Mr. Ilmari Rudolf    male  20.00      0      0    SOTON/O2 3101287    7.9250              NaN        S
841          842         0       2                                                            Mudd, Mr. Thomas Charles    male  16.00      0      0         S.O./P.P. 3   10.5000              NaN        S
842          843         1       1                                                             Serepeca, Miss. Augusta  female  30.00      0      0              113798   31.0000              NaN        C
843          844         0       3                                                          Lemberopolous, Mr. Peter L    male  34.50      0      0                2683    6.4375              NaN        C
844          845         0       3                                                                 Culumovic, Mr. Jeso    male  17.00      0      0              315090    8.6625              NaN        S
845          846         0       3                                                                 Abbing, Mr. Anthony    male  42.00      0      0           C.A. 5547    7.5500              NaN        S
846          847         0       3                                                            Sage, Mr. Douglas Bullen    male    NaN      8      2            CA. 2343   69.5500              NaN        S
847          848         0       3                                                                  Markoff, Mr. Marin    male  35.00      0      0              349213    7.8958              NaN        C
848          849         0       2                                                                   Harper, Rev. John    male  28.00      0      1              248727   33.0000              NaN        S
849          850         1       1                                        Goldenberg, Mrs. Samuel L (Edwiga Grabowska)  female    NaN      1      0               17453   89.1042              C92        C
850          851         0       3                                             Andersson, Master. Sigvard Harald Elias    male   4.00      4      2              347082   31.2750              NaN        S
851          852         0       3                                                                 Svensson, Mr. Johan    male  74.00      0      0              347060    7.7750              NaN        S
852          853         0       3                                                             Boulos, Miss. Nourelain  female   9.00      1      1                2678   15.2458              NaN        C
853          854         1       1                                                           Lines, Miss. Mary Conover  female  16.00      0      1            PC 17592   39.4000              D28        S
854          855         0       2                                       Carter, Mrs. Ernest Courtenay (Lilian Hughes)  female  44.00      1      0              244252   26.0000              NaN        S
855          856         1       3                                                          Aks, Mrs. Sam (Leah Rosen)  female  18.00      0      1              392091    9.3500              NaN        S
856          857         1       1                                          Wick, Mrs. George Dennick (Mary Hitchcock)  female  45.00      1      1               36928  164.8667              NaN        S
857          858         1       1                                                              Daly, Mr. Peter Denis     male  51.00      0      0              113055   26.5500              E17        S
858          859         1       3                                               Baclini, Mrs. Solomon (Latifa Qurban)  female  24.00      0      3                2666   19.2583              NaN        C
859          860         0       3                                                                    Razi, Mr. Raihed    male    NaN      0      0                2629    7.2292              NaN        C
860          861         0       3                                                             Hansen, Mr. Claus Peter    male  41.00      2      0              350026   14.1083              NaN        S
861          862         0       2                                                         Giles, Mr. Frederick Edward    male  21.00      1      0               28134   11.5000              NaN        S
862          863         1       1                                 Swift, Mrs. Frederick Joel (Margaret Welles Barron)  female  48.00      0      0               17466   25.9292              D17        S
863          864         0       3                                                   Sage, Miss. Dorothy Edith "Dolly"  female    NaN      8      2            CA. 2343   69.5500              NaN        S
864          865         0       2                                                              Gill, Mr. John William    male  24.00      0      0              233866   13.0000              NaN        S
865          866         1       2                                                            Bystrom, Mrs. (Karolina)  female  42.00      0      0              236852   13.0000              NaN        S
866          867         1       2                                                        Duran y More, Miss. Asuncion  female  27.00      1      0       SC/PARIS 2149   13.8583              NaN        C
867          868         0       1                                                Roebling, Mr. Washington Augustus II    male  31.00      0      0            PC 17590   50.4958              A24        S
868          869         0       3                                                         van Melkebeke, Mr. Philemon    male    NaN      0      0              345777    9.5000              NaN        S
869          870         1       3                                                     Johnson, Master. Harold Theodor    male   4.00      1      1              347742   11.1333              NaN        S
870          871         0       3                                                                   Balkic, Mr. Cerin    male  26.00      0      0              349248    7.8958              NaN        S
871          872         1       1                                    Beckwith, Mrs. Richard Leonard (Sallie Monypeny)  female  47.00      1      1               11751   52.5542              D35        S
872          873         0       1                                                            Carlsson, Mr. Frans Olof    male  33.00      0      0                 695    5.0000      B51 B53 B55        S
873          874         0       3                                                         Vander Cruyssen, Mr. Victor    male  47.00      0      0              345765    9.0000              NaN        S
874          875         1       2                                               Abelson, Mrs. Samuel (Hannah Wizosky)  female  28.00      1      0           P/PP 3381   24.0000              NaN        C
875          876         1       3                                                    Najib, Miss. Adele Kiamie "Jane"  female  15.00      0      0                2667    7.2250              NaN        C
876          877         0       3                                                       Gustafsson, Mr. Alfred Ossian    male  20.00      0      0                7534    9.8458              NaN        S
877          878         0       3                                                                Petroff, Mr. Nedelio    male  19.00      0      0              349212    7.8958              NaN        S
878          879         0       3                                                                  Laleff, Mr. Kristo    male    NaN      0      0              349217    7.8958              NaN        S
879          880         1       1                                       Potter, Mrs. Thomas Jr (Lily Alexenia Wilson)  female  56.00      0      1               11767   83.1583              C50        C
880          881         1       2                                        Shelley, Mrs. William (Imanita Parrish Hall)  female  25.00      0      1              230433   26.0000              NaN        S
881          882         0       3                                                                  Markun, Mr. Johann    male  33.00      0      0              349257    7.8958              NaN        S
882          883         0       3                                                        Dahlberg, Miss. Gerda Ulrika  female  22.00      0      0                7552   10.5167              NaN        S
883          884         0       2                                                       Banfield, Mr. Frederick James    male  28.00      0      0    C.A./SOTON 34068   10.5000              NaN        S
884          885         0       3                                                              Sutehall, Mr. Henry Jr    male  25.00      0      0     SOTON/OQ 392076    7.0500              NaN        S
885          886         0       3                                                Rice, Mrs. William (Margaret Norton)  female  39.00      0      5              382652   29.1250              NaN        Q
886          887         0       2                                                               Montvila, Rev. Juozas    male  27.00      0      0              211536   13.0000              NaN        S
887          888         1       1                                                        Graham, Miss. Margaret Edith  female  19.00      0      0              112053   30.0000              B42        S
888          889         0       3                                            Johnston, Miss. Catherine Helen "Carrie"  female    NaN      1      2          W./C. 6607   23.4500              NaN        S
889          890         1       1                                                               Behr, Mr. Karl Howell    male  26.00      0      0              111369   30.0000             C148        C
890          891         0       3                                                                 Dooley, Mr. Patrick    male  32.00      0      0              370376    7.7500              NaN        Q
	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--	33--
   Survived                                                 Name     Sex
0         0                              Braund, Mr. Owen Harris    male
1         1  Cumings, Mrs. John Bradley (Florence Briggs Thayer)  female
2         1                               Heikkinen, Miss. Laina  female
3         1         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female
4         0                             Allen, Mr. William Henry    male
5         0                                     Moran, Mr. James    male
6         0                              McCarthy, Mr. Timothy J    male
7         0                       Palsson, Master. Gosta Leonard    male
8         1    Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)  female
9         1                  Nasser, Mrs. Nicholas (Adele Achem)  female
	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--	34--
     PassengerId  Survived  Pclass                                      Name     Sex   Age  SibSp  Parch             Ticket    Fare Cabin Embarked
0              1         0       3                   Braund, Mr. Owen Harris    male  22.0      1      0          A/5 21171  7.2500   NaN        S
100          101         0       3                   Petranec, Miss. Matilda  female  28.0      0      0             349245  7.8958   NaN        S
200          201         0       3            Vande Walle, Mr. Nestor Cyriel    male  28.0      0      0             345770  9.5000   NaN        S
300          301         1       3  Kelly, Miss. Anna Katherine "Annie Kate"  female   NaN      0      0               9234  7.7500   NaN        Q
400          401         1       3                        Niskanen, Mr. Juha    male  39.0      0      0  STON/O 2. 3101289  7.9250   NaN        S
	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--	35--
  letter  number
0      a       0
1      b       1
2      c       2
3      e       3
4      d       4
5      f       5
	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--	36--

 Формат столбцов:
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
SibSp            int64
Parch            int64
Ticket          object
Fare           float64
Cabin           object
Embarked        object
dtype: object
	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--	37-1--

 Размерность:
(10, 12)
	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--	37-2--

 Общая статистика
       PassengerId   Survived     Pclass        Age      SibSp      Parch       Fare
count     10.00000  10.000000  10.000000   9.000000  10.000000  10.000000  10.000000
mean       5.50000   0.500000   2.300000  28.111111   0.700000   0.300000  27.020820
std        3.02765   0.527046   0.948683  14.945271   0.948683   0.674949  23.601938
min        1.00000   0.000000   1.000000   2.000000   0.000000   0.000000   7.250000
25%        3.25000   0.000000   1.250000  22.000000   0.000000   0.000000   8.152075
50%        5.50000   0.500000   3.000000  27.000000   0.500000   0.000000  16.104150
75%        7.75000   1.000000   3.000000  35.000000   1.000000   0.000000  46.414575
max       10.00000   1.000000   3.000000  54.000000   3.000000   2.000000  71.283300
	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--	37-3--
сформированный DataFrame:
   0  1  2  3  4 letter r_letter
0  6  1  1  2  3      a        r
1  3  1  5  4  2      b        z
2  5  8  2  4  8      c        v
	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--	38-1--
индексы строк и столбцов:
[1 2]
[2 0]
	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--	38-2--
данные по индексации (строка, столбец):
5
5
	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--	38-3--
данные по индексации и наименованию:
1
b
	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--	38-4--
данные по условию:
   0  1  2  3  4 letter r_letter
0  6  1  1  2  3      a        r
	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--	38-5--
0     Low
1    High
2    High
3    High
4    High
5    None
6    High
7     Low
8    High
9     Low
Name: Age, dtype: object
	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--	39--
   PassengerId_  Survived_  Pclass_                                            FullName_    Sex_  Age_  SibSp_  Parch_           Ticket_    Fare_ Cabin_ Embarked_
0             1          0        3                              Braund, Mr. Owen Harris    male  22.0       1       0         A/5 21171   7.2500    NaN         S
1             2          1        1  Cumings, Mrs. John Bradley (Florence Briggs Thayer)  female  38.0       1       0          PC 17599  71.2833    C85         C
2             3          1        3                               Heikkinen, Miss. Laina  female  26.0       0       0  STON/O2. 3101282   7.9250    NaN         S
3             4          1        1         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0       1       0            113803  53.1000   C123         S
4             5          0        3                             Allen, Mr. William Henry    male  35.0       0       0            373450   8.0500    NaN         S
5             6          0        3                                     Moran, Mr. James    male   NaN       0       0            330877   8.4583    NaN         Q
6             7          0        1                              McCarthy, Mr. Timothy J    male  54.0       0       0             17463  51.8625    E46         S
7             8          0        3                       Palsson, Master. Gosta Leonard    male   2.0       3       1            349909  21.0750    NaN         S
8             9          1        3    Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)  female  27.0       0       2            347742  11.1333    NaN         S
9            10          1        2                  Nasser, Mrs. Nicholas (Adele Achem)  female  14.0       1       0            237736  30.0708    NaN         C
	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--	40--
True
	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--	41--
Age       3
Cabin    15
dtype: int64
	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--	42--
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--	43-1--
0                              Braund, Mr. Owen Harris
1    Cumings, Mrs. John Bradley (Florence Briggs Th...
2                               Heikkinen, Miss. Laina
3         Futrelle, Mrs. Jacques Heath (Lily May Peel)
4                             Allen, Mr. William Henry
5                                     Moran, Mr. James
6                              McCarthy, Mr. Timothy J
7                       Palsson, Master. Gosta Leonard
8    Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)
9                  Nasser, Mrs. Nicholas (Adele Achem)
Name: Name, dtype: object
	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--
Mr          517
Miss        182
Mrs         125
Master       40
Dr            7
Rev           6
Mlle          2
Major         2
Col           2
Countess      1
Capt          1
Ms            1
Sir           1
Lady          1
Mme           1
Don           1
Jonkheer      1
Name: Title, dtype: int64
	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--	43-2--

Process finished with exit code 0
