
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