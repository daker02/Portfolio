class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree():
    def __init__(self): #트리 생성
        self.root = None

    def preorder(self, n):
        if n !=None:
            print(n.data,' ',end='') #노드방문
            if n.left:
                self.preorder(n.left) #왼쪽 서브트리 순회
            if n.right:
                self.preorder(n.right) #오른쪽 서브트리 순회
    
    def inorder(self, n):
        if n !=None:
            if n.left:
                self.preorder(n.left) #왼쪽 서브트리 순회
            print(n.data,' ',end='') #노드방문
            if n.right:
                self.preorder(n.right) #오른쪽 서브트리 순회

    def postorder(self, n):
        if n !=None:
            if n.left:
                self.preorder(n.left) #왼쪽 서브트리 순회
            if n.right:
                self.preorder(n.right) #오른쪽 서브트리 순회
            print(n.data,' ',end='') #노드방문

    def levelorder(self, root):
        q = [] #리스트 구현(큐로 사용하기 위해)
        q.append(root)
        while q:
            t = q.pop(0)
            print(t.data,' ',end='') #큐에서 첫 항목을 삭제하고 삭제한 노드 방문
            if t.left != None:
                q.append(t.left) #왼쪽 자식 큐에 삽입
            if t.right != None:
                q.append(t.right) #오른쪽 자식 큐에 삽입

    def height(self, root):
        if root == None:
            return 0
        # 루트 노드를 기준으로 두 자식노드의 높이 중 큰 높이
        return max(self.height(root.left), self.height(root.right)) + 1

tree = BinaryTree()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)
n9 = Node(90)
n10 = Node(100)
n11 = Node(110)
n12 = Node(120)
n13 = Node(130)



tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
n4.right = n9
n5.left = n10
n5.right = n11
n6.left = n12
n6.right = n13

print("트리 높이: ", tree.height(tree.root))

# 출력 -> 전위순회 : 10  20  40  80  90  50  100  110  30  60  120  130  70
print("전위순회 : ", end='')
tree.preorder(tree.root)

# 출력 -> 중위순회 : 20  40  80  90  50  100  110  10  30  60  120  130  70
print("\n중위순회 : ", end='')
tree.inorder(tree.root)

# 출력 -> 후위순회 : 20  40  80  90  50  100  110  30  60  120  130  70  10
print("\n후위순회 : ", end='')
tree.postorder(tree.root)