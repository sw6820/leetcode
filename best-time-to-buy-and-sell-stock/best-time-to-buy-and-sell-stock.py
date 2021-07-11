class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m_profit,min_price=0,10000
        for p in prices:
            min_price=min(min_price,p)
            pr=p-min_price
            m_profit=max(m_profit,pr)
        return m_profit
    