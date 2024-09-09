# this script is about bubble sorting in python

# function of the bubble sorting algor
def bubble_sort(arr):
#initializing the arguments needed for the bubble sort to run 
    length_arr = len(arr)

    for i in range(length_arr):
        swapped = False
        for j in range(0, length_arr -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    arr = [64, 34, 3, 25, 12, 22, 2, 11, 90, 1, 6 ]
    print(bubble_sort(arr))

