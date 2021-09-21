The Game of Sebastian ->
--------------------

## Probelm Formulation

* The problem here is to write the algorithm for getting maximum score after rolling 5 dice and re-rolling specific dice/s "2 more times" to increase the score.

* One game will have 13 turns. In problem statement, 13 categories has been given and we need to assign a category only once can't assigned again in 13 turns 
![image](https://user-images.githubusercontent.com/85077692/134213683-45f3459c-9543-4a78-8a3a-de3ade1bd2a6.png)


Here, we used Expect minimax algorithm to get the best score. 

* the key idea we have used is to select all combinations of dices to re-roll and for each combination we have calculated the expected value. 
We have considered the combination which has maximum expected value and continued the process. 

We have given two classes(Sebastian, SebastianState). 
Our task is to implement Sebastian AutoPlayer class which will return the dice numbers that needs to be re-rolled. 

## Our Algorithm Description
* We have created two functions (cat_score, expected_score) 
* cat_score will take the dices output and returns the best category we can assign for that output.
* expected_score will take the combination of dice to be re-rolled and will returns the combination which has maximum expected value. 
* We have used there two functions and we returned the dices to be re-rolled in first re-roll (function: first_roll(self, dice, scorecard)) 
and second re-roll (function: second_roll(self, dice, scorecard)). 
* function "third_roll(self, dice, scorecard)" will return the best category we can assign after second re-roll to main function (Sebastian.py). 
* After playing 100 games of 13 turns in each gaem, it will calculate the Minimum, Maximum and Mean scores of 100 games. 

## Assumptions, Difficulties.

* We have assumed that if we are unable to assign category for a combination, we assigned score as "0(zero)" for that combination. 
* We have faced dificulties while assigning the best category for each time in 13 turns of one game. 
* We have overcome that issue by declaring a dictionary in constructor of SebastianAutoPlayer class which will store the categories those are already assigned. 
So by doing this, our algorithm will assign the next best category if best category is already assigned in previous turns.

********-------------------------------------********
