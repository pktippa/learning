# Data Structures Interview Questions

Q. How can we implement a Queue with enqueue and dequeue operations using two stacks which has push and pop operations.

A: Name two stacks as stack1 and stack2, 

When a enqueue request came.
   
   push the value to stack1

When a dequeue request came

   check if stack2 is empty or not.

   If empty

        pop all the elements from stack1 and push to stack2 then pop a element.

   Else

       pop an element from stack2


Q: How to get to a particular nth element from end(last) in Single Linked List.
A: 

Method 1
(Use length of linked list)
1) Calculate the length of Linked List. Let the length be len.
2) Print the (len – n + 1)th node from the begining of the Linked List.

Method 2
Maintain two pointers – reference pointer and main pointer. Initialize both reference and main pointers to head. First move reference pointer to n nodes from head. Now move both pointers one by one until reference pointer reaches end. Now main pointer will point to nth node from the end. Return main pointer.

1,2,3,4,5,6

3 element from last -> 4 value

Take 4 steps for refernce

1,2,3,4

r: 4
m: 1

Go till end

r: 5
m: 2
--
r: 6
m: 3
--
r: null
m: 4

for n=2 see it in text editor

-------
--R
M

-------
------R
----M