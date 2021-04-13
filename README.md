# imdbProject
Downloads and parses top 1000 movies from IMDB to gather and search movie info.
## Requeriments:

1. Intenet connection
2. ipython

# how to run:

1. Clone the repository

2. Open an ipython console inside the cloned repo's directory

3. Downloading the data (run this commands in the ipython console):

    `%run movies.py`
    `%run search.py`
    ```python
    from movies import Movie
    db = Movie()
    db = db.get_top_movies()
    #This last step may take some time
    ```
4. Search the database (still on the ipython console)

    ```python
    print(search_by_name('spielberg',db))

    #Output
    ['Saving Private Ryan', "Schindler's List", 'Jurassic Park', 'Raiders of the Lost Ark', 'Catch Me If You Can', 'Jaws', 'E.T. the Extra-Terrestrial', 'Minority Report', 'Indiana Jones and the Last Crusade', 'The Color Purple', 'Bridge of Spies', 'Close Encounters of the Third Kind', 'Empire of the Sun']

    print(search_by_name('spielberg hanks',db))
    ['Saving Private Ryan', 'Catch Me If You Can', 'Bridge of Spies']
    ```

5. TODO: 
    a. Move the db to an sqlite database
    b. Create a cron job to update db once a x time
    c. Exposing the api vie django or flask
    d. add search by movie name and by year mothods 







