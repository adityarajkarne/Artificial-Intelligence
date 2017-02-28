# Please Note: This is python 3 code, while the other question has been coded in python 2

# (1) Made a list of lists to represent the states
# The successor function calls the 4 operations left,right,up,down corresponding to the 4 legal moves
# The heuristic function is no of misplaced tiles/4, it is admissible cause it never overestimates.
# 1 move will at max disturb 4 tiles.So any move will not result in more than that.
#
# (2) a brief description of how your search algorithm works: while the queue is not empty,
# element popped and successor is called upon it and the successors are compared to goal state,
# if not heuristic found out for states not already visited.the heuristic value and state are then put in queue.

# (3) discussion of any problems , assumptions, simplifications, and/or design decisions you made:Nothing unusual



import sys
import copy
from queue import PriorityQueue


def down(state,col_num):#performs down operation on a list of lists
    d_state = copy.deepcopy(state[1][0])
    z = d_state[len(d_state)-1][col_num]
    for j in range(len(d_state)-1,0,-1):
        d_state[j][col_num] = d_state[j-1][col_num]
    d_state[0][col_num] = z
    a = state[0] + 1
    c = state[1][1] + "D" + str(col_num + 1) + ' '
    return a, (d_state, c)


def up(state,col_num):#performs up operation on a list of lists
    u_state = copy.deepcopy(state[1][0])
    z = u_state[0][col_num]
    for j in range(len(u_state)-1):
        u_state[j][col_num]=u_state[j+1][col_num]
    u_state[len(u_state)-1][col_num]=z
    a = state[0] + 1
    c = state[1][1] + "U" + str(col_num + 1) + ' '
    return a, (u_state, c)



def left(state,row_num):#performs left operation on a list of lists
    l_state = state[1][0][:]
    new_state=[]
    for j in range(len(l_state[row_num])-1):
        new_state.append(l_state[row_num][j+1])
    new_state.insert(len(l_state[row_num])-1,l_state[row_num][0])
    l_state[row_num] = new_state
    a = state[0]+1
    c = state[1][1] + "L" + str(row_num + 1) + ' '
    return a,(l_state, c)


def right(state,row_num):#performs right operation on a list of lists
    r_state=state[1][0][:]
    new_state = []
    for j in range(1,len(r_state[row_num])):
        new_state.append(r_state[row_num][j-1])
    new_state.insert(0, r_state[row_num][-1])
    r_state[row_num]=new_state
    a=state[0]+1
    c=state[1][1]+"R"+str(row_num+1)+' '
    return a,(r_state,c)



def successors(node):#calls the 4 operations left,right,up,down returns 16 successors
    succ_list=[]

    for i in range(len(node[1][0])):
        succ_list.append(left(node, i))
        succ_list.append(right(node, i))
        succ_list.append(up(node, i))
        succ_list.append(down(node, i))


    return succ_list

def is_goal(state):#checks if goal
    if state[1][0]== [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]:
        return True
    else:
        return False


def heuristic(state):#misplaced tiles/4
    combine=state[1][0][0]+state[1][0][1]+state[1][0][2]+state[1][0][3]
    return state[0]+len([i for i in range(len(combine)) if combine[i]!=i+1 ])/4,(state[1][0],state[1][1])

def solve(given):#implementation
    closed=[]
    q= PriorityQueue()
    list_succ=[]
    if is_goal(given):
        print("GOAL!!!")
        print(given[1][1][:-1])
        return (given[1][1][:-1])

    else:
        q.put((given[0],(given[1][0],given[1][1])))#pass to queue


        while not q.empty():
            pop=q.get()
            closed.append(pop[1][0])
            revealed= successors(pop)
            for successor in revealed:
                if is_goal(successor):
                    print("GOAL!!!")
                    print(successor[1][1][:-1])
                    return (successor[1][1][:-1])

                else:
                    list_succ.append(successor)

            for item in [heuristic(succ) for succ in revealed if succ[1][0] not in closed]:#all successors not already visited

                calc=[i for i in range(len(q.queue)) if item[1][0] == q.queue[i][1][0]]#checks presence in fringe
                if len(calc)!=0:
                    if q.queue[calc[0]][0] > item[0]:
                        q.queue[calc[0]] = item
                else:
                    q.put(item)





#main
filename = str(sys.argv[1])
extract = (0,([[int(y) for y in x] for x in [line.strip().split(" ") for line in open(filename, 'r')]],''))
solve(extract)
