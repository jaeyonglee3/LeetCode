class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Approach - check the constraints of the 2 objects w/o manually
        # performing the operations themselves.
        freq_one = Counter(word1)
        freq_two = Counter(word2)

        # Sort lists of each the number of occurances for words 1 and 2
        # This is O(NlogN + MlogM), the overall time complexity is this too.
        sorted_values_one = sorted(freq_one.values())
        sorted_values_two = sorted(freq_two.values())

        # Ensure the sorted values are equal (word1 and 2 have the same count of each character)
        # We sort first b/c we need to compare frequencies regardless of the associated character
        # This was for operation 1. Then...
        # also ensure the sets of keys are the same. 
        # This ensures words 1 and 2 have the same unique characters.
        # This is b/c operation 2 can only be performed if a character exists in both strings. 
        return (sorted_values_one == sorted_values_two and 
                set(freq_one.keys()) == set(freq_two.keys()))
