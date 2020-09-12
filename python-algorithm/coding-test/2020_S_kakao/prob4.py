"""
1. 합승을 하고 갈 경우, S에서 각 노드로 가는 최소값을 구한다

2. 각 노드에서 흩어진다고 가정하고, 출발점을 해당 노드로 잡고 각자의 집에 가는 길을 구한다

3. 이를 출발점에서 각자의 집에 가는 길을 구한다

4. 두 값을 비교해 결론을 내린다
"""
def make_weight_matrix(n,fares) :
    # 파이썬 2차원배열 선언에 주의
    matrix = [[987654321]*(n) for _ in range(n)]
    for i in range(n) : 
        matrix[i][i] = 0
    for fare in fares :
        # print(fare[0],",",fare[1],",",fare[2])
        matrix[fare[0]-1][fare[1]-1] = fare[2]
        matrix[fare[1]-1][fare[0]-1] = fare[2]
        
    # print(matrix)
    return matrix

def make_fw_matrix(n,weight_matrix) :
    for j in range(n) : # 경유지
        for i in range(n) : # 출발점
            for k in range(n) : # 도착점
                if weight_matrix[i][k] > weight_matrix[i][j] + weight_matrix[j][k] :
                    weight_matrix[i][k] = weight_matrix[i][j] + weight_matrix[j][k]
    return weight_matrix

def solution(n, s, a, b, fares):
    weight_matrix = make_weight_matrix(n,fares)
    fw_matrix = make_fw_matrix(n,weight_matrix)

    # 출발점에서 각자 흩어지는 경우
    solo_cost = fw_matrix[s-1][a-1] + fw_matrix[s-1][b-1]
    # 다른곳까지 택시를 탄 후 흩어지는 경우
    cost = 987654321
    for i in range(n) :
        temp_cost = fw_matrix[s-1][i-1] + fw_matrix[i-1][a-1] + fw_matrix[i-1][b-1]
        cost = min(temp_cost,cost)
    return min(solo_cost,cost)

if __name__ == "__main__" :
    minima = 987654321
    n = 6;s = 4;a = 6;b = 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

    n=7; s=3;a=4;b=1;
    fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    
    n=6;	s= 4;a=	5;b=	6
    fares=	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
    print(solution(n,s,a,b,fares))