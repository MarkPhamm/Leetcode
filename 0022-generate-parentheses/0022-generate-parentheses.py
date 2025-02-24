class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 2 factors
        # number of open bracket = close bracket
        # all open bracket must be closed after

        # 1. at the end, number of open bracket = close bracket
        # at any position, number of open bracket >= closed bracket

        ans = []
        curr = []
        current_open, current_close = 0,0


        def chose(i):
            """
                chose bracket for i position
            """
            nonlocal current_open, current_close
            # base case (when to stop)
            if i == 2*n:
                if current_close == current_open: # valid curr:
                    ans.append("".join(curr[:]))
                return

            # recursion
            if current_open + 1 <= n:
                curr.append("(")
                current_open+=1
                chose(i+1)
                current_open-=1
                curr.pop()
            
            if current_close + 1 <= current_open:
                curr.append(")")
                current_close+=1
                chose(i+1)
                current_close-=1
                curr.pop()
            
        chose(0)
        return ans
        