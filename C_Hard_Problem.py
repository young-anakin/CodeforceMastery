t = int(input())
for _ in range(t):
    m, a, b, c = list(map(int, input().split(" ")))
    m_a = m
    m_b = m
    cp = 0

    if m >= a:
        cp += a
        m_a -= a   
    else:
        cp += m_a
        m_a = 0
    
    if m >= b:
        cp += b
        m_b -= b
    
    else:
        cp += m_b
        m_b = 0

    left = m_a + m_b
    cp += min(left, c)
    # print(m_a, m_b)
    print(cp)
    






    