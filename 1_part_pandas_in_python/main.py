#1.Importuokite pandas ir numpy
import pandas as pd
#2.Nuskaitykite į DF failą 'miestai isvalyti.csv', failas bus kartu tame paciame Folderyje(1_part_pandas_in_python)
df=pd.read_csv('miestai_isvalyti.csv')
print(df.shape)
print(df.info())
print('\t2--'*20)
#3.Atspausdinkite pirmas penkias df eilutes
print(df.head())
print('\t3--'*20)
#4.Padarykite, kad indeksas būtų stulpelis 'Miestas', ir kad šis pasikeitimas išliktų originale
df.set_index('Miestas', inplace=True)
print(df.head())
print('\t4--'*20)
#5.Ištraukite reikšmę, kiek gyventojų gyveno Marijampolėje 1923m.
print(df.loc['Marijampolė', '1923'])
print('\t5--'*20)
#6.Ištraukite stulpelį '1897', pirmas penkias eilutes.
print(df['1897'].head())
print('\t6--'*20)
#7.Ištraukite stulpelius '2019', '1970', '1923', pirmas 10 eilučių.
print(df[['2019', '1970', '1923']].head(10))
print('\t7--'*20)
#8.Su.shape patikrinkite, kiek eilučių turi lentelė (pamenat numpy? :)
print(df.shape)
print('\t8--'*20)
#9.pridėkite stulpelį su numeracija.
numbers = list(range(1, 104))
df['nr'] = numbers
print(df.head())
print('\t9--'*20)
#10.Ištraukite miestus nuo 30 iki 39 pozicijos.
print(df[(df['nr']>29) & (df['nr']<40)])
print('\t10--'*20)
#11.Ištrinkite numeracijos stulpelį.
df.drop('nr', axis=1, inplace=True)
print(df.head())
print('\t11--'*20)
#12.Kurių miestų dar nebuvo 1959m.?
print(df[df['1959'] == 0])
print('\t12--'*20)
#13.Kokie miestai 1897 turėjo daugiau gyventojų, negu 2019?
print(df[df['1897']>df['2019']])
print('\t13--'*20)
#14 Kuriuose miestuose padaugėjo gyventojų nuo 2011 iki 2019?
print(df[df['2019']>df['2011']][['2019', '2011']])
print('\t14--'*20)
#15.Kuriuose miestuose gyventojų skaičius nuosekliai mažėjo nuo pat 1897m.?
print(df[(df['1897'] > df['1923']) &
   (df['1923'] > df['1959']) &
   (df['1959'] > df['1979']) &
   (df['1979'] > df['1989']) &
   (df['1989'] > df['2001']) &
   (df['2001'] > df['2011']) &
   (df['2011'] > df['2019'])] )
print('\t15--'*20)
#arba dar toki radau:
decline = df[df.diff(axis=1, periods=-1) > 0]
select = decline[decline.isna().all(axis=1)]
print(select)
print(df.loc[select.index])
print('\t15a--'*20)
#16.Suraskite labiausiai procentaliai gyventojų skaičiumi padidėjusį ir sumažėjusį miestus nuo 1989m.
procentinis_skirt = ((df['2019'] - df['1989'])/df['1989'])*100
print(f'\
{procentinis_skirt.idxmax()}\t {int(procentinis_skirt.max())}%\n\
{procentinis_skirt.idxmin()}\t{int(procentinis_skirt.min())}%')
print('\t16--'*20)
#17.Nuresetinkite indeksą
print(df.reset_index().head())
print('\t17--'*20)
#18.irasyti i csv faila
df.to_csv('test.csv', encoding='utf-8',sep='\t')
pd.read_csv('test.csv', encoding='utf-8',sep='\t')

#output
(103, 10)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 103 entries, 0 to 102
Data columns (total 10 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Miestas  103 non-null    object
 1   2019     103 non-null    int64 
 2   2011     103 non-null    int64 
 3   2001     103 non-null    int64 
 4   1989     103 non-null    int64 
 5   1979     103 non-null    int64 
 6   1970     103 non-null    int64 
 7   1959     103 non-null    int64 
 8   1923     103 non-null    int64 
 9   1897     103 non-null    int64 
dtypes: int64(9), object(1)
memory usage: 8.2+ KB
None
	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--	2--
     Miestas    2019    2011    2001  ...    1970    1959    1923    1897
0    Vilnius  540919  535631  542287  ...  370153  236100  167400  154532
1     Kaunas  286763  315993  378650  ...  305600  216850   92446   70920
2   Klaipėda  147898  162360  192954  ...  140342   89500   35845   20100
3   Šiauliai  100119  109328  133883  ...   92375   59700   21387   16128
4  Panevėžys   87148   99690  119749  ...   74497   41100   19197   12968

[5 rows x 10 columns]
	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--	3--
             2019    2011    2001    1989  ...    1970    1959    1923    1897
Miestas                                    ...                                
Vilnius    540919  535631  542287  576747  ...  370153  236100  167400  154532
Kaunas     286763  315993  378650  419745  ...  305600  216850   92446   70920
Klaipėda   147898  162360  192954  202929  ...  140342   89500   35845   20100
Šiauliai   100119  109328  133883  145629  ...   92375   59700   21387   16128
Panevėžys   87148   99690  119749  126483  ...   74497   41100   19197   12968

[5 rows x 9 columns]
	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--	4--
9488
	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--	5--
Miestas
Vilnius      154532
Kaunas        70920
Klaipėda      20100
Šiauliai      16128
Panevėžys     12968
Name: 1897, dtype: int64
	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--	6--
               2019    1970    1923
Miestas                            
Vilnius      540919  370153  167400
Kaunas       286763  305600   92446
Klaipėda     147898  140342   35845
Šiauliai     100119   92375   21387
Panevėžys     87148   74497   19197
Alytus        50421   28165    6322
Marijampolė   35253   29073    9488
Mažeikiai     32711   13313    4300
Jonava        26715   14563    4115
Utena         25496   13309    4890
	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--	7--
(103, 9)
	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--	8--
             2019    2011    2001    1989  ...    1959    1923    1897  nr
Miestas                                    ...                            
Vilnius    540919  535631  542287  576747  ...  236100  167400  154532   1
Kaunas     286763  315993  378650  419745  ...  216850   92446   70920   2
Klaipėda   147898  162360  192954  202929  ...   89500   35845   20100   3
Šiauliai   100119  109328  133883  145629  ...   59700   21387   16128   4
Panevėžys   87148   99690  119749  126483  ...   41100   19197   12968   5

[5 rows x 10 columns]
	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--	9--
                2019   2011   2001   1989   1979   1970  1959  1923  1897  nr
Miestas                                                                      
Jurbarkas       9831  11232  13797  14310  10644   6541  4422  4409  7400  30
Raseiniai       9784  11203  12541  13211  11403   8946  6200  5270  7455  31
Vilkaviškis     9621  11547  13283  13829  11836   8452  5072  7263  5788  32
Anykščiai       8632  10575  11958  12758  10325   8250  5442  3500  3900  33
Prienai         8516   9867  11353  11909   9398   7550  5423  3260  2477  34
Joniškis        8358   9899  11329  11773   9303   7488  5889  4100  4828  35
Varėna          7987   9240  10845  12291   8015   4478  2401   407  2624  36
Kelmė           7655   9150  10900  11557   9073   6934  5140  2900  3914  37
Kaišiadorys     7486   8664  10002  10964   9022   4618  3011  1929   833  38
Naujoji Akmenė  7266   9300  12345  13590  14195  10127  5400     0     0  39
	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--	10--
             2019    2011    2001    1989  ...    1970    1959    1923    1897
Miestas                                    ...                                
Vilnius    540919  535631  542287  576747  ...  370153  236100  167400  154532
Kaunas     286763  315993  378650  419745  ...  305600  216850   92446   70920
Klaipėda   147898  162360  192954  202929  ...  140342   89500   35845   20100
Šiauliai   100119  109328  133883  145629  ...   92375   59700   21387   16128
Panevėžys   87148   99690  119749  126483  ...   74497   41100   19197   12968

[5 rows x 9 columns]
	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--	11--
             2019   2011   2001   1989  1979  1970  1959  1923  1897
Miestas                                                             
Visaginas   18185  26804  29554  32438  6212     0     0     0     0
Elektrėnai  11276  12012  14050  15871  8466  6730     0     0     0
	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--	12--
                     2019  2011  2001  1989  1979  1970  1959  1923  1897
Miestas                                                                  
Zarasai              6140  7349  8365  8916  7250  6624  4700  3785  6359
Švenčionys           4139  4980  5684  6469  5284  4617  4006     0  6025
Kalvarija            3858  4457  5090  5701  5879  5622  4698  4529  9378
Eišiškės             3071  3416  3765  3789  3467  3481  2532  2382  3196
Šeduva               2541  2895  3400  3584  3347  3309  3253  3186  4474
Vilkija              1898  2131  2338  2629  2371  2286  1996  2068  2012
Viekšniai            1670  1938  2270  2410  2781  2748  2734  2024  2951
Kudirkos Naumiestis  1480  1732  1997  2061  2090  2486  2574  3067  4595
Žagarė               1366  1712  2312  2649  2918  3386  3800  4730  8285
Salantai             1360  1615  1942  2431  2086  2156  2321  1942  2446
Linkuva              1277  1679  1797  2025  1876  1950  2144  1851  2077
Simnas               1269  1514  1980  2313  1625  1716  1661  1549  1642
Veisiejai            1211  1430  1762  2079  1687  1450  1513  1295  1540
Jieznas              1023  1204  1476  1883  1854  1658  1803  1000  1255
Varniai               995  1140  1355  2028  2059  2027  1902     0  2834
Daugai                980  1120  1458  2790  2054  1384  1287  1153  1288
Seda                  953  1138  1309  1500  1679  1821  2133  1851  2062
Virbalis              885  1095  1351  1566  1635  1489  1429  4018  3293
Vabalninkas           875  1057  1328  1905  2205  2070  2360  1267  2333
Obeliai               847  1074  1371  1804  1648  1681  1907  1328   975
Dūkštas               765   888  1070  1193  1633  1444  1968  1076  1000
Pandėlys              752   809  1024  1167  1129  1184  1277  1000  1221
Užventis              649   833   898  1149  1229  1406  1704     0   945
Dusetos               560   717   914  1184  1357  1600  1806  1164  1278
Kavarskas             528   666   809   972  1113  1191  1287  1041  1546
Troškūnai             372   451   525   672  1174  1417  1495  1252  1000
	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--	13--
                2019    2011
Miestas                     
Vilnius       540919  535631
Šalčininkai     6753    6402
Baltoji Vokė    1052    1047
	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--	14--
                     2019  2011  2001  1989  1979  1970  1959  1923  1897
Miestas                                                                  
Kudirkos Naumiestis  1480  1732  1997  2061  2090  2486  2574  3067  4595
Žagarė               1366  1712  2312  2649  2918  3386  3800  4730  8285
	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--	15--
                     2019  2011  2001  1989  1979  1970  1959  1923  1897
Miestas                                                                  
Kudirkos Naumiestis   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
Žagarė                NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
                     2019  2011  2001  1989  1979  1970  1959  1923  1897
Miestas                                                                  
Kudirkos Naumiestis  1480  1732  1997  2061  2090  2486  2574  3067  4595
Žagarė               1366  1712  2312  2649  2918  3386  3800  4730  8285
	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--	15a--
Neringa	 39%
Daugai	-64%
	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--	16--
     Miestas    2019    2011    2001  ...    1970    1959    1923    1897
0    Vilnius  540919  535631  542287  ...  370153  236100  167400  154532
1     Kaunas  286763  315993  378650  ...  305600  216850   92446   70920
2   Klaipėda  147898  162360  192954  ...  140342   89500   35845   20100
3   Šiauliai  100119  109328  133883  ...   92375   59700   21387   16128
4  Panevėžys   87148   99690  119749  ...   74497   41100   19197   12968

[5 rows x 10 columns]
	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--	17--

Process finished with exit code 0
