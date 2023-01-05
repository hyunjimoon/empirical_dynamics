1 m immigrates to 10m country;
```
###### ITER perparing COMPLETE, size : 1048575 ###### ITER perparing COMPLETE, size : 10301370
```
after identifying
gene composition [[common_mutant_nativeex.png]]
- how to translate? 1001 gece -1001 Nights

protocol: after reading [[def(weekly_dominance)]], write summary of a day
[[Pasted image 20221228074709.png]] shows nan can result from both outer-join with mutant and native's absense

- [cinemagoer's 2006 log](https://github.com/cinemagoer/cinemagoer/blob/f23449c1ac5ee9ab728874c3fa18ba05a285ed9b/CHANGELOG.txt#L1178) introduced the isSame() method for both Movie and Person classes,useful to compare object by movieID/personID and accessSystem.

12.25
- old data title aka is not usuable (doesn't have id to match with the original)
- `old_id` as (title, year) of old movie confuses the analysis as most operations can be done with (title, year) groupy, instead of (old_id) groupby.
- after filtering only year +-1, remaining old but not new would be between 85k to 92k (~ 10k decrease)
- 
12.13 
- finding 
- 
12.5 
- rename `old_movie.pkl` to `old_title.pkl` (the initial dataset where iter0 starts from)
12.4
#jcq list of verification check? currently, three checkpoints (after iter1-weak_sel, after join, after iter2-strong_sel)
list of validation check? (are we building the right product)

12.3
- table:
	- old_movie_lang: `old_id`, `lang` (`old_id` is (language, production year) )
- tracing movies (movie marketing paper [Lane04 traced 2001: A space odyssey and Saving private Ryan](marginnote3app://note/EB711E20-6073-4F57-83F9-41C4B0CACBA5) , Alkowatly19 traced A day after tomorrow)
- datafication: legitimate mean to access, understand, observe people's behavior
12.1
- For year 1980, 1990, 2000 (old에만 있는 영화 솎아내기)
```
# 1980, 1990, 2000 (remove old_only, old\new; filtering빼고  old-id - new-id -genre - filtering)
```
- 
- join first processed old movie series with new movie + genre and check wether the 300 movies that were in old but not in new is
- the following 11 files are genre

```
short
movie
tvSeries
tvShort
tvMovie
tvEpisode
tvMiniSeries
tvSpecial
video
videoGame
tvPilot
```

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



- study: trade can worsen income inequality
- 
<img width="406" alt="image" src="https://user-images.githubusercontent.com/30194633/194927543-634a13d8-84f8-48d6-bc19-cf47ac44cad8.png">
