class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        return max(0, self.getDayOfYear(min(leaveAlice, leaveBob)) - self.getDayOfYear(max(arriveAlice, arriveBob)) + 1)
    
    # For example, "01-01" is day 1, and "12-31" is day 365
    def getDayOfYear(self, date):
        monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(date[:2])
        days = int(date[3:])

        # Return sum of days in each month before current month 
        # + any additional days from curr month
        return sum(monthList[: month - 1]) + days