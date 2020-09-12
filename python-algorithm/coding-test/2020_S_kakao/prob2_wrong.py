def make_tuple(orders) :
    order_list = []
    for order in orders :
        order_list.append((len(order),order))
    return sorted(order_list)

def find_exist(order_list) :
    order_cnt_list = []
    for src_order in order_list :
        order_cnt = 0
        for tgt_order in orders :
            if src_order[1] in tgt_order :
                order_cnt += 1
        order_cnt_list.append((order_cnt,src_order[0],src_order[1]))

    return sorted(order_cnt_list)

def compare(order_cnt_list) : 
    final_order_list =[]
    for order in order_cnt_list :
        if order[1] in courses : 
            if order[0] >= 2 :
                final_order_list.append(order[2])
    return sorted(final_order_list)


def solution(orders,course) :
    funcs = [make_tuple,find_exist,compare]
    answer = orders
    for func in funcs :
        answer = func(answer)
        # print(func.__name__, answer)
    

    return answer
                
if __name__ == "__main__" :
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    courses = [2,3,4]
    solution(orders,courses)