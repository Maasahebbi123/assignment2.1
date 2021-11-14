
#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

'''pseudocode for printing above pgm:
define a list of tuples,find length of the list,
"now by applying the concept of swapping"
 take the nested for loop for iteration,
finds 2nd value in current element,
finds 2nd value in next element
if 2nd value in current element is greater than the 2nd value
in next element swap it.'''

L = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
length = len(L)

for count in range(length):
    for count2 in range(length - 1):
        sec_val = L[count2][1] 
        sec_val_next = L[count2 + 1][1] 
        if sec_val > sec_val_next:
            temp = L[count2] 
            L[count2] = L[count2 + 1] 
            L[count2 + 1] = temp 

print(L)

