C, P = map(int, input().split())
graph = list(map(int, input().split()))
block = []

shape = [
    [(0, 1), (0, 2), (0, 3)],       #ㅡ 모양
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1)],       #ㅁ 모양
    [(0, 1), (1, 0), (1, -1)],      #ㄹ 모양
    [(1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (-1, 1)],
    [(1, 0), (1, 1), (1, -1)],      #ㅗ 모양
    [(1, 0), (1, 1), (2, 0)],
    [(0, 1), (0, 2), (1, 1)],
    [(0, 1), (1, 1), (-1, 1)],
    [(0, 1), (0, 2), (-1, 2)],      #ㄱ 모양
    [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (0, 2), (1, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (1, 2)],       #ㄴ 모양
    [(0, 1), (1, 0), (2, 0)],
    [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (2, 0), (2, -1)]
]

if P == 1:
    block.append(shape[0])
    block.append(shape[1])
elif P == 2:
    block.append(shape[2])
elif P == 3:
    block.append(shape[3])
    block.append(shape[4])
elif P == 4:
    block.append(shape[5])
    block.append(shape[6])
elif P == 5:
    block.append(shape[7])
    block.append(shape[8])
    block.append(shape[9])
    block.append(shape[10])
elif P == 6:
    block.append(shape[11])
    block.append(shape[12])
    block.append(shape[13])
    block.append(shape[14])
elif P == 7:
    block.append(shape[15])
    block.append(shape[16])
    block.append(shape[17])
    block.append(shape[18])



for i in range(len(block)):
    for j in range(C):

#모든 블럭이 모든 열에 오는 경우 구하기
#모든 블럭 각 열에 어떤 행에 와야하나는
#각 열마다 위에서부터 밑으로 오면서 1이 오다가 0이 되면 continue
#0없이 1로만 된 열만 있으면 cnt 1 증가

