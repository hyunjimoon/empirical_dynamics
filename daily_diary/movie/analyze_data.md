11.20

11.19
- new: use `startYear` as `productionYear`
>new_movie = pd.merge(new_movie_en, new_movie_basic[['titleId','primaryTitle', 'title', 'startYear']], on = 'titleId', how = "left")
print(new_movie_basic.shape[0],new_movie_en.shape[0], new_movie.shape[0], )
> 9m, 400k, 400k


- dropna for `NA` for old_movie year
- > old_movie['year'] = old_movie['year'].dropna().astype(int)
- 
11.18
- remake tsv file containing (title, year), language = 'en'
- upload to engaing db (oldtitle.tsv, newtitle.tsv)
- join with index (title, year) - if oldtitle's one (2m?) is spanish :) 
- actor
11.13
- used cinemagoer, easy for checking

### oldtitle
- `dropna` from oldtitle.title (two rows which prevented filtering us films) 
- filter out #, -0, ! containing filmtitles: 2.5m ->  1.8m 


### newtitle
- filter `region` == US: 33m -> 1m
- filter language == en: 33m ->  400k ({'\\N', 'cr', 'en', 'es', 'fr', 'haw', 'hi', 'myv', 'yi'})
- filter type == imdbDisplay: 33m ->  3m {'\\N','alternative','dvd','dvd\x02video','festival','festival\x02working','imdbDisplay','original','tv', 'tv\x02video','tv\x02working','video','video\x02working','working'}

#jcq agree region filter is better


## OctW4
- analyze the [[cinemagoer]] code

## OctW3
- data [[imdb17]] and [[imdb22]] doesn't seem to match well (heading, heading) 
- https://github.com/cinemagoer/cinemagoer/blob/996fde11697d72a1196b3619ec97cfb9599dd492/imdb/parser/sql/dbschema.py#L220 name, id, gender, 
- 13 vs 22 table (actor, title)
- aiming for not pickle but [netcdf](https://docs.xarray.dev/en/v2022.10.0/user-guide/io.html#netcdf)


## OctW2
- 사람, title, mapping (합; actor, actress)
- identifier match btw 13 and 22 (nm0000123 george clooney)
- 

JC asked:
0.  compare and document the coverage between them in terms of variables and entities; and any other salient differences.
- [[fr17
2.  I’ve attached the simplest version of my recent Elite Fragmentation and Power agent-based model.
## Data
- variables
- entities
- other salient differences.

- study: trade can worsen income inequality
- 
<img width="406" alt="image" src="https://user-images.githubusercontent.com/30194633/194927543-634a13d8-84f8-48d6-bc19-cf47ac44cad8.png">
