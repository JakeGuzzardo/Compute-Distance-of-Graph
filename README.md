Compute Distance given a node in a graph

Input structure:
The first line in the input file represents the starting node in a graph. The next line represents the first node in the graph starting at 0. All values in this line represent
this nodes connecting neighbors

example:
2 #start from node 2
1 2 3 #node 0: neighbor nodes 1 2 and 3
0 2 3 #node 1: neighbor nodes 0 2 and 3
0 1 3
0 1 2

to run use the command `python driver.py testcases/input.txt` input.txt must be one of the files under testcases

will return the distance/levels of all nodes starting from the start/root node, where each conection is a distance of 1.
Example:
if it takes 3 connecting nodes to get to the root node the distance output will be 3
