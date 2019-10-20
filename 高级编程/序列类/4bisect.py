
import bisect

# 维持序列升序排序 采用二分查找
list = []
bisect.insort(list, 3)
bisect.insort(list, 2)
bisect.insort(list, 5)
bisect.insort(list, 1)
bisect.insort(list, 4)

print(list)

# 查找一个值插入的位置
print(bisect.bisect_left(list, 3))
print(bisect.bisect_right(list, 3))