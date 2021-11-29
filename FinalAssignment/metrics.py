import numpy as np

def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''

    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score
    # https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9
    count = 0
    for i in range(len(prediction)):
        if prediction[i] == ground_truth[i] and prediction[i] == True:
            count += 1
    precision = count / np.sum(prediction)
    recall = count / np.sum(ground_truth)
    accuracy = np.sum(prediction == ground_truth) / len(prediction)
    f1 = 2 * precision*recall/(precision + recall)
    return precision, recall, f1, accuracy



def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    # TODO: Implement computing accuracy
    accuracy = np.sum(prediction == ground_truth) / len(prediction)
    return accuracy
