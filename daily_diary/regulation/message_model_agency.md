- larger approval
- cost to mistake 

interview question:
- how much time you spend reporting people
- are there new reporting you need to do compared to a few years (if so, what is the cause?)
- national lab (ethernet, longer time, data security encoding)

#vyq 
1. should we use reference task for initial value for done right, done wrong, checked, undetected, detected etc?
2. perceived error rate being affected by reinitiated by reinitiated * delay penalty?
3. how to model hour/month to form desired nm?
4. why is availability value 1? (not 160?)

policy opt
![[Pasted image 20221207145733.png]]

12.6
`done right` + `done wrong` pile is one and all of them are realsed indefferentially after `max review lag`; currently, `done right` and `done wrong` can have different flow modes (i.e. in reality, could all four combination of [chekcing, gettting lucky] X [skipping, missing]) happen?

MORE EXPLICIT TRADEOFF: form only affects task flow via `done wrong` pile; mutiplication of two proportions (frac of `done right`, `done wrong`  and `form reviw accuracy`. i.e. main action is sending back so that it doesn't affect quality. but tradeoff is delayed time.
- form review accuracy is true negative sensitivity (saying no to false)

10 task ()


##
- `perceived error rate`: XIDZ(enraging+reinitiating * delay penalty,enjoying+enraging+reinitiating,a priori error rate)
- 
## attractiveness
[[Pasted image 20221206145636.png]]
- `error attractiveness`:  EXP(-error sensitivity * perceived error rate/a priori error rate)
- `delay attractiveness`: 1/(1+EXP(delay sensitivity*(average delivery time-reference delivery time)))

## average delivery time
- 
- multimodality makes optimization algorithm challenging
- to be improved from the last model: 1. how `done wrong` is moved to `done right` (physically or via smoothed speed change?)
- `perceived error rate`: XIDZ(enraging+reinitiating*delay penalty,enjoying+enraging+reinitiating,a priori error rate)
- tasks are not release until they are checked; exceptions are max review lag (when this is over, we drain)
- advantage of new model: delivery time component for attractiveness determining factor
- how to differentiate the role of nonmanager and manager in the language of flow? for `checking` and ``
- question:
	- relative allocation of task and form by their availability?
	- `work available` and `time available` resources*availability
	- why is `time available` = resources* availability
	- `resource`'s unit is FTE
	- form review accuracy as fraction between  \frac{(`checking or getting lucky` + `detecting`}{(`checking or getting lucky` + `skipping or missing + detecting`)}
	- `checking`: time checking/time per form/forms per task
	- `checking or getting lucky`: MAX( minimum release rate right, checking*fraction done right )
	- `form work available`: (done right+done wrong)* forms per task* time per form/normal form time
	- 
	- fraction of time for forms: ZIDZ(form work available,task work available+form work available)/(1+time pressure*shortcut sensitivity)
	- skipping or missing: MAX(0, minimum release rate wrong - checking*(1-fraction done right)) + checking*(1-fraction done right)*(1-form review accuracy)
	- 


12.5
1. accucracy as variable (manager complexity; more work, schedule pressure; task richness)
2. mng, nonmng capability 
average time자체가 feature라서 역함수
- doing right: MIN(Tasks/TIME STEP, time doing/time per task)*accuracy 
- 납기가 quality중요요소 (deliverty time, quality) ; tradeoff +
- quality's balance loop
두 모델을 task1, task2라 하면,
- 1. why is `time_doing` 's unit `hour/month`? It is defined as resources* productivity*(1-fraction of time for forms) 
- 2. from task1 model, mechanism of `productivity` and `resources` affecting `time_doing`, `time_checking`?
- 3. role of unit `fraction`? (`fraction of time for forms`, `fraction done right`)? differnce with `dmnl`?
- 
- 
- unit: taskmonths / Month
task가 done wrong에서 done right로 물리적으로 넘어가지는 않고, flow가 조절, 

보고자 하는 시간을 다 봤느냐 (dynamic aggregaton)
11.28
- reflecting Vicky's feedback 
	- change quality from stock to aux.var (perceived stock on stock variable is awkard, time to adj quality is long)
	- remove desired manager
-  reference mode dependent time horizon (if optimized agent's reference mode is oscillatory, long time horizon and observe growth of agency)
- add filling form as a switch which affects task completion rate (non-manager) and error rate 

how to model 
i) cost-optimizing agent 
- cost mistake
- cost rework
- cost coordination: 
- cost salary: manager (test) and nonmanager
- cost brand image: quality
[[CovidCost.png]]: cost of deaths, gdp, hospitalization aggregated over 1100 days

- elasticity of total cost (= salary, rework cost (baseline is zero error rate? does this correspond to 100 manager), manager what is the marginal value of cost of manager, nonmanager, task, quality
- frame it as finishing 100 amount of task
- #vyq calculating task cost is difficult as we don't have "normal or baseline" (compared to error frac = 0, base, base * 1.1, what is the cost summation (as the sum of salary cost, quality cost, task cost (mistake ))

- cost for spectrum of terrible to perfect mananger and nonmanger quality. test frac is conditional on error frac, as with zero error frac, test frac cannot exist wehreas zero test frac doesn't mean error frac cannot exist
	- assumption: managers perfectly detect task done wront and turn them into task done right

$\underset{p \in [0,0.2]}{argmin} \underset{t = 1..T}{\Sigma}\text{Profit(t, p)}$

$\frac{\partial{Revenue}}{\partial{PCQ}}$


| nmng success frac (task) \ mng success frac (test) | 1   | .5  | 0   |
| --------------------- | --- | --- | --- |
| 1                     | N1M1     |  N1M.5   |  N1M0    |
| .5                    | N.5M1    | N.5M.5     | N.5M0     |
| 0                     | N0M1    |   N0M.5  | N0M0    |

### Comparing the cost
- N1M.5 > N.5M1
N1M1 : perfect quality, but salary is high (manager having to go through every task)
N1M.5: perfect quality, 
N1M0: perfect quality, how can this achieved?????? manager number to `nm success frac` needs to be endogenized ()

--
N.5M1:    
N.5M.5:   
N.5M0: 

--
N0M1  
N0M.5: 
N0M0: quality plummets    

16 cases of environment, risk aversion, 


ii) effect of filling form
- 
11.22
- unified units, colored variables according to latent/measured, actionable/determined (orange-red-green-blue),  
- need debugging from negative desired nonmanagers (floating point from 0 resolved by setting initial stock value near equilibrium)


## Intended Story
- 100 weeks (2 years)

- Department with five professors and one administer.
- 40 tasks per week,
- standard workweek is 4 days per week, standard task completion rate is 2, standard test completion rate is 4 per week
- 40 = 5 professors * 2 tasks per day*professors * 4 days per week
- initial test frac ~ 4 * 1 * 4 / 40  = .4
2 tasks per week for professors, regulated by administer who tests .25 tasks per week giving .4 test fraction.

with more work rates (task/week),
1. cut corners (h/task)
2. overtime -  (h/week person)
3. hiring - person


![[Pasted image 20221116070820.png]]

#smq why probability is stock?