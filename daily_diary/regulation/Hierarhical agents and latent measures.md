- [[#Research question|Research question]]
- [[#Literature|Literature]]
- [[#Literature#Data, Model, Methodology|Data, Model, Methodology]]
- [[#Literature#Application|Application]]


### Research hypothesis
- regularization mechanism would be different for functional VS innovative organization (two types)
- functional : innovative =  top-down : bottom-up
- organization structure templete exist, which can express both types of mechanism can exist with the change of parameter values
- the only differnce being parameter value in hierarchical organization and establishing the verification procedure for its modeling assuption
- how to design parameter estimation for policy improvement for hierarchical system
	- organize parameters as recursive global-local relation and estimate in gibbs sampling way until both layers of estimated values convergence: lookup function parameters (e.g. how quality affects employment rate and task arrival rate) are more aggregated than adjustment time parameters (e.g. time to adjust employee, cusomters' perction of quality)

## Literature
- diversity captured with hierarchical bayes [[BayesSD/ContinuousCode/empirical_dynamics/reference/agency/Mackey15_CorporateDiv.pdf]]
- analyzing nasa's failure with type1-type2 error and system reliability [[Heimann93_ChallengerOrgStr.pdf]]
- optimal dynamic policy (5 years) [[Cai22_HierBayesDecision_The Effect of Loan Debt on Graduation by Department.pdf]]
- system dynamics: [[Rahmandad21_Covid.pdf]] estimation-based projection for covid from 92 countries
- bayesian: hierarchial bayesian introduced in paper [[Moon21_Hierarchical spline for time series prediction  An application to naval ship engine.pdf]], which uses splines to model hierarchical structure of engine in Korean Navy

### Data, Model, Methodology

Data: 
- federal agency from 98-21 on nonmanager/manager ratio and organization size. Agency has nested hierarchical structure which is preprocessed as ![[hier_agency]]

Model:
- stock and flow structure: how task, worker, perceived quality (stock) time series are determined by differential equations
- numeric value of adjustment time parmaters (time to submit, time to adjust [worker, quality] ) and analytical function parameters explaining [company quality to worker employement, quality to arriving task])
![[task_quality_worker]]



### Application
- every organization with hierarchical structure, for every area where concrete objective function can be defined using latent measures such as satisfaction, diversity, functionality e.g. bureaucracy, education  
- another diagram that can help enhance system structure is government reaction to iteawon catastrophe from [this](http://www.snujn.com/news/58826) article


--- (in progress)
- coding: making plots for hierarchical bayes which is being progressed in [here](https://github.com/Data4DM/stanify/blob/main/vignette/prey_predator_mpnoisedot1.ipynb)

- estimation plans:
```
1. table (quality to desired worker, quality to task) 변수들의 관계 (추정), adjustment time
endo: time to adj (stock-stock)
exo: 

estimation은 가설설정의 역방향 (p-q)

innovation firm and r and d firm 

structure, payoff, (환경, 구조, 전략 / 환경에 따라 전략이 달라지고, 전략에 따라 구조를 만들거냐, 구조)

제품에 따라 구조가 달라진다 (2가지, fisher, 96: functional innovative=variety)
a, b subscript (모수 차이) 구조가 달라서 (dominant)
local mean을 잘 모른다 (분산은 잘 안다)
```

should the two org. differ in structure or parameter level?

### Data
#### Layer1 (1 AGY archetype)

#### Layer2 (4 AGYTYP)
1: 'Cabinet Level Agencies':  
2: 'Large Independent Agencies (1000 or more employees)': 
3: 'Medium Independent Agencies (100-999 employees)': 
4: 'Small Independent Agencies (less than 100 employees)':   

#### Layer3 (130 AGY)
e.g. AF-DEPARTMENT OF THE AIR FORCE , full list:
'AA-ADMINISTRATIVE CONFERENCE OF THE UNITED STATES',
 'AB-AMERICAN BATTLE MONUMENTS COMMISSION',
...
 'ZS-UNITED STATES-CHINA ECONOMIC AND SECURITY REVIEW COMMISSION',
 'ZU-DWIGHT D. EISENHOWER MEMORIAL COMMISSION'}
 

#### Layer4 (530 AGYSUB)
AGYSUB, AGYSUBT: 533 types  
e.g. airforce: 55 AF02 (AIR FORCE INSPECTION AGENCY), AF03 (AIR FORCE OPERARTIOANL TEST AND EVALUATION)

bigger has better quality

full list is in [[hierarchical data structure of agency]].