def balloon_arrange(data):
    # 获取气球总数
    total = 0
    for i in data.values():
        total = total + i
    # 气球颜色最多的数量
    sort_balloon = sorted(data.items(), key=lambda x:x[1], reverse=True)
    # print(sort_balloon)
    max_count = sort_balloon[0][1]
    if max_count > (total + 1) // 2:
        return "无法做到相同颜色的气球不挂在一起"

    res = []
    list = [None] * total
    for k, count in sort_balloon:
        res.extend(k * count)
    # print(res)
    if max_count == (total + 1) // 2:
        list[::2], list[1::2] = res[:(total + 1) // 2], res[(total + 1) // 2:]
        # print(list)
    else:
        list[::2], list[1::2] = res[total // 2:], res[:total // 2]
        # print(list)
    return "-".join(list)

data = {'r': 2, 'b': 4, 'w': 1, }
data1 = {'r': 2, 'b': 5, 'w': 1, }
data2 = [('r',2),('b',2),('w',1)]
print(balloon_arrange(data))
print(balloon_arrange(data1))


list = [1,2,3,4,5,6,7,8,9]
# print(list[1::])
list.extend('m')
list.append((1,1))
list.extend((1,'m'))
print(list)
