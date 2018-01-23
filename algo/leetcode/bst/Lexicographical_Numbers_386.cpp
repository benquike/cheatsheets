#include <iostream>
#include <string> 
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> lexicalOrder(int n) {
      vector<int> ret;

      if (n == 0)
	return ret;

      map<string, int> m;
      for (int i = 1; i <= n; i++) {
	m.insert(pair<string, int>(to_string(i), i));
      }

      for (auto it = m.begin(); it != m.end(); it ++) {
	ret.push_back(it->second);
      }


      return ret;
    }
};


int main() {
  // map<string, int> m;

  // for (int i = 1; i <= 20; i++) {
  //   m.insert(pair<string, int>(to_string(i), i));
  // }

  // for (auto it = m.begin(); it != m.end(); it++) {
  //   cout << it->second << endl;
  // }


  Solution s;

  vector<int> v = s.lexicalOrder(0);

  cout << "========== 0 ===========" << endl;
  for (auto i : v) {
    cout << i << endl;
  }

  v = s.lexicalOrder(20);


  cout << "========== 0 ===========" << endl;
  for (auto i : v) {
    cout << i << endl;
  }


  return 0;
}
