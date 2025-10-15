from DataStructures.Lists import single_linked_list as sl

def new_queue():
    return sl.new_list()

def enqueue (my_queue, element):
    return sl.add_last(my_queue, element)

def dequeue (my_queue):
    
    if my_queue["size"] == 0:
        raise Exception("EmptyStructureError: queue is empty")
    elemento = my_queue["first"]["info"]
    my_queue["first"] = my_queue["first"]["next"]
    
    if my_queue["first"] is None:
        my_queue["last"] = None    
    my_queue ["size"]-=1
    return elemento

def peek(my_queue):
    if sl.is_empty(my_queue):
        raise Exception("EmptyStructureError: queue is empty")
    
    return sl.first_element(my_queue)

def is_empty(my_queue):
    return my_queue["size"] == 0

def size(my_queue):
    return sl.size(my_queue)