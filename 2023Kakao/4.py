def solution(coin, cards):
    answer = 0
    n = len(cards)
    goal = n+1

    deck = []
    for i in cards:
        if i > n//2:
            deck.append(n-i+1)
        else:
            deck.append(i)

    # print(deck)

    get = []
    new = []

    # print('original deck: ', deck)

    for i in range(n//3):
        get.append(deck.pop(0))

    stage = 0

# game start
    while True:
        stage += 1
        if len(deck) <= 0:
            break
        new.append(deck.pop(0))
        if len(deck) > 0:
            new.append(deck.pop(0))

        # print("get: ", get)
        # print("new: ", new)
        # print("coin: ", coin)
        # print("deck: ", deck)

        chekcer = False

        for i in range(len(get)):  # get에 둘

            temp = get.pop(i)

            if temp in get:
                get.remove(temp)
                chekcer = True
                break
            else:
                get.insert(i, temp)

        if chekcer == False:
            for i in range(len(get)):  # new하나 get하나

                temp = get.pop(i)

                if temp in new and coin > 0:  # new하나 get하나
                    coin -= 1
                    new.remove(temp)
                    chekcer = True
                    break
                else:  # 없음
                    get.insert(i, temp)

        if chekcer == False:  # new에 두개 있는지 확인
            for j in range(len(new)):
                temp_2 = new.pop(j)
                if temp_2 in new and coin > 1:
                    new.remove(temp_2)
                    chekcer = True
                    coin -= 2
                    break
                else:
                    new.insert(j, temp_2)

        if chekcer == False:  # 둘다 안된경우
            break

    return stage
