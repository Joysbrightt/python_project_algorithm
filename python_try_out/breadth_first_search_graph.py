from collections import deque

# Graphs are made up of nodes and edges. A node
# can be directly connected to many other nodes. Those nodes are called
# its neighbors.

# todo to implement graph queue DSA will be used

graph = {}
graph["you"] = ["bob", "ade", "shade"]

search_deque = deque()
search_deque += graph["you"]


def person_is_seller(name):
    return name[-1] == 'a'


while search_deque:
    person = search_deque.popleft()
    if person_is_seller(person):
        print(person + " is a mango seller")


def search(name):
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + "is a mango seller")
                return True
            else:
                search_deque += graph[person]
                searched.append(person)
    return False



search("you")
