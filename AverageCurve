import sys
# Method: return a list of ints corresponding to a list of strings
def convert_to_int(string_list):

    scores = []

    for string_score in string_list:
        score = int(string_score)
        scores.append(score)

    return scores


# Method: compute the average of a list of ints
def average(int_list):

    sum = 0

    for value in int_list:
        sum += value

    avg = sum / len(int_list)
    return avg


# Method: report the indexes
def indexes_above(threshold, int_list):

    indexes = []

    for index in range(len(int_list)):
        if int_list[index] > threshold:
            indexes.append(index)

    return indexes

def print_lowest_highest(int_list):
    int_min = sys.maxsize
    int_max = -2000
    for index in range(len(int_list)):
        if int_list[index] < int_min:
            int_min = int_list[index]
        if int_list[index] > int_max:
            int_max = int_list[index]
    print('Highest Score =', int_max)
    print('Lowest Score =', int_min)

def curve(int_list, avg):
    curve = 100 - avg
    print('Curve:', curve, 'points')
    for index in range(len(int_list)):
        int_list[index] += curve
    return int_list

## Input/Output sequences

# Acquire sequence as string and split into list
print('Enter the scores, separating each score by a space')
string_sequence = input()
string_sequence = string_sequence.split(' ')


# Create corresponding list of ints rather than strings
scores = convert_to_int(string_sequence)


# Show the scores to ensure the data was properly converted
print("Scores:", scores)
print_lowest_highest(scores)


# Compute and print the average, calculate rounded average for curve
avg = average(scores)
round_avg = round(avg)
print('Average:', avg)



# Determine and print which items are above average
above_indexes = indexes_above(avg, scores)
print(len(above_indexes), "scores above average at indexes:", end=' ')
for index in above_indexes:
    print(index, end=" ")
    
print('\n')

# Determine curved scores
curved_scores= curve(scores, round_avg)
print('Curved scores:', curved_scores)
print_lowest_highest(curved_scores)

