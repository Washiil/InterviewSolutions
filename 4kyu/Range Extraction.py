def solution(args):
    result = []
    i = 0
    while i < len(args):
        start = args[i]
        end = start
        while i + 1 < len(args) and args[i + 1] == end + 1:
            end = args[i + 1]
            i += 1
        if end - start >= 2:
            result.append(f"{start}-{end}")
        else:
            result.append(str(start))
            if end != start:
                result.append(str(end))
        i += 1
    
    return ','.join(result)


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))