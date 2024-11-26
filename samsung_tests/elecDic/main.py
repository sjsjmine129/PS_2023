import sys
from typing import List
from collections import defaultdict, deque
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from bisect import bisect_left, bisect_right, insort, bisect

global Wdic, Pdic, Wmaxh, Pmaxh
Wdic, Pdic, Wmaxh, Pmaxh = None, None, None, None


class Write:
    def __init__(self, usr, mid, pnt):
        self.usr = usr
        self.mid = mid
        self.pnt = pnt
        self.tot = pnt
        self.par = None
        self.childs = []
        self.dep = -1


def init() -> None:
    global Wdic, Pdic, Wmaxh, Pmaxh
    Wdic, Pdic, Wmaxh, Pmaxh = {}, defaultdict(int), [], []
    pass


def writeMessage(mUser: str, mID: int, mPoint: int) -> int:
    global Wdic, Pdic, Wmaxh, Pmaxh
    Wdic[mID] = Write(mUser, mID, mPoint)
    Wdic[mID].dep = 0
    heappush(Wmaxh, (-mPoint, mID))
    Pdic[mUser] += mPoint
    heappush(Pmaxh, (-Pdic[mUser], mUser))
    return Pdic[mUser]


def commentTo(mUser: str, mID: int, mTargetID: int, mPoint: int) -> int:
    global Wdic, Pdic, Wmaxh, Pmaxh
    chi = Wdic[mID] = Write(mUser, mID, mPoint)
    par = Wdic[mTargetID]
    chi.par = par
    par.childs.append(chi.mid)
    chi.dep = par.dep + 1
    p = chi
    Pdic[mUser] += mPoint
    heappush(Pmaxh, (-Pdic[mUser], mUser))
    while p.dep != 0:
        p.par.tot += chi.pnt
        p = p.par
    heappush(Wmaxh, (-p.tot, p.mid))
    return p.tot


def bfsRemove(sid):
    global Wdic, Pdic
    Qu = deque([sid])
    while Qu:
        mid = Qu.popleft()
        nd = Wdic[mid]
        Pdic[nd.usr] -= nd.pnt
        heappush(Pmaxh, (-Pdic[nd.usr], nd.usr))
        Wdic.pop(mid)
        for nid in nd.childs:
            Qu.append(nid)


def erase(mID: int) -> int:
    global Wdic, Pdic
    chi = Wdic[mID]
    if not chi.par:
        bfsRemove(chi.mid)
        return Pdic[chi.usr]
    par = chi.par
    p = chi
    while p.dep != 0:
        p.par.tot -= chi.tot
        p = p.par
    heappush(Wmaxh, (-p.tot, p.mid))
    par.childs.remove(chi.mid)
    bfsRemove(chi.mid)
    return p.tot


def lazyUpdateW():
    global Wdic, Wmaxh
    if not Wdic:
        Wmaxh.clear()

    while Wmaxh:
        h = Wmaxh[0]
        if h[1] in Wdic and -h[0] == Wdic[h[1]].tot:
            return
        else:
            while Wmaxh and h == Wmaxh[0]:
                heappop(Wmaxh)


def lazyUpdateP():
    global Pdic, Pmaxh
    if not Pdic:
        Pmaxh.clear()

    while Pmaxh:
        h = Pmaxh[0]
        if h[1] in Pdic and -h[0] == Pdic[h[1]]:
            return
        else:
            while Pmaxh and h == Pmaxh[0]:
                heappop(Pmaxh)


def getBestMessages(mBestMessageList: List[int]) -> None:
    global Wmaxh
    tmp = []
    for i in range(5):
        lazyUpdateW()
        tu = heappop(Wmaxh)
        mid = tu[1]
        tmp.append(tu)
        mBestMessageList[i] = mid
        while Wmaxh and Wmaxh[0][1] == mid:
            heappop(Wmaxh)
    while tmp:
        heappush(Wmaxh, tmp.pop())

    pass


def getBestUsers(mBestUserList: List[str]) -> None:
    global Pmaxh
    tmp = []
    for i in range(5):
        lazyUpdateP()
        tu = heappop(Pmaxh)
        usr = tu[1]
        tmp.append(tu)
        mBestUserList[i] = usr
        while Pmaxh and Pmaxh[0][1] == usr:
            heappop(Pmaxh)
    while tmp:
        heappush(Pmaxh, tmp.pop())
    pass


# Do not change below
CMD_INIT = 100
CMD_WRITE_MESSAGE = 200
CMD_COMMENT_TO = 300
CMD_ERASE = 400
CMD_GET_BEST_MESSAGES = 500
CMD_GET_BEST_USERS = 600


def run():
    Q = int(input())
    okay = False

    mBestUserList = [None for _ in range(5)]
    mBestMessageList = [0 for _ in range(5)]

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            init()
            okay = True
        elif cmd == CMD_WRITE_MESSAGE:
            mUser = next(input_iter)
            mID = int(next(input_iter))
            mPoint = int(next(input_iter))
            ret = writeMessage(mUser, mID, mPoint)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_COMMENT_TO:
            mUser = next(input_iter)
            mID = int(next(input_iter))
            mTargetID = int(next(input_iter))
            mPoint = int(next(input_iter))
            ret = commentTo(mUser, mID, mTargetID, mPoint)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_ERASE:
            mID = int(next(input_iter))
            ret = erase(mID)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_GET_BEST_MESSAGES:
            getBestMessages(mBestMessageList)
            for i in range(5):
                ans = int(next(input_iter))
                if mBestMessageList[i] != ans:
                    okay = False
        elif cmd == CMD_GET_BEST_USERS:
            getBestUsers(mBestUserList)
            for i in range(5):
                ans = next(input_iter)
                if mBestUserList[i] != ans:
                    okay = False
        else:
            okay = False
    return okay


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)
