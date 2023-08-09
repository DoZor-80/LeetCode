class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = abs(n)
            x = 1 / x
        powers = {0: x}
        bits = f'{n:b}'[::-1]
        i = 0
        products = [powers[0]] if bits[0] == '1' else []
        for degree in bits[1:]:
            i += 1
            powers[i] = powers[i-1] * powers[i-1]
            if degree == '1':
                products.append(powers[i])
        result = 1
        for p in products:
            result = result * p
        return result
