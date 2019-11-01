import urllib.request



def load_deniro():
    global deniro_movies
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/deniro.csv"
    stream = urllib.request.urlopen(url)
    stream.readline()

    for line in stream:
        d = {}
        decoded = line.decode("UTF-8").split(',')
        if len(decoded) < 3:
            continue;
        d['year'] = int(decoded[0].strip())
        d['rating'] = int(decoded[1].strip())
        d['title'] = decoded[2].strip()
        deniro_movies.append(d)


def get_num_bad_movies(lst):
    bad_movies = 0;
    for movie in lst:
        if movie['rating'] <= 25:
            bad_movies += 1
    return bad_movies


def get_best_movie(lst):
    best_score = -1
    best_movie = None
    for movie in lst:
        if movie['rating'] > best_score:
            best_score = movie['rating']
            best_movie = movie['title']
    return best_movie


def get_average_rating_by_decade(lst):
    d = {}
    for movie in lst:
        decade = get_decade_from_year(movie['year'])
        if decade in d:
            d[decade].append(movie['rating'])
        else:
            d[decade] = [movie['rating']]
    for decade in d:
        d[decade] = sum(d[decade])/len(d[decade])
    return d



def get_decade_from_year(year):
    year = int(year/10)
    return year * 10

deniro_movies = []
load_deniro()
print(deniro_movies)
print(get_num_bad_movies(deniro_movies))
print(get_best_movie(deniro_movies))
decades_of_deniro = get_average_rating_by_decade(deniro_movies);
for d in decades_of_deniro:
    print(d, " : ", decades_of_deniro[d])