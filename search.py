import re

def search_by_name(name,moviedb):

    mv = []
    name = [x for x in name.split()]
    for i in moviedb:
        actor_director = [ x.lower() for x in moviedb[i]['director_actor']]

        if len(name) > 1:
            #print(name)
            #print(actor_director)
            itr = []
            for ad in actor_director:
                for n in name:
                    if re.findall('.*' + n.lower() + '.*', ad):
                        itr.append(True)
                    else:
                        pass
            
            if len(name) == len(itr):
                if all(itr):
                    mv.append(moviedb[i]['movie_title'])
                    

        else:
            for j in actor_director:
                if re.findall('.*' + name[0].lower() + '.*', j):
                    mv.append(moviedb[i]['movie_title'])
    
    return(mv)
