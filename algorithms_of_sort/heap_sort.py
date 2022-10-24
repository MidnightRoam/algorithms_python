def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считаем корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня - допустимый индекс, а элемент больше, чем текущий наибольший,
    # обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент больше не корневой, то они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # Увеличиваем новый корневой элемент, чтобы убедиться, что он самый большой
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # Создаем Max Heap из списка
    # Второй аргумент означается остановку алгоритма перед элементом -1,
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении
    # уменьшая счетчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

# Проверка на работоспособность
random_list_of_nums = [35, 12, 12, 31, -31, -32, 0, -215, 92, 99]
heap_sort(random_list_of_nums)
print(random_list_of_nums)
