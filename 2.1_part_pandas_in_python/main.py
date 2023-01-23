import numpy as np
import pandas as pd

#1.Sulipdykite iš 4 fragmentų vieną lentelę:
#fragmentus rasite čia
#top_left = pd.read_csv('top1-25-1.csv')
#top_right = pd.read_csv('top1-25-2.csv')
# bottom_left = pd.read_csv('top26-50-1.csv')
# bottom_right = pd.read_csv('top26-50-2.csv')
#pirmiausiai sujunkite apatinę dalį,
# tada viršutinę (yra persidengiančių stulpelių!),
# galiausiai viršų su apačia. Naudokite .concat() ir .merge() metodus.
top_left = pd.read_csv('D:/DUMENYS/DARIUS/Desktop/A_pandaz/top1-25-1.csv')
top_right = pd.read_csv('D:/DUMENYS/DARIUS/Desktop/A_pandaz/top1-25-2.csv')
bottom_left = pd.read_csv('D:/DUMENYS/DARIUS/Desktop/A_pandaz/top26-50-1.csv')
bottom_right = pd.read_csv('D:/DUMENYS/DARIUS/Desktop/A_pandaz/top26-50-2.csv')
data_bottom = pd.concat([bottom_left, bottom_right], axis=1)
data_top = pd.merge(top_left, top_right, on=['Track.Name', 'Popularity'])
data = pd.concat([data_top, data_bottom], sort=False)
print(pd.set_option('display.max_columns', 13))
print(data.head())
print('\t1--'*20)
#2.Sutvarkykite indeksą - padarykite, kad prasidėtų nuo 1.
data['#'] = list(range(1, 51))
data.set_index('#', inplace=True)
print(data.head())
print('\t2--'*20)
#3.Sukurkite grupavimo pagal žanrą objektą
grupavimas = data.groupby('Genre')
print(grupavimas)
print('\t3--'*20)
#4.kokie žanrai lentelėje pasitaiko daugiau negu 3 kartus?
newdf = grupavimas.count()
print(newdf.head())
print(newdf[newdf['Energy']>3]['Energy'])
print('\t4--'*20)
#5.Koks žanras pats populiariausias? Koks mažiausiai populiarus?
#(pagal populiarumo vidurkį)
most_popular_genre = grupavimas.mean(numeric_only=True)['Popularity'].idxmax()
most_popular_score = grupavimas.mean(numeric_only=True)['Popularity'].max()
least_popular_genre = grupavimas.mean(numeric_only=True)['Popularity'].idxmin()
least_popular_score = grupavimas.mean(numeric_only=True)['Popularity'].min()
print(most_popular_genre, most_popular_score)
print(least_popular_genre, least_popular_score)
print('\t5--'*20)
#6.Sukurkite lentelę, kurioje matytųsi, koks žanras turi aukščiausią vidurkį kiekviename indikatoriuje, bei pats vidurkis.
#kad nereikėtų daug vargti su stulpelių pavadinimais, galima juos ištraukti su .columns.tolist()
indikatoriai = data.columns.tolist()[3:]
zanrai = grupavimas.mean(numeric_only=True).idxmax(axis="columns")
skaiciai = grupavimas.mean(numeric_only=True).max(axis="columns")
result = pd.DataFrame([indikatoriai, zanrai, skaiciai],['Indikatorius', 'Žanras', 'Balai']).transpose()
print(result)
print('\t6--'*20)
#7.Grįžkime prie sulipdytos lentelės. Ištraukite visas eilutes, kurios turi NaN reikšmių.
#filtravimo sąlygose naudokite .isnull()* funkciją.*
print(data.info())
print(data[data['Genre'].isnull() | data['Popularity'].isnull()])
print('\t7--'*20)
#8.Stulpelyje 'Genre' NaN reikšmes pakeiskite į 'pop'
print(data['Genre'])
data['Genre'] = data['Genre'].fillna('popsas')
print(data['Genre'])
print('\t8--'*20)
#9.Stulpelyje 'Popularity' trūkstamas reikšmes pakeiskite į stulpelio vidurkį
print(data['Popularity'])
data['Popularity'] = data['Popularity'].fillna(value=data['Popularity'].mean())
print(data['Popularity'])
print('\t9--'*20)

#output
None
                        Track.Name    Artist.Name           Genre  Popularity  \
0                         Senorita   Shawn Mendes    canadian pop        79.0   
1                            China       Anuel AA  reggaeton flow        92.0   
2    boyfriend (with Social House)  Ariana Grande       dance pop        85.0   
3  Beautiful People (feat. Khalid)     Ed Sheeran             pop         NaN   
4      Goodbyes (Feat. Young Thug)    Post Malone         dfw rap        94.0   

   Beats.Per.Minute  Energy  Danceability  Loudness..dB..  Liveness  Valence.  \
0               117      55            76              -6         8        75   
1               105      81            79              -4         8        61   
2               190      80            40              -4        16        70   
3                93      65            64              -8         8        55   
4               150      65            58              -4        11        18   

   Length.  Acousticness..  Speechiness.  
0      191               4             3  
1      302               8             9  
2      186              12            46  
3      198              12            19  
4      175              45             7  
	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--	1--
                        Track.Name    Artist.Name           Genre  Popularity  \
#                                                                               
1                         Senorita   Shawn Mendes    canadian pop        79.0   
2                            China       Anuel AA  reggaeton flow        92.0   
3    boyfriend (with Social House)  Ariana Grande       dance pop        85.0   
4  Beautiful People (feat. Khalid)     Ed Sheeran             pop         NaN   
5      Goodbyes (Feat. Young Thug)    Post Malone         dfw rap        94.0   

   Beats.Per.Minute  Energy  Danceability  Loudness..dB..  Liveness  Valence.  \
#                                                                               
1               117      55            76              -6         8        75   
2               105      81            79              -4         8        61   
3               190      80            40              -4        16        70   
4                93      65            64              -8         8        55   
5               150      65            58              -4        11        18   

   Length.  Acousticness..  Speechiness.  
#                                         
1      191               4             3  
2      302               8             9  
3      186              12            46  
4      198              12            19  
5      175              45             7  
	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000019460A5ED10>
	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--
                Track.Name  Artist.Name  Popularity  Beats.Per.Minute  Energy  \
Genre                                                                           
atl hip hop              1            1           1                 1       1   
australian pop           1            1           1                 1       1   
big room                 1            1           1                 1       1   
boy band                 1            1           1                 1       1   
brostep                  2            2           1                 2       2   

                Danceability  Loudness..dB..  Liveness  Valence.  Length.  \
Genre                                                                       
atl hip hop                1               1         1         1        1   
australian pop             1               1         1         1        1   
big room                   1               1         1         1        1   
boy band                   1               1         1         1        1   
brostep                    2               2         2         2        2   

                Acousticness..  Speechiness.  
Genre                                         
atl hip hop                  1             1  
australian pop               1             1  
big room                     1             1  
boy band                     1             1  
brostep                      2             2  
Genre
dance pop    8
latin        5
pop          6
Name: Energy, dtype: int64
	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--
electropop 95.0
canadian pop 74.5
	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--
        Indikatorius            Žanras       Balai
0         Popularity           Length.       200.0
1   Beats.Per.Minute           Length.       210.0
2             Energy           Length.       164.0
3       Danceability           Length.       181.0
4     Loudness..dB..           Length.       198.0
5           Liveness           Length.       209.0
6           Valence.           Length.       191.0
7            Length.  Beats.Per.Minute       145.0
8     Acousticness..           Length.     202.625
9       Speechiness.           Length.       166.5
10              None           Length.  218.666667
11              None           Length.       194.5
12              None           Length.       173.0
13              None           Length.       225.2
14              None           Length.       257.0
15              None           Length.  193.666667
16              None           Length.       153.0
17              None           Length.       162.0
18              None           Length.       213.5
19              None           Length.       305.5
20              None  Beats.Per.Minute       180.0
	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--
<class 'pandas.core.frame.DataFrame'>
Int64Index: 50 entries, 1 to 50
Data columns (total 13 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Track.Name        50 non-null     object 
 1   Artist.Name       50 non-null     object 
 2   Genre             48 non-null     object 
 3   Popularity        47 non-null     float64
 4   Beats.Per.Minute  50 non-null     int64  
 5   Energy            50 non-null     int64  
 6   Danceability      50 non-null     int64  
 7   Loudness..dB..    50 non-null     int64  
 8   Liveness          50 non-null     int64  
 9   Valence.          50 non-null     int64  
 10  Length.           50 non-null     int64  
 11  Acousticness..    50 non-null     int64  
 12  Speechiness.      50 non-null     int64  
dtypes: float64(1), int64(9), object(3)
memory usage: 5.5+ KB
None
                                       Track.Name    Artist.Name       Genre  \
#                                                                              
4                 Beautiful People (feat. Khalid)     Ed Sheeran         pop   
19                                         Lalala            Y2K         NaN   
25                   bad guy (with Justin Bieber)  Billie Eilish  electropop   
48                                        Happier     Marshmello     brostep   
50  Cross Me (feat. Chance the Rapper & PnB Rock)     Ed Sheeran         NaN   

    Popularity  Beats.Per.Minute  Energy  Danceability  Loudness..dB..  \
#                                                                        
4          NaN                93      65            64              -8   
19        88.0               130      39            84              -8   
25         NaN               135      45            67             -11   
48         NaN               100      79            69              -3   
50        82.0                95      79            75              -6   

    Liveness  Valence.  Length.  Acousticness..  Speechiness.  
#                                                              
4          8        55      198              12            19  
19        14        50      161              18             8  
25        12        68      195              25            30  
48        17        67      214              19             5  
50         7        61      206              21            12  
	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--
#
1         canadian pop
2       reggaeton flow
3            dance pop
4                  pop
5              dfw rap
6                  pop
7           trap music
8                  pop
9          country rap
10          electropop
11           reggaeton
12           dance pop
13                 pop
14      panamanian pop
15    canadian hip hop
16           dance pop
17               latin
18             dfw rap
19                 NaN
20         escape room
21           pop house
22         country rap
23      reggaeton flow
24               latin
25          electropop
26        canadian pop
27      australian pop
28    canadian hip hop
29               latin
30               latin
31                 edm
32           dance pop
33           reggaeton
34         atl hip hop
35           dance pop
36            big room
37      panamanian pop
38                 pop
39            boy band
40           dance pop
41                 edm
42           dance pop
43           dance pop
44                 pop
45      r&b en espanol
46             brostep
47               latin
48             brostep
49                 edm
50                 NaN
Name: Genre, dtype: object
#
1         canadian pop
2       reggaeton flow
3            dance pop
4                  pop
5              dfw rap
6                  pop
7           trap music
8                  pop
9          country rap
10          electropop
11           reggaeton
12           dance pop
13                 pop
14      panamanian pop
15    canadian hip hop
16           dance pop
17               latin
18             dfw rap
19              popsas
20         escape room
21           pop house
22         country rap
23      reggaeton flow
24               latin
25          electropop
26        canadian pop
27      australian pop
28    canadian hip hop
29               latin
30               latin
31                 edm
32           dance pop
33           reggaeton
34         atl hip hop
35           dance pop
36            big room
37      panamanian pop
38                 pop
39            boy band
40           dance pop
41                 edm
42           dance pop
43           dance pop
44                 pop
45      r&b en espanol
46             brostep
47               latin
48             brostep
49                 edm
50              popsas
Name: Genre, dtype: object
	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--
#
1     79.0
2     92.0
3     85.0
4      NaN
5     94.0
6     84.0
7     92.0
8     90.0
9     87.0
10    95.0
11    93.0
12    86.0
13    88.0
14    87.0
15    92.0
16    82.0
17    90.0
18    91.0
19    88.0
20    91.0
21    91.0
22    91.0
23    83.0
24    91.0
25     NaN
26    70.0
27    83.0
28    89.0
29    91.0
30    89.0
31    84.0
32    89.0
33    89.0
34    89.0
35    89.0
36    89.0
37    91.0
38    87.0
39    80.0
40    78.0
41    88.0
42    90.0
43    87.0
44    84.0
45    88.0
46    88.0
47    88.0
48     NaN
49    88.0
50    82.0
Name: Popularity, dtype: float64
#
1     79.000000
2     92.000000
3     85.000000
4     87.489362
5     94.000000
6     84.000000
7     92.000000
8     90.000000
9     87.000000
10    95.000000
11    93.000000
12    86.000000
13    88.000000
14    87.000000
15    92.000000
16    82.000000
17    90.000000
18    91.000000
19    88.000000
20    91.000000
21    91.000000
22    91.000000
23    83.000000
24    91.000000
25    87.489362
26    70.000000
27    83.000000
28    89.000000
29    91.000000
30    89.000000
31    84.000000
32    89.000000
33    89.000000
34    89.000000
35    89.000000
36    89.000000
37    91.000000
38    87.000000
39    80.000000
40    78.000000
41    88.000000
42    90.000000
43    87.000000
44    84.000000
45    88.000000
46    88.000000
47    88.000000
48    87.489362
49    88.000000
50    82.000000
Name: Popularity, dtype: float64
	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--

Process finished with exit code 0
