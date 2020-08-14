import sys
input = sys.stdin.readline

# 전위 순회 (루트 - 왼쪽자식 - 오른쪽 자식)
def preorder(tree, root):
    stack = []
    stack.append(root)
    result = ''
    while stack:
        data = stack.pop()
        result += data

        # 오른쪽 자식 노드 체크
        if tree[data][1] != '.':
            stack.append(tree[data][1])

        # 왼쪽 자식 노드 체크
        if tree[data][0] != '.':
            stack.append(tree[data][0])
    return result

# 중위 순회 (왼쪽 자식 - 루트 - 오른쪽 자식)
def inorder(tree, root):
    stack = []
    result = ''
    data = root
    stack.append(root)
    while stack:
        # 왼쪽 자식 노드
        if tree[data][0] != '.' and data not in result:
            stack.append(tree[data][0])
            data = tree[data][0]
        elif stack[-1] in result:
            stack.append(tree[stack[-1][1]])

        else:
            data = stack.pop()
            result += data
            if tree[data][1] != '.':
                stack.append(tree[data][1])
                data = tree[data][1]
    return result

# 후위 순회 (왼쪽 자식 - 오른쪽 자식 - 루트)
def postorder(tree, root):
    stack = []
    result = ''
    stack.append(root)

    while stack:
        # 왼쪽 자식 체크
        if tree[stack[-1]][0] != '.' and tree[stack[-1]][0] not in result:
            stack.append(tree[stack[-1]][0])

        elif tree[stack[-1]][1] == '.' or tree[stack[-1]][1] in result:
            result += stack.pop()

        else:
            stack.append(tree[stack[-1]][1])
    return result

node = int(input())
tree = {}
root = None
for i in range(node):
    info = input().strip().split()
    tree[info[0]] = [info[1], info[2]]

print(preorder(tree, "A"))
print(inorder(tree, "A"))
print(postorder(tree, "A"))
