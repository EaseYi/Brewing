# Python语法

### 奇怪的知识

- xxx[-1] 对于一个list或deque，负索引 -1 表示从右到左的第一个元素

### str基本用法

```
s = " Hello, World! "

# 转换为小写
print(s.lower())  # 输出:  hello, world!

# 转换为大写
print(s.upper())  # 输出:  HELLO, WORLD!

# 首字母大写
print(s.capitalize())  # 输出:  hello, world!

# 每个单词首字母大写
print(s.title())  # 输出:  Hello, World!

# 去除两端空格
print(s.strip())  # 输出: Hello, World!

# 替换子字符串
print(s.replace("World", "Python"))  # 输出:  Hello, Python!

# 拆分字符串
print(s.split(", "))  # 输出: [' Hello', 'World! ']

# 查找子字符串
print(s.find("World"))  # 输出: 8

# 判断前缀
print(s.startswith(" Hello"))  # 输出: True

# 判断后缀
print(s.endswith("! "))  # 输出: True
```

### 双端队列的基本用法

```
from collections import deque

# 创建一个 deque
d = deque([1, 2, 3])

# 添加元素
d.append(4)          # 在右端添加元素 4
d.appendleft(0)      # 在左端添加元素 0
print(f"After append and appendleft: {d}")  # 输出: deque([0, 1, 2, 3, 4])

# 删除元素
right_elem = d.pop()       # 从右端弹出元素
left_elem = d.popleft()    # 从左端弹出元素
print(f"Popped elements: right_elem={right_elem}, left_elem={left_elem}")  # 输出: 4 和 0
print(f"After pop and popleft: {d}")  # 输出: deque([1, 2, 3])

# 访问元素
index_of_2 = d.index(2)    # 获取元素 2 的索引
count_of_2 = d.count(2)    # 计算元素 2 的数量
print(f"Index of 2: {index_of_2}, Count of 2: {count_of_2}")  # 输出: 1 和 1

# 插入和删除特定元素
d.insert(1, 1.5)     # 在索引 1 位置插入 1.5
print(f"After insert: {d}")  # 输出: deque([1, 1.5, 2, 3])
d.remove(1.5)        # 删除第一个匹配的元素 1.5
print(f"After remove: {d}")  # 输出: deque([1, 2, 3])

# 旋转
d.rotate(1)          # 向右旋转 1 步
print(f"After rotate(1): {d}")  # 输出: deque([3, 1, 2])
d.rotate(-1)         # 向左旋转 1 步
print(f"After rotate(-1): {d}")  # 输出: deque([1, 2, 3])
```