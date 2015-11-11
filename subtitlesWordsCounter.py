from itertools import groupby
from collections import namedtuple
from collections import defaultdict
from operator import itemgetter
import re
import glob

regex = re.compile('[^\W\d]+')
western_dict = defaultdict(int)
movie_genre = ['drama','action','comedy','sci-fi','crime','thriller','romance','horror','war','fantasy','western']
genre = movie_genre[0]

def countWords(filename):

    try:
        with open(filename,encoding="utf8") as f:
            res = [list(g) for b,g in groupby(f, lambda x: bool(x.strip())) if b]

        Subtitle = namedtuple('Subtitle', 'number start end content')

        subs = []

        for sub in res:
            if len(sub) >= 3: # not strictly necessary, but better safe than sorry
                sub = [x.strip() for x in sub]
                number, start_end, *content = sub # py3 syntax
                start, end = start_end.split(' --> ')
                subs.append(Subtitle(number, start, end, content))

        for sub in subs:
            m = re.findall(regex,str(sub.content))
            for i in m:
                western_dict[i.lower()] += 1

        f.close()
    except Exception as e:
        print(e)

list_files = glob.glob('C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\subtitles\\' + genre + '\\*.srt')

for filename in list_files:
        print(filename)
        countWords(filename)

temp = sorted(western_dict.items(), key=itemgetter(1),reverse=True)

file_result = open('C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\results\\' + genre + '.txt','w',encoding='utf8')

for result in temp:
    file_result.write(result[0] + ';' + str(result[1]) + '\n')
file_result.close()
