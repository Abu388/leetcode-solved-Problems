class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if sum(range(1, maxChoosableInteger + 1)) < desiredTotal:
            return False

        memo = {}

        def can_win(used_numbers, current_total):
            if used_numbers in memo:
                return memo[used_numbers]
            
            for i in range(maxChoosableInteger):
                current_mask = 1 << i
                if used_numbers & current_mask == 0:
                    
                    if current_total + (i + 1) >= desiredTotal or not can_win(used_numbers | current_mask, current_total + (i + 1)):
                        memo[used_numbers] = True
                        return True
            
            memo[used_numbers] = False
            return False
        
        return can_win(0, 0)
