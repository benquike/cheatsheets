#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

void dump(set<int> &s) {
  for(set<int>::iterator it = s.begin(); it != s.end(); it++) {
    cout << *it << " ";
  }

  cout << endl;
}

int main() {

  int array1[] = {1, 2, 3, 4, 5};
  int array2[] = {1, 2, 3, 4, 5, 7};
  int array3[] = {1, 2, 3, 4, 5, 6};
  set<int> s1(array1, array1 + 5);
  set<int> s2(array2, array2 + 6);
  set<int> s3(array3, array3 + 6);

  set<int> i12;

  set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(i12, i12.begin()));

  set<int> i13;
  set_intersection(s1.begin(), s1.end(), s3.begin(), s3.end(), inserter(i13, i13.begin()));


  dump(i12);
  dump(i13);

  if (i12 == i13) {
    cout << "They are the same" << endl;
  }
  
  return 0;
}
