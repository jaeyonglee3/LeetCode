class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # paraphrase
        # for all i, each item at priced at prices[i] gets a discount
        # the discount amount is prices[j], where j is the FIRST index after i
        # where prices[j] is less than or equal to prices[i]
        # return an array answers of size len(prices) where answers[i] is the
        # price of i with that discount applied

        # dry runs (examples)
        # prices = [8,4,6,2,3] - Note that not every item will have a discount
        # initialize answers as a copy of prices: answers = [4,2,4,2,3]
        # use technique called monotonic increasing (never decreasing) stack
        # stack = 2, 3

        # approach
        # we'll use a monotonically increading stack
        # visit each price one by one. If the curr price is lesser than the price at
        # the top of the stack, pop from the stack and update its index in answers
        # continue until each element is visited

        # implementation
        answers = prices.copy()
        stack = []  # contains (index, price) pairs. Monotonically increasing.

        for i, price in enumerate(prices):
            while stack and price <= stack[-1][1]:
                removed_i = stack.pop()[0]
                answers[removed_i] -= price  # apply the discount

            stack.append((i, price))

        return answers