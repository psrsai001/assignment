from graph import Graph
from ll_node import LinkedList
from q import Queue, QueueLL
from stk import Stack
from tree import TreeNode


def missing_num():
    arr = [1, 3, 4, 5, 6, 7]
    n = 7
    sn = n * (n + 1) // 2
    sa = sum(arr)
    print("missing number:", sn - sa)


def first_non_repeating_char():
    st = "hello world"
    memo = {}
    for i in st:
        if i not in memo:
            memo[i] = 1
        else:
            memo[i] += 1
    for k, v in memo.items():
        if v == 1:
            print(f"{k} is the first non repeating char")
            return


def linkedlists():
    ll = LinkedList()
    ll.insert_end(2)
    print(ll)

    ll.insert_begining(1)
    print(ll)

    ll.insert_end(3)
    print(ll)

    ll.insert_end(4)
    print(ll)

    ll.insert_end(5)
    print(ll)

    ll.insert_end(6)
    print(ll)

    ll.delete_val(6)
    print(ll)

    ll.insert_end(6)
    print(ll)

    ll.delete_val(7)
    print(ll)

    ll.delete_val(1)
    print(ll)

    ll.delete_val(5)
    print(ll)

    ll.reverse()
    print(ll)


def queue():
    q = Queue()
    q.dequeue()
    q.enqueue(2)
    q.enqueue(1)
    print(q)
    q.dequeue()
    print(q)
    print("size:", q.size())


def stack():
    stack = Stack()
    print(stack.pop())
    stack.push(1)
    stack.push(2)
    print("popped:", stack.pop())
    print("size:", stack.size())


def queueLL():
    q = QueueLL()
    q.dequeue()
    q.enqueue(2)
    q.enqueue(1)
    print(q)
    q.dequeue()
    print(q)
    print("size:", q.size())


def balanced_paranthesis():
    stk = []
    open = {"{": "}", "(": ")", "[": "]"}
    close = {"}": "{", ")": "(", "]": "["}
    st = "[[(({{}}))]]"

    for i in st:
        if i in open:
            stk.append(i)
        elif i in close:
            try:
                popped = stk.pop()
                if popped in open and open[popped] == i:
                    continue
                else:
                    raise IndexError
            except IndexError:
                print("not balanced")
                return

        else:
            print("invalid braces")
            return
    if len(stk):
        print("not balanced")
    else:
        print("balanced")


def height_of_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    if not root:
        print("Height = 0")
    height = 0
    q = [(root, 1)]
    while q:
        r = q.pop(0)
        if r[0].left:
            q.append((r[0].left, r[1] + 1))
            height = max(height, r[1] + 1)
        if r[0].right:
            q.append((r[0].right, r[1] + 1))
            height = max(height, r[1] + 1)
    print("Height =", height)


def graph():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")
    print(g)


# missing_num()
# first_non_repeating_char()
# linkedlists()
# queue()
# stack()
# queueLL()
# balanced_paranthesis()
graph()
