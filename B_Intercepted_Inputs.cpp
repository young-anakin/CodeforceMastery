#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> arr(n);
        unordered_map<int, int> freq;

        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
            freq[arr[i]]++;
        }

        int x = n - 2;
        int a = 0, b = 0;

        for (int ind : arr) {
            double rest = static_cast<double>(x) / ind;

            // Check if rest is an integer
            if (rest == static_cast<int>(rest)) {
                int restInt = static_cast<int>(rest);

                if (freq[restInt] >= 1) {
                    if (freq[restInt] == 1) {
                        if (restInt != ind) {
                            a = restInt;
                            b = ind;
                            break;
                        }
                    } else {
                        a = restInt;
                        b = ind;
                        break;
                    }
                }
            }
        }

        cout << a << " " << b << endl;
    }

    return 0;
}
