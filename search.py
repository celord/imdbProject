#from movies import Movies
import re

def search_by_name(name,moviedb):

    #name = [x for x in name.split()]
    for i in moviedb:
        actor_director = [ x.lower() for x in moviedb[i]['director_actor']]
        #print("*************************")
        #print(name)
        #print(actor_director)
        #if len(name) > 1:
        #    pass
        #else:
        #    print('*************************************')
        for j in actor_director:
            pattern = re.compile('.*' + name.lower() + '.*')
            #print(pattern)
            if re.findall(pattern,j):
                print(moviedb[i])
        

#
#if __name__ == '__main__':
#    #db = Movies()
#    #movies = db.get_top_movies()
#
#    search_by_name('spielberg',movies)
#