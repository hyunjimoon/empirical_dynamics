- [[#Research question|Research question]]
- [[#Methodology|Methodology]]
- [[#Application|Application]]
- [[#Action|Action]]
- [[#Data|Data]]


### Research question
: capturing latent measure in hierarchical organization and establishing the verification procedure for its modeling assuption

### Methodology
Based on data processng of [fedscope](https://www.opm.gov/data/index.aspx),  the hierarchical structure like the following diagram is observed:
![[hierarchize_engine_failure]]

sd: [[Rahmandad21_Covid.pdf]] (Hazhir has empirical good job paper, but I cannot share without permission so we should ask for this)
bayesian: hierarchial bayesian introduced in paper [[Moon21_Hierarchical spline for time series prediction  An application to naval ship engine.pdf]], which uses splines to model hierarchical structure of engine in Korean Navy

### Application
- every organization with hierarchical structure, for every area where concrete objective function can be defined using latent measures such as satisfaction, diversity, functionality e.g. bureaucracy, education 

### Action
- item1: making simple (~ 3 stocks) to capture latent measure of the system.  I need help from you :) Two papers are great guide.
	- [[BayesSD/ContinuousCode/3_Data4DM/empirical_dynamics/reference/agency/Mackey15_CorporateDiv.pdf]]
	- [[Cai22_HierBayesDecision_The Effect of Loan Debt on Graduation by Department.pdf]]
- item2: making plots for hierarchical bayes which is being progressed in [here](https://github.com/Data4DM/stanify/blob/main/vignette/prey_predator_mpnoisedot1.ipynb)


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

full list is in [[hierarchical data structure of agency]].