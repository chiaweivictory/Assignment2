import collections
import os
from collections import defaultdict
from z3 import *
from itertools import combinations
s=Solver()
# creat an integer Variable for the Sudoku grid
lits=[]
for i in range(9):
    lits += [[]]
    for j in range(9):
        lits[i]+=[[]]
        for digit in range(9):
            lits[i][j] += [Bool("x_%i_%i_%i" % (i,j,digit))] 

def only_one(literals):
    clauses=[literals]
    # no more than one literal is true
    for pair in combinations(literals,2):
        clauses +=[[Not(pair[0]),Not(pair[1])]]
    return clauses

#find the duplicate numbers in sudoku
def find_wrong(grid):
    count1 = collections.defaultdict(int)
    count2 = collections.defaultdict(int)
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                count1[grid[i][j]] = count1[grid[i][j]] + 1
                if count1[grid[i][j]]>1:
                    print('Duplicate numbers appear in row ',i+1,'and column ',j+1)
            if grid[j][i] != 0:
                count2[grid[j][i]] = count2[grid[j][i]] + 1
                if count2[grid[j][i]]>1:
                    print('Duplicate numbers appear in row ',j+1,'and column ',i+1)
        for z in count1.values():
            if z > 1:
                return True
        for z in count2.values():
            if z > 1:
                return True
        count1.clear()
        count2.clear()

#print the solution
def print_solution(model,lits):
    lines=[]
    for i in range(9):
        lines += [[]]
        for j in range(9):
            digit=0
            for x in range(9):
                if model.evaluate(lits[i][j][x]):
                    digit = x+1
            lines[i].append(digit)

    for line in lines:
        print(",".join([str(x) for x in line]))
                
#solve_sudoku
def solve_sudoku(grid):
    clauses=[]
    #only has one value
    for i in range(9):
        for j in range(9):
            clauses += only_one(lits[i][j])

    #only has one value in a row     
    for j in range(9):
        for x in range(9):
            clauses += only_one([lits[i][j][x] for i in range(9)])

    #only has one value in a column
    for i in range(9):
        for x in range(9):
            clauses += only_one([lits[i][j][x] for j in range(9)])


    # digit has to be placed once in each 3*3 subgrid
    for i in range(3):
        for j in range(3):
            for k in range(9):
                grid_cells=[]
                for x in range(3):
                    for y in range(3):
                        grid_cells += [lits[3*i+x][3*j+y][k]]
                clauses += only_one(grid_cells) 

    #enter a known number
    for i in range(9):
        for j in range(9):
            if grid[i][j]>0:
                clauses += [[lits[i][j][grid[i][j]-1]]]   

    #encode the constraints
    for clause in clauses:
        s.add(Or(clause))


    if str(s.check())=='sat':
        print('The answer is')
        print_solution(s.model(),lits)
    else:
        if find_wrong(grid):
            print('The wrong location is:')
        else:
            print('The sudoku has no solution')

        print('unsat')
        


if __name__ =='__main__':
    grid=[]
    #check if the path is valid 
    state=os.path.exists("C:/Users/10500/Desktop/assignment2/sudoku.txt")
    if state:
        print('can open the txt')
    else:
        print('we can not find the path')
    
    input_f=open("C:/Users/10500/Desktop/assignment2/sudoku.txt","r",encoding='utf-8')
    for line in input_f.readlines():
        curLine=line.strip().split(",")
        curLine=list(map(int,curLine))
        grid.append(curLine)

    solve_sudoku(grid)
    exit(0)