import random

def choose(val_list, prob_list):
    # Assume that all floats in prob_list add up to 100.0
    lottery = random.uniform(0, 100)
    
    if not lottery >= 0.0 and lottery <= 100.0:
        raise ValueError("Lottery out of range. WTF")
    
    min = 0.0
    index = 0
    max = prob_list[index]
    
    
    while lottery > max:
        
        if index >= len(prob_list)-1:
            raise ValueError("No viable choice for lottery.  Probability of list did not add up to 100.0")
        min += prob_list[index]
        index += 1
        max += prob_list[index]
        
    return val_list[index]