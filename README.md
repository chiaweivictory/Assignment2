# Assignment2
solve Sudoku(propositional logic)
## Ideas for solving this problem
1.The numbers 1-9 can appear only once in each row.<br>
2.The numbers 1-9 can only appear once in each column.<br>
3.The numbers 1-9 can only occur once in each 3x3 chamber separated by a thick solid line.<br>
## prompt
1.Count1 and count2 are stores that count keys<br>
2.grid [i][j] is a digit or '0 '.<br>
3.The problem data ensures that the input sudoku has only one solution<br>
4.We need to install z3 before we code: pip install z3-solver
5.Add the ability to judge whether txt can be opened
## Sudoku with demand solutions
5,3,0,0,7,0,0,0,0<br>
6,0,0,1,9,5,0,0,0<br>
0,9,8,0,0,0,0,6,0<br>
8,0,0,0,6,0,0,0,3<br>
4,0,0,8,0,3,0,0,1<br>
7,0,0,0,2,0,0,0,6<br>
0,6,0,0,0,0,2,8,0<br>
0,0,0,4,1,9,0,0,5<br>
0,0,0,0,8,0,0,7,9<br>
## The results of
### 1. Verify that Sudoku is valid and solve it
grid=<br>
5,3,0,0,7,0,0,0,0<br>
6,0,0,1,9,5,0,0,0<br>
0,9,8,0,0,0,0,6,0<br>
8,0,0,0,6,0,0,0,3<br>
4,0,0,8,0,3,0,0,1<br>
7,0,0,0,2,0,0,0,6<br>
0,6,0,0,0,0,2,8,0<br>
0,0,0,4,1,9,0,0,5<br>
0,0,0,0,8,0,0,7,9<br>
output:<br>
can open the txt<br>
The answer is:<br>
5,3,4,6,7,8,9,1,2<br>
6,7,2,1,9,5,3,4,8<br>
1,9,8,3,4,2,5,6,7<br>
8,5,9,7,6,1,4,2,3<br>
4,2,6,8,5,3,7,9,1<br>
7,1,3,9,2,4,8,5,6<br>
9,6,1,5,3,7,2,8,4<br>
2,8,7,4,1,9,6,3,5<br>
3,4,5,2,8,6,1,7,9<br>
### 2. Verify that Sudoku is valid but cannot be solved
grid=<br>
1,3,0,0,7,0,0,0,0(I replace the 5 in row 1, column 1 with a 1)<br>
6,0,0,1,9,5,0,0,0<br>
0,9,8,0,0,0,0,6,0<br>
8,0,0,0,6,0,0,0,3<br>
4,0,0,8,0,3,0,0,1<br>
7,0,0,0,2,0,0,0,6<br>
0,6,0,0,0,0,2,8,0<br>
0,0,0,4,1,9,0,0,5<br>
0,0,0,0,8,0,0,7,9<br>
output:<br>
can open the txt<br>
The sudoku has no solution<br>
unsat<br>
### 3. Verify that Sudoku is invalid
Case 1:<br>
grid=<br>
6,3,0,0,7,0,0,0,0(Replace the 5 in row 1, column 1 with 6)<br>
6,0,0,1,9,5,0,0,0<br>
0,9,8,0,0,0,0,6,0<br>
8,0,0,0,6,0,0,0,3<br>
4,0,0,8,0,3,0,0,1<br>
7,0,0,0,2,0,0,0,6<br>
0,6,0,0,0,0,2,8,0<br>
0,0,0,4,1,9,0,0,5<br>
0,0,0,0,8,0,0,7,9<br>
output:<br>
can open the txt<br>
Duplicate numbers appear in row  2 and column  1<br>
The result is:<br>
unsat<br>
Case 2:<br>
grid=<br>
5,3,0,0,7,0,0,0,0<br>
6,0,0,1,9,5,0,0,0<br>
0,9,8,0,0,0,0,6,0<br>
8,0,0,0,6,0,0,0,3<br>
4,0,0,8,0,3,0,0,1<br>
7,0,0,0,2,0,0,8,6（Replace the 0 in row 6, column 8 with 8）<br>
0,6,0,0,0,0,2,8,0<br>
0,0,0,4,1,9,0,0,5<br>
0,0,0,0,8,0,0,7,9<br>
output:<br>
can open the txt<br>
Duplicate numbers appear in row  7 and column  8<br>
The result is:<br>
unsat<br>
## Bad place
Need to change the path to open txt in the code<br>
sorry about this
