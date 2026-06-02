class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        m_pr=0
        while r<len(prices):
            if prices[l] < prices[r]:
                pr = prices[r] - prices[l]
                m_pr = max(m_pr,pr)
            else:
                l=r
            r+=1

        return m_pr
        