import requests
import json
import re
import urllib.request
import shutil
import os

english = re.compile('(english)')
start_count = 1262

file_key = open('import.key','r')
api_key = file_key.readline().rstrip('\n')
file_key.close()

# Downloading zipfile
def downloadingFile(data):

    json = data['pages']
    count = 0

    for j in json:

        movies = j['results']

        for movie in movies:

            #source = movie['small_links']
            isContinue = False
            try:
                small_link_1 = movie['small_link_1']
                small_link_2 = movie['small_link_2']
                small_link_3 = movie['small_link_3']
            except Exception as e:
                continue
            """if(len(source) <= 3):

                for small_link in source:
                    print(small_link)
                    small_link_1 = small_link
                    small_link_2 = small_link
                    small_link_3 = small_link
                    if(bool(re.search(english,small_link))):
                        small_link_final = small_link
                        isContinue = True;
                        break;
            else:
                small_link_final = source
                small_link_2 = source
                small_link_3 = source

            name = small_link_final.split('/')[3]
            language = small_link_final.split('/')[4]
            id_movie = small_link_final.split('/')[5]"""

            if(bool(re.search(english,small_link_1))):
                name = small_link_1.split('/')[3]
                language = small_link_1.split('/')[4]
                id_movie = small_link_1.split('/')[5]
            elif(bool(re.search(english,small_link_2))):
                name = small_link_2.split('/')[3]
                language = small_link_2.split('/')[4]
                id_movie = small_link_2.split('/')[5]
            elif(bool(re.search(english,small_link_3))):
                name = small_link_3.split('/')[3]
                language = small_link_3.split('/')[4]
                id_movie = small_link_3.split('/')[5]
            else:
                continue

            """if(isContinue == False):
                continue"""

            genres = movie['col_links/_text']

            url_download = 'https://mvsubtitles.com/download/' + name + '/' + language + '/' + id_movie
            filepath = 'C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\subtitles\\'+ name + '.zip'
            print('Downloading : ' + url_download)
            count = count + 1

            if(count >= start_count):
                try:
                    urllib.request.urlretrieve(url_download,filepath)
                except Exception as e:
                    print('ERROR - No Download for this file')
                    continue

            if(len(genres) <= 3):

                for genre in genres:
                    #print(genre)
                    destination_directory = 'C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\subtitles\\' + genre.lower() + '\\'
                    os.makedirs(destination_directory, exist_ok=True)
                    print('Copying in directory : ' + destination_directory)
                    if(count >= start_count):
                        shutil.copy2(filepath,destination_directory)

            else:
                destination_directory = 'C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\subtitles\\' + genres.lower() + '\\'
                os.makedirs(destination_directory, exist_ok=True)
                print('Copying in directory : ' + destination_directory)
                if(count >= start_count):
                    shutil.copy2(filepath,destination_directory)

            print('Step : ' + str(count))

    print('Total Count : ' + str(count))

json_file = open('Movies_list.json','r')
data_file = json_file.read()
data = json.loads(data_file)
downloadingFile(data)

print('-------------------------')
