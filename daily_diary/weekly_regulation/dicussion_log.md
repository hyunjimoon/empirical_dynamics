Nov w2
#vyq
1. between non manager and manager, who stays longer in the firm, could we learn this from data?
2. what is the probability outflow?
3. expected workweek?
5. initial value of Tasks to be Done: Desired Non Managers * Time to Non Manager Retire
- WIP: expected customer order rate * ()
- Inventory: expected customer order rate * 
6. why wass desired non mangers connected with non manager retiring
7. expected non managers workweek?
8. for expected non managers workweek, isn't connecting it with task arriving rather than task to be done better? (think of production start rate and production rate)
9. table function always dmnl?
10. advantage of difference over functional expression?


## oct w3 prep

Oct W2 discussion:
1. Two plots:  
i) statistical plot: average against average (regression, time aggregation)  
ii) science plot: trace the trajectory of real agent (under retrograde-allowing system, super-linear is not unsustainable)  
finding empirical case would be interesting e.g. agency gradually demising over > 3 moths  
get slope on log-log scale x: number of employee y: supervisor number,  

2. research hypothesis: Prey-predator dynamic of bureaucracy and its win-win strategy via preventive mainted
- fractal structure (judge-lawyer, lawyer-companies, `sup`-`sub` are similary structured)  
- Q2. how to model preventive maintenence role of `sup`  (model uploaded)
- Q3. how to formulate additional result of interaction of sup and sub (developing other factors than detected mistake that affects birth and death of each stocks)
- Q4. could capability traps (worse than better dynamics (zero-sum) be incoporated with preventive maintenceyen fig2.11)  


## oct w2 prep
- https://github.com/hyunjimoon/defense-reliability/blob/484eaf26a677d84ce5b7d7bb6ad42a559e946c4a/twin/RepairInven.ipynb

```
df18_sup = df_18[df_18["SUPERVIS"].isin(('2', '6', '7'))] # 291271
df21_sup = df_21[df_21["SUPERVIS"].isin(('2', '6', '7'))] #295234
df18_sub = df_18[~df_18["SUPERVIS"].isin(('2', '6', '7'))] #1809531
df21_sub = df_21[~df_21["SUPERVIS"].isin(('2', '6', '7'))] #1885872

sup_sub_ratio_18 = df18_sub.shape[0]/ df18_sup.shape[0] #6.21
sup_sub_ratio_21 = df21_sub.shape[0]/ df21_sup.shape[0] #6.39
```

- dynamic hierarchy 
- https://github.com/hyunjimoon/defense-reliability/blob/484eaf26a677d84ce5b7d7bb6ad42a559e946c4a/twin/RepairInven.ipynb

- https://github.com/Data4DM/BayesSD/issues/34
<img width="783" alt="image" src="https://user-images.githubusercontent.com/30194633/195704332-6e6c9584-8b6d-4260-9305-304b307ec162.png">


# Optimal level of Bureaucracy  

## List of possible problems (what do system fear?)
- unfair


## List of possible improvements (what do system desire?)
- lower use of budget (always?)


## List of administer's work to prevent system's fear

## List of administer's work to go towards system's desire
regulation to prevent possible problem (i.e. Administer's job)
- ensure reported represent reality, post-stratification (or its [multi-level version]([url](https://en.wikipedia.org/wiki/Multilevel_regression_with_poststratification)))
