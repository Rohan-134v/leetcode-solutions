class Solution:
    def reverseVowels(self, s: str) -> str:
        first = 0
        last = len(s) - 1
        a = list(s)
        owels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O','U'}
        while first < last :
            if (a[first] in  owels) and (a[last] in owels) :
                a[first], a[last] = a[last], a[first]
                first += 1
                last -= 1
            elif a[first] not in owels:
                first += 1
            elif a[last] not in owels:
                last -= 1
        return "".join(a)

