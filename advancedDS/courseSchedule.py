from collections import defaultdict, deque

def can_finish(num_courses, prerequisites):

    course_graph = {course: set() for course in range(0, num_courses)}
    indegree = {node: 0 for node in course_graph}

    for course, prereq in prerequisites:
        course_graph[prereq].add(course)
        indegree[course] += 1

    # Add nodes with 0 in-degree to the queue
    queue = deque()
    for item in indegree:
        if indegree[item] == 0:
            queue.append(item)

    topo_order = []
    while queue:
        # Step 2: Remove a node from the queue
        u = queue.popleft()
        topo_order.append(u)

        # Step 3: For each neighbor, decrement indegree
        for v in course_graph[u]:
            indegree[v] -= 1
            # If indegree becomes 0, it's ready to be processed
            if indegree[v] == 0:
                queue.append(v)

    # If topo_order doesn't contain all characters, there was a cycle
    if (len(topo_order) != len(course_graph)):
        return False
    return True
# Driver code
def main():

    prereq = [
              [[1, 0], [2, 1]],
              [[1, 0], [0, 1]],
              [[1, 0], [2, 1], [3, 2], [4, 3]],
              [[1, 0], [2, 1], [3, 2], [4, 3], [0, 4]],
              [[2, 0], [2, 1], [3, 2], [4, 2], [3, 1]]
            ]
    courses = [3, 2, 10, 5, 5]
    for i in range(len(courses)):
        print((i + 1), ".\tNumber of courses: ", courses[i], sep="")
        print("\tNumber of pre-requisites: ", prereq[i])
        print("\tOutput: ", can_finish(courses[i], prereq[i]))
        print('-'*100)


if __name__ == "__main__":
    main()

