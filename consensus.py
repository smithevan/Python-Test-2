import math
import random
from platform import node

nodes = {}
node_number = 0

def create_node (nodes, node_number):
    print('Create new node (y/n)?  ')
    print('Type "q" to quit.')
    node_creation = input()
    if node_creation == 'y':
        node_number += 1
        node_weight = random.randint(0, 999)
        nodes.update({node_number: node_weight})
        print('Node ' + str(node_number) + ' created.')
        print('Node weight: ' + str(node_weight))
    elif node_creation == 'n':
        print('Node not created.')
    elif node_creation == 'q':
        print('Process terminated')
    

def main():
    create_node(nodes, node_number)
    print(nodes)
main()



