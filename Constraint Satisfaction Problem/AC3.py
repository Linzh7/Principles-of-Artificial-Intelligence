# 关于AC3、AC4等比较
# https://blog.csdn.net/weixin_38354912/article/details/84753763


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
