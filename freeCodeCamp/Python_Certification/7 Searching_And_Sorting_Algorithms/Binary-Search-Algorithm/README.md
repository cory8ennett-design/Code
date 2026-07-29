Binary Search Algorithm

Technologies
Uses Python3.

Deployment
Copy main.py into the text editor of your choice. If using terminal, use the command python3 main.py to run the code.

Credits
Acknowledgements
FreeCodeCamp
-------------------------------------------------------------------------------------------------------------

Step 1
In a previous lesson, you learned about binary search and how it differs from linear search.
In this workshop, you will put that into practice by building a binary search algorithm.
To begin, create a binary_search function with a search_list and value parameters.
search_list is the list of elements the function will search within, and value is the target the function will try to find within the search_list.
Add the pass keyword inside the function for now so the test can pass.

Step 2
The binary search algorithm you're building will not just return True or False to indicate whether the value was found or not. It will also return the path it takes to find that value. And for that, you will have a path_to_target variable to track the path.
Inside your binary_search function, replace the pass keyword with a path_to_target variable and initialize it to an empty list, for a start.

Step 3
In binary search, there is the lowest possible index and the highest possible index.
The lowest possible index represents the leftmost boundary in the current portion of the values being searched within, in this case, search_list. The highest possible index, on the other hand, represents the rightmost boundary in the values being searched.
To account for those two, you have to consider the entire list being searched. So, inside the binary_search function, define a low variable with a value of 0, and a high variable with a value that accounts for the last index in the list being searched.

Step 4
Now that you've defined the boundaries of your search, it's time to create the loop that will perform the binary search algorithm.
Binary search works by repeatedly narrowing down the search space. This process continues as long as there is a valid range of elements to check.
You can express this with a while loop that will continue as long as your low pointer is less than or equal to your high pointer.
If low ever becomes greater than high, it means the search space has become empty, and the value is not in the list.
Inside the binary_search function, create a while loop with a condition that checks if low is less than or equal to high. Inside the loop, add the pass keyword as a placeholder for now.

Step 5
To get started with the loop, you need to find the middle index of the current search space.
You can get the middle index by calculating the average of the low and high variables. You will have to use floor division to get the average after adding the two values, so the answer would always be an integer rounded down, as the indices must be integers.
Remove the pass keyword from your while loop and create a mid variable set to the average of low and high.

Step 6
Now that you've calculated the mid index, you need to actually retrieve the value from the search_list at that index. This value is what you will compare against your value parameter, which is the target you are searching for.
Create a value_at_middle variable and assign it the element from search_list that is located at the mid index.

Step 7
Now, include value_at_middle in the path_to_target list to track the steps taken during the search, regardless of whether it's the target.

Step 8
The next thing to do is to create a condition that will check if the target value is in the middle.
Inside the while loop, create an if statement that checks if the target value is equal to value_at_middle. If it is, return the path_to_target variable.

Step 9
You need to test out things so you will understand the flow of the algorithm at this initial stage.
To do that, you need to first break out of the loop. That's because the current implementation will only allow one iteration, so if the condition is not met, there will be an infinite loop.
Just after the ifstatement, use the break keyword to break out of the while loop. Then, after the while loop, return an empty list to signify that the value was not found.

Step 10
Be reminded that the function takes a list called search_list and the value you're looking for.
Now, call the function with binary_search([1, 2, 3, 4, 5], 3) and binary_search([1, 2, 3, 4, 5, 9], 4) and print the calls right away.

Step 11
You can see that the first call returns [3]. That's because 3 is the middle value in [1, 2, 3, 4, 5].
On the other hand, the second call returns an empty list. This happens because, after checking the middle value, the loop currently lacks the logic to narrow the search range by updating the low or high variables. It only acts as a single midpoint check and then finishes without further searching.
To allow the binary search to continue narrowing its search, add an elif block that checks if value is greater than value_at_middle. Add the pass keyword inside the elif for now.

Step 12
If the condition in the elif is true, then remove the pass keyword and update the value of the low variable by adding 1 to the mid variable.
This will extend the search to the right half of the current search areas in the list, because if the value is greater than value_at_middle, it means the value must be in the right half of the current search area.

Step 13
Finally, if the value is not found at the middle and is also not greater than value_at_middle, then the value must be less than value_at_middle, and must be on the left. The else block will handle this.
So, finish up the loop by removing the break keyword and adding an else block. Inside it, update the high variable by subtracting 1 from mid.

Step 14
Did you notice the second function call now has the values 3, 5, 4 in the list? That indicates the binary search is working as intended.
This is how it happened: The algorithm first checked 3 as the middle of the initial list. Since 4 is greater than 3, the search shifted to the right half. It then examined 5 as the new middle. Because 4 is less than 5, the search moved to the left, ultimately identifying 4 as the middle of the final range.
To test the function again, call it with [1, 3, 5, 9, 14, 22], 10 and print the call right away. This is a situation in which the value will not be found.

Step 15
You can see that the last call prints an empty list. To further specify that the value is not in the searched list, update the return statement and return an empty list and the message Value not found.

Step 16
One final small enhancement you can add is to also show the index at which the target value is found.
So, instead of returning only path_to_target in the if statement, add an f-string with the message Value found at index {mid}.
With that, your binary search algorithm workshop is complete!