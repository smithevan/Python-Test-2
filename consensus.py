import math
import random
from platform import node

def create_node ():
    print('Create new node (y/n)?  ')
    print('Type "q" to quit.')
    node_creation = input()
    if node_creation == 'y':
        node_weight = random.randint(0, 999)
        print('Node created.')
        print(node_weight)
    elif node_creation == 'n':
        print('Node not created.')

create_node()


