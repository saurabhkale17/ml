def get_mean(lst):
    """
    Calculate the mean of a list of numbers.
    """
    return sum(lst) / len(lst)


def get_standard_deviation(lst, mean):
    """
    Calculate the standard deviation of a list of numbers.
    """
    if len(lst) <= 1:
        return 0

    summ = 0
    for x in lst:
        summ += (x - mean) ** 2

    std_dev = (summ / len(lst)) ** 0.5
    return std_dev


def col_standardization_prep(lst):
    """
    Perform column standardization (z-score normalization) on a list of numbers.
    """
    mu = get_mean(lst)
    std_dev = get_standard_deviation(lst, mu)

    new_lst = []
    for data in lst:
        new_lst.append((data - mu) / std_dev)

    return new_lst


def col_standardization(dataset):
    """
    Perform column standardization (z-score normalization) on a dataset.
    """
    no_of_features = len(dataset[0])
    no_of_data_points = len(dataset)
    col_std_dataset = [[0 for _ in range(no_of_features)] for _ in range(no_of_data_points)]

    for feature in range(no_of_features):
        std_feature = []
        for data_point in range(no_of_data_points):
            std_feature.append(dataset[data_point][feature])
        final_std_feature = col_standardization_prep(std_feature)

        for data_point in range(no_of_data_points):
            col_std_dataset[data_point][feature] = final_std_feature[data_point]

    return col_std_dataset


def get_covariance_value(feature1, feature2):
    """
    Calculate the covariance between two lists of numbers.
    """
    final_value = 0
    for f1, f2 in zip(feature1, feature2):
        final_value += (f1 * f2)
    return final_value / (len(feature1) - 1)


def get_covariance_matrix(dataset):
    """
    Calculate the covariance matrix for a dataset.
    Prints the covariance matrix for the dataset.
    """
    no_of_features = len(dataset[0])
    covariance_matrix = [[0 for _ in range(no_of_features)] for _ in range(no_of_features)]

    for i in range(no_of_features):
        for j in range(i, no_of_features):
            feature1 = []
            feature2 = []
            for data in dataset:
                feature1.append(data[i])
                feature2.append(data[j])
            covariance_matrix[i][j] = get_covariance_value(feature1, feature2)
            covariance_matrix[j][i] = covariance_matrix[i][j]

    print("Covariance matrix:")
    for row in covariance_matrix:
        print(row)
