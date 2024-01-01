def findContentChildren(self, g: list[int], s: list[int]) -> int:
    children = sorted(g)
    cookies = sorted(s)

    output = 0

    for cookie in cookies:
        for i in range(len(children)):
            if cookie >= children[i]:
                output += 1
                children.pop(i)
                break
    
    return output