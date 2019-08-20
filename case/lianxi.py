l=[5, 2, 12, 31, 23]
l.sort()
print(l)  # 从小到大  [2, 5, 12, 23, 31]

l.sort(reverse=True)
print(l)  # 从大到小  [31, 23, 12, 5, 2]

str_l=['cai', 'wang', 'Zhou', 'wu']
str_l.sort()
print(str_l)  # 字符串列表是按照第一个字符的大小排序，一般是大写在前，小写在后  ['Zhou', 'cai', 'wang', 'wu']

str_l.sort(key=str.lower)
print(str_l)  # 忽略大小写，按abcd排序  ['cai', 'wang', 'wu', 'Zhou']

str_l.sort(key=len)
print(str_l)  # 按字符串长度排序  ['wu', 'cai', 'wang', 'Zhou']

str_l.sort(key=len, reverse=True)
print(str_l)  # 按字符串长度反向排序   [2, 5, 12, 23, 31]

a=[('b', 4), ('a', 0), ('c', 2), ('d', 3)]
print(sorted(a, key=lambda x: x[0]))  # 按元组中的第一个元素进行排序 [('a', 0), ('b', 4), ('c', 2), ('d', 3)]

print(sorted(a, key=lambda x: x[1]))  # 按元组中的第二个元素进行排序 [('a', 0), ('c', 2), ('d', 3), ('b', 4)]

dic={'a:': 1, 'b': 2, 'c': 3}
a=dic.items()  # 将字典返回为一个列表格式 dict_items([('a:', 1), ('b', 2), ('c', 3)])
b=dic.keys()  # 将字典中的key都返回在一个列表中
c=dic.values()  # 将字典中的values返回在一个列表中
d=sorted(dic.items(), key=lambda w: w[1], reverse=True)  #  items是将字典{a:b}转化为[(a,b)],对第二个元素进行排序,
                                                                         # [('c', 3), ('b', 2), ('a:', 1)]
print(a)
print(b)
print(c)
print(d)

