import json
part_nums = ['ECA-1EHG102','CL05B103KB5NNNC','CC0402KRX5R8BB104']


def json_list(list):
    lst = []
    for pn in list:
        d = {}
        d['mpn']=pn
        lst.append(d)
    return json.dumps(lst)

print (json_list(part_nums))