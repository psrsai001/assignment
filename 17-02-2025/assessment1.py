# check if there is a path between 2 nodes in a graph
from graph import Graph
from ll import LinkedList
from ll import Node as LLNode


def graph_problems():
    def dfs_find(node1: int, node2: int, adj_list: dict[int, list[int]]):

        nodes = adj_list.keys()
        visited = {}
        if node1 not in nodes or node2 not in nodes:
            print("node doesnt exists. please give a valid nodes")
            return

        stk = [node1]
        visited[node1] = True
        while stk:
            node = stk.pop()
            if node == node2:
                print(f"there is a valid path betweeen {node1} and {node2}")
                return
            else:
                for adj_node in adj_list[node]:
                    if adj_node not in visited:
                        visited[adj_node] = True
                        stk.append(adj_node)
        print(f"there is no valid path betweeen {node1} and {node2}")

    def nodes_in_range(start_node: int, max_dist: int, adj_list: dict[int, list[int]]):
        nodes = adj_list.keys()
        if start_node not in nodes:
            print("node is not found in the graph")
            return
        visited = {}
        ans = []
        q = [(start_node, 0)]
        visited[start_node] = True
        while q:
            node, temp_dist = q.pop(0)
            if temp_dist <= max_dist:
                ans.append(node)
                for adj_node in adj_list[node]:
                    if adj_node not in visited and temp_dist + 1 <= max_dist:
                        visited[adj_node] = True
                        q.append((adj_node, temp_dist + 1))
        print("nodes:", " ".join(map(str, ans)))

    g = Graph()
    r"""
     1--4--6
    / \
    2--3 5--7
    """
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)
    g.add_vertex(6)
    g.add_vertex(7)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(4, 6)
    g.add_edge(5, 7)
    dfs_find(4, 3, g.adj_list)
    dfs_find(4, 5, g.adj_list)
    nodes_in_range(1, 2, g.adj_list)


def ll_problems():
    ll = LinkedList()
    ll.insert_end(1)
    ll.insert_end(2)
    ll.insert_end(3)
    ll.insert_end(4)
    ll.insert_end(5)
    ll.insert_end(6)
    """
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    """
    print(ll)
    ll.reverse()
    print(ll)

    # detect loop
    def detect_loop(head: LLNode | None):
        if not head:
            print("LL is empty")

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            if slow:
                slow = slow.next
            if slow and fast and slow.data == fast.data:
                print("Loop detected in the LL")
                return
        print("loop not detected.")

    head = LLNode(1)
    head.next = second = LLNode(2)
    second.next = third = LLNode(3)
    third.next = fourth = LLNode(4)
    fourth.next = fifth = LLNode(5)
    fifth.next = third

    detect_loop(head)
    detect_loop(ll.head)
    """
    1 -> 2 -> 3 -> 4 -> 5 ->
              ^             |
              |_____________|
    """


def sorting_problems():

    def bubble_sort(arr):
        n = len(arr)
        print("before bubble sort:", arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print("bubble sort: ", arr)

    def selection_sort(arr):
        print("before selection sort:", arr)
        n = len(arr)
        for i in range(n - 1):
            min_ind = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_ind]:
                    min_ind = j
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
        print("after selection sort:", arr)

    arr = [1, 4, 3, 2, 9, 7, 5, 1]
    bubble_sort(arr)
    arr = [1, 4, 3, 2, 9, 7, 5, 1]
    selection_sort(arr)


def searching_problems():
    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) >> 1
            if arr[mid] == target:
                print(f"{target} found at index: {mid}")
                return
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        print(f"{target} not found.")

    def left_occurance(arr, target):
        low = 0
        high = len(arr) - 1
        l = -1
        while low <= high:
            mid = (low + high) >> 1
            if arr[mid] == target:
                l = mid
                high = mid - 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if l != -1:
            print(f"last occurance of {target} is at {l}")
        else:
            print(f"{target} not found.")

    def right_occurance(arr, target):
        low = 0
        high = len(arr) - 1
        r = -1
        while low <= high:
            mid = (low + high) >> 1
            if arr[mid] == target:
                r = mid
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if r != -1:
            print(f"last occurance of {target} is at {r}")
        else:
            print(f"{target} not found.")

    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7]
    binary_search(arr, 3)
    left_occurance(arr, 3)
    right_occurance(arr, 3)


# graph_problems()
# ll_problems()
# sorting_problems()
# searching_problems()
