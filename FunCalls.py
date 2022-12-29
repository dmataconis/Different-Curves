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
  
