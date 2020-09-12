
"""
개념 : 빡 구현 문제
접근 : id가 1000자이므로, 효율성 상관없이 그냥 푼다

"""
def step1(new_id) :
    return new_id.lower()

def step2(new_id) :
    denied_char ="~!@#$%^&*()=+[{]}:?,<>"
    for char in denied_char :
        new_id = new_id.replace(char,'')

    return new_id

def step3(new_id) :
    if len(new_id) <= 1 : return new_id
    
    index_list = []
    for idx in range(1,len(new_id)) :
        if (new_id[idx] == new_id[idx-1]) and (new_id[idx] == '.') :
            index_list.append(idx)
    for idx in reversed(index_list) :
        new_id = new_id[:idx] + new_id[idx+1:]
    return new_id

def step4(new_id) :
    if len(new_id) == 0 : new_id = ""
    elif len(new_id) == 1 : 
        if new_id[0] == '.' : new_id = ""
    elif len(new_id) >= 2 :
        if new_id[0] == '.' : new_id = new_id[1:]
        if new_id[-1] == '.' : new_id = new_id[:-1]
    return new_id

def step5(new_id) :
    if len(new_id) == 0 : new_id = 'a'
    return new_id

def step6(new_id) :
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        if new_id[-1] == '.' : new_id = new_id[:-1]
    return new_id

def step7(new_id) :
    if len(new_id) <= 2 :
        last_char = new_id[-1]
        while len(new_id) < 3 :
            new_id+=last_char
    return new_id


def solution(new_id) :
    funcs = [step1,step2,step3,step4,step5,step6,step7]
    for func in funcs :
        new_id = func(new_id)
        print(new_id)
    return new_id

if __name__ == "__main__" :
    new_id = "#########################"
    solution(new_id)