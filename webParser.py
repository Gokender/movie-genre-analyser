from bs4 import BeautifulSoup
import re
import requests
import urllib.request

regex_1 = re.compile('(".*?")')
regex_2 = re.compile('(/\d+")')
pages = 30 #number of pages to crawl by genre
start_page = 0
#movie_genre = ['drama','action','comedy','sci-fi','crime','thriller','romance','horror','war','fantasy','western']
movie_genre = ['thriller']

domain = 'https://mvsubtitles.com'

def getIdDownload(url):

    list_id = []
    response = requests.get(url)
    #print(response.status_code)
    data = response.text

    soup = BeautifulSoup(data, 'html.parser')
    subtitles = soup.find_all('a')

    for subtitle in subtitles:

        m = re.search(regex_2,str(subtitle))
        if(m):
            list_id.append(m.group().rstrip('"').lstrip("/"))

    return int(list_id[0])

def findUrlMovie(genre,pages):

    for page in range(start_page,pages):

        url = 'https://mvsubtitles.com/Gender/' + genre + '-subtitles?p=' + str(page+1)
        print(url)
        response = requests.get(url)
        data = response.text

        soup = BeautifulSoup(data, 'html.parser')
        movies = soup.find_all('h3')

        for movie in movies:

            m = re.search(regex_1,str(movie))
            url = m.group()
            url = url[:-11]
            url = url.lstrip('"')
            list_url.append(url)


    return list_url

##Find ID movie and download subtitle zipfile
for genre in movie_genre:
    #genre = movie_genre[0]
    list_url = []
    print('We\'re looking for the genre : ' + genre)
    list_u = findUrlMovie(genre,pages)
    print('We have ' + str(len(list_u)) + ' subtitles to download')

    for i in list_url:

        movie_name = i.lstrip().rstrip()
        #print(movie_name)
        web = domain + movie_name + '/english-subtitles'

        try:
            id_movie = getIdDownload(web)
            url_download = domain + '/download' + movie_name + '/english/' + str(id_movie) #+ '.zip'
            print('Downloading : ' + url_download)

            response = requests.get(url_download)
            filepath = 'C:\\Users\\Gauthier\\Documents\\Projets\\movie-genre-analyser\\subtitles\\' + genre + '\\' + movie_name + '.zip'

            urllib.request.urlretrieve(url_download,filepath)

        except Exception as e:
            print(e)

    print('---------------------------------------')
