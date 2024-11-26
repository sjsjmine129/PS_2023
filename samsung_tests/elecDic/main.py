import sys
from typing import List
from collections import defaultdict, deque
from heapq import heappush, heappop

global message_dict
global user_points
global message_heap
global user_heap
message_dict = None
user_points = None
message_heap = None
user_heap = None


def init() -> None:
    global message_dict, user_points, message_heap, user_heap
    message_dict = {}
    user_points = defaultdict(int)
    message_heap = []
    user_heap = []


def writeMessage(user: str, message_id: int, points: int) -> int:
    global message_dict, user_points, message_heap, user_heap
    # [user, message_id, points, total_points, parent, children, depth]
    new_message = [user, message_id, points, points, None, [], 0]
    message_dict[message_id] = new_message

    heappush(message_heap, (-points, message_id))
    user_points[user] += points
    heappush(user_heap, (-user_points[user], user))

    return user_points[user]


def commentTo(user: str, message_id: int, target_message_id: int, points: int) -> int:
    global message_dict, user_points, message_heap, user_heap
    parent_message = message_dict[target_message_id]
    # [user, message_id, points, total_points, parent, children, depth]
    new_message = [user, message_id, points, points,
                   parent_message, [], parent_message[6] + 1]
    parent_message[5].append(message_id)  # Add to parent's children
    message_dict[message_id] = new_message

    user_points[user] += points
    heappush(user_heap, (-user_points[user], user))

    # Update total points up the chain
    current_message = new_message
    while current_message[4]:
        current_message[4][3] += points  # Update parent's total points
        current_message = current_message[4]

    heappush(message_heap, (-current_message[3], current_message[1]))
    return current_message[3]


def erase(message_id: int) -> int:
    global message_dict, user_points, message_heap
    message_to_erase = message_dict[message_id]
    if not message_to_erase[4]:  # No parent means it's a root message
        queue = deque([message_id])
        while queue:
            mid = queue.popleft()
            message = message_dict[mid]
            user_points[message[0]] -= message[2]  # Subtract points
            heappush(user_heap, (-user_points[message[0]], message[0]))
            del message_dict[mid]
            queue.extend(message[5])  # Add children to the queue
        return user_points[message_to_erase[0]]

    parent_message = message_to_erase[4]
    current_message = message_to_erase
    while current_message[4]:
        # Subtract total points from parent
        current_message[4][3] -= message_to_erase[3]
        current_message = current_message[4]

    heappush(message_heap, (-current_message[3], current_message[1]))
    parent_message[5].remove(message_id)  # Remove from parent's children
    queue = deque([message_id])
    while queue:
        mid = queue.popleft()
        message = message_dict[mid]
        user_points[message[0]] -= message[2]  # Subtract points
        heappush(user_heap, (-user_points[message[0]], message[0]))
        del message_dict[mid]
        queue.extend(message[5])  # Add children to the queue
    return current_message[3]


def getBestMessages(best_message_list: List[int]) -> None:
    global message_heap
    temp_heap = []
    for i in range(5):
        while message_heap:
            points, message_id = message_heap[0]
            if message_id in message_dict and -points == message_dict[message_id][3]:
                break
            heappop(message_heap)
        points, message_id = heappop(message_heap)
        best_message_list[i] = message_id
        temp_heap.append((points, message_id))
        while message_heap and message_heap[0][1] == message_id:
            heappop(message_heap)
    for entry in temp_heap:
        heappush(message_heap, entry)


def getBestUsers(best_user_list: List[str]) -> None:
    global user_heap
    temp_heap = []
    for i in range(5):
        while user_heap:
            points, user = user_heap[0]
            if user in user_points and -points == user_points[user]:
                break
            heappop(user_heap)
        points, user = heappop(user_heap)
        best_user_list[i] = user
        temp_heap.append((points, user))
        while user_heap and user_heap[0][1] == user:
            heappop(user_heap)
    for entry in temp_heap:
        heappush(user_heap, entry)


# Do not change below
CMD_INIT = 100
CMD_WRITE_MESSAGE = 200
CMD_COMMENT_TO = 300
CMD_ERASE = 400
CMD_GET_BEST_MESSAGES = 500
CMD_GET_BEST_USERS = 600


def run():
    Q = int(input())
    success = False

    best_user_list = [None for _ in range(5)]
    best_message_list = [0 for _ in range(5)]

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            init()
            success = True
        elif cmd == CMD_WRITE_MESSAGE:
            user = next(input_iter)
            message_id = int(next(input_iter))
            points = int(next(input_iter))
            result = writeMessage(user, message_id, points)
            expected_result = int(next(input_iter))
            if result != expected_result:
                success = False
        elif cmd == CMD_COMMENT_TO:
            user = next(input_iter)
            message_id = int(next(input_iter))
            target_message_id = int(next(input_iter))
            points = int(next(input_iter))
            result = commentTo(user, message_id, target_message_id, points)
            expected_result = int(next(input_iter))
            if result != expected_result:
                success = False
        elif cmd == CMD_ERASE:
            message_id = int(next(input_iter))
            result = erase(message_id)
            expected_result = int(next(input_iter))
            if result != expected_result:
                success = False
        elif cmd == CMD_GET_BEST_MESSAGES:
            getBestMessages(best_message_list)
            for i in range(5):
                expected_result = int(next(input_iter))
                if best_message_list[i] != expected_result:
                    success = False
        elif cmd == CMD_GET_BEST_USERS:
            getBestUsers(best_user_list)
            for i in range(5):
                expected_result = next(input_iter)
                if best_user_list[i] != expected_result:
                    success = False
        else:
            success = False
    return success


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)
