
class Ex1(object):
    """
    Algorithms pag. 308
    Suppose you are managing the construction of billboards on the Stephen Daedalus Memorial Highway, a heavily traveled stretch of road that runs west-east for M miles. The possible sites for billboards are given by numbers x1, x2, . . . , xn, each in the interval [0, M] (specifying their position along the highway, measured in miles from its western end). If you place a billboard at location xi, you receive a revenue of ri > 0.
    Regulations imposed by the county’s Highway Department require that no two of the billboards be within less than or equal to 5 miles of each other. You’d like to place billboards at a subset of the sites so as to maximize your total revenue, subject to this restriction.
    Example. Suppose M = 20, n = 4,
    {x1, x2, x3, x4} = {6, 7, 12, 14},
    and
    {r1,r2,r3,r4}={5,6,5,1}.
    Then the optimal solution would be to place billboards at x1 and x3, for a total
    revenue of 10.
    Give an algorithm that takes an instance of this problem as input and returns the maximum total revenue that can be obtained from any valid subset of sites. The running time of the algorithm should be polynomial in n.
    """
    def __init__(self, M, a, r):
        assert max(a) <= M
        assert len(a) == len(r)
        self.N = len(a)
        self.a = a
        self.r = r

    def solve_exp(self):
        return self.f_exp(self.N, 0, None)

    def f_exp(self, i, R, prev):
        curr = i-1
        if curr < 0:
            return R
        if prev and prev - self.a[curr] <= 5: # 5 miles constraint, skip
            return self.f_exp(curr, R, prev)
        else:
            return max( self.f_exp(  curr, R + self.r[curr] , self.a[curr]),        # take this
                        self.f_exp(  curr, R                , prev)   )             # go to the next

    # def solve_memo(self):
    #     self.memo = {}  
    #     return self.f_memo(self.N, 0, None)

    # def index(self, i, j):
    #     return i*self.N + j

    # def get_memo(self, i, j):
    #     return self.memo.get(self.index(i,j))

    # def has_memo(self, i, j):
    #     return self.get_memo(i,j) is not None
    
    # def set_memo(self, i, j, score):
    #     print("set {} {} {}".format(i,j,score))
    #     self.memo[self.index(i,j)] = score

    # def f_memo(self, i, R, prev, sol=""):
    #     curr = i-1
    #     print("curr: {:<4}, R: {:<4}, a: {:<4}, sol: {}".format(curr, R, self.a[curr], sol))
    #     if not self.has_memo(curr, R) or R > self.get_memo(curr, R):
    #         print("building memo")
    #         if curr < 0:
    #             self.set_memo(curr, R, R)
    #         elif prev and prev - self.a[curr] <= 5: # 5 miles contstraint, skip
    #             self.set_memo(curr, R, self.f_memo(curr, R, prev, sol + ' - ' + str(self.a[curr])))
    #         else:
    #             self.set_memo(curr, R, max( 
    #                 self.f_memo(  curr, R + self.r[curr] , self.a[curr], sol + ' + ' + str(self.a[curr])),
    #                 self.f_memo(  curr, R                , prev,         sol + ' - ' + str(self.a[curr]))   )  
    #             )
    #     return self.get_memo(curr, R)

    def solve_memo(self):
        memo = {}
        def opt(j):
            if j < 0:
                return 0
            if not memo.get(j):
                memo[j] = max(  self.r[j] + opt(self.next(j)),
                                opt(j-1)    )
            return memo[j]
        return opt(self.N-1)

    def next(self, j):
        for i in range(j-1, -1, -1):
            if self.a[j] - self.a[i] > 5:
                return i
        return -1

def test1():
    print("Exercise 1")
    print("1.1")
    print("---")
    a = [6, 7, 12, 14]
    r = [5, 6, 5, 1]
    M = 20
    ex = Ex1(M, a, r)

    # exp
    print("exp")
    res = ex.solve_exp()
    print( res, 10, res == 10)

    # memo
    print("memo")
    res = ex.solve_memo()
    print( res, 10, res == 10)

    print("1.2")
    print("---")
    a = [6, 7, 12, 14, 15, 20, 45, 59, 60, 61, 62, 63, 75, 81, 90, 96, 100]
    r = [5, 6, 15, 11, 10, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    M = 100
    ex = Ex1(M, a, r)

    # exp
    print("exp")
    res = ex.solve_exp()
    print( res, 126, res == 126)

    # memo
    print("memo")
    res = ex.solve_memo()
    print( res, 126, res == 126)

class Exercise2(object):
    """
    Through some friends of friends, you end up on a consulting visit to the cutting-edge biotech firm Clones ‘R’ Us (CRU). At first you’re not sure how your algorithmic background will be of any help to them, but you soon find yourself called upon to help two identical-looking software engineers tackle a perplexing problem.
    The problem they are currently working on is based on the concatenation of sequences of genetic material. If X and Y are each strings over a fixed alphabet S, then XY denotes the string obtained by concatenating them— writing X followed by Y. CRU has identified a target sequence A of genetic material, consisting of m symbols, and they want to produce a sequence that is as similar to A as possible. For this purpose, they have a library L consisting of k (shorter) sequences, each of length at most n. They can cheaply produce any sequence consisting of copies of the strings in L concatenated together (with repetitions allowed).
    Thus we say that a concatenation over L is any sequence of the form B1B2 . . . Bl, where each Bi belongs the set L. (Again, repetitions are allowed, so Bi and Bj could be the same string in L, for different values of i and j.) The problem is to find a concatenation over {Bi} for which the sequence alignment cost is as small as possible. (For the purpose of computing the sequence alignment cost, you may assume that you are given a gap cost δ and a mismatch cost αpq for each pair p, q ∈ S.)
    Give a polynomial-time algorithm for this problem.
    """
    def __init__(self):
        pass


if __name__ == '__main__':
    test1()
