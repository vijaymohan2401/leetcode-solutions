class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        def convert(date):

            m,d=map(int,date.split("-"))
            return sum(days[:m-1])+d
        a1=convert(arriveAlice)
        a2=convert(leaveAlice)
        a3=convert(arriveBob)
        a4=convert(leaveBob)
        s=max(a1,a3)
        e=min(a2,a4)
        if s<=e:
            return e-s+1
        else:
            return 0