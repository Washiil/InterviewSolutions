import collections

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        T = collections.defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)
            
        seen = set()
        def solve(A):
            if len(A) == 1: return True
            if A in seen: return False
            seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i = 0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)