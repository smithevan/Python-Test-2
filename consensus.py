import math
import random
from platform import node

nodes = {}

def create_node (nodes, node_number):
    print('Create new node (y/n/q)?  ')
    node_creation = input()
    if node_creation == 'y':
        print(node_number)
        node_weight = random.randint(0, 999)
        nodes.update({node_number: node_weight})
        print('Node ' + str(node_number) + ' created.')
        print('Node weight: ' + str(node_weight))
        return True
    elif node_creation == 'n':
        print('Node not created.')
        return True
    elif node_creation == 'q': 
        return False
    


def main():
    node_number = 0
    while create_node(nodes, node_number):
        print(nodes)
        node_number += 1
        print('xx:' + str(node_number))
    else:
        print('Process terminated')
    
main()




