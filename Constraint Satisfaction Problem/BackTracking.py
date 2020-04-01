def backTrack(assignment, csp, domain, method):
    # assignment的定义:dict index=color
    # backTrack:通过递归，对assignment做尝试赋值并AC-3检查，保存副本（浪费空间，但是作为练习够用），失败则回复副本.
    # domain:当前domain assignment:当前赋值位置 csp:问题描述(static)
    # method:选择下一个变量采用的方法
    if len(assignment) == len(csp):
        return assignment
    backupdomain = list.copy(domain)
    index = nextVariableIndex(csp, domain, assignment, method)
    for val in valueOrder(index, assignment, csp, domain):
        assignment[index] = val
        domain[index] = [val]
        if AC3(csp, domain):
            result = backTrack(assignment, csp, domain, method)
            if result:
                return result
        # 运行到这里说明此路不通,回复状态,删掉val=value from domain
        domain = backupdomain
        domain[index].remove(val)
        del assignment[index]
    # 运行到这里说明全都不行
    return False


def nextVariableIndex(csp, domain, assignment, method):
    # 这里实现两种方式，MRV与自然序
    if method == 'natural':
        for x in range(len(domain)):
            if assignment.get(x) == None:
                return x
    if method == 'MRV':
        # MRV:find the variable that has the smallest domain
        size = float('inf')
        for index, unit in zip(range(len(domain)), domain):
            if len(unit) < size and assignment.get(index) == None:
                mrv = index
                size = len(unit)
        return mrv


def valueOrder(index, assignment, csp, domain):
    # 自然序
    return domain[index][0]


def AC3(csp, domain):
    # revise for 2-consistent
    # input: csp-the csp matrix domain-the current domain list
    # output:the revised domain list or failure if there is no solution
    queue = []
    # init the queue
    queue = [[rowindex, columnindex] for rowindex, row in zip(range(
        15), csp) for columnindex, column in zip(range(15), row) if column == 1 and rowindex != columnindex]
    # loop
    while(len(queue) != 0):
        constraint = queue.pop()
        # 一次梳理一对
        for c in range(2):
            if c == 1:
                constraint = [constraint[1], constraint[0]]
            if revise(domain, constraint):
                if len(domain[constraint[0]]) == 0:
                    return False
                # 因为是三角形矩阵，所以在找i的邻接的时候要判断一下i
                # 添加邻接
                # 不要相等的情况
                for everyone in range(15):
                    if everyone < constraint[0]:
                        if csp[constraint[0]][everyone] == 1:
                            queue.append([everyone, constraint[0]])
                    elif everyone > constraint[0]:
                        if csp[everyone][constraint[0]] == 1:
                            queue.append([everyone, constraint[0]])
    return True


def revise(domain, constraint):
    # for every item in x there should be a satisfied one in y
    # specified for this, there should be at least 2 items in y or delete all x that is the same from y[0]
    x = domain[constraint[0]]
    y = domain[constraint[1]]
    flag = False
    if len(y) >= 2:
        return False
    # y cannot be 0.
    for o in x:
        if o == y[0]:
            x.remove(o)
            flag = True
    return flag

# https://blog.csdn.net/tianhan4/java/article/details/19991899
