# TODO реализовать функцию count
def count(list_, k):
    count_ = 0
    for i in list_:
        if i == k:
            count_ += 1
    return count_


list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
