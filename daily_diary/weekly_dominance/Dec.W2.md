- Ajeossi is in six other region for newtitle with current tid (filtered out because non-eng region)
	- reason why  we couldn't find in .tsv file was `tt1527788` is not in movie_basic (merged movie_basics and movie_principals)
	- [[Pasted image 20221214075635.png]]
- [[winner's woe]]
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

output_format = dict(
	"iter0_otitle": ["titleId"], 
	"iter0_ntitle": ["titleId"], 
	"iter1_title": ["titleId"], 
	"iter2_title": ["titleId"],  # usregion, english title, 
	"iter0_operson": ["personId"], 
	"iter0_nperson": ["personId"], 
	"iter1_person": ["personId"], 
	"iter2_person": ["personId"],  
)
indexed by (title, year). Interestingly this reminds me of stacking chain and draw into `prior_draw`.

and wondering what advantage I can have if I trun this into inferencedata (other than conveinience of)

iter0_old

Interestingly, `.stack(old_id = ["title", "year"])` 

![[Pasted image 20221213103732.png]]