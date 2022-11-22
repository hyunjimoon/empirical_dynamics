Done
- code summary: movie and person compare, cinemagoer schema
- model summary: movie, role, persons - matching + endogen. quality of labor+movie dependent task arrrival rate
- paper summary: 
	- diffusion model for movie marketing strategy (+ explain short product lifecycle of movie) [[Lane02_MovieMarketing.pdf]]
	- media production automation workflow [[Atta_auto_media_prod.pdf]], [[film_production_workflow]]

Discussion
- ok to filter only imdbDisplay type?
- seems to order, based on proximity? 
```
> dfo.title[12]
'The Eye of Ra: Part 2'
> ia.search_movie(dfo.title[12])
[<Movie id:0504987[http] title:_"Ace of Wands" The Eye of Ra: Part 2 (1971)_>,
 <Movie id:0504989[http] title:_"Ace of Wands" The Eye of Ra: Part 4 (1971)_>,
 <Movie id:0504986[http] title:_"Ace of Wands" The Eye of Ra: Part 1 (1971)_>,
 <Movie id:0504988[http] title:_"Ace of Wands" The Eye of Ra: Part 3 (1971)_>]
```
newtitle
- filter `region` == US: 33m -> 1m
- filter language == en: 33m ->  400k ({'\\N', 'cr', 'en', 'es', 'fr', 'haw', 'hi', 'myv', 'yi'})
- filter type == imdbDisplay: 33m ->  3m {'\\N','alternative','dvd','dvd\x02video','festival','festival\x02working','imdbDisplay','original','tv', 'tv\x02video','tv\x02working','video','video\x02working','working'}
oldtitle
- `dropna` from oldtitle.title (two rows which prevented filtering us films) 
- filter out #, -0,-1 ! containing filmtitles: 2.5m ->  1.8m 
(1991-01-01)

#jcq agree region filter is better
- easier way to import package on engagingdb
- quality of main-nonmain VS star-nonstar quality

To do:
- add year, remove duplicate
- unify trivially different dataset, 
- language (hypo: spanish title)
- persons preprocess
- person-movie
- ![[Pasted image 20221114124722.png]]

11.13
- analysis of cinemagoer [[cinemagoer]]

- for next: merging new's (movieID, title) with old's title so that detailed roles (crew information which old data seem to have??) can be added.

## search
- number of titles did not decreased after merge. This implied that all the titles included in **title.ratings** are actually a **_subset_** of the titles in **title.basics**
-

### 11.12
old: merge to map id with name, filter out #,0 containing[^1]
new: filter region = us films 

benefits of xarray, labeled multidimensional data structure[^2]
- looking into [[cinemagoer]]

Q1. question on python import: [why is the name cinemagoer but importing from imdb](https://github.com/cinemagoer/cinemagoer#installation)
Q2. 


[^1]: Evasión o victoria is included
[^2]: pysd's datastructure with dimension, coordinate, data variables: (time, 