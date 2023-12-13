def d_t_l_converter(inp_d_t_l):
    dict_list = []
    list_dict = {}
    if isinstance(inp_d_t_l, (list, tuple)):
        for item in inp_d_t_l:
            list_dict[item[0]] = item[1]
        return list_dict
    elif isinstance(inp_d_t_l, dict):
        for k in inp_d_t_l:
            dict_list.append((k, inp_d_t_l[k]))
        return dict_list
    else:
        print("You should enter tuple, list or dictionary.")
        return None


print(d_t_l_converter(((1, "ali"), (2, "mahdi"))))
print(d_t_l_converter([(1, "ali"), (2, "mahdi")]))
print(d_t_l_converter({1: "ali", 2: "mahdi"}))
