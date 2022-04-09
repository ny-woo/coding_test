def solution(name):
    answer = 0
    origin = ''
    cur = 0
    for i in range(len(name)):
        origin += 'A'
    while True:
        temp1 = ord(name[cur]) - ord('A')
        temp2 = ord('Z') - ord(name[cur])
        if temp1 < temp2:
            answer += temp1
        else:
            answer += (temp2 + 1)
        origin = origin[0:cur] + name[cur] + origin[cur+1:len(name)]
        # print(cur)
        # print(origin)
        # print(answer)
        if name == origin:
            return answer
        left = cur
        right = cur
        while True:
            left -= 1
            right += 1
            if left < 0:
                left = len(name) - 1
            if right > (len(name) - 1):
                right = 0
            answer += 1
            if origin[right] != name[right]:
                cur = right
                break
            if origin[left] != name[left]:
                cur = left
                break
    return answer