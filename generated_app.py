def quicksort(arr):
    """
    對列表執行快速排序（in-place）。
    """
    _quicksort_recursive(arr, 0, len(arr) - 1)

def _quicksort_recursive(arr, low, high):
    """
    快速排序的遞迴輔助函數。
    """
    if low < high:
        # pi 是分區索引，arr[pi] 現在位於正確的位置
        pi = _partition(arr, low, high)

        # 分別對分區前和分區後的元素進行排序
        _quicksort_recursive(arr, low, pi - 1)
        _quicksort_recursive(arr, pi + 1, high)

def _partition(arr, low, high):
    """
    使用最後一個元素作為基準值（pivot）來進行分區。
    將所有小於等於基準值的元素放在其左側，所有大於基準值的元素放在其右側。
    """
    pivot = arr[high]  # 選擇最後一個元素作為基準值
    i = (low - 1)      # 較小元素的索引

    for j in range(low, high):
        # 如果當前元素小於或等於基準值
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] # 交換元素

    arr[i + 1], arr[high] = arr[high], arr[i + 1] # 將基準值放到正確的位置
    return (i + 1) # 返回基準值的最終索引

if __name__ == "__main__":
    # --- 測試案例 ---

    # 測試案例 1: 標準亂序列表
    list1 = [10, 7, 8, 9, 1, 5]
    print("原始列表 1:", list1)
    quicksort(list1)
    print("排序後列表 1:", list1)
    print("-" * 30)

    # 測試案例 2: 包含負數和零的列表
    list2 = [3, 0, 2, 5, -1, 4]
    print("原始列表 2:", list2)
    quicksort(list2)
    print("排序後列表 2:", list2)
    print("-" * 30)

    # 測試案例 3: 空列表
    list3 = []
    print("原始列表 3 (空):", list3)
    quicksort(list3)
    print("排序後列表 3:", list3)
    print("-" * 30)

    # 測試案例 4: 只有一個元素的列表
    list4 = [42]
    print("原始列表 4 (單一元素):", list4)
    quicksort(list4)
    print("排序後列表 4:", list4)
    print("-" * 30)

    # 測試案例 5: 已排序的列表
    list5 = [1, 2, 3, 4, 5]
    print("原始列表 5 (已排序):", list5)
    quicksort(list5)
    print("排序後列表 5:", list5)
    print("-" * 30)

    # 測試案例 6: 逆序排序的列表
    list6 = [5, 4, 3, 2, 1]
    print("原始列表 6 (逆序):", list6)
    quicksort(list6)
    print("排序後列表 6:", list6)
    print("-" * 30)

    # 測試案例 7: 包含重複元素的列表
    list7 = [4, 2, 5, 2, 1, 4, 3]
    print("原始列表 7 (重複元素):", list7)
    quicksort(list7)
    print("排序後列表 7:", list7)
    print("-" * 30)

    # 測試案例 8: 浮點數列表
    list8 = [3.14, 1.618, 2.718, 0.577, 1.414]
    print("原始列表 8 (浮點數):", list8)
    quicksort(list8)
    print("排序後列表 8:", list8)
    print("-" * 30)