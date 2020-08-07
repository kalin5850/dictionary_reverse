def dictElementGet(d):
    for k, v in d.items():
        if type(v) is dict:
            a = dictElementGet(v)
            a.append(k)
            return a
        else:
            tmp = []
            tmp.append(v)
            tmp.append(k)
            return tmp


def get_reverse_dict(result_list):

    tree_dict = {}
    result_list.reverse()
    i = 1

    while i < len(result_list):
        if i == 1:
            tree_dict = {result_list[i]: result_list[0]}
        else:
            tree_dict = {result_list[i]: tree_dict}
        i += 1

    return tree_dict


if __name__ == '__main__':

    input_value = {
        'hired': {
            'be': {
                'to': {
                    'deserve': 'I'
                }
            }
        }
    }

    list = dictElementGet(input_value)
    result_reverst_dict = get_reverse_dict(list)
    print(result_reverst_dict)


