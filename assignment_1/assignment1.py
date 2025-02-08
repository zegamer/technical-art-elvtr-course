"""
Calculate the vector length of a vector from a given list of vectors.

Each vector is of the form (x, y, z)
"""


def calculate_vector_length(vector_components: tuple) -> float:
    """
    Calculate the length of a given vector.

    Args:
        vector (tuple): The vector to calculate the length of

    Returns:
        float: The length of the vector
    """
    return sum(i ** 2 for i in vector_components) ** 0.5


if __name__ == "__main__":

    vectors = [
        (3, 5.23, 2.1532),
        (3.28, 5.19, 9.11)
    ]

    for vector in vectors:
        vector_length = calculate_vector_length(vector)
        print(f"The length of vector {vector} is {vector_length}")
