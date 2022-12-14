## code review
- movie, person, character are three main objects
```
class IMDbBase:  
    """The base class used to search for a movie/person/character and  
    to get a Movie/Person/Character object
```

- it has [search/get] `sg_movie`, `sg_person`, `sg_episode`, (Q. difference of search vs get)
```
def get_person(self, personID, info=Person.Person.default_info, modFunct=None):  
    """Return a Person object for the given personID.  
  
    The personID is something used to univocally identify a person;    it can be the imdbID used by the IMDb web server, a file    pointer, a line number in a file, an ID in a database, etc.  
    info is the list of sets of information to retrieve.  
    If specified, modFunct will be the function used by the Person    object when accessing its text fields (like 'mini biography')."""    personID = self._normalize_personID(personID)  
    personID = self._get_real_personID(personID)  
    person = Person.Person(personID=personID, accessSystem=self.accessSystem)  
    modFunct = modFunct or self._defModFunct  
    if modFunct is not None:  
        person.set_mod_funct(modFunct)  
    self.update(person, info)  
    return person
```

```
def search_person(self, name, results=None):  
    """Return a list of Person objects for a query for the given name.  
  
    The results argument is the maximum number of results to return."""    if results is None:  
        results = self._results  
    try:  
        results = int(results)  
    except (ValueError, OverflowError):  
        results = 20  
    res = self._search_person(name, results)  
    return [Person.Person(personID=self._get_real_personID(pi),  
            data=pd, modFunct=self._defModFunct,  
            accessSystem=self.accessSystem) for pi, pd in res][:results]
```

- `get_[imdbPersonID, imdbCharacterID, ]
- `title2imdbID`: Translate a movie title (in the plain text data files format) to an imdbID
- `name2imdbID`: Translate a person name in an imdbID.
- `character2imdbID`: Translate a character name in an imdbID.
- `get_imdbID(self, mop)` #jcq?  Return the imdbID for the given Movie, Person, Character or Company object

## roles
- [link](https://cinemagoer.readthedocs.io/en/latest/usage/role.html) 
- people in the cast (actors and actresses), the `currentRole` attribute is set to the name of the character they played:
- "Since the end of 2017, IMDb has removed the Character kind of information. This document is still valid, but only for the obsolete “sql” data access system."
- 


link: 
keyword, aka_name, aka_title, cast_info, char_name, movie_info, movie_link, person_info, company_name, complete_cast, 
movie_keyword, movie_info_idx, movie_companies

## Title
- X 10
- https://github.com/cinemagoer/cinemagoer/blob/996fde11697d72a1196b3619ec97cfb9599dd492/imdb/parser/sql/dbschema.py#L258


## Actor
- [name](https://github.com/cinemagoer/cinemagoer/blob/996fde11697d72a1196b3619ec97cfb9599dd492/imdb/parser/sql/dbschema.py#L211)
- [charname](https://github.com/cinemagoer/cinemagoer/blob/996fde11697d72a1196b3619ec97cfb9599dd492/imdb/parser/sql/dbschema.py#L230): id, name, imdbindex (#?), imdbID (#?), namePcodeNF, surnamePcode


## Role
- 
others
- companyname