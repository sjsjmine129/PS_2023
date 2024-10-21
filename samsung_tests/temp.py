import sys
from collections import defaultdict
import heapq

def printAll():
	for i in range(partNum):
		print(i+1, "Empty:", partEmptySize)
		print(partEmptyData[i])
		print("")


def init(N):
	global partSize
	global partNum
	global midData
	# global partData
	global partEmptyData
	global partEmptySize
	global n

	n = N
	partSize = min(10000, n)
	partNum = (n-1)//partSize + 1
	midData = defaultdict(list)
	# partData = [ {} for _ in range(partNum)]
	partEmptyData = [ [[1 + i*partSize, partSize*(i+1)]] for i in range(partNum)]
	partEmptySize = [ partSize for _ in range(partNum)]


#12,000
def add(mId, mSize):
	ret = -1
	sizeLeft = mSize

	for i in range(partNum):
		if sizeLeft <= 0: # 다 기록함
			break

		if partEmptySize[i] != 0: # 이 부분에 공간 있음
			delIndex = 0
			newEmpty = [-1, -1]
			for emptyPart in partEmptyData[i]:
				if sizeLeft <= 0: break # 다 기록 하면
				if ret == -1: ret = emptyPart[0] #첫 위치 면 기록 #최적화 가능

				delIndex += 1 #이번 놈은 삭제
				#빈칸 채우기
				nowEmptySize = 	emptyPart[1] - emptyPart[0] + 1
				if nowEmptySize <= sizeLeft: #이 빈칸을 다 쓰는 경우
					heapq.heappush(midData[mId],(emptyPart[0],emptyPart[1]))
					partEmptySize[i] -= nowEmptySize
					sizeLeft -= nowEmptySize
				else: #빈칸에서 끝나는 경우
					heapq.heappush(midData[mId], (emptyPart[0],emptyPart[0]+sizeLeft-1))
					partEmptySize[i] -= sizeLeft
					newEmpty = [emptyPart[0]+sizeLeft, emptyPart[1]] #쓰고 남은 부분
					sizeLeft = 0

			#삭제할 빈칸 삭제
			partEmptyData[i] = partEmptyData[i][delIndex:]
			#새로 넣을 빈칸 추가
			if newEmpty[0] != -1:
				partEmptyData[i].insert(0, newEmpty)

	# printAll()
	print(ret)
	return ret

#7,000
def remove(mId):
	ret = 0
	mIDList = midData[mId]
	before = -1

	for fileData in mIDList: # 각 데이터 가서 갱신
		#나뉜 개수 세기
		if before + 1 != fileData[0]:
			ret += 1
		before = fileData[1]

		partIndex = (fileData[0]-1)//partSize #어느 파트 인지 확인
		partEmptySize[partIndex] += fileData[1] - fileData[0] + 1 # 빈칸 늘리기

		# 빈칸 정보들 갱신하기
		nowPart = partEmptyData[partIndex]
		insertIndex = 0

		for i in range(len(nowPart)):
			emptyPart = nowPart[i]
			if emptyPart[1] < fileData[0]:
				insertIndex == i + 1
			else:
				break

		nowPart.insert(insertIndex, [fileData[0], fileData[1]])

		#앞뒤 확인해서 붙이기
		if insertIndex != 0:
			before = nowPart[insertIndex-1]
			if before[1]+1 == nowPart[insertIndex][0]: #앞이랑 붙어 있음
				temp = nowPart[insertIndex]
				nowPart.pop(insertIndex)
				nowPart[insertIndex-1][1] = temp[1]
				insertIndex -= 1
		if insertIndex != len(nowPart)-1:
			after = nowPart[insertIndex+1]
			if after[0] == nowPart[insertIndex][1] + 1: #뒤랑 붙어 있음
				temp = nowPart[insertIndex]
				nowPart.pop(insertIndex)
				nowPart[insertIndex][0] = temp[0]

	del midData[mId]

	# printAll()
	print(ret)
	return ret

#1,000
def count(mStart, mEnd):
	return 0

##########################################################################################

CMD_INIT = 1
CMD_ADD = 2
CMD_REMOVE = 3
CMD_COUNT = 4

def run():
	q = int(input())
	okay = False

	for i in range(q):
		inputarray = input().split()
		cmd = int(inputarray[0])

		if cmd == CMD_INIT:
			n = int(inputarray[1])
			init(n)
			okay = True
		elif cmd == CMD_ADD:
			mid = int(inputarray[1])
			msize = int(inputarray[2])
			ans = int(inputarray[3])
			ret = add(mid, msize)
			if ans != ret:
				okay = False
		elif cmd == CMD_REMOVE:
			mid = int(inputarray[1])
			ans = int(inputarray[2])
			ret = remove(mid)
			if ans != ret:
				okay = False
		elif cmd == CMD_COUNT:
			mstart = int(inputarray[1])
			mend = int(inputarray[2])
			ans = int(inputarray[3])
			ret = count(mstart, mend)
			if ans != ret:
				okay = False
		else:
			okay = False

	return okay


if __name__ == '__main__':
	sys.stdin = open('sample_input.txt', 'r')
	inputarray = input().split()
	TC = int(inputarray[0])
	MARK = int(inputarray[1])

	for testcase in range(1, TC + 1):
		score = MARK if run() else 0
		print("#%d %d" % (testcase, score), flush = True)
