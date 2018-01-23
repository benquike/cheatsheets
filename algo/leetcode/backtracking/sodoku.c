#include <stdio.h>

void dumpBoard(char **board) {

  for (int i = 0; i < 9; i++) {
    printf("%s\n", board[i]);
  }
  //printf("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
}

int check(char **board, int i, int j, int x){
    char c = '0' + x;
    for (int k = 0; k < 9; k++) {
        if (k != i && board[k][j] == c){
            return 0;
        }

        if (k != j && board[i][k] == c) {
            return 0;
        }
    }

    for (int u = 0; u < 3; u ++) {
        for (int v = 0; v < 3; v ++) {
          if ((i/3)*3 + u != i && (j/3)*3 + v != j && board[(i/3)*3 + u][(j/3)*3 + v] == c){
                return 0;
            }
        }
    }

    return 1;
}

int sodoku(char **board, int i, int j) {
    if (j > 8) {
        j = 0;
        i ++;
    }

    if (i > 8)
        return 1;

    printf("before: i=%d, j=%d\n", i, j);
    while (board[i][j] != '.') {
        j ++;
        if (j > 8) {
            j = 0;
            i ++;
            if (i > 8)
                return 1;
        }
    }

    printf("after: i=%d, j=%d\n", i, j);
    dumpBoard(board);
    // we find a location where it is a '.'
    for (int x = 1; x <= 9; x++) {
        board[i][j] = '0' + x;
        if (check(board, i, j, x)) {
          printf("%d is OK for position (%d, %d)\n", x, i, j);
        }
        if (check(board, i, j, x) && sodoku(board, i, j+1))
            return 1;
        board[i][j] = '.';
    }

    printf("======================================\n");
    return 0;
}

int solveSudoku(char** board, int boardRowSize, int boardColSize) {
   return sodoku(board, 0, 0);
}


int main() {
  char l0[10] = "..9748...";
  char l1[10] = "7........";
  char l2[10] = ".2.1.9...";
  char l3[10] = "..7...24.";
  char l4[10] = ".64.1.59.";
  char l5[10] = ".98...3..";
  char l6[10] = "...8.3.2.";
  char l7[10] = "........6";
  char l8[10] = "...2759..";
  char* board[] = {l0, l1, l2, l3, l4, l5, l6, l7, l8};

  int ret = solveSudoku(board, 9, 9);

  printf("ret:%d\n", ret);
  dumpBoard(board);

  return 0;
}
