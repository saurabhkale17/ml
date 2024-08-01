from math import sqrt
from csv import reader

filename = 'iris.csv'

# Load a CSV file
def load_csv(filename):
    dataset = list()  # Initialize an empty list to store the dataset
    with open(filename, 'r') as file:  # Open the CSV file
        csv_reader = reader(file)  # Create a CSV reader object
        for row in csv_reader:  # Iterate over each row in the CSV file
            if not row:
                continue  # Skip empty rows
            dataset.append(row)  # Append the row to the dataset list
    return dataset

dataset = load_csv(filename)

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column])  # Convert the column value to float

# Convert all columns except the last one to float
for i in range(len(dataset[0])-1):
    str_column_to_float(dataset, i)

# Normalization of dataset columns to a range between 0 and 1
# Formula: (x - xmin) / (xmax - xmin)

# Find the min and max for each column (except the last one)
maxmin = []
X = dataset
for i in range(len(X[0])-1):
    lst = []
    for j in range(len(X)):
        lst.append(X[j][i])  # Collect values from column i
    maxmin.append([max(lst), min(lst)])  # Store max and min of the column

X_ = dataset

# Apply normalization to each value in the dataset (except the last column)
for i in range(len(X)):
    for j in range(len(X[0])-1):
        X_[i][j] = (X[i][j] - maxmin[j][1]) / (maxmin[j][0] - maxmin[j][1])

# Calculate Euclidean distance between two rows
def cal_euclidian_distance(row1, row2):
    distance = 0
    for i in range(len(row1)-1):  # Ignore the last column (label)
        distance += (row1[i] - row2[i])**2  # Sum the squared differences
    return distance

# Find the nearest neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = []

    for train_row in range(len(train)):
        distance = cal_euclidian_distance(test_row, train[train_row])  # Calculate distance
        distances.append((train_row, distance))  # Store the index and distance
    distances.sort(key=lambda tup: tup[1])  # Sort by distance

    neighbors = []
    for i in range(num_neighbors):
        neighbors.append(dataset[distances[i][0]])  # Get the top neighbors

    return neighbors

# Make a prediction using the neighbors
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)  # Find neighbors
    output_values = [row[-1] for row in neighbors]  # Extract the output values (labels)
    prediction = max(set(output_values), key=output_values.count)  # Find the most common label
    return prediction

# Main function to run the KNN classification
def main():
    # Define model parameter
    num_neighbors = 5
    # Define a new record for prediction
    row = [5.7, 2.9, 4.2, 1.3]
    # Predict the label for the new record
    label = predict_classification(dataset, row, num_neighbors)
    print('Data=%s, Predicted: %s' % (row, label))
    print("Label:", label)

main()
