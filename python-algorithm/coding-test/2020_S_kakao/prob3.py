def make_info_dict(info) :
    info_dict = []
    for i in info :
        i_list = i.split()
        info_dict.append({
                        'lang':i_list[0],
                        'job':i_list[1],
                        'age':i_list[2],
                        'soul':i_list[3],
                        'score':int(i_list[4])
                        })
    return info_dict

def make_query_dict(query) :
    query_dict = []
    for i in query :
        i_list = i.split(" and ")
        query_dict.append({
                        'lang':i_list[0],
                        'job':i_list[1],
                        'age':i_list[2],
                        'soul':i_list[3].split()[0],
                        'score':int(i_list[3].split()[1])
                        })
    return query_dict

def find_people(info_dict,query_dict) :
    passCntList = []
    for query in query_dict : # {'lang',...}
        # print("------")
        # print(query)
        # print("------")

        passCnt = 0
        condition_yn = []
        for condition,value in query.items() : # 'lang'
            if value != '-' :
                condition_yn.append(condition)
        # print("따질 조건은",condition_yn)
        # print("-------------")
        for info in info_dict :
            # print("지원자의 조건 :",info)
            isPass = True
            for condition in condition_yn :
                if type(query[condition]) == str : 
                    if query[condition] != info[condition] :
                        isPass = False
                else :
                    if query[condition] > info[condition] :
                        isPass = False
            if isPass : 
                passCnt +=1 

        passCntList.append(passCnt)
    return passCntList

def solution(info, query):
    funcs = [make_info_dict,make_query_dict,find_people]
    # answer = make_info_dict(info)
    # answer = make_query_dict(query)
    info_dict = make_info_dict(info)
    query_dict = make_query_dict(query)
    answer = find_people(info_dict,query_dict)
    # print(answer)
    return answer
    
if __name__ == "__main__" :
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    solution(info,query)