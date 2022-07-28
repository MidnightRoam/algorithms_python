def selection_sort(nums):
    # Значение i соответствует количеству отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает неотсортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# Проверка на работоспособность
random_list_of_nums = [1, 8, 9, 4, 5, -2, -5, -8, 0, 1, 2, 3]
selection_sort(random_list_of_nums)
print(random_list_of_nums)
