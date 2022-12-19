- Ajeossi is in six other region for newtitle with current tid (filtered out because non-eng region)
	- reason why  we couldn't find in .tsv file was `tt1527788` is not in movie_basic (merged movie_basics and movie_principals)
	- ![[Pasted image 20221214075635.png]]
- data provanence 2 by 2 table of (`title`, `year`)

| -            | title | allowable difference |     |
| ------------ | ----- | -------------------- | --- |
| year         |   1    |    2                  |     |
| <2 year diff | 3      |   4                   |     |

- fill in the four cells (using `drop_duplicates`)
- iter2_mt[iter2_mt.titleId=='tt1527788']

 - data provenance is defined as: a record that describes entities and processes involved in producing and delivering or otherwise influencing that resource. Provenance provides a critical foundation for assessing authenticity, enabling trust, and allowing reproducibility. Provenance assertions are a form of contextual metadata and can themselves become important records with their own provenance


- feedback on [[winner's woe]]
	- need to be more in concrete setting; more veracity, reflect reality amap
	- movie or subscription (assumption user will only choose between the two)
	- change follower vs leader name to company A, B(as it would oscillate)
	- marketing companies would have data on `push unit` (e.g. AB testing)
	- need concrete mechanism on how pull strategy is activated in specific setting
		- is it movie or subscription? if movie (disney, pixar), people does not necessarily see only one movies, if subscription (netflix, hbo), people discarding `adopted` compartment of either leader or follower would not return to leader for certain amount of period (hazir's formulation of vaccine effect erosion would help)
		- network effect could be one e.g. ipod earphone is white which is easily seen by others
- data structure: xarray, [datatree](https://xarray-datatree.readthedocs.io/en/latest/api.html#indexing)

```
# dimensions are names describing what each axis is representing and coords are data related to datavariables, e.g. it could contain similar named object as some dim  
# If dim is not found in coords its values are range(0,n)  
# coords can also contain other (meta)data than dim info  
output_format = dict(  
    iter0_om=["index"],  
    iter0_nm =["index"],  
    iter1 = ["index"],  
    log_likelihood={  
        "loglik": "loglik"  
    },  
    coords={  
        "year": [n for n in range(precision['N'])],  
        "movie": setting['target_simulated_vector_names'],  
        "region": [r for r in range(precision['R'])]  
    },  
    dims={  
        'person': ["name", "year"],  
        'movie': ["title", "year"],  
        'character': ["movie", "person"],  
    }  
)
```

Inferencedata

| -   | inf data         | dyn data |     |
| --- | ---------------- | -------- | --- |
|     | draw             | year     |     |
|     | chain            | title    |     |
|     | prior            |          |     |
|     | prior predictive |          |     |
|     |                  |          |     |



- coord (school, prior_draw), data variables (inv_adj_time)

Just like `prior` , `observed_data`, `prior_predictive`
Groups have `title_string` ,`year` etc dims

and wondering what advantage I can have if I trun this into inferencedata (other than conveinience of)

iter0_old

Interestingly, `.stack(old_id = ["title", "year"])` 

![[Pasted image 20221213103732.png]]