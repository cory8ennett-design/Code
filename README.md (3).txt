Step 1
In this workshop, you'll implement a function that generates all valid combinations of parentheses using a breadth-first search (BFS) approach. For example, the valid combinations of two pairs of parentheses are (()) and ()().
Start by creating a function named gen_parentheses with a single parameter pairs. For now, return an empty list from the function.

Step 2
Before implementing the core algorithm, you need to validate the input. The pairs parameter should be an integer, as it represents the number of parentheses pairs to generate.
Add an if statement at the beginning of your function to check if pairs is not an integer. Use the isinstance() function for that.
If the condition is true, return the string The number of pairs should be an integer.

Step 3
Next, you need to validate that the number of pairs is at least one, since you can't generate parentheses combinations with zero or negative pairs.
Add another if statement to check if pairs is less than 1. If this condition is true, return the string The number of pairs should be at least 1.

Step 4
Now you'll set up the data structure to store your results. Create a variable named result and initialize it as an empty list. This list will store all the valid parentheses combinations you generate.
Update your return statement to return result instead of an empty list.

Step 5
For the breadth-first search approach, you'll use a queue to track different states as you build the parentheses combinations. Each state will be represented as a tuple containing three elements:
The current string being built
The number of opening parentheses used so far
The number of closing parentheses used so far
Create a variable named queue and initialize it with a list containing one tuple: ('', 0, 0). This represents the starting state with an empty string and zero parentheses used.

Step 6
Now you'll implement the main BFS loop. Create a while loop that continues as long as the queue is not empty (while queue evaluates to True).
Inside the loop, print queue.

Step 7
Inside your while loop, use queue.pop(0) to remove and get the first element from the queue. This implements the first-in-first-out (FIFO) behavior characteristic of BFS.
Unpack this tuple into three variables: current, opens_used, and closes_used.

Step 8
Before you keep working on the BFS logic, call gen_parentheses(1) and print the result to the console.

Step 9
Now you need to identify when you've built a complete parentheses combination. A complete combination has a length equal to twice the number of pairs (since each pair contributes one opening and one closing parenthesis).
Inside your while loop, add an if statement to check if len(current) == 2 * pairs. When this condition is true, append current to the result list.

Step 10
If the current string isn't complete yet, you need to explore the next possible states. Add an else clause to your if statement.
Inside the else block, you'll handle adding opening parentheses. Add an if statement to check if opens_used < pairs. This ensures you don't use more opening parentheses than allowed.
If this condition is true, append a new tuple to the queue: (current + '(', opens_used + 1, closes_used). This represents the state after adding an opening parenthesis.

Step 11
Now you need to handle adding closing parentheses. The key rule is that you can only add a closing parenthesis if it maintains balance, meaning there must be more opening parentheses used than closing parentheses.
Still within the else block, add second if statement to check if closes_used < opens_used.
If this condition is true, append another new tuple to the queue: (current + ')', opens_used, closes_used + 1). This represents the state after adding a closing parenthesis.

Step 12
Your function is now complete. Test it again by printing gen_parentheses(2) instead of gen_parentheses(1).

Step 13
Now you don't need to print the queue anymore. So remove print(queue) from your while loop.

Step 14
Finally, call gen_parentheses with 3 as its argument to generate all five valid combinations of three pairs of parentheses and print the result to the console. With that the workshop is complete.