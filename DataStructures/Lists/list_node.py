def new_single_node(element):
    """ Estructura que contiene la información a guardar en una lista encadenada

        :param element: Elemento a guardar en el nodo
        :type element: any

        :returns: Nodo creado
        :rtype: dict
    """
    node = {'info': element, 'next': None}
    return (node)


def get_element(node):
    """ Retorna la información de un nodo

        :param node: El nodo a examinar
        :type node: list_node

        :returns: La información almacenada en el nodo
        :rtype: any
    """
    return node['info']


def new_double_node(element):
    """ Estructura que contiene la información a guardar en un nodo de una lista doblemente encadenada
    """
    node = {'info': element,
            'next': None,
            'prev': None
            }
    return node