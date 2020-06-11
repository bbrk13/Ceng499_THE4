from random import seed

# fix randomness; DO NOT CHANGE THIS
seed(1234)


def naive_bayes(train_path, test_path):
    """
    Performs naive Bayes classification
    :param train_path: path of the training set, a string
    :param test_path: path of the test set, a string
    :return: percent accuracy value for the test set, e.g., 85.43
    """
    label_array = []
    feature_array = []
    probability_array = []

    test_data = open_input_file(test_path)
    train_data = open_input_file(train_path)

    first_line = train_data[0]
    first_line_splitted = first_line.split(',')
    feature_number = len(first_line_splitted) - 1

    for i in range(feature_number):
        tmp_list = []
        feature_array.append(tmp_list)

    # Checking test data to find all possible labels
    for line in test_data:
        if line[-1] == '\n':
            line = line[:-1]
        tmp_line_splitted = line.split(',')
        tmp_label = tmp_line_splitted[-1]
        if not is_in_list(label_array, tmp_label):
            tmp_list = []
            tmp_list.append(tmp_label)
            tmp_list.append(0)
            label_array.append(tmp_list)

    # Checking train data to find possible all labels
    for line in train_data:
        if line[-1] == '\n':
            line = line[:-1]
        tmp_line_splitted = line.split(',')
        tmp_label = tmp_line_splitted[-1]
        if not is_in_list(label_array, tmp_label):
            tmp_list = []
            tmp_list.append(tmp_label)
            tmp_list.append(1)
            label_array.append(tmp_list)
        else:
            for label in label_array:
                if label[0] == tmp_label:
                    label[1] = label[1] + 1
    # Checking test data to find all possible feature values
    for line in test_data:
        if line[-1] == '\n':
            line = line[:-1]
        tmp_line_splitted = line.split(',')
        tmp_label = tmp_line_splitted[-1]
        for index in range(feature_number):
            for each_label in label_array:
                if not is_in_feature_list(feature_array, tmp_line_splitted[index], each_label[0], index):
                    tmp_list = []
                    tmp_list.append(index)
                    tmp_list.append(tmp_line_splitted[index])
                    tmp_list.append(each_label[0])
                    tmp_list.append(0)
                    feature_array[index].append(tmp_list)
    # Checking train data to find all possible feature values
    for line in train_data:
        if line[-1] == '\n':
            line = line[:-1]
        tmp_line_splitted = line.split(',')
        tmp_label = tmp_line_splitted[-1]
        for index in range(feature_number):
            for each_label in label_array:
                if not is_in_feature_list(feature_array, tmp_line_splitted[index], each_label[0], index):
                    tmp_list = []
                    tmp_list.append(index)
                    tmp_list.append(tmp_line_splitted[index])
                    tmp_list.append(each_label[0])
                    tmp_list.append(0)
                    feature_array[index].append(tmp_list)
            if not is_in_feature_list(feature_array, tmp_line_splitted[index], tmp_label, index):
                tmp_list = []
                tmp_list.append(index)
                tmp_list.append(tmp_line_splitted[index])
                tmp_list.append(tmp_label)
                tmp_list.append(1)
                feature_array[index].append(tmp_list)
            else:
                tmp_list = feature_array[index]
                for list_item in tmp_list:
                    if list_item[0] == index and list_item[1] == tmp_line_splitted[index] and list_item[2] == tmp_label:
                        list_item[3] = list_item[3] + 1

    # For each entry in test data, calculate the probabilities according to data above and make guess
    number_of_correct_guess = 0
    for test_instance in test_data:
        possibility_array = []
        for each_label in label_array:
            tmp_label = each_label[0]
            tmp_label_probability = 1
            tmp_probability_array = [tmp_label, tmp_label_probability]
            possibility_array.append(tmp_probability_array)

        p_temp = 1
        if test_instance[-1] == '\n':
            test_instance = test_instance[:-1]
        tmp_line_splitted = test_instance.split(',')
        real_label = tmp_line_splitted[-1]
        for index in range(feature_number):
            for feature_order in feature_array[index]:
                for pos in possibility_array:
                    if feature_order[0] == index and feature_order[1] == tmp_line_splitted[index] and pos[0] == feature_order[2]:
                        label_number = 1
                        for each_label in label_array:
                            if each_label[0] == pos[0]:
                                label_number = each_label[1]

                        pos[1] = pos[1] * (feature_order[3] / label_number)

        dummy_index = 1
        for each_pos in possibility_array:
            for each_label in label_array:
                if each_pos[0] == each_label[0]:
                    dummy_index = dummy_index + 1
                    possibilit_of_class = each_label[1] / len(train_data)
                    each_pos[1] = each_pos[1] * possibilit_of_class

        highest_probability = - 1
        model_guess = 'dummy'

        for guess in possibility_array:
            if guess[1] > highest_probability:
                highest_probability = guess[1]
                model_guess = guess[0]

        if model_guess == real_label:
            number_of_correct_guess = number_of_correct_guess + 1

    accuracy = (number_of_correct_guess / len(test_data)) * 100
    print(round(accuracy, 2))


def open_input_file(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    return lines


def is_in_list(list_input, item):
    if len(list_input) == 0:
        return False
    for list_item in list_input:
        if item == list_item[0]:
            return True
    return False


def is_in_feature_list(feature_array_input, item, label, feature_number):
    tmp_list = feature_array_input[feature_number]
    if len(tmp_list) == 0:
        return False
    for list_item in tmp_list:
        if list_item[1] == item and list_item[2] == label:
            return True
    return False


def is_in_possibility_array(p_array, key):
    if len(p_array) == 0:
        return False
    for entry in p_array:
        if entry[0] == key:
            return True

    return False


naive_bayes('task1_data/train.txt', 'task1_data/test.txt')