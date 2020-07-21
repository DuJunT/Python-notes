def hang_the_balloon(data):
    total = 0
    for i in data.values():
        total += i
    sort_balloon = sorted(data.items(),key=lambda x:x[1],reverse=True)
    # print(data.items())
    # print(sort_balloon)
    max_count = sort_balloon[0][1]
    if max_count > (total+1)//2:
        return '无法做到相同颜色的气球不挂在一起'
    
    balloon_list = []
    res = [None]*total
    for key,count in sort_balloon:
        balloon_list.extend(key*count)
    print(balloon_list)
    if max_count == (total+1)//2:
        res[::2],res[1::2] = balloon_list[:(total+1)//2],balloon_list[(total+1)//2:]
    else:
        res[::2],res[1::2] = balloon_list[total//2:],balloon_list[:total//2]
    return '-'.join(res)

data = {'r':3,'y':5,'g':3}
print(hang_the_balloon(data))