class Node(object):
    def __init__(self, name, value): #TODO: ver si hay que pasar profundidad
        self.name = name
        self.value = value
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)
