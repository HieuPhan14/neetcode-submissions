class Solution:
    def numDecodings(self, s: str) -> int:
        return self.pick(s, 0, {})

    def pick(self, s, i, memo):
        if i in memo:
            return memo[i]

        if i == len(s):
            return 1

        if s[i] == '0':
            return 0

        pick_first = self.pick(s, i + 1, memo)

        pick_two = 0
        if i < len(s) - 1 and int(s[i:i+2]) <= 26:
            pick_first_and_second = self.pick(s, i + 2, memo)  
            pick_two += pick_first_and_second

        memo[i] = pick_first + pick_two
        return memo[i]
           
    