import json
import math
import random

import jsbeautifier
import sys

from Record import Node
from Record import CustomObject

# Precision for values
precision = 10 ** 2

# Calculates the entropy of the given dataset
def entropy(dataset):
    entropy_value = 0
    p = []
    classes = set()
    for data in dataset:
        classes.add(getattr(data, target_attribute))
    for label in classes:
        label_count = 0
        for data in dataset:
            if getattr(data, target_attribute) == label:
                label_count += 1
        p.append(label_count)
    for pi in p:
        pi = pi / len(dataset)
        entropy_value += -(pi * math.log2(pi))
    return math.floor(entropy_value * precision) / precision


# Calculate the information gain of the given attribute in the dataset
def gain(dataset, attribute):
    values = set()
    sum = 0
    for data in dataset:
        values.add(getattr(data, attribute))
    for v in values:
        sv = set()
        for data in dataset:
            if getattr(data, attribute) == v:
                sv.add(data)
        sum += (len(sv) / len(dataset)) * entropy(sv)
    return math.floor((entropy(dataset) - sum) * precision) / precision


# Retrieves unique values of the given attributes
def get_values(attributes):
    return_this = {}
    for a in attributes:
        values = set()
        for d in data:
            values.add(getattr(d, a))
        return_this[a] = values
    return return_this


# Checks if the dataset has all the target value of the same class
def all_same(dataset):
    value = set()
    for d in dataset:
        value.add(getattr(d, target_attribute))
    if len(value) == 1:
        return True, value.pop()
    else:
        return False, ''


# Retrieves the most common value, i.e., the class value which appears more than others
def most_common_value(dataset):
    values = {}
    v = set()
    for d in dataset:
        v.add(getattr(d, target_attribute))
    for vv in v:
        values[vv] = 0
    for d in dataset:
        values[getattr(d, target_attribute)] += 1

    max_v = ('blank', -99)
    for vv in values:
        if values[vv] >= max_v[1]:
            max_v = (vv, values[vv])
    return max_v[0]


# Retrieves the best attribute, i.e., the attribute with the maximum information gain
def best_attribute(dataset, attributes):
    best_a = ('', -99)
    for a in attributes:
        gain_v = gain(dataset, a)
        if gain_v > best_a[1]:
            best_a = (a, gain_v)
    return best_a[0]


# Splits the dataset into array of given values for the given attribute
def split(dataset, attribute, vi):
    splitted = []
    for d in dataset:
        if getattr(d, attribute) == vi:
            splitted.append(d)
    return splitted


# Calculate the accuracy of the generated tree using the data provided
def accuracy(data, tree):
    count = 0
    for d in data:
        instance = {}
        for a in attributes:
            instance[a] = getattr(d, a)
        if getattr(d, target_attribute) == predict(tree, instance):
            count += 1
    return "Accuracy =", math.floor((count * 100 / len(data)) * precision) / precision


# K-Fold data splitting and cross-validation
def kfold(k=10):
    bins = []
    a = []
    #random.shuffle(data)
    k = len(data)//7
    for i in range(0, len(data)):
        a.append(data[i])
        if len(a) % k == 0:
            bins.append(a)
            a = []
    bins.append(a)
    efficiency = 0
    for i in range(0, len(bins)):
        testing_set = bins[i]
        training_set = []
        for j in range(0, len(bins)):
            if i is not j:
                for b in bins[j]:
                    training_set.append(b)
        tree = id3(training_set, target_attribute, attributes)
        acccr = (accuracy(testing_set, tree)[1])
        efficiency += acccr
        print("Bin", i, " accuracy =", acccr)
    print("Average accuracy =", efficiency / len(bins))


# Function to predict the record using the tree provided
def predict(tree, record):
    if not isinstance(tree, dict):
        return tree
    root_node = list(tree.keys())[0]
    root_value = list(tree.values())[0]
    instance_attribute_value = record[root_node]
    return predict(root_value[instance_attribute_value], record)


# The ID3 algorithm.
# https://en.wikipedia.org/wiki/ID3_algorithm#Pseudocode
def id3(dataset, target_attribute, attributes):
    root = Node()
    if all_same(dataset)[0]:
        root.label = all_same(dataset)[1]
        return root.label
    if len(attributes) == 0:
        root.label = most_common_value(dataset)
        return root.label
    else:
        A = best_attribute(dataset, attributes)
        root.label = A
        tree = {A: {}}
        for vi in get_values(attributes)[A]:
            examples_vi = split(dataset, A, vi)
            if len(examples_vi) == 0:
                leaf = Node()
                leaf.label = most_common_value(dataset)
                return leaf.label
            else:
                attributes_minus_A = []
                for a in attributes:
                    if a is not A:
                        attributes_minus_A.append(a)
                tree[A][vi] = id3(examples_vi, target_attribute, attributes_minus_A)
    return tree


dd = open(sys.argv[2]).readlines()
data = []
aa = open(sys.argv[1]).readlines()
attributes = aa[0].split(",")
target_attribute = attributes[-1]

for d in dd:
    data.append(CustomObject(d.strip().split(","), attributes))
attributes.remove(target_attribute)

random.shuffle(data)
eighty_data = data[:math.floor(.8 * len(data))]
twenty_data = data[math.floor(.8 * len(data)):]

kfold(k=7)
tree = id3(data, target_attribute, attributes)
print(accuracy(twenty_data, tree))
# print(tree)
print(jsbeautifier.beautify(json.dumps(tree)))
