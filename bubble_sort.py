def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                # Set swapped to True for next iteration
                swapped = True


# Проверка на работоспособность
# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4, 8, 10, 9, 0, -5, -3]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
