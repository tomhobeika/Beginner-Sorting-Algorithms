# Beginner-Sorting-Algorithms
My first attempts at manually sorting lists algorithmically. The program takes in a txt file to then turn the file into a large list of words, and sort them by count. The list is then sorted alphabetically. A more detailed description of each algorithm used, along with the steps taken to achieve the solution can be found bellow.

Steps:
Read file, with a try/except to catch incorrect file names, and exit program if an invalid file name is entered.
Split words from file into individual strings. Make them lowercase and get rid of punctuation.
Check if the word has already been used and increment the count of that word if it is already in the list. If not, make a new object for the word and add to the list.
Sort the list by count using the Quick Sort algorithm.
Sort the list alphabetically using a single pass of Bubble Sort.

Algorithms Used:
Quick Sort was used to sort the list by count. Quick sort was used as it is efficient for sorting a list by amount, and has an average time complexity of O(n log (n)). This algorithm works similarly to merge sort as it uses a pivot point to compare and swap elements. This algorithm based on the information from the following website: https://www.geeksforgeeks.org/quick-sort/

Bubble Sort was used to sort the list alphabetically. In my program, the list is only sorted alphabetically after it has already been added and sorted by count. This means that only one pass is needed to sort. Additionally, in order to maintain the previous sort, this sort needed to run incrementally for each part of the list bit by bit. While bubble sort can be quite inefficient with a time complexity of O(n2), it was chosen to allow for the algorithm to be run both incrementally and as a single pass without disturbing the previous sort by count. 
