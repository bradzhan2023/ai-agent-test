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

def bubble_sort(arr):
    """
    對列表執行泡沫排序（in-place）。

    泡沫排序是一種簡單的排序演算法，它重複地遍歷列表，
    比較每對相鄰元素，並交換位置不正確的元素，直到列表排序完成。
    """
    n = len(arr)
    # 遍歷所有陣列元素
    for i in range(n - 1):
        # 最後 i 個元素已經在正確的位置
        # 每次遍歷都會將最大的未排序元素“冒泡”到其正確位置
        swapped = False # 優化：如果沒有發生交換，說明列表已經排序，可以提前結束
        for j in range(0, n - i - 1):
            # 遍歷從 0 到 n-i-1 的陣列
            # 如果找到的元素比下一個元素大，就交換它們
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果在這一輪中沒有發生任何交換，那麼陣列已經排序完成
        if not swapped:
            break


if __name__ == "__main__":
    # --- 測試案例 ---

    print("--- 快速排序測試 ---")

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

    print("\n" + "=" * 30 + "\n")
    print("--- 泡沫排序測試 ---")

    # 測試案例 B1: 標準亂序列表
    listB1 = [10, 7, 8, 9, 1, 5]
    print("原始列表 B1:", listB1)
    bubble_sort(listB1)
    print("排序後列表 B1:", listB1)
    print("-" * 30)

    # 測試案例 B2: 包含負數和零的列表
    listB2 = [3, 0, 2, 5, -1, 4]
    print("原始列表 B2:", listB2)
    bubble_sort(listB2)
    print("排序後列表 B2:", listB2)
    print("-" * 30)

    # 測試案例 B3: 空列表
    listB3 = []
    print("原始列表 B3 (空):", listB3)
    bubble_sort(listB3)
    print("排序後列表 B3:", listB3)
    print("-" * 30)

    # 測試案例 B4: 只有一個元素的列表
    listB4 = [42]
    print("原始列表 B4 (單一元素):", listB4)
    bubble_sort(listB4)
    print("排序後列表 B4:", listB4)
    print("-" * 30)

    # 測試案例 B5: 已排序的列表
    listB5 = [1, 2, 3, 4, 5]
    print("原始列表 B5 (已排序):", listB5)
    bubble_sort(listB5)
    print("排序後列表 B5:", listB5)
    print("-" * 30)

    # 測試案例 B6: 逆序排序的列表
    listB6 = [5, 4, 3, 2, 1]
    print("原始列表 B6 (逆序):", listB6)
    bubble_sort(listB6)
    print("排序後列表 B6:", listB6)
    print("-" * 30)

    # 測試案例 B7: 包含重複元素的列表
    listB7 = [4, 2, 5, 2, 1, 4, 3]
    print("原始列表 B7 (重複元素):", listB7)
    bubble_sort(listB7)
    print("排序後列表 B7:", listB7)
    print("-" * 30)

    # 測試案例 B8: 浮點數列表
    listB8 = [3.14, 1.618, 2.718, 0.577, 1.414]
    print("原始列表 B8 (浮點數):", listB8)
    bubble_sort(listB8)
    print("排序後列表 B8:", listB8)
    print("-" * 30)