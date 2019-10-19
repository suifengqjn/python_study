#!/usr/bin/python3


#
# pickle 模块
# python的pickle模块实现了基本的数据序列和反序列化。
# 基本接口：
#
# pickle.dump(obj, file, [,protocol])
# 有了 pickle 这个对象, 就能对 file 以读取的形式打开:
#
# x = pickle.load(file)

import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()