from collections import deque


class Stack:
    def __init__(self):
        self._container = []

    @property
    def is_empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


class Queue:
    def __init__(self):
        self._container = deque()

    @property
    def is_empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.popleft()

    def __repr__(self):
        return repr(self._container)


class Node:
    def __init__(self, state, parent, cost=0.0, heuristic=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def search(initial, frontier, is_goal, successors):
    node = Node(initial, None)
    frontier.push(node)
    explored = set([initial])

    while not frontier.is_empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if is_goal(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def breadth_first_serach(initial, is_goal, successors):
    """Frontier is where we've yet to go."""
    frontier = Queue()
    return search(initial, frontier, is_goal, successors)


def depth_first_search(initial, is_goal, successors):
    """Frontier is where we've yet to go."""
    frontier = Stack()
    return search(initial, frontier, is_goal, successors)


def node_to_path(node):
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
