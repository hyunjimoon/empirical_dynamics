![[Pasted image 20221207125951.png]]
12.4
#jcq list of verification check? currently, three checkpoints (after iter1-weak_sel, after join, after iter2-strong_sel)
list of validation check? (are we building the right product)

12.3
- table:
	- old_movie_lang: `old_id`, `lang` (`old_id` is (language, production year) )
- tracing movies (movie marketing paper [Lane04 traced 2001: A space odyssey and Saving private Ryan](marginnote3app://note/EB711E20-6073-4F57-83F9-41C4B0CACBA5) , Alkowatly19 traced A day after tomorrow)
- datafication: legitimate mean to access, understand, observe people's behavior
- 
## two imdb source (old, new)
- deleted movie title '4.45'
- why does the movie peak in 1920, 1970, 1990?
	- [[Pasted image 20221203072003.png]]
- report of old_only_movie
	- (out on a limb, 2011) vs (out on a limb, 2013)
	- `Pretty Woman, 2013 (old584036)` vs `Pretty Woman, 2003 (tt0396817) 1990 (tt0100405) 
	- `Ajeossi, 2010` is translated into `The Man from Nowhere, 2010 (tt1527788)` is abscent from new_data.tsv 
		-  36275,(2012-11-26), 36275 1682642 The Man from Nowhere NULL 1 2010 M5165

- 
## yet another source
[ftp.fu](https://ftp.fu-berlin.de/pub/misc/movies/database/frozendata/diffs/README) has `85948 movies with *known* complete cast data` and this seems to be basecamp of imdb (message from ceo col needham) more in [[imdb history]]
- weekly update from 1998-2017 (when Needham started when imdb message board was shut down)
- 
```
Ajeossi (2010)
   (aka Ajussi (2010))	(South Korea) (alternative transliteration)
   (aka L'uomo che veniva dal nulla (2010))	(Italy) (imdb display title)
   (aka The Man from Nowhere (2010))	(International: English title)
   (aka The Man from Nowhere (2011))	(Germany) (imdb display title)
   (aka The Man from Nowhere (2011))	(USA) (imdb display title)
```
	doesn't exist in new
	- `on the edge of eden` 
	- `a day of violence`
	- `About my father, 2010`
	- `made in berlin` (tt0256166): not included in raw move.aka file

between iter0, iter1, iter2, when are the movies `Ajeossi`, `on the edge of eden`, `a day of violence`, `about my father`  filtered out?
	1. first check `Ajeossi`, `on the edge of even`, `a day of violence`, `about my father` are in 

## paper and model
- "Do the ‘actors’ in the system, in this case the producers, perceive the risks of greater outlay as in line with possible gains? And is this the case, given that the appeal of a movie is impossible to guarantee?" from Lane – Movie Marketing Strategy Formation with System Dynamics
- marketing strategy it is called the ‘start-up problem’. Related to this is the assumption that purchases are only made in an ‘imitative mode’, that is, a consumer only purchases when having acquired information and/or a recommendation from an existing user and so chooses to imitate that user’s purchase decision
- structural divide associated with the advent of new forms of data-driven sense making will be increasingly apparent in the era of “big data" (Big data divide, Andrejevic14)
- 