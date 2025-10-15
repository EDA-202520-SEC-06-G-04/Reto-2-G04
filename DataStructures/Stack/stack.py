from DataStructures.Lists import single_linked_list as sl

def new_stack():
    return sl.new_list()

def push(my_stack, element):
    sl.add_last(my_stack, element)
    return my_stack

def pop(my_stack):
    elemento = sl.remove_last(my_stack)
    return elemento
 
def size(my_stack):
    return sl.size(my_stack)

def is_empty(my_stack):
    empty = sl.is_empty(my_stack)
    return empty

def top(my_stack):
    return sl.last_element(my_stack)