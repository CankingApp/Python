# 类调用实例
# 列表
# 递归

def print_test(the_list):
     if isinstance(the_list, list):
           for t in the_list:
                 print(t)
                 print_test("not list")
     else:
           print(the_list)
