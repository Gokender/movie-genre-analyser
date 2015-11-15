import codecs

def uniqueWord(list_1, list_2):

    list_res = []

    for it in list_1:
        try:
            #print(it)
            if it not in list_2:
                 list_res.append(it)
        except Exception as e:
            continue

    return list_res




movie_genres = ['drama','action','comedy','sci-fi','crime','thriller','romance','horror','war','fantasy','western','adventure']
list_drama = []
list_action = []
list_comedy = []
list_scifi = []
list_crime = []
list_thriller = []
list_romance = []
list_horror = []
list_war = []
list_fantasy = []
list_western = []
list_adventure = []

list_result = []

for movie_genre in movie_genres:

    file_result = codecs.open('results\\' + movie_genre + '_reduced2.txt',encoding='utf8')
    print('Openning : ' + movie_genre)

    if(movie_genre == 'drama'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_drama.append(word)

    elif(movie_genre == 'action'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_action.append(word)
    elif(movie_genre == 'comedy'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_comedy.append(word)
    elif(movie_genre == 'sci-fi'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_scifi.append(word)
    elif(movie_genre == 'crime'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_crime.append(word)
    elif(movie_genre == 'thriller'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_thriller.append(word)
    elif(movie_genre == 'romance'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_romance.append(word)
    elif(movie_genre == 'horror'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_horror.append(word)
    elif(movie_genre == 'war'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_war.append(word)
    elif(movie_genre == 'fantasy'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_fantasy.append(word)
    elif(movie_genre == 'western'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_western.append(word)
    elif(movie_genre == 'adventure'):

         lines = file_result.readlines()

         for line in lines:

             word = line.split(';')[0]
             list_adventure.append(word)

    file_result.close()

#DRAMA
print('Searching Drama')
list_result = uniqueWord(list_drama,list_action)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\drama_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#ACTION
print('Searching Action')
list_result = uniqueWord(list_action,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\action_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#COMEDY
print('Searching Comedy')
list_result = uniqueWord(list_comedy,list_drama)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\comedy_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#SCI-FI
print('Searching Sci-fi')
list_result = uniqueWord(list_scifi,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\sci-fi_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#CRIME
print('Searching Crime')
list_result = uniqueWord(list_crime,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\crime_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#THRILLER
print('Searching Thriller')
list_result = uniqueWord(list_thriller,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\thriller_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#ROMANCE
print('Searching Romance')
list_result = uniqueWord(list_romance,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\romance_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#HORROR
print('Searching Horror')
list_result = uniqueWord(list_horror,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\horror_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#WAR
print('Searching War')
list_result = uniqueWord(list_war,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\war_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#FANTASY
print('Searching Fantasy')
list_result = uniqueWord(list_fantasy,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\fantasy_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#WESTERN
print('Searching Western')
list_result = uniqueWord(list_western,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_horror)
list_result = uniqueWord(list_result,list_adventure)

result = codecs.open('results\\western_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()

#ADVENTURE
print('Searching Adventure')
list_result = uniqueWord(list_adventure,list_drama)
list_result = uniqueWord(list_result,list_comedy)
list_result = uniqueWord(list_result,list_scifi)
list_result = uniqueWord(list_result,list_crime)
list_result = uniqueWord(list_result,list_thriller)
list_result = uniqueWord(list_result,list_romance)
list_result = uniqueWord(list_result,list_action)
list_result = uniqueWord(list_result,list_war)
list_result = uniqueWord(list_result,list_fantasy)
list_result = uniqueWord(list_result,list_western)
list_result = uniqueWord(list_result,list_horror)

result = codecs.open('results\\adventure_final.txt','w',encoding='utf8')

for i in list_result:

    result.write(i + '\n')

result.close()
