from Node import *
from sys import MAX_INT

def get_cheapest_cost(rootNode):
    if (rootNode.children):
        minVal = MAX_INT
        for child in rootNode.children:
            minVal = min(get_cheapest_cost(child), minVal)
            return minVal+rootNode.cost
    else:
        return rootNode.cost
  
    
