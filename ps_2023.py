
from typing import List

MAX_L = 10
MAX_N = 50000
MAX_U = 10000


class User:
    def __init__(self, name: str):
        self.totalPoint = 0
        self.name = name


class Message:
    def __init__(self, index: int, point: int, user: User):
        self.index = index
        self.point = point
        self.totalPoint = point
        self.removed = False
        self.user = user
        self.parent = None
        self.child = []


userPool = []
userHash = {}
userPQ = []

messagePool = []
msgHash = {}
msgPQ = []


def init() -> None:
    global userPool, userHash, userPQ, messagePool, msgHash, msgPQ
    userPool = []
    userHash = {}
    userPQ = []
    messagePool = []
    msgHash = {}
    msgPQ = []


def writeMessage(mUser: str, mindex: int, mPoint: int) -> int:
    global userPool, userHash, userPQ, messagePool, msgHash, msgPQ

    if mUser not in userHash:
        user = User(mUser)
        userPool.append(user)
        userHash[mUser] = user
    else:
        user = userHash[mUser]
        userPQ.remove(user)

    user.totalPoint += mPoint
    userPQ.append(user)
    userPQ.sort(key=lambda x: (-x.totalPoint, x.name))

    msg = Message(mindex, mPoint, user)
    messagePool.append(msg)
    msgHash[mindex] = msg
    msgPQ.append(msg)
    msgPQ.sort(key=lambda x: (-x.totalPoint, x.index))

    return user.totalPoint


def commentTo(mUser: str, mindex: int, mTargetindex: int, mPoint: int) -> int:
    global userPool, userHash, userPQ, messagePool, msgHash, msgPQ

    if mUser not in userHash:
        user = User(mUser)
        userPool.append(user)
        userHash[mUser] = user
    else:
        user = userHash[mUser]
        userPQ.remove(user)

    user.totalPoint += mPoint
    userPQ.append(user)
    userPQ.sort(key=lambda x: (-x.totalPoint, x.name))

    msg = Message(mindex, mPoint, user)
    messagePool.append(msg)
    msgHash[mindex] = msg

    parent = msgHash[mTargetindex]
    msg.parent = parent
    parent.child.append(msg)

    curr = parent
    while curr:
        msgPQ.remove(curr)
        curr.totalPoint += mPoint
        msgPQ.append(curr)
        msgPQ.sort(key=lambda x: (-x.totalPoint, x.index))
        curr = curr.parent

    return parent.totalPoint


def erase(mindex: int) -> int:
    global userPool, userHash, userPQ, messagePool, msgHash, msgPQ

    msg = msgHash[mindex]
    if msg.parent:
        msg.removed = True
        user = msg.user
        userPQ.remove(user)
        user.totalPoint -= msg.point
        userPQ.append(user)
        userPQ.sort(key=lambda x: (-x.totalPoint, x.name))

        for child in msg.child:
            if not child.removed:
                child.removed = True
                user = child.user
                userPQ.remove(user)
                user.totalPoint -= child.point
                userPQ.append(user)
                userPQ.sort(key=lambda x: (-x.totalPoint, x.name))

        curr = msg.parent
        while curr:
            msgPQ.remove(curr)
            curr.totalPoint -= msg.totalPoint
            msgPQ.append(curr)
            msgPQ.sort(key=lambda x: (-x.totalPoint, x.index))
            curr = curr.parent

        return msg.parent.totalPoint
    else:
        user = msg.user
        userPQ.remove(user)
        user.totalPoint -= msg.point
        userPQ.append(user)
        userPQ.sort(key=lambda x: (-x.totalPoint, x.name))

        for child in msg.child:
            if not child.removed:
                child.removed = True
                user = child.user
                userPQ.remove(user)
                user.totalPoint -= child.point
                userPQ.append(user)
                userPQ.sort(key=lambda x: (-x.totalPoint, x.name))

                for grandchild in child.child:
                    if not grandchild.removed:
                        grandchild.removed = True
                        user = grandchild.user
                        userPQ.remove(user)
                        user.totalPoint -= grandchild.point
                        userPQ.append(user)
                        userPQ.sort(key=lambda x: (-x.totalPoint, x.name))

        msgPQ.remove(msg)
        return user.totalPoint


def getBestMessages(mBestMessageList: List[int]) -> None:
    global msgPQ
    for i in range(5):
        mBestMessageList[i] = msgPQ[i].index


def getBestUsers(mBestUserList: List[str]) -> None:
    global userPQ
    for i in range(5):
        mBestUserList[i] = userPQ[i].name
