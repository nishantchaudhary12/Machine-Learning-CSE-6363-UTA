class CustomObject:
    def __init__(self, array, attrs):
        for i in range(len(attrs)):
            setattr(self, attrs[i], array[i])


class Node(object):
    def __init__(self):
        self.label = ""
        self.subset = []

    def set_children_values(self, values):
        self.subset = []
        for i in values:
            self.subset.append(i)

    def __repr__(self):
        return "{}{}".format(self.label, self.subset)
