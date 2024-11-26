from typing import List

MAXL = 10


class Text:
    def __init__(self, _ID: int, _point: int, _user: int, _tcnt: int) -> None:
        self.point = _point
        self.total_point = _point
        self.ID = _ID  # Real ID
        self.user_ID = _user
        self.tcnt = _tcnt
        self.parent = None
        self.child = None
        self.prev = None
        self.next = None


class User:
    def __init__(self, name: str, _point: int) -> None:
        self.name = name
        self.total_point = _point


user_hashmap = {}
ID_hashmap = {}
ID_list = set()
user_list = set()

tcnt = 1
ucnt = 1


def init() -> None:
    global tcnt, ucnt
    tcnt = 1
    ucnt = 1
    user_hashmap.clear()
    ID_hashmap.clear()
    ID_list.clear()
    user_list.clear()


def writeMessage(mUser: str, mID: int, mPoint: int) -> int:
    global tcnt, ucnt
    ID_hashmap[mID] = tcnt
    ukey = 0
    if mUser not in user_hashmap:
        user_hashmap[mUser] = ucnt
        ukey = ucnt
        user[ucnt] = User(mUser, mPoint)
        user_list.add(ukey)
        ucnt += 1
    else:
        ukey = user_hashmap[mUser]
        user_list.remove(ukey)
        user[ukey].total_point += mPoint
        user_list.add(ukey)

    text[tcnt] = Text(mID, mPoint, ukey, tcnt)
    ID_list.add(tcnt)
    tcnt += 1
    return user[ukey].total_point


def Mate(parent: Text, now: Text) -> None:
    if parent.child is None:
        parent.child = now
        now.parent = parent
    else:
        next_node = parent.child
        parent.child = now
        now.parent = parent
        now.next = next_node
        next_node.prev = now


def update_point(now: Text, add: int) -> None:
    while now.parent is not None:
        now = now.parent
        if now.parent is None:
            ID_list.discard(now.tcnt)
        now.total_point += add
        if now.parent is None:
            ID_list.add(now.tcnt)


def commentTo(mUser: str, mID: int, mTargetID: int, mPoint: int) -> int:
    global tcnt
    ID_hashmap[mID] = tcnt
    ukey = 0
    if mUser not in user_hashmap:
        user_hashmap[mUser] = ucnt
        ukey = ucnt
        user[ucnt] = User(mUser, mPoint)
        user_list.add(ukey)
        ucnt += 1
    else:
        ukey = user_hashmap[mUser]
        user_list.remove(ukey)
        user[ukey].total_point += mPoint
        user_list.add(ukey)

    text[tcnt] = Text(mID, mPoint, ukey, tcnt)

    parent = text[ID_hashmap[mTargetID]]
    now = text[tcnt]

    Mate(parent, now)
    update_point(now, now.point)
    tcnt += 1

    while parent.parent is not None:
        parent = parent.parent
    return parent.total_point


def dismate(parent: Text, now: Text) -> None:
    if now.prev is None:
        if now.next is not None:
            next_node = now.next
            parent.child = next_node
            next_node.prev = None
        else:
            parent.child = None
        now.parent = None
    else:
        if now.next is None:
            now.parent = None
            prev_node = now.prev
            prev_node.next = None
            now.prev = None
        else:
            prev_node = now.prev
            next_node = now.next
            now.parent = None
            prev_node.next = next_node
            next_node.prev = prev_node


def delete_score(now: Text) -> None:
    if now is None:
        return
    while True:
        user_list.remove(now.user_ID)
        user[now.user_ID].total_point -= now.point
        user_list.add(now.user_ID)
        delete_score(now.child)
        if now.next is None:
            break
        now = now.next


def erase(mID: int) -> int:
    global tcnt
    ans = 0
    IDkey = ID_hashmap[mID]

    if text[IDkey].parent is None:
        ID_hashmap[mID] = 0
        ID_list.discard(IDkey)
        now = text[IDkey]
        delete_score(now)
        return user[text[IDkey].user_ID].total_point
    else:
        ID_hashmap[mID] = 0
        parent = text[IDkey].parent
        now = text[IDkey]

        update_point(now, -now.total_point)
        dismate(parent, now)
        user_list.remove(now.user_ID)
        user[now.user_ID].total_point -= now.point
        user_list.add(now.user_ID)

        if now.child is not None:
            delete_score(now.child)
        while parent.parent is not None:
            parent = parent.parent
        return parent.total_point
    return -1


def getBestMessages(mBestMessageList: List[int]) -> None:
    j = 0
    for iter in ID_list:
        mBestMessageList[j] = text[iter].ID
        j += 1
        if j == 5:
            return


def getBestUsers(mBestUserList: List[str]) -> None:
    j = 0
    for iter in user_list:
        mBestUserList[j] = user[iter].name
        j += 1
        if j == 5:
            return
