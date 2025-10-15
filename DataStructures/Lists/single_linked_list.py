class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self._head = None   # usamos _head para evitar choque con método
        self.size = 0   

    def first(self):
        if self._head is None:
            raise Exception("La lista está vacía")
        return self._head.info

    def head(self):
        """Devuelve el nodo cabeza de la lista"""
        return self._head

    def add_first(self, element):
        new_node = Node(element)
        new_node.next = self._head
        self._head = new_node
        self.size += 1

    def add_last(self, element):
        new_node = Node(element)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def is_present(self, element, cmp_function):
        """Devuelve la posición si el elemento está presente, -1 si no"""
        current = self._head
        pos = 0
        while current is not None:
            if cmp_function(current.info, element) == 0:
                return pos
            current = current.next
            pos += 1
        return -1

    @staticmethod
    def default_function(a, b):
        """Función de comparación por defecto"""
        if a == b:
            return 0
        elif a > b:
            return 1
        else:
            return -1


def new_list():
    """Crea una nueva lista (representada como dict)"""
    return {"first": None, "last": None, "size": 0}


def _make_node(element):
    return {"info": element, "next": None}


def is_empty(my_list):
    return my_list["size"] == 0


def size(my_list):
    return my_list["size"]


def add_first(my_list, element):
    new_node = _make_node(element)

    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node

    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    new_node = _make_node(element)

    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node

    my_list["size"] += 1
    return my_list


def first_element(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    return my_list["first"]["info"]


def last_element(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    return my_list["last"]["info"]


def get_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise IndexError("list index out of range")
    cur = my_list["first"]
    i = 0
    while i < pos:
        cur = cur["next"]
        i += 1
    return cur["info"]


def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise IndexError("list index out of range")

    if pos == 0:
        return add_first(my_list, element)

    if pos == size(my_list):
        return add_last(my_list, element)

    new_node = _make_node(element)
    cur = my_list["first"]
    for _ in range(pos - 1):
        cur = cur["next"]
    new_node["next"] = cur["next"]
    cur["next"] = new_node
    my_list["size"] += 1
    return my_list


def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise IndexError("list index out of range")

    if pos == 0:
        # eliminar cabeza
        removed = my_list["first"]
        my_list["first"] = removed["next"]
        if my_list["size"] == 1:
            my_list["last"] = None
    else:
        prev = my_list["first"]
        for _ in range(pos - 1):
            prev = prev["next"]
        removed = prev["next"]
        prev["next"] = removed["next"] if removed else None
        if pos == my_list["size"] - 1:
            # si borramos el último, actualizar referencia last
            my_list["last"] = prev

    my_list["size"] -= 1
    return my_list


def remove_first(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    removed_info = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    if my_list["size"] == 0:
        my_list["last"] = None
    return removed_info


def remove_last(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")

    if my_list["size"] == 1:
        removed_info = my_list["first"]["info"]
        my_list["first"] = None
        my_list["last"] = None
        my_list["size"] = 0
        return removed_info

    cur = my_list["first"]
    while cur["next"] is not my_list["last"]:
        cur = cur["next"]
    # cur es el penúltimo
    removed_info = my_list["last"]["info"]
    cur["next"] = None
    my_list["last"] = cur
    my_list["size"] -= 1
    return removed_info


def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise IndexError("list index out of range")
    cur = my_list["first"]
    for _ in range(pos):
        cur = cur["next"]
    cur["info"] = new_info
    return my_list


def exchange(my_list, pos_1, pos_2):
    if (pos_1 < 0 or pos_1 >= size(my_list)) or (pos_2 < 0 or pos_2 >= size(my_list)):
        raise IndexError("list index out of range")
    if pos_1 == pos_2:
        return my_list

    if pos_1 > pos_2:
        pos_1, pos_2 = pos_2, pos_1

    cur = my_list["first"]
    i = 0
    node1 = node2 = None
    while cur:
        if i == pos_1:
            node1 = cur
        if i == pos_2:
            node2 = cur
            break
        cur = cur["next"]
        i += 1

    node1["info"], node2["info"] = node2["info"], node1["info"]
    return my_list


def is_present(my_list, element, cmp_function):
    current = my_list["first"]   # acceder al primer nodo
    while current is not None:
        if cmp_function(current["info"], element) == 0:
            return 1
        current = current["next"]
    return 0

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= size(my_list):
        raise IndexError("list index out of range")
    sub = new_list()
    cur = my_list["first"]
    for _ in range(pos):
        cur = cur["next"]
    count = 0
    while cur and count < num_elements:
        add_last(sub, cur["info"])
        cur = cur["next"]
        count += 1
    return sub
