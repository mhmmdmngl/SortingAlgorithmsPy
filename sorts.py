from random import seed
from random import randint
import time
import sys

# best case O(1) implementetion has been added 
def bubble_Sort(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(len(arr) - 1 - i):
            if arr[j] >  arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag == False:
            break
    return arr

def selection_Sort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def insertion_Sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1

        while key < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

#merging step for merge sort
def merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_Array = arr[:mid]
        right_Array = arr[mid:]

        merge(left_Array)
        merge(right_Array)
        merge_Sort(arr, left_Array, right_Array)

#main algorithm for merge sort
def merge_Sort(arr, left_Array, right_Array):

    i = 0
    j = 0
    k = 0

    while i < len(left_Array) and j < len(right_Array):
        if left_Array[i] < right_Array[j]:
            arr[k] = left_Array[i]
            i = i + 1
        else:
            arr[k] = right_Array[j]
            j = j + 1
        k = k + 1

    while i < len(left_Array):
        arr[k] = left_Array[i]
        i = i + 1
        k = k + 1

    while j < len(right_Array):
        arr[k] = right_Array[j]
        j = j + 1
        k = k + 1


# this function for your test, you should need high numbered numbers
# this function create ordered numbers for your list
def ordered_Number_Generator(quantity):
    arr = []
    for i in range(quantity):
        arr.append(i)
    return arr

# this function for your test, you should need high numbered reversed numbers
# this function create reversed ordered numbers for your list
def reversed_Ordered_Number_Generator(quantity):
    arr = []
    for i in range(quantity):
        arr.append(quantity-i)
    return arr

# this function for your test, you should need high numbered random numbers
# this function create random  numbers for your list
def create_Random_Number(quantity):
    arr = []
    for i in range(quantity):
        arr.append(randint(0, quantity*9))
    return arr

# this function is part of quicksort. Actually it does real job!
def partition(arr, leftIndex, rightIndex):
    i = leftIndex - 1
    pivot = arr[rightIndex]

    for j in range(leftIndex, rightIndex):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[rightIndex] = arr[rightIndex], arr[i+1]
    return i+1

def quickSort(arr, leftIndex, rightIndex):
    if leftIndex < rightIndex:
        pivot = partition(arr, leftIndex, rightIndex)
        quickSort(arr, leftIndex, pivot-1)
        quickSort(arr, pivot+1, rightIndex)

#this function makes max_heapify for heap sort
def max_heapify(arr, size, rootIndex):
    leftChild = (rootIndex * 2) + 1
    rightChild = (rootIndex * 2) + 2

    current_Bigest = rootIndex

    if leftChild < size and arr[rootIndex] < arr[leftChild]:
        current_Bigest = leftChild
    if rightChild < size and arr[current_Bigest] < arr[rightChild]:
        current_Bigest = rightChild

    if current_Bigest != rootIndex:
        arr[rootIndex], arr[current_Bigest] = arr[current_Bigest], arr[rootIndex]
        max_heapify(arr, size, current_Bigest)

#main function of heap sort
def heap_sort(arr): 
    for i in range(len(arr), -1, -1):
        max_heapify(arr, len(arr), i)

    for i in range(len(arr) - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)



