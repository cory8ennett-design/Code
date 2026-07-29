Step 1
In this workshop, you will implement the shortest path algorithm. You will write a Python function that computes the shortest path between the nodes in a graph, and also returns the path taken.
For example, given a graph where cities are connected by roads with different distances, the algorithm will find the shortest route from one city to another. If you want to travel from City A to City D, the algorithm might find that going A ⇨ B ⇨ C ⇨ D (total: 15km) is shorter than going directly A ⇨ D (20km).
To get started, define a variable named INF and assign it the value float('inf'), which represents positive infinity. Later, you'll use it to indicate an infinite distance between two nodes.

Step 2
You will need to create a 2D list to represent the adjacency matrix of the graph. This matrix will be used to represent the weights of the edges between nodes in the graph.
Create a variable named adj_matrix and assign it a 2D list representing the graph with the following weights:

[0, 5, 3, INF, 11, INF],
[5, 0, 1, INF, INF, 2],
[3, 1, 0, 1, 5, INF],
[INF, INF, 1, 0, 9, 3],
[11, INF, 5, 9, 0, INF],
[INF, 2, INF, 3, INF, 0]

Step 3
You will now create the main function that accepts three parameters: the adjacency matrix, the starting node, and an optional target node.
Create a function named shortest_path that takes in three parameters: matrix, start_node, and target_node. Assign None as the default value for target_node.
The target_node parameter is set to None by default, indicating that if no target node is specified, the function should compute the shortest paths from the starting node to all other nodes in the graph.
Add a pass statement inside the function body for now.

Step 4
You need to store the number of nodes in the graph. For this you will need a variable that matches the length of the adjacency matrix.
Inside the shortest_path function, create a variable n and set it to the length of the matrix.

Step 5
You need to keep track of the shortest known distance from the start node to every other node in the graph.
To do this, create a variable named distances and initialize it as a list containing a single element: INF.

Step 6
Right now, the distances list only has one element. However, you need one distance value for each node in the graph.
In Python, you can multiply a list by an integer to repeat it. For example, [0] * 3 creates [0, 0, 0].
Update the distances list to contain n copies of INF by multiplying [INF] by n.

Step 7
Now that you have your distances list initialized, you need to update the distance for the starting node.
Since the distance from the starting node to itself is always 0, set the value at the start_node index in the distances list to 0.

Step 8
In addition to tracking distances, you also need to keep track of the actual paths taken to reach each node.
You'll create a list where each entry stores the path taken to reach that node. Initially, each node's path will just contain itself.
List comprehensions provide a concise way to create lists. For example:
[x * 2 for x in range(3)]
Create a variable named paths and initialize it using a list comprehension that creates a list containing [node_no] for each node_no in range(n).

Step 9
As the algorithm runs, you need to keep track of which nodes you've already visited, so you don't process them more than once.
To do this, create a list named visited and initialize it with False for every node.

Step 10
In this step, you will add a loop that will run once for each node in the graph. This loop will allow the algorithm to update distances and paths over multiple passes.
Create a for loop that runs n times. Use _ as the loop variable since you don't need to use the iteration value.
Inside the loop, you need to prepare for selecting the next node to process by creating two variables:
one to hold the smallest distance found so far in the current iteration
and another to store the index of the node that has this smallest distance.
Create variables min_distance and current, and set them to INF and -1, respectively.

Step 11
Now you need to check every node to find the one with the smallest known distance that has not been visited yet.
To do this, add a for loop inside the main loop.
The loop should iterate through each node_no in range(n), where n is the number of nodes in the graph. Add pass as the body of the loop for now.

Step 12
You need to decide whether the current node is a better choice than the one you've already found (if any). To do this, you'll add a conditional statement inside the loop.
The condition should do two things:
Check if the node has not been visited yet.
Compare the known distance to the current min_distance.
Inside the inner for loop, add an if statement that checks whether node_no has not been visited and whether distances[node_no] is less than min_distance.
Add pass as a placeholder inside the conditional block.

Step 13
If the conditional you just added is true, that means the current node is the best unvisited option you've found so far and you need to update your variables to reflect that.
Inside the if block, update min_distance to distances[node_no] and set current to node_no.

Step 14
After the loop that finds the nearest unvisited node, you need to check whether a valid node was actually found.
If no such node exists, that means the remaining nodes are unreachable from the start node, and the algorithm should stop early.
On the same level as the nested for loop, add an if statement that checks if current == -1 and breaks out of the loop if true.

Step 15
If a valid node was found in the pass, you need to mark it as visited so it won't be considered again in future iterations.
After the if statement you added in the previous step, set visited[current] to True.

Step 16
Now that you've selected and marked a node as visited, it's time to look at all of its neighbors to see if you can find shorter paths to them.
After the line visited[current] = True, add a for loop that iterates through node_no in range(n).
Inside this loop, create a variable distance and set it to matrix[current][node_no]. This will give you the distance from the current node to the neighbor node.

Step 17
Before trying to update the distance to a neighbor, you need to verify that the neighbor is both reachable and unvisited. Then you'll calculate what the total distance would be to reach that neighbor through the current node.
Inside the for loop, add an if statement that checks:
The distance is not equal to INF (meaning there's an edge between the nodes)
The neighbor node_no has not been visited yet
Inside the if block, create a variable named new_distance and assign it the sum of distances[current] (the shortest distance to the current node) and distance (the distance from the current node to the neighbor).

Step 18
Now that you've calculated the new possible distance to the neighbor, check if it's better than the one currently stored in the distances list. If it is, update the distance.
Inside the existing if block, add an if statement that checks if new_distance is less than distances[node_no].
Inside this new conditional block, update distances[node_no] to store the new_distance.

Step 19
When you find a shorter path to a node, you also need to update the actual path taken to reach it.
Inside the same conditional block, update the paths list at the neighbor's index to reflect the new, shorter path.
You should update paths[node_no] to be the current path to the current node, with the node_no (the neighbor) added at the end.

Step 20
Once the algorithm has finished running, you need to decide which node(s) to display results for.
If a specific target_node was provided, you'll only show the distance and path to that node. Otherwise, you'll show results for all nodes.
After the outer for _ in range(n): loop ends, create a variable named targets. Use a conditional expression to assign it [target_node] if target_node is not None, otherwise assign it range(n).

Step 21
Now that you've defined which nodes you want to display results for, you need to loop through them.
Add a for loop that iterates through each node_no in the targets list. Add pass as a placeholder inside the loop body.

Step 22
At this point, you only want to display results for nodes that are not the start node and are reachable from it.
Add a conditional that checks if node_no equals start_node or if distances[node_no] equals INF.
If either condition is true, use continue to skip to the next iteration of the loop.

Step 23
Now that you've determined a node should be displayed, you need to format its path so it can be printed clearly. For this you will use a generator expression.
A generator expression is similar to a list comprehension, but instead of creating a list, it generates each value one at a time. It uses parentheses () instead of square brackets []. For example:
numbers = [1, 2, 3]
squared = (x**2 for x in numbers)  # Generator expression
Inside the loop after the if statement, create a variable called string_path. Assign it a generator expression that converts each node number in paths[node_no] to a string using str().
The generator expression should iterate over each node number n in paths[node_no].

Step 24
Now you'll use the join() method to combine the string representations of the node numbers into a single readable path.
The join() method takes an iterable (like your generator expression) and combines all elements into one string, placing the separator between each element. For example:
numbers = ['1', '2', '3']
route = ' -> '.join(numbers) # route will be '1 -> 2 -> 3'
Create a variable called path and assign it the result of joining string_path using ' -> ' as the separator.

Step 25
Finally, print the results for the current node.
Your output should show two things, the distance from the start_node to node_no and the path taken to get there.
Use an f-string to format the output to show both the distance and the full path using the format:
\n[starting node]-[node number] distance: [distance]\nPath: [path]
Where:

[starting node] is the start_node
[node number] is the node_no
[distance] is the distance from the start_node to node_no
[path] is the path taken to get to node_no

Step 26
At the end of your function, return the data you've computed so it can be used outside the function.
Return both the list of shortest distances from the start_node to all other nodes and the list of paths that lead to each node

Step 27
Now you will demonstrate that your function works. At the end of your program, call your function shortest_path with the adj_matrix and a start_node of 0 and a target_node of 5 as arguments.
With that, the shortest path algorithm is complete!