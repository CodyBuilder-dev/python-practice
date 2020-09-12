"""
의미 : 파이썬에서 시계열을 처리하는 방법에 대한 문제?

접근 :
1. 모든 시간의 분절점들을 파악한다. 
2. 분절점을 기준으로 나눈다 ("시작시간" 기준으로 파악)
3 . 각 시간구간에 존재하는 시청자수를 파악한다. "시작시간":시청자수
4. 00:00:00 부터 99:59:59까지 for문 돌면서 시청자수의 총합을 구한다
"""

def str2time(timestr) :
    h = int(timestr[:2])
    m = int(timestr[3:5])
    s = int(timestr[6:])

    return h,m,s

def time2str(h,m,s) :
    # if h<0 or m <0 or s <0 : raise("no")
    h_str = f"{h}" if h>=10 else f"0{h}"
    m_str = f"{m}" if m>=10 else f"0{m}"
    s_str = f"{s}" if m>=10 else f"0{s}"
    return f"{h_str}:{m_str}:{s_str}"

def get_timeadd(str1,str2) :
    h2,m2,s2 = str2time(str2)
    h1,m1,s1 = str2time(str1)

    min_borrow = False
    if s2 + s1 >= 60 : 
        delta_s = s2+s1-60
        min_borrow = True
    else : 
        delta_s = s2+s1
    
    if min_borrow :
        m2 += 1
    hour_borrow = False
    if m2+m1 >= 60 : 
        delta_m = m2+m1 - 60
        hour_borrow = True
    else : 
        delta_m = m2+m1
        

    if hour_borrow :
        h2 += 1
    delta_h = h2+h1
    
    return time2str(delta_h,delta_m,delta_s)

def get_timedelta(str1,str2) :
    # str1 < str2라는 보장 하에서만 사용 가능
    h2,m2,s2 = str2time(str2)
    h1,m1,s1 = str2time(str1)

    min_borrow = False
    if s2 >= s1 : delta_s = s2-s1
    else : 
        delta_s = 60-s1+s2
        min_borrow = True
    
    if min_borrow :
        m2 -= 1
    
    hour_borrow = False
    if m2>=m1 : delta_m = m2-m1
    else : 
        delta_m = 60-m1+m2
        hour_borrow = True

    if hour_borrow :
        h2 -= 1
    delta_h = h2-h1
    
    return time2str(delta_h,delta_m,delta_s)

def get_timeframe(logs) :
    time_set = set()
    for log in logs :
        time_set.add(log.split('-')[0])
        time_set.add(log.split('-')[1])
    
    timeframe = {}
    for idx,time in enumerate(sorted(time_set)) :
        if idx == len(time_set) : continue
        timeframe[time] = {"user":0}

    return timeframe


def get_time_user(timeframe,logs) :
    for log in logs :
        start_time = log.split('-')[0]
        end_time = log.split('-')[1]
        for time in timeframe :
            if time >= start_time and time < end_time :
                timeframe[time]["user"] += 1
    return timeframe


def get_most_user(play_time,adv_time,timeframe) :
    play_h,play_m,play_s = str2time(play_time)
    adv_h,adv_m,adv_s = str2time(adv_time)

    for h in range(play_h) :
        for m in range(play_m) :
            for s in range(play_s) :
                # 시작시간과 종료시간을 정하고, 그 사이에 있는 구간들의 시간 계산
                start_time = time2str(h,m,s)
                end_time = get_timeadd(start_time,adv_time)
                total_duration = "00:00:00"
                for time in timeframe :
                    if time >= start_time and time < end_time :
                        timeframe[time] += 1
                

def solution(play_time, adv_time, logs):
    timeframe = get_timeframe(logs)
    timeframe_user = get_time_user(timeframe,logs)
    print(timeframe_user)
    return timeframe_user

if __name__ == "__main__" :
    play_time = "02:03:55";adv_time=	"00:14:15"
    logs=	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    # solution(play_time,adv_time,logs)
    # print(str2time("04:53:42"))
    # print(time2str(3,43,53))
    # print(get_timedelta("21:42:43","22:54:10"))