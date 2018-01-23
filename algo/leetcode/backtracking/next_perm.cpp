#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void dump(vector<int> &x) {
  for (int i = 0; i < x.size(); i ++)
    cout << x[i] << ' ';
  cout << endl;
}

int main() {
  int a[] = {1,2,3,4};
  vector<int> v(a, a + sizeof(a)/sizeof(a[0]));

  dump(v);
  next_permutation(v.begin(), v.end());
  dump(v);
  return 0;
}
