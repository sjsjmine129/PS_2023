import sys
MAXL = 10
MAX_USER = 50007
MAX_X = 10007


class User:
    def __init__(self):
        self.point = 0
        self.uname = ""


class Message:
    def __init__(self):
        self.message_id = 0  # Renamed from 'id'
        self.point = 0
        self.user_id = 0  # Renamed from 'userid'
        self.parent = -1
        self.isdel = False


# Initialize variables
usr = [User() for _ in range(MAX_USER)]
msg = [Message() for _ in range(MAX_USER)]
setUser = set()  # For storing user ids, sorted by points and names
setMsg = set()  # For storing message ids, sorted by points
umap = {}  # Map for username to user id
mmap = {}  # Map for message id to message index
v = [[] for _ in range(MAX_USER)]  # Stores replies to messages
modifyUser = [0] * MAX_X
len_modifyUser = 0
user_counter = 1  # Renamed from 'uid'
message_counter = 1  # Renamed from 'mid'


def init() -> None:
    global user_counter, message_counter, setUser, setMsg, umap, mmap
    user_counter = 1
    message_counter = 1
    setUser.clear()
    setMsg.clear()
    umap.clear()
    mmap.clear()


def update_usr(uname: str, point: int) -> int:
    global user_counter
    if uname not in umap:
        umap[uname] = user_counter
        usr[user_counter].uname = uname
        usr[user_counter].point = 0
        user_counter += 1

    user_id = umap[uname]
    setUser.discard(user_id)
    usr[user_id].point += point
    setUser.add(user_id)
    return user_id


def find_parent(p: int) -> int:
    while msg[p].parent != -1:
        p = msg[p].parent
    return p


def writeMessage(mUser: str, mID: int, mPoint: int) -> int:
    global message_counter
    user_id = update_usr(mUser, mPoint)

    mmap[mID] = message_counter
    msg[message_counter].message_id = mID  # Renamed from 'id'
    msg[message_counter].parent = -1
    msg[message_counter].point = mPoint
    msg[message_counter].user_id = user_id  # Renamed from 'userid'
    msg[message_counter].isdel = False

    v[message_counter].clear()
    setMsg.add(message_counter)
    message_counter += 1
    return usr[user_id].point


def commentTo(mUser: str, mID: int, mTargetID: int, mPoint: int) -> int:
    global message_counter
    user_id = update_usr(mUser, mPoint)
    target_message_id = mmap[mTargetID]

    parent_message_id = find_parent(target_message_id)
    mmap[mID] = message_counter
    msg[message_counter].message_id = mID  # Renamed from 'id'
    msg[message_counter].parent = target_message_id
    msg[message_counter].point = mPoint
    msg[message_counter].user_id = user_id  # Renamed from 'userid'
    msg[message_counter].isdel = False

    v[message_counter].clear()
    v[target_message_id].append(message_counter)

    setMsg.discard(parent_message_id)
    msg[parent_message_id].point += mPoint
    setMsg.add(parent_message_id)

    message_counter += 1
    return msg[parent_message_id].point


def sub_erase(cur: int, p: int) -> None:
    global len_modifyUser
    for it in v[cur]:
        if not msg[it].isdel:
            setUser.discard(msg[it].user_id)  # Renamed from 'userid'
            msg[p].point -= msg[it].point
            usr[msg[it].user_id].point -= msg[it].point  # Renamed from 'userid'
            # Renamed from 'userid'
            modifyUser[len_modifyUser] = msg[it].user_id
            len_modifyUser += 1
            sub_erase(it, p)
            msg[it].isdel = True


def erase(mID: int) -> int:
    global len_modifyUser, message_counter
    len_modifyUser = 0
    msg_id = mmap[mID]
    parent_message_id = find_parent(msg_id)
    setMsg.discard(parent_message_id)

    sub_erase(msg_id, parent_message_id)
    user_id = msg[msg_id].user_id  # Renamed from 'userid'
    setUser.discard(user_id)
    usr[user_id].point -= msg[msg_id].point
    modifyUser[len_modifyUser] = user_id  # Renamed from 'userid'
    len_modifyUser += 1

    for i in range(len_modifyUser):
        setUser.add(modifyUser[i])

    if msg[msg_id].parent == -1:
        return usr[user_id].point
    else:
        msg[parent_message_id].point -= msg[msg_id].point
        setMsg.add(parent_message_id)
        msg[msg_id].isdel = True
        return msg[parent_message_id].point


def getBestMessages(mBestMessageList) -> None:
    inx = 0
    # Renamed from 'id'
    for msg_id in sorted(setMsg, key=lambda id: (-msg[id].point, msg[id].message_id)):
        if inx >= 5:
            break
        mBestMessageList[inx] = msg[msg_id].message_id  # Renamed from 'id'
        inx += 1


def getBestUsers(mBestUserList) -> None:
    inx = 0
    for user_id in sorted(setUser, key=lambda id: (-usr[id].point, usr[id].uname)):
        if inx >= 5:
            break
        mBestUserList[inx] = usr[user_id].uname
        inx += 1


# ===== Do not change the code below ==========
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
