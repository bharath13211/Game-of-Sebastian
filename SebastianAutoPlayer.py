# Automatic Sebastian game player
# B551 Fall 2020
# PUT YOUR NAME AND USER ID HERE!
# Based on skeleton code by D. Crandall
#
#
# This is the file you should modify to create your new smart player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#
#from SebastianState import Dice
#from SebastianState import Scorecard
#import random

class SebastianAutoPlayer:

    def __init__(self):
        self.cat_auto = {}
    
    def cat_score(self, dice11):
        #dice = [int(j) for j in list(str(dice_m)) if j!=' ']
        
        counts_auto = [0,0,0,0,0,0]
        for i in dice11:
            counts_auto[i-1] += 1
        Numbers_auto = { "primis" : 1, "secundus" : 2, "tertium" : 3, "quartus" : 4, "quintus" : 5, "sextus" : 6 }
        Categories_auto = [ "primis", "secundus", "tertium", "quartus", "quintus", "sextus", "company", "prattle", "squadron", "triplex", "quadrupla", "quintuplicatam", "pandemonium" ]
#         if category in self.scorecard:
#             print("Error: category already full!")
        score = {}
        score1 = 0
        for category in Numbers_auto:
            if category not in self.cat_auto:               
                sco = counts_auto[Numbers_auto[category]-1] * Numbers_auto[category]
                score[category] = sco
         
        if sorted(dice11) == [1,2,3,4,5] or sorted(dice11) == [2,3,4,5,6]:
            if "company" not in self.cat_auto:
                sco = 40
                score["company"] = sco
                
        if (len(set([1,2,3,4]) - set(dice11)) == 0 or len(set([2,3,4,5]) - set(dice11)) == 0 or len(set([3,4,5,6]) - set(dice11)) == 0):
            if "prattle" not in self.cat_auto:
                sco = 30 
                score["prattle"] = sco
                        
        if (2 in counts_auto) and (3 in counts_auto):
            if "squadron" not in self.cat_auto:
                sco = 25
                score["squadron"] = sco

        if max(counts_auto) >= 3:
            if "triplex" not in self.cat_auto:
                sco = sum(dice11)
                score["triplex"] = sco
        
        if max(counts_auto) >= 4:
            if "quadrupla" not in self.cat_auto:
                sco = sum(dice11)
                score["quadrupla"] = sco
                
        if max(counts_auto) == 5:
            if "quintuplicatam" not in self.cat_auto:
                sco = 50
                score["quintuplicatam"] = sco
        
        if 1==1:
            if "pandemonium" not in self.cat_auto:
                sco = sum(dice11)
                score["pandemonium"] = sco
                
        score_keys = list(score.keys())
        score_values = list(score.values())
        if len(score_values)>0:
            bbb = score_keys[score_values.index(max(score_values))] 
            #self.cat_auto[bbb]= max(score_values)
            return [bbb,max(score_values)]
        else:
            return [Categories_auto[0],0]
                    
        
        
    def expected_score(self,dice_e,combi):
        dice_e1 = [int(j) for j in list(str(dice_e)) if j!=' ']
        exp = 0
        exp_count = 0
        ccc = []
        for c1 in ((dice_e1[0],) if not combi[0] else range(1,7)):
            for c2 in ((dice_e1[1],) if not combi[1] else range(1,7)):
                for c3 in ((dice_e1[2],) if not combi[2] else range(1,7)):
                    for c4 in ((dice_e1[3],) if not combi[3] else range(1,7)):
                        for c5 in ((dice_e1[4],) if not combi[4] else range(1,7)):
                            cc = sorted([c1,c2,c3,c4,c5])
                            if cc not in ccc:
                                ccc.append(cc)
                            #exp+= self.cat_score([c1,c2,c3,c4,c5])[1]
                            #exp_count += 1
        for i in ccc:
            #if i is not None:
            exp+= self.cat_score(i)[1]
            exp_count += 1
        return exp/exp_count
             
        
    def first_roll(self, dice, scorecard):
        dice_combi = []
        for d1 in (True,False):
            for d2 in (True,False):
                for d3 in (True,False):
                    for d4 in (True,False):
                        for d5 in (True,False):
                            dice_combi.append([d1,d2,d3,d4,d5])
        max_till_now = [0,[]]
        for com in dice_combi:
            exp_auto = self.expected_score(dice,com)
            if exp_auto > max_till_now[0]:
                max_till_now = [exp_auto,com]
        first_ret_ind = []
        for i in range(len(max_till_now[1])):
            if max_till_now[1][i] == True:
                first_ret_ind.append(i)
                        
        return first_ret_ind  

    def second_roll(self, dice, scorecard):
        dice_combi = []
        for d1 in (True,False):
            for d2 in (True,False):
                for d3 in (True,False):
                    for d4 in (True,False):
                        for d5 in (True,False):
                            dice_combi.append([d1,d2,d3,d4,d5])
        max_till_now = [0,[]]
        for com in dice_combi:
            exp_auto = self.expected_score(dice,com)
            if exp_auto > max_till_now[0]:
                max_till_now = [exp_auto,com]
        second_ret_ind = []
        for i in range(len(max_till_now[1])):
            if max_till_now[1][i] == True:
                second_ret_ind.append(i)
                        
        return second_ret_ind
        
      
    def third_roll(self, dice, scorecard):
        dice_e3 = [int(j) for j in list(str(dice)) if j!=' ']
        aaa = self.cat_score(dice_e3)
        self.cat_auto[aaa[0]]= aaa[1]
        return aaa[0]
        #return random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) )
                        