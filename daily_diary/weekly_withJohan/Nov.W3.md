


## Before
- movies on screen from different country has the same titleId
![[Pasted image 20221119112156.png]]
- terrible language column quality; going with us region
![[Pasted image 20221119112632.png]]
- terrible year column quality (70k nan, after (#) filter: 43k )
- ![[Pasted image 20221119154622.png]]
- new_movie: 1.1m to 1m when filtering out `nan` year 
- 1.8m old_movie, 1m (230k with titleType == movie) new_movie
- `titleId` same movie-year but different id (drop_duplicate with id for now)
- ![[Pasted image 20221120231010.png]]
- droping title
- which titleType? (movie only)
- ![[Pasted image 20221121003720.png]]
## During
- #jcq 
- why would imdb22 call director and write as crew and would we need this?
- what use could person-knownForTitle have? ![[Pasted image 20221122034802.png]]
**title.crew.tsv.gz** – Contains the director and writer information for all the titles in IMDb. Fields include:

-   tconst (string) - alphanumeric unique identifier of the title
-   directors (array of nconsts) - director(s) of the given title
-   writers (array of nconsts) – writer(s) of the given title

## After
- filter movies in old but not in new by mapping the title with genre in new 
- apply this algorithm to not only movies but also tv series 