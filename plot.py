import matplotlib.pyplot as plt
import numpy as np


def grouped_bar_chart(groups: list[str], categories: list[str], data: np.ndarray):
    # Set up bar positions
    num_groups = len(groups)
    num_categories = len(categories)

    bar_width = 0.8 / num_categories  # Adjust bar width based on number of categories

    x = np.arange(num_groups)

    # Create bars
    for i in range(num_categories):
        plt.bar(x + (i - num_categories/2 + 0.5) * bar_width, data[i], bar_width, label=categories[i])

    # Customize chart
    plt.xlabel('Group')
    plt.ylabel('Values')
    plt.title('Grouped Bar Chart')
    plt.xticks(x, groups)
    plt.legend()
    plt.tight_layout()
    plt.show()


# # Define data
# groups = ['A', 'B', 'C']
# categories = ['X', 'Y', 'Z', 'W']  # Example with 4 categories
# data = np.array([[5, 8, 3], [4, 6, 9], [2, 5, 7], [1, 3, 5]])  # 4x3 array
# grouped_bar_chart(groups, categories, data)