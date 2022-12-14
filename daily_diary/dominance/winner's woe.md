Winner’s woe with system dynamics - Angie moon

- [[#Examples|Examples]]
- [[#Introduction|Introduction]]
- [[#Research Background|Research Background]]
- [[#Simulation Model|Simulation Model]]
- [[#Simulation Results|Simulation Results]]
- [[#Conclusion|Conclusion]]


push unit, pull unit 

영화사 (disney vs pixar)
서론

팔로워가 파지티브 루프를 선택하게 되면 리더를 추월할 수 있다는 것을 보여준다.

선택의 문제

리더와 팔로워는 특정 시점에 네가티브 루프 (push)와 파지티브 루프 (pull)중 하나를 선택한다.

네가티브 루프는 효과가 즉각적이고 비교적 달성하기 쉽다. (advertisement)

파지티브 루프는 효과가 장기적이고 달성이 어렵다. (wom, quality)

리더와 팔로워는 자신의 목표를 달성하기 위해 네가티브 루프를 선택하게 된다.

è Capacity trap, 내쉬 균형

이를 구현하기 위해,

-       푸시전략과 풀전략의 효과 모수를 어떻게 정할 것인가? 기존의 연구에서 가져오면 가장 좋을 것 같음. BASS모델을 이용한 연구들을 살펴봐서 모수를 어떻게 설정하였는지 살펴볼 필요가 있음.

-       전략에 따른 효과의 지속성 부분 : 하지르 교수의 연구와 같이 일정기간 유지되다가 소멸되는 것을 구현하여 포함시킬 필요가 있음.

**파지티브 루프를 선택할 수 있는 방안이 무엇인지 고민해봐야 할 것임.**

단기적인 목표지향이 아닌 장기적인 목표지향으로 가는 조직의 성과 시스템

전문경영인이 아닌 오너쉽에 의한 경영이 장기적인 목표 지향이 될 것인가? 하는 점

동적 시뮬레이션으로의 발전 모색

## Examples
- facebook > myspace
- edison > tesler
- betamax couldn't make use of wom () > vcr
- ebay > Craigslist
- orea > hydrox


## Introduction

There are no permanent winners. Even if the leader responds a little, the follower will not be able to catch up, so why does the reversal occur? How this phenomenon occurs is to be investigated through a system dynamics approach.

There is a stagnant market. A total of 100 customers live in this market. Leader has 50 of these customers. This is when followers jump into the market. There are only two strategies that leaders and followers can choose: a pull strategy and a push strategy. The pull strategy is assumed to be a strategy that encourages people around you to purchase by providing promotions to customers who have purchased. The full strategy uses advertising. It is assumed that the effects of the push strategy and the pull strategy are independent of each other. It is assumed that the effect of the pull strategy and the effect of the push strategy are the same for both the leader and the follower.

As a result of the simulation, if the followers follow the leader's strategy, the leader cannot defeat the followers. The winner's curse is inevitable.

## Research Background

System dynamics is the study of analyzing the behavior of a system. It would be nice to understand that actions are different from actions and are the results that appear over time. The system consists of flow and stock variables. System dynamics is the study of analyzing the behavior of a system. It would be nice to understand that actions are different from actions and are the results that appear over time. The system consists of flow and stock variables. Examples of a typical system are shown in Figure 1.

Figure 1 Examples of systems

![](file:////Users/hyunjimoon/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image001.png)

Population, inventory, and task boxed in the middle in Figure 1 are stock variables. The inputs and outputs of stock variables are called flow variables. Stock is the accumulated difference between inflow and outflow.

An open system has feedback. Since there is no feedback in Figure 1, it is not called an open system. Feedback is the process of making a purchase because the inventory is small. Feedback is made up of relationships between variables, and those relationships make a loop. Looking at the simultaneity of the relationship, a reinforcing loop and a balancing loop are distinguished. If the direction changes when going around the loop once, it is a balancing loop, and if it does not change, it is a reinforcing loop.

One balancing loop can lead to a systemic behavior called goal seeking. One reinforcing loop creates a behavior called exponential growth or exponential decay. When one balancing loop and one reinforcing loop meet, an S-shape is created. Of course, this isn't always the case. It depends on the parameter value used for the relationship between the variables. Some loops may be formed but not dominant, or not even functioning. You can guess which loops are contained in the system by looking at the behavior of the system, but it is not easy to infer which behaviors will be derived by looking at which loops. This is also due to the degree of influence of the parameters discussed above.

f the number of loops is more than 3, it is not easy to infer the behavior of the system. It is also not easy to determine which loops are inherent when the behavior of the system appears. Such a case is called a complex world. System dynamics is an attractive approach in that it allows you to dig through a complex world loop by loop.

Figure 2 SI and PA Model

![](file:////Users/hyunjimoon/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.png)

The Adoption Rate (AR) per unit time (here, 1 day for convenience) is determined as follows.

AR= A*c*i*P/N

AR : Adoption Rate

A: Adopters

c: Contact Rate

i: Adoption Fraction

P: Potential Adopters

N: Total Population

An adopter meets and introduces 6 people a day, among which the ratio of potential adopters (40 people) is P/N (the total population is 100 people and the number of adopters is 60 people), and the probability of success is Assuming 0.02 (2%), the amount newly adopted per day is 2.8 people/day.

AR = 60*6*0.02*0.4= 2.8

Figure 2 is the SI model consisting of two stocks and one flow. Although it is expressed relatively simply, a logistic function is inherent, two loops are operated, and it generally represents an S-shape. Primarily, the SI model is heavily utilized when implementing the spread of an epidemic such as Covid. A similar PA model is often used to represent a new technology or marketing strategy.

Figure 3 BASS Diffusion Model with Replacement Purchase

![](file:////Users/hyunjimoon/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image003.png)

The BASS model reflects advertising and word-of-mouth effects by applying the PA model in Figure 2. The BASS model expressed advertising and word-of-mouth effects. The PA model has the characteristics of compensating for the small initial AR value. The replacement purchase loop is added to the model in Figure 3. Currently, adopters mainly show S-shape. Adopters return to potential customers after using the product for a period of time. <Figure 3> The model contains four loops, so it is difficult to guess what behavior it will show. Depending on the parameters, different system behaviors emerge. Overall, it is a form that returns through the Discard Rate flow, and it is a model that cannot diverge because it moves within the Total Population.

## Simulation Model

In this study, the model in Figure 3 was expanded and a model that reflected strategic behavior was constructed. The advertising was renamed the push strategy, and the word-of-mouth strategy was named the pull strategy.

Figure 4 Simulation model in this study

![](file:////Users/hyunjimoon/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image004.png)

The same 0.05 was applied to both the effect of the pull strategy and the effect of the push strategy. However, the push strategy works by a balancing loop, and the pull strategy affects AR by a reinforcing loop. If the pull strategy is continuously performed, the number of adopters can increase through exponential growth, and if the push strategy is performed, the number of adopters of the goal seeking type is expected to increase.

In Figure 4, parts C and D depict the expansion of leader and follower strategies. Leader Investment Choice acts as a kind of switch. When a leader loses his market share relative to his target market share, he chooses a pull strategy and a push strategy. Since the selection cannot be changed every day, the relational expression was set by inserting a period called Decisiontime. Here, it is assumed that strategy selection is made once every 30 days. Choosing a pull strategy or a push strategy increases the adoption effect. When it rises, it is modeled as rising as much as the basic unit (Leader Unit Chunk). The investment according to the strategy increases in a stepwise fashion based on a specific day. Leader Push Fraction is initially 0.05%, and increases by 0.05% when the leader chooses the push strategy.

There is a delay for push and pull strategy because the effect does not occur immediately when the investment is made. The delay time was set to 5 days. Delay3 was used as the delay function.

Detailed relational expressions are included in Appendix 1.

## Simulation Results

1)     When the follower follows the leader’s strategy  
  

Just include the same number in the relationship between Leader Investment Choice and Follower Investment Choice.

Leader Investment Choice=IF THEN ELSE(MODULO( Time, Decisiontime)=0 :AND:Leader Market Share Difference>0, 2, 0)

In the above relationship, 1 is when leader select push strategy, 2 is when leader select push strategy. If you put 0 or other numbers other than 1 or 2, the expansion strategy is not used. The case where the expansion strategy is not used refers to the case where the influence of the pull strategy and the push strategy were initially 0.05, but they are maintained as they are.

First, the case where the leader and followers no longer expand the strategy was set as 00 and the simulation was run.

Figure 5 In case 00, market shares of leader and follower

![](file:////Users/hyunjimoon/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image005.png)

The follower's pull strategy effect (although it does not expand any further) is insignificant at first compared to the leader's pull strategy effect, but it gradually takes away the leader's market share. show %.

Compare the case where both the leader and the follower perform 1 strategy (full strategy). In other words, it can be said that it is a competition by utilizing the advertising effect and the like and using a balancing loop. It is assumed that the initial value (0.05) of the pull effect of both the leader and the follower is maintained.

Figure 6 In case 11, market shares of leader and follower

[[Pasted image 20221213131834.png]]

Followers' market share rises rapidly and exceeds 50% before the 25th. Then, it gradually decreases so that the market share of the leader and the follower proceeds to the same level. Since this simulation was performed only for 500 days, it did not reach the same level within 500 days. It should be noted that the leader's market share, once reversed, cannot be reversed as long as the same strategy is employed. However, the gap gradually narrows.

Let's look at a case where both the leader and the follower continuously expand the pull strategy.

Figure 7 In case 11, market shares of leader and follower
[[Pasted image 20221213131845.png]]

If both the leader and the followers continuously expand the pull strategy, the leader continuously loses the market. The follower outstrips the leader's market share after 25 days, and continues to widen the market share gap. Leader's market share at 500 days is 0.3978. In the case of the pull strategy, it is judged that the path dependency phenomenon appears because the reinforcing loop operates.

2)     Follower does not follow the leader’s strategy

  
The change in market share when the leader chooses the pull strategy, and the follower chooses the push strategy is shown in Figure 8 below.

Figure 8 market shares in case (21) leader-pull, follower-push strategy
[[Pasted image 20221213131906.png]]


If the leader chooses the pull strategy and the follower chooses the push strategy, the follower has an absolute advantage. Before the 25th, the market share reverses. Only about 1/3 of the market is occupied by the leader. For followers, this is a good strategy to achieve your goals in a short period of time. The reason why the follower's market share fluctuates around 0.7 is because the Follower Target Market Share is set to 0.7. In other words, followers stop expanding the full strategy when their market share exceeds 70%. At this time, the competitor, the leader, takes over the market, and in the following period, the follower expands the pool strategy. These actions are reflected in the market with a delay.

Figure 9 market shares in case(12) leader-push, follower-pull strategy
[[Pasted image 20221213131925.png]]



Conversely, if the leader chooses the push strategy and the follower chooses the pull strategy, the leader does not lose the market significantly and succeeds in defending. The leader's average market share for 501 days (from day 0 to day 500) is 06706, and the average for followers is 0.3293. Between the 25th and the 50th, the follower sometimes outpaced the leader, but the leader expanded the pool strategy and took market share from the follower again.

## Conclusion

-       50%에서의 민감도와 100%의 민감도는 다름 leader (90-95%, 50-55%)

The winner's curse doesn't happen every time. But it happens often. In particular, if the follower follows the leader's strategy, the winner's curse takes place.

Table 1 Market share winner according to leader and follower strategies

Leader’s strategies

No-expansion(0)

Push strategy expansion(1)

Pull strategy expansion(2)

Follower’s stretegies

No-expansion(0)

F=L

F<L

F<L

Push strategy expansion (1)

F>L

F>L

F>L

Pull strategy expansion(2)

F>L

F<L

F>L

If the follower chooses the same strategy when the leader does not choose the expansion strategy, when expanding the push strategy, or when expanding the pull strategy, the follower can have a higher market share than the leader. In particular, when the leader chooses the pull strategy, if the followers follow the pull strategy, the followers can gradually expand their market share.

On the other hand, the leader can regain market share only if the follower chooses the push strategy if the follower chooses the pull strategy. Therefore, the leader's strategy choice is conditional. This is a condition for followers to choose a pull strategy.

In this situation, if both the leader and the follower are fully informed, the leader will choose the full strategy. Followers should also choose a push strategy to increase their market share. 11 is considered to be a Nash Equilibrium situation.

부록1. <그림 4> 모델에서 사용된 변수들과 수식들

Average Adoption Life=10

Decisiontime=30

Desired Follower Adoption Rate=Follower Adoption from Push+Follower Adoption from Pull

Desired Leader Adoption Rate=Leader Adoption from Push+Leader Adoption from Pull

Follower Adopter= INTEG (Follower Adoption Rate-Follower Discard Rate,0)

Follower Adoption Fraction=DELAY3(Follower Pull Investment, Pull Delay)

Follower Adoption from Push=Potential Adopter*Follower Push Fraction

Follower Adoption from Pull=Follower Adopter*Follower Adoption Fraction*XIDZ( Total Population-Leader Adopter-Follower Adopter, Total Population, 0)

Follower Adoption Rate=MIN(Desired Follower Adoption Rate, Potential Adopter*XIDZ(Desired Follower Adoption Rate, Desired Follower Adoption Rate+Desired Leader Adoption Rate, 0))

Follower Discard Rate=Follower Adopter/Average Adoption Life

Follower Investment Choice=IF THEN ELSE(MODULO( Time, Decisiontime)=1:AND:Follower Market Share Difference>0, 2, 0)

Follower Market Share Difference=Follower Target Market Share-Follower Market Share

Follower Market Share=         XIDZ(Follower Adopter, Follower Adopter+Leader Adopter, 1)

Follower Push Chunk=IF THEN ELSE(Follower Investment Choice=1, Push Unit Chunk, 0)

Follower Push Fraction=         DELAY3(Follower Push Investment, Push Delay)

Follower Push Investment= INTEG (Follower Push Chunk,   Push Unit Chunk)

Follower Pull Chunk=IF THEN ELSE(Follower Investment Choice=2, Pull Unit Chunk, 0)

Follower Pull Investment= INTEG (Follower Pull Chunk,Pull Unit Chunk)

Follower Target Market Share=0.7

Leader Adopter= INTEG (-Leader Discard Rate+Leader Adoption Rate,Leader Initial Adopter)

Leader Adoption from Push=Leader Push Fraction*Potential Adopter

Leader Adoption from Pull=Leader Adopter*Leader Pull Fraction*XIDZ( Total Population-Leader Adopter-Follower Adopter, Total Population, 0)

Leader Adoption Rate=MIN(Desired Leader Adoption Rate, Potential Adopter*XIDZ(Desired Leader Adoption Rate, Desired Follower Adoption Rate+Desired Leader Adoption Rate, 0))

Leader Discard Rate=Leader Adopter/Average Adoption Life

Leader Initial Adopter=50

Leader Investment Choice=IF THEN ELSE(MODULO( Time, Decisiontime)=0 :AND:Leader Market Share Difference>0, 2, 0)

Leader Market Share Difference=Leader Target Market Share-Leader Market Share

Leader Market Share=XIDZ(Leader Adopter, Leader Adopter+Follower Adopter, 1)

Leader Push Chunk=IF THEN ELSE(Leader Investment Choice=1, Push Unit Chunk, 0)

Leader Push Fraction=DELAY3(Leader Push Investment, Push Delay)

Leader Push Investment= INTEG (Leader Push Chunk,Push Unit Chunk)

Leader Pull Chunk=IF THEN ELSE(Leader Investment Choice=2, Pull Unit Chunk, 0)

Leader Pull Fraction=DELAY3( Leader Pull Investment, Pull Delay)

Leader Pull Investment= INTEG (Leader Pull Chunk,Pull Unit Chunk)

Leader Target Market Share=0.7

Potential Adopter= INTEG (Leader Discard Rate+Follower Discard Rate-Leader Adoption Rate-Follower Adoption Rate,           Total Population-Leader Initial Adopter)

Push Delay=5

Push Unit Chunk=0.05

Pull Delay=5

Pull Unit Chunk=0.05

Total Population=100

FINAL TIME = 500

INITIAL TIME = 0

TIME STEP = 1