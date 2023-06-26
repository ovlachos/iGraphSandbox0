from igraph import *


class GraphManager:
    def __init__(self):
        self.g = None

    def createGraph(self):
        self.g = Graph(directed=True)

    def printGraph(self):
        try:
            print(f" Graph g: {self.g}")
        except Exception as e:
            print(f" No such Attribute")

    def printGraph_NodeNames(self):
        try:
            print(f" Graph g: {self.g.vs['name']}")
        except Exception as e:
            print(f" No such Attribute")

    def addVertex_withName(self, name):
        if not self.g == None:
            if not self.findNodeByName(name):
                self.g.add_vertices(1)
                latestNodeIndex = len(self.g.vs) - 1
                latestNodeObj = self.g.vs[latestNodeIndex]
                latestNodeObj['name'] = name

    def modifyNodeFollowersCount(self, name, count):
        node = self.findNodeByName(name)
        if node:
            node['followers'] = count

    def modifyNodeFollowingCount(self, name, count):
        node = self.findNodeByName(name)
        if node:
            node['followers'] = count

    def findNodeByName(self, name):
        try:
            return self.g.vs.find(name=name)
        except:
            return None

    def AfollowsB(self, a, b):
        if not self.g == None:
            self.addEdgeBetweenAandB_ByName(a, b, 'follow')

    def addEdgeBetweenAandB_ByName(self, a, b, edgeType):
        if self.g != None:
            node_a = self.findNodeByName(a)
            node_b = self.findNodeByName(b)
            self.g.add_edges([(node_a.index, node_b.index)])
            latestEdgeIndex = len(self.g.es) - 1
            latestEdgeObj = self.g.vs[latestEdgeIndex]
            latestEdgeObj['follow'] = True
