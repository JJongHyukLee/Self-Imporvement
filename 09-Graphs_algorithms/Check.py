size = 5
graph = [[] for _ in range(size)] # 2중 리스트 선언

for _ in range(size):
    graph.append(list(str(input())))

'''


graph1 = copy.deepcopy(graph)
graph2 = copy.deepcopy(graph)

depth_fist_search(graph1,6,0)
'''
print(graph)