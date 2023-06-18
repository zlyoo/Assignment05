import matplotlib.pyplot as plt


def mergeSort(arr):
    if (len(arr) )> 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        l = r = i =0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr[i] = left[l]
                i += 1
            else:
                arr[i] = right[r]
                j += 1
            i += 1

        while i < len(left):
            arr[i] = left[i]
            l += 1
            i += 1

        while r < len(right):
            arr[i] = right[r];
            r += 1
            i += 1



def my_plot(list):
    x = range(len(list))
    new_list = mergeSort(list)
    fig, axes = plt.subplots(1, 2)
    axes[0].plot(x,list)
    axes[0].set_title("unsorted list")

    axes[1].plot(x,new_list)
    axes[1].set_title("sorted list")

    plt.show()



my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
plot(my_list)
