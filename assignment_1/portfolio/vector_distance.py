
def n_dimension_euclidean_distance(coordinate_1: tuple, coordinate_2: tuple) -> float:
    """
    Calculate the Euclidean distance between two coordinates of n dimensions.

    Args:
        coordinate_1 (tuple): The first coordinate.
        coordinate_2 (tuple): The second coordinate.

    Returns:
        float: The Euclidean distance between the two coordinates.
    """
    if len(coordinate_1) == len(coordinate_2):
        sum_val = 0
        for i in range(len(coordinate_1)):
            sum_val += element(coordinate_1[i], coordinate_2[i])
        return sum_val ** 0.5
    return 0


def two_dimension_euclidean_distance(coordinate_1: tuple, coordinate_2: tuple) -> float:
    """
    Calculate the Euclidean distance between two coordinates of 2 dimensions.

    Args:
        coordinate_1 (tuple): The first coordinate.
        coordinate_2 (tuple): The second coordinate.

    Returns:
        float: The Euclidean distance between the two coordinates.
    """
    return ((coordinate_2[0] - coordinate_1[0]) ** 2 + (coordinate_2[1] - coordinate_1[1]) ** 2) ** 0.5


def calculate_unit_vector(vector: tuple) -> float:
    """
    Calculate the unit vector between 2 given vectors.

    Args:
        vector (tuple): The vector to calculate the length of

    Returns:
        float: The length of the vector
    """
    return sum(i ** 2 for i in vector) ** 0.5

def element(a, b):
    return (b - a) ** 2

if __name__ == '__main__':
    print(two_dimension_euclidean_distance((0,1), (5,2)))
    print(two_dimension_euclidean_distance((0,0), (3,4)))
    print(n_dimension_euclidean_distance((1,2,3), (4,5,6)))
    print(n_dimension_euclidean_distance((1,2,3), (4,5,6,7)))
