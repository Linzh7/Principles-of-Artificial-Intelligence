def alphabeta2(self, chessborad, alpha, beta, isMax, depth=3):
    tempChess = chessborad.copy()
    alpha_beta = alpha if isMax else beta
    empty_cells = [(i, j) for i in range(3)
                   for j in range(3) if tempChess[i][j] == 0]
    if len(empty_cells) != 0:  # 有子节点
        change_i, change_j = empty_cells[0]
        for index in range(len(empty_cells)):
            i, j = empty_cells[index]
            tempChess[i][j] = 1 if isMax else 2
            if self.win(tempChess, 1 if isMax else 2):
                print(tempChess)
                if isMax:
                    score = 10000
                else:
                    score = -10000
            elif depth == 0:  # 不再向下搜索
                score = self.evaluate(tempChess)
            else:
                if isMax:
                    temp_i, temp_j, score = self.alphabeta2(
                        tempChess, alpha_beta, beta, not isMax, depth - 1)
                else:
                    temp_i, temp_j, score = self.alphabeta2(
                        tempChess, alpha, alpha_beta, not isMax, depth - 1)
            if isMax:
                if score > alpha_beta:
                    alpha_beta = score
                    change_i, change_j = i, j
                if alpha_beta >= beta:
                    break
            else:
                if score < alpha_beta:
                    alpha_beta = score
                    change_i, change_j = i, j
                if alpha_beta <= alpha:
                    break
            tempChess[i][j] = 0
        return change_i, change_j, alpha_beta
    else:  # 没有子节点，对当前节点进行评估并返回
        score = self.evaluate(tempChess)
        if isMax and score > alpha_beta:
            alpha_beta = score
        # MIN
        if not isMax and score < alpha_beta:
            alpha_beta = score
        return -1, -1, alpha_beta
# https: // blog.csdn.net/s_p_y_s/java/article/details/88391674
