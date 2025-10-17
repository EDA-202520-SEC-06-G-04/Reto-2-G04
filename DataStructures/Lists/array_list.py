def new_list():
    newlist = {
        'elements': [], 
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
            if keyexist:
                return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"] = [element] + my_list["elements"]
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    
    
    if my_list["size"] == 0:
        my_list["elements"].append(element)
    
    else:
        my_list["elements"].append(element)
    
    my_list["size"] += 1
    
    return my_list

def is_empty(my_list):
    
    size = my_list["size"]
    
    if size == 0:
        iss = True
    else:
        iss = False
    
    return iss

def size(my_list):

    size = my_list["size"]
    
    return size

def first_element(my_list):
    
    return my_list["elements"][0]

    
def last_element(my_list):
    
    return my_list["elements"][-1]

def delete_element(my_list, pos):
    
    if (pos >= 0) and (pos < (my_list["size"])):
      my_list["elements"] = my_list["elements"][:pos] + my_list["elements"][pos+1:]
      
      my_list["size"] -= 1
      
      return my_list
    
    else:
        
        return my_list["elements"][pos]
    
    
def remove_first(my_list):
    
    if my_list["size"] == 0:
        first = my_list["elements"][0] 
        
    else:
        first = my_list["elements"][0]
        my_list["elements"] = my_list["elements"][1:]
        
        my_list["size"] -= 1
        
        return first

def remove_last(my_list):
    
    if my_list["size"] == 0:
        element = my_list["elements"][0] 
        
    else:
        last = my_list["elements"][-1]
        my_list["elements"] = my_list["elements"][:-1]
        
        my_list["size"] -= 1
        
        return last

def insert_element(my_list, element, pos):
    my_list["elements"] = (my_list["elements"][:pos] + [element] + my_list["elements"][pos:])
    my_list["size"] += 1
    return my_list



def change_info(my_list, pos, new_info):

    if (pos >= 0) and (pos < (my_list["size"])):

         my_list["elements"][pos] = new_info

         return my_list
    
    else: 
        return None


def exchange(my_list, pos1, pos2):

    if ((pos1 >= 0) and (pos1 < (my_list["size"]))) and ((pos2 >= 0) and (pos2 < (my_list["size"]))):
        
        element_1 = my_list["elements"][pos1]
        element_2 = my_list["elements"][pos2]

        my_list["elements"][pos1] = element_2
        my_list["elements"][pos2] = element_1

        return my_list
    
    else:
        
        return None 

def sub_list(my_list, pos_i, num_elements):

    if (pos_i >= 0) and (pos_i < (my_list["size"])):
        
        final_list = pos_i + num_elements

        if final_list > my_list["size"]:
            final_list = my_list["size"]

        elements = my_list["elements"][pos_i: final_list]
        sublist = {"size": len(elements), "elements": elements}

        return sublist
    
    else: 
        
        return None
    
def default_sort_criteria(element_1, element_2):
    rta = False
    if element_1 < element_2:
        rta = True
    else:
        rta = False
    return rta

def selection_sort(my_list, sort_crit): 
    
    siz = size(my_list)
    
    for i in range(siz):
        for j in range(i, my_list["size"]):
            if sort_crit(get_element(my_list, i), get_element(my_list, j)) == True:
                exchange(my_list, i, j)
    return my_list

def insertion_sort(my_list, sort_crit):
    
    siz = size(my_list)
    
    for i in range(1, siz):
        j = i 
        while j > 0 and sort_crit(get_element(my_list, j), get_element(my_list, (j - 1))) == True:
                exchange(my_list, j, j-1)
                j -= 1
    
    return my_list 



def shell_sort(my_list, sort_crit):
    
    siz = size(my_list)
    dist = siz // 2
    
    
    while dist > 0:
        for i in range (dist, siz):
            j = i 
            elem =  j - dist
            
            while j>= dist and sort_crit(get_element(my_list, j), get_element(my_list, (elem))):
                exchange(my_list, j, elem)
                j -= dist
        
        dist //= 2
        
    return my_list


def merge_sort(my_list, sort_crit):
    
    rta = new_list()
    siz = size(my_list)
    i = 0
    j = 0 
    
    if siz <= 1:
        return my_list
    
    mitad = siz // 2 
    lt1 = sub_list(my_list, 0, mitad)
    lt2 = sub_list(my_list, mitad, (siz - mitad))
    
    p_iz = merge_sort(lt1, sort_crit)
    p_der = merge_sort(lt2, sort_crit)       
    

    while i < p_iz["size"] and j < p_der["size"]:
        elem1 = get_element(p_iz, i)
        elem2 = get_element(p_der, j)
        
        if sort_crit(elem1, elem2) == True:
            add_last(rta, elem1)
            i += 1
        else:
            add_last(rta, elem2)
            j += 1
    
    while i < p_iz["size"]:
        add_last(rta, get_element(p_iz, i))
        i += 1
    while j < p_der["size"]:
        add_last(rta, get_element(p_der, j))
        j += 1
    
    return rta 


def quick_sort(my_list, sort_crit):
    
    men = new_list()
    mayo = new_list()
    siz = size(my_list)
    
    if siz <= 1:
        return my_list
    pivot = get_element(my_list, (siz -1))
    
    
    for i in range(0, siz -1):
        elem = get_element(my_list, i)
        if sort_crit(elem, pivot) == True:
            add_last(men, elem)    
        else: 
            add_last(mayo, elem)

    lt_men = quick_sort(men, sort_crit)
    lt_may = quick_sort(mayo, sort_crit)
    
    rta = new_list()
    
    for i in range (lt_men["size"]):
        add_last(rta, get_element(lt_men, i)) 
        
    for j in range(lt_may["size"]):
        add_last(rta, get_element(lt_may, j) )
                       
    return rta