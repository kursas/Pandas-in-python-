import pandas as pd
# 1 uzduotis
top_left = pd.read_csv('top1-25-1.csv')
top_right = pd.read_csv('top1-25-2.csv')
bottom_left = pd.read_csv('top26-50-1.csv')
bottom_right = pd.read_csv('top26-50-2.csv')
data_bottom = pd.concat([bottom_left, bottom_right], axis=1)
data_top = pd.merge(top_left, top_right, on=['Track.Name', 'Popularity'])
data = pd.concat([data_top, data_bottom], sort=False)

# 2 uzduotis
data['#'] = list(range(1, 51))
data.set_index('#', inplace=True)
# print(data.to_string())
# 3 uzduotis
grouped = data.groupby('Genre')
# 4 uzduotis
newdf = grouped.count()
# print(newdf[newdf['Energy']>3]['Energy'])
# 5 uzduotis
most_popular_genre = grouped.mean()['Popularity'].idxmax()
most_popular_score = grouped.mean()['Popularity'].max()
least_popular_genre = grouped.mean()['Popularity'].idxmin()
least_popular_score = grouped.mean()['Popularity'].min()
# print(most_popular_genre, most_popular_score)
# print(least_popular_genre, least_popular_score)
# 6 uzduotis
indikatoriai = data.columns.tolist()[3:]
zanrai = grouped.mean()[indikatoriai].idxmax()
skaiciai = grouped.mean()[indikatoriai].max()
result = pd.DataFrame([indikatoriai, zanrai, skaiciai],
                      ['Indikatorius', 'Žanras', 'Balai']).transpose()
# print(result.to_string())
# 7 uzduotis
print(data.info())
with_NaN = data[data['Genre'].isnull() | data['Popularity'].isnull()]
print(with_NaN.to_string())
# 8 uzduotis
data['Genre'].fillna('poop', inplace=True)
# 9 uzduotis
data['Popularity'].fillna(data['Popularity'].mean(), inplace=True)
print(data.to_string())

#output
FutureWarning: The default value of numeric_only in DataFrameGroupBy.mean is deprecated. In a future version, numeric_only will default to False. Either specify numeric_only or select only columns which should be valid for the function.
  skaiciai = grouped.mean()[indikatoriai].max()
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
                                       Track.Name    Artist.Name       Genre  Popularity  Beats.Per.Minute  Energy  Danceability  Loudness..dB..  Liveness  Valence.  Length.  Acousticness..  Speechiness.
#                                                                                                                                                                                                          
4                 Beautiful People (feat. Khalid)     Ed Sheeran         pop         NaN                93      65            64              -8         8        55      198              12            19
19                                         Lalala            Y2K         NaN        88.0               130      39            84              -8        14        50      161              18             8
25                   bad guy (with Justin Bieber)  Billie Eilish  electropop         NaN               135      45            67             -11        12        68      195              25            30
48                                        Happier     Marshmello     brostep         NaN               100      79            69              -3        17        67      214              19             5
50  Cross Me (feat. Chance the Rapper & PnB Rock)     Ed Sheeran         NaN        82.0                95      79            75              -6         7        61      206              21            12
                                                            Track.Name       Artist.Name             Genre  Popularity  Beats.Per.Minute  Energy  Danceability  Loudness..dB..  Liveness  Valence.  Length.  Acousticness..  Speechiness.
#                                                                                                                                                                                                                                        
1                                                             Senorita      Shawn Mendes      canadian pop   79.000000               117      55            76              -6         8        75      191               4             3
2                                                                China          Anuel AA    reggaeton flow   92.000000               105      81            79              -4         8        61      302               8             9
3                                        boyfriend (with Social House)     Ariana Grande         dance pop   85.000000               190      80            40              -4        16        70      186              12            46
4                                      Beautiful People (feat. Khalid)        Ed Sheeran               pop   87.489362                93      65            64              -8         8        55      198              12            19
5                                          Goodbyes (Feat. Young Thug)       Post Malone           dfw rap   94.000000               150      65            58              -4        11        18      175              45             7
6                                    I Don't Care (with Justin Bieber)        Ed Sheeran               pop   84.000000               102      68            80              -5         9        84      220               9             4
7                                                               Ransom         Lil Tecca        trap music   92.000000               180      64            75              -6         7        23      131               2            29
8                                                    How Do You Sleep?         Sam Smith               pop   90.000000               111      68            48              -5         8        35      202              15             9
9                                                Old Town Road - Remix         Lil Nas X       country rap   87.000000               136      62            88              -6        11        64      157               5            10
10                                                             bad guy     Billie Eilish        electropop   95.000000               135      43            70             -11        10        56      194              33            38
11                                                            Callaita         Bad Bunny         reggaeton   93.000000               176      62            61              -5        24        24      251              60            31
12                               Loco Contigo (feat. J. Balvin & Tyga)          DJ Snake         dance pop   86.000000                96      71            82              -4        15        38      185              28             7
13                                                   Someone You Loved     Lewis Capaldi               pop   88.000000               110      41            50              -6        11        45      182              75             3
14                                                  Otro Trago - Remix              Sech    panamanian pop   87.000000               176      79            73              -2         6        76      288               7            20
15                            Money In The Grave (Drake ft. Rick Ross)             Drake  canadian hip hop   92.000000               101      50            83              -4        12        10      205              10             5
16                                           No Guidance (feat. Drake)       Chris Brown         dance pop   82.000000                93      45            70              -7        16        14      261              12            15
17                                                          LA CANCION          J Balvin             latin   90.000000               176      65            75              -6        11        43      243              15            32
18                       Sunflower - Spider-Man: Into the Spider-Verse       Post Malone           dfw rap   91.000000                90      48            76              -6         7        91      158              56             5
19                                                              Lalala               Y2K              poop   88.000000               130      39            84              -8        14        50      161              18             8
20                                                         Truth Hurts             Lizzo       escape room   91.000000               158      62            72              -3        12        41      173              11            11
21                                                 Piece Of Your Heart            MEDUZA         pop house   91.000000               124      74            68              -7         7        63      153               4             3
22                                                              Panini         Lil Nas X       country rap   91.000000               154      59            70              -6        12        48      115              34             8
23                                                No Me Conoce - Remix       Jhay Cortez    reggaeton flow   83.000000                92      79            81              -4         9        58      309              14             7
24                                                     Soltera - Remix             Lunay             latin   91.000000                92      78            80              -4        44        80      266              36             4
25                                        bad guy (with Justin Bieber)     Billie Eilish        electropop   87.489362               135      45            67             -11        12        68      195              25            30
26                                                 If I Can't Have You      Shawn Mendes      canadian pop   70.000000               124      82            69              -4        13        87      191              49             6
27                                                        Dance Monkey       Tones and I    australian pop   83.000000                98      59            82              -6        18        54      210              69            10
28                                                            It's You         Ali Gatie  canadian hip hop   89.000000                96      46            73              -7        19        40      213              37             3
29                                                           Con Calma      Daddy Yankee             latin   91.000000                94      86            74              -3         6        66      193              11             6
30                                                       QUE PRETENDES          J Balvin             latin   89.000000                93      79            64              -4        36        94      222               3            25
31                                                            Takeaway  The Chainsmokers               edm   84.000000                85      51            29              -8        10        36      210              12             4
32                                                             7 rings     Ariana Grande         dance pop   89.000000               140      32            78             -11         9        33      179              59            33
33                                                   0.958333333333333            Maluma         reggaeton   89.000000                96      71            78              -5         9        68      176              22            28
34                           The London (feat. J. Cole & Travis Scott)        Young Thug       atl hip hop   89.000000                98      59            80              -7        13        18      200               2            15
35                                                   Never Really Over        Katy Perry         dance pop   89.000000               100      88            77              -5        32        39      224              19             6
36      Summer Days (feat. Macklemore & Patrick Stump of Fall Out Boy)     Martin Garrix          big room   89.000000               114      72            66              -7        14        32      164              18             6
37                                                          Otro Trago              Sech    panamanian pop   91.000000               176      70            75              -5        11        62      226              14            34
38                                      Antisocial (with Travis Scott)        Ed Sheeran               pop   87.000000               152      82            72              -5        36        91      162              13             5
39                                                              Sucker    Jonas Brothers          boy band   80.000000               138      73            84              -5        11        95      181               4             6
40  fuck, i'm lonely (with Anne-Marie) - from 13 Reasons Why: Season 3              Lauv         dance pop   78.000000                95      56            81              -6         6        68      199              48             7
41                                                         Higher Love              Kygo               edm   88.000000               104      68            69              -7        10        40      228               2             3
42                                               You Need To Calm Down      Taylor Swift         dance pop   90.000000                85      68            77              -6         7        73      171               1             5
43                                                             Shallow         Lady Gaga         dance pop   87.000000                96      39            57              -6        23        32      216              37             3
44                                                                Talk            Khalid               pop   84.000000               136      40            90              -9         6        35      198               5            13
45                                                          Con Altura           ROSALNA    r&b en espanol   88.000000                98      69            88              -4         5        75      162              39            12
46                                                     One Thing Right        Marshmello           brostep   88.000000                88      62            66              -2        58        44      182               7             5
47                                                            Te Robar         Nicky Jam             latin   88.000000               176      75            67              -4         8        80      202              24             6
48                                                             Happier        Marshmello           brostep   87.489362               100      79            69              -3        17        67      214              19             5
49                                                       Call You Mine  The Chainsmokers               edm   88.000000               104      70            59              -6        41        50      218              23             3
50                       Cross Me (feat. Chance the Rapper & PnB Rock)        Ed Sheeran              poop   82.000000                95      79            75              -6         7        61      206              21            12

Process finished with exit code 0

