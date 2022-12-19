```
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
```

out of 8199,165 movies, 4,179,580 are unique meaning most of them have two titles 
dataprevelance which sorts the data quality 
- 100k out of 8000k ~ 1/80 display differences (relatively good enough data)
- old movie's aka title

- year difference of +-1

| -    | title exact | a.k.a. title match |
| ---- | ----------- | ------------------ |
| year | 1        |2                |
| year +-1     |      3       |    4                |

- us film중에는 품질1은 old에만 있는 것 없음
- 품질2는 이미 반은 해결.  newtitle + newtitleaka합친것과 old를 비교중 (old+oldaka)
- 품질3 위해, title별로 정렬 후 year1년 이내인것 count하기