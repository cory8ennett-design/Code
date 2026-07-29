Implement the Merge sort Method
Technologies
Uses Python3.
Deployment
Copy main.py into the text editor of your choice. If using terminal, use the command python3 main.py to run the code.
Credits
Acknowledgements
FreeCodeCamp
-------------------------------------------------------------------------------------------------------------



Step 1
Merge sort is a sorting algorithm that uses the divide-and-conquer principle to sort collections of data. That is, it "divides" a collection into smaller sub-parts, and "conquers" the sub-parts by sorting them independently, then merges the sorted sub-parts.
Begin by creating a function called merge\_sort that takes the parameter array. This function will handle the task of sorting a list of numbers. Use the pass keyword in the function body.

Step 2
The merge sort algorithm performs three actions:
Divide an unsorted sequence of items into sub-parts
Sort the items in the sub-parts
Merge the sorted sub-parts
The above happens recursively until the sub-parts are merged into the complete sorted sequence. Start by dividing the sequence.
First, replace the pass keyword with a variable middle\_point. Use the integer division operator (//) to divide the length of the array list by 2 and assign the result to your new middle\_point variable. Remember to indent your code.

Step 3
In the previous step, you got the mid point. You can use it to divide array into two and assign each part to new variables.
Use the slice syntax to extract the left half of array and assign it to a variable named left\_part.

Step 4
Use the slice syntax to extract the right half of array and assign it to a variable named right\_part.

Step 5
Now that you've divided the array list into two separate lists, you'll keep dividing each list until every element stands alone in its own list. A list with a single number is always sorted.
To do that, recursively call merge\_sort inside your function and pass left\_part as the argument to the call.

Step 6
At the bottom of your function body, call the merge\_sort() function again. This time, pass in right\_part as the argument to the function call.

Step 7
Now it's time to sort and merge the lists (left\_part and right\_part) into the original list.
You can do this by comparing elements on both lists, and merging the smaller element to the main list. You are going to do this comparison for all the indexes in left\_part and right\_part.
Create three variables: left\_array\_index, right\_array\_index, and sorted\_index and set their values to 0. These variables will help you keep track of each index during the sorting process.

Step 8
Next, you need to create a loop that continues as long as there are elements remaining in both left\_part and right\_part.
For that, create a while loop with two conditions: one that checks whether the left\_array\_index is less than the length of left\_part and another condition that checks whether right\_array\_index is less than the length of right\_part.

Step 9
Within the while loop, replace pass with an if statement that checks if the element in the left\_part is less than the element in the right\_part.
Use the pass keyword in the body of the if statement.

Step 10
When the if condition evaluates to True, it means that the element in the left\_part list is smaller than the element it is being compared to in the right\_part list.
In that case, you can put the element found at left\_array\_index in left\_part within the sorted array.
Inside the if block, remove pass and assign left\_part\[left\_array\_index] to array\[sorted\_index].

Step 11
After assigning the element in left\_part to the sorted array, increment left\_array\_index by 1.

Step 12
In a previous step, you assigned the element in the left\_part to the array list because it was smaller. But this will not always be the case. In some comparison cases, the element on the right could be smaller.
Create an else clause to execute when the element in left\_part is not less than the element in right\_part.
Inside the else block, assign right\_part\[right\_array\_index] to array\[sorted\_index].

Step 13
Still within the else block, increment right\_array\_index by 1.

Step 14
The if and else statements you created in the previous steps will assign elements to the sorted array.
Each element assigned to the sorted array takes up an index in the list. So you have to move to the next index in the sorted array after each assignment.
Below the if/else block, but still within the while loop, increment sorted\_index by 1.

Step 15
The while loop you created compares one element from left\_part with another in right\_part, then adds the smaller element to the main array list.
It will continue this operation until there are no elements left to be compared. But left\_part may still have elements left while right\_part has none, and vice versa.
Create another while loop that runs when left\_array\_index is less than len(left\_part). In the next steps, you'll use it to copy the remaining elements in left\_part into the array list.

Step 16
Remove the pass keyword. For the while loop's code block, assign left\_part\[left\_array\_index] to array\[sorted\_index].

Step 17
Still within the while loop, increment the value of left\_array\_index by 1.

Step 18
The last thing to do for the while loop is to move to the next index in the sorted array.
Add 1 to the value of sorted\_index.

Step 19
Now, you are going to replicate the same while loop logic for right\_part.
Create a while loop that runs when right\_array\_index is less than len(right\_part). Within the while loop, assign right\_part\[right\_array\_index] to array\[sorted\_index]. At the end, increment right\_array\_index and sorted\_index by 1.

Step 20
Before testing the merge\_sort() function, you need to create a base case that stops the function execution when the length of array is less than or equal to 1.
This base case will stop the recursion call. Without it, the merge sort operation would continue to run even when the list has been sorted or has no elements in it.
Right after the function declaration, create an if statement with this condition: len(array) <= 1. Within the body of the if statement add a return statement to stop the execution of the function.

Step 21
As you learned in a previous lesson, you can use the **name** variable to determine if a Python script is being run as the main program or if it is being imported as a module (code written in another Python file).
If the value of **name** is set to '**main**', it implies that the current script is the main program, and not a module.
In this project, you'll use the current script as the main program.
Create an if statement that checks whether the value of **name** is '**main**'. Within the if statement, create a list called numbers, and assign these values to it: \[4, 10, 6, 14, 2, 1, 8, 5].

Step 22
Use the print() function to print the string 'Unsorted array: '.

Step 23
Call the print() function again to print the numbers list. This will print the unsorted list in the console.

Step 24
After your print() calls, call the merge\_sort function and pass in the numbers list as an argument.

Step 25
At this point, the numbers list has been sorted. Call the print function to print string 'Sorted array: ' followed by another print call to print the numbers list.
With that, the merge sort algorithm is complete.

