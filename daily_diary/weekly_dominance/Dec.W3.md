- pure old-new merge is 8m,  out of 100k null `titleId`, 40k is unique, but non-english was (german etc) too many, 
- improved `is_eng` function by allowing ' and `"``
- (after, # 52k increased to )
- 

- 2 by 2 table
- [[Pasted image 20221214165407.png]] shows two cases of one year difference (count then drop those with titleId.isnull() instances)

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
