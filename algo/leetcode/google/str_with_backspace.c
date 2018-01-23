#include <stdio.h>

int clean(char *str, int len) {
  int i = 0;
  int j = 0;

  while (j < len) {
    if (str[j] >= 'a' && str[j] <= 'z') {
      str[i++] = str[j];
    } else if (str[j] == 'B') {
      // TODO
      if (i > 0) {
        i--;
      } else {
        // unexpected
      }

    } else if (str[j] == 0) {
      // end of string
      break;
    } else {
      // unexpected input
    }

    j ++;
  }

  str[i] = 0;

  return i;
}

int same(char *str1, int len1, char *str2, int len2) {
  
}

int main() {

  char str1[10] = "a";
  int x = clean(str1, 10);
  printf("%s\n", str1);

  char str2[10] = "aB";
  int x2 = clean(str2, 10);
  printf("%s\n", str2);



  char str3[10] = "aaaBaBaB";
  int x3 = clean(str3, 10);
  printf("%s\n", str3);

  return 0;
}
