# largest-difference

<h1>Overview</h1>

The largest_difference() function calculates the difference between the largest and smallest numbers in a list.<br>
It does this by sorting the list, finding the smallest and largest values, and then returning the numerical difference between them.

<h2>How it works</h2>
How It Works
<ul>
<li>The input list (param) is sorted in ascending order using .sort().</li>
<li>The length of the list is stored in size.</li>
<li>The smallest number is accessed with param[0].</li>
<li>The largest number is accessed with param[size - 1].</li>
<li>Their difference (largest - smallest) is stored in value and returned.</li>
</ul>


<h3>Example</h3>
numbers = [3, 8, 1, 10, 5]

result = largest_difference(numbers)

print(result)

<h3>Output</h3>
9
