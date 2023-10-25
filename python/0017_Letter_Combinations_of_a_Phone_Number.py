class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = [letter for letter in phone[digits[0]]]
        for i in range(1, len(digits)):
            r = []
            for combination in result:
                r.extend([combination + letter for letter in phone[digits[i]]])
            result = r

        return result
