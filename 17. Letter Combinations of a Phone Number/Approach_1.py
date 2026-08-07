class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        all_combinations = []

        def generate_combinations(current_combo, remaining_digits):
            if not remaining_digits:
                all_combinations.append(current_combo)
                return

            first_digit = remaining_digits[0]
            letters_for_digit = digit_to_letters[first_digit]

            for letter in letters_for_digit:
                generate_combinations(current_combo + letter, remaining_digits[1:])

        generate_combinations("", digits)

        return all_combinations