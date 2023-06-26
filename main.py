import graph


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    graphMg = graph.GraphManager()
    graphMg.createGraph()
    graphMg.addVertex_withName('john')
    graphMg.printGraph_NodeNames()
    graphMg.addVertex_withName('mary')
    graphMg.printGraph_NodeNames()
    john = graphMg.findNodeByName('john')
    print(john)
    print(john['name'])
    graphMg.AfollowsB('john', 'mary')
    graphMg.printGraph()
    print('\n')
    # graphMg.AfollowsB('mary', 'john')
    graphMg.printGraph()
    print(f"John's degree is: {graphMg.g.degree('john')}")


    def checkMembership(name):

        if graphMg.findNodeByName(name):
            print(f" I got it ! {graphMg.findNodeByName(name)}")
        else:
            print(f" No {name} here ")


    checkMembership('bob')
    checkMembership('susan')
    checkMembership('john')
    graphMg.modifyNodeFollowersCount('john', 456)
    print(john['followers'])
    print(john)
    mary = graphMg.findNodeByName('mary')
    print(mary)
    graphMg.printGraph()
    lay = graphMg.g.layout("kamada_kawai")

    a = graph.plot(graphMg.g, layout=lay)
    print(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
