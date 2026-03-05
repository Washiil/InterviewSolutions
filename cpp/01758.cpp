#include <string>
#include <algorithm>

using namespace std;

int minOperations(string s) {
    int start_zero = 0;

    for(int i = 0; i < s.length(); i++) {
        if(i % 2 == 0) {
            if(s[i] == '1') {
                start_zero++;
            }
        } else {
            if(s[i] == '0') {
                start_zero++;
            }
        }
    }

    return min(start_zero, (int)s.length() - start_zero);
}