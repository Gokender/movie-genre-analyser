from itertools import groupby
from collections import namedtuple
from collections import defaultdict
from operator import itemgetter
import re
import codecs
import glob

regex = re.compile('[^\W\d]+')
western_dict = defaultdict(int)
movie_genre = ['drama','action','comedy','sci-fi','crime','thriller','romance','horror','war','fantasy','western']
genre = movie_genre[0]
utf8 = True

def countWords(filename):

    try:
        with codecs.open(filename,encoding="utf8") as f:
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

if(utf8 == True):
    list_files = glob.glob('C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\subtitles\\' + genre + '\\utf8\\*.srt')
else:
    list_files = glob.glob('C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\subtitles\\' + genre + '\\*.srt')

for filename in list_files:
        print(filename)
        countWords(filename)

temp = sorted(western_dict.items(), key=itemgetter(1),reverse=True)

file_result = codecs.open('C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\results\\' + genre + '.txt','w',encoding='utf8',errors='ignore')

for result in temp:
    file_result.write(result[0] + ';' + str(result[1]) + '\n')
file_result.close()

def compareUnique(compare_1,compare_2):

    filename1 = 'C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\results\\' + compare_1 + '.txt'
    filename2 = 'C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\results\\' + compare_2 + '.txt'

    list_1 = []
    list_2 = []
    list_result_1 = []
    list_result_2 = []

    file_1 = codecs.open(filename1,'r',encoding='utf8')
    file_2 = codecs.open(filename2,'r',encoding='utf8')

    lines1 = file_1.readlines()
    lines2 = file_2.readlines()

    for line in lines1:
        try:
            print(line)
            word = line.split(';')[0]
            list_1.append(word)
        except Exception as e:
            #print(e)
            count = 1


    for line in lines2:
        try:
            print(line)
            word = line.split(';')[0]
            list_2.append(word)
        except Exception as e:
            #print(e)
            count = 1

    for it in list_1:
        #print(it)
        try:
            if it not in list_2:
                 list_result_1.append(it)
        except UnicodeDecodeError:
            count = 1
            pass

    for it in list_2:
        #print(it)
        try:
            if it not in list_1:
                list_result_2.append(it)
        except UnicodeDecodeError:
            count = 1
            pass

    print(list_result_1)
    print('/n')
    print(list_result_2)

    file_result = codecs.open('C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\results\\' + compare_1 + '_' + compare_2 + '.txt','w',encoding='utf8')

    for result in list_result_1:
        file_result.write(result + '\n')
    file_result.close()

    file_result = codecs.open('C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\results\\' + compare_2 + '_' + compare_1 + '.txt','w',encoding='utf8')

    for result in list_result_2:
        file_result.write(result + '\n')
    file_result.close()

compare_1 = movie_genre[0]
compare_2 = movie_genre[1]

compareUnique(compare_1,compare_2)
