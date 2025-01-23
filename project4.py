import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Sorting Algorithms
def bubble_sort(data, update_func):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                update_func(data, j, j + 1)
    return data

def selection_sort(data, update_func):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        update_func(data, i, min_idx)
    return data

def insertion_sort(data, update_func):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        update_func(data, i, j)
    return data

# Visualization
def visualize_sorting(sort_func, data):
    fig, ax = plt.subplots()
    ax.set_title(f"{sort_func.__name__.replace('_', ' ').capitalize()} Visualization")

    bar_rects = ax.bar(range(len(data)), data, align="edge", color="skyblue")
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, int(max(data) * 1.1))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_fig(data, bar_idx1=None, bar_idx2=None):
        for rect, val in zip(bar_rects, data):
            rect.set_height(val)
        if bar_idx1 is not None and bar_idx2 is not None:
            bar_rects[bar_idx1].set_color("red")
            bar_rects[bar_idx2].set_color("green")
        else:
            for rect in bar_rects:
                rect.set_color("skyblue")
        text.set_text(f"Step: {update_fig.step_count}")
        update_fig.step_count += 1

    update_fig.step_count = 0

    ani = animation.FuncAnimation(
        fig,
        lambda _: sort_func(data, update_fig),
        repeat=False,
        interval=50,
        blit=False
    )
    plt.show()

# Main Function
def main():
    num_elements = 20  # Number of elements to sort
    data = [random.randint(1, 100) for _ in range(num_elements)]
    print("Unsorted Data:", data)

    # Visualize Sorting
    print("\nChoose Sorting Algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        visualize_sorting(bubble_sort, data)
    elif choice == "2":
        visualize_sorting(selection_sort, data)
    elif choice == "3":
        visualize_sorting(insertion_sort, data)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
