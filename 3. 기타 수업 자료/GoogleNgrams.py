import pandas as pd
import re, requests
from ast import literal_eval
corpora = dict(eng_2019=26, eng_us_2019=28, eng_gb_2019=29, eng_fiction_2019=27,
               chi_sim_2019=34, fre_2019=30, ger_2019=31, heb_2019=35,
               ita_2019=33, rus_2019=36, spa_2019=32,          
               eng_us_2012=17, eng_us_2009=5, eng_gb_2012=18, eng_gb_2009=6,
               chi_sim_2012=23, chi_sim_2009=11, eng_2012=15, eng_2009=0,
               eng_fiction_2012=16, eng_fiction_2009=4, eng_1m_2009=1,
               fre_2012=19, fre_2009=7, ger_2012=20, ger_2009=8, heb_2012=24,
               heb_2009=9, spa_2012=21, spa_2009=10, rus_2012=25, rus_2009=12,
               ita_2012=22)
def Ngrams(A, start = 1800, end = 2019, language = 'eng_2019'):
    search = dict(content=A, year_start=start, year_end=end,
                  corpus=corpora[language])
    a = requests.get('http://books.google.com/ngrams/graph', params=search)
    b = literal_eval(re.findall('ngrams.data = (.*?);\\n', a.text)[0])
    c = pd.DataFrame({i['ngram']: i['timeseries'] for i in b},
                 index = range(search['year_start'],
                               search['year_end']+1))
    return(c)
