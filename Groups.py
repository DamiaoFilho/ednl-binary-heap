from BinaryHeap import BinaryHeap, BinaryItem
import copy

def group_1():
    values = [10, 5, 20, 1, 15, 30, 25]

    binary_heap = BinaryHeap()

    print("-----Inserções-----")
    for v in values:
        binary_heap.insert(v, v)
        print("---/---")

    #Case 2
    print("-----Alteração de Prioridade-----")

    print("---Indice 3 com 50---")
    binary_heap.change_priority(3, 50)
    binary_heap.display_heap()

    print("---Indice 1 com 8---")
    binary_heap.change_priority(1, 8)
    binary_heap.display_heap()

    #Case 3
    print("-----Display depois da remoção-----")
    for i in range(0, 3):
        print(f"---Removendo {i+1} vez(es)---")
        binary_heap.remove()
        binary_heap.display_heap()


    #Case 4
    print("-----Display Heap Sort-----")
    #Create a true copy
    bh_copy = copy.deepcopy(binary_heap)
    bh_copy.heap_sort()

    #Case 5
    print("-----Elemento de alta Prioridade-----")
    print(binary_heap.get_high_priority().key)



def group_2():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    binary_heap = BinaryHeap()

    print("-----Inserções-----")
    for v in values:
        binary_heap.insert(v, v)
        print("---/---")

    #Case 2
    print("-----Alteração de Prioridade-----")

    print("---Indice 4 com 15---")
    binary_heap.change_priority(4, 15)
    binary_heap.display_heap()

    print("---Indice 8 com 3---")
    binary_heap.change_priority(8, 3)
    binary_heap.display_heap()

    #Case 3
    print("-----Display depois da remoção-----")
    for i in range(0, 5):
        print(f"---Removendo {i+1} vez(es)---")
        binary_heap.remove()
        binary_heap.display_heap()


    #Case 4
    print("-----Display Heap Sort-----")
    #Create a true copy
    bh_copy = copy.deepcopy(binary_heap)
    bh_copy.heap_sort()

    #Case 5
    print("-----Elemento de alta Prioridade-----")
    print(binary_heap.get_high_priority().key)


def group_3():
    values = [50, 40, 30, 20, 10, 5, 3]

    binary_heap = BinaryHeap()

    print("-----Inserções-----")
    for v in values:
        binary_heap.insert(v, v)
        print("---/---")

    #Case 2
    print("-----Alteração de Prioridade-----")

    print("---Indice 2 com 60---")
    binary_heap.change_priority(2, 60)
    binary_heap.display_heap()

    print("---Indice 5 com 1---")
    binary_heap.change_priority(5, 1)
    binary_heap.display_heap()

    #Case 3
    print("-----Display depois da remoção-----")
    for i in range(0, 3):
        print(f"---Removendo {i+1} vez(es)---")
        binary_heap.remove()
        binary_heap.display_heap()


    #Case 4
    print("-----Display Heap Sort-----")
    #Create a true copy
    bh_copy = copy.deepcopy(binary_heap)
    bh_copy.heap_sort()

    #Case 5
    print("-----Elemento de alta Prioridade-----")
    print(binary_heap.get_high_priority().key)


def group_4():
    values = [13, 26, 18, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]

    binary_heap = BinaryHeap()

    print("-----Inserções-----")
    for v in values:
        binary_heap.insert(v, v)
        print("---/---")

    #Case 2
    print("-----Alteração de Prioridade-----")

    print("---Indice 7 com 35---")
    binary_heap.change_priority(7, 35)
    binary_heap.display_heap()

    print("---Indice 10 com 12---")
    binary_heap.change_priority(10, 12)
    binary_heap.display_heap()

    #Case 3
    print("-----Display depois da remoção-----")
    for i in range(0, 4):
        print(f"---Removendo {i+1} vez(es)---")
        binary_heap.remove()
        binary_heap.display_heap()


    #Case 4
    print("-----Display Heap Sort-----")
    #Create a true copy
    bh_copy = copy.deepcopy(binary_heap)
    bh_copy.heap_sort()

    #Case 5
    print("-----Elemento de alta Prioridade-----")
    print(binary_heap.get_high_priority().key)