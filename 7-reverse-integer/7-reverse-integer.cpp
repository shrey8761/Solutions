// Updated important online web 

// class Solution {
// public:
//     int reverse(int x) {
//         int rev = 0;
//         while (x != 0) {
//             int pop = x % 10;
//             x /= 10;
//             if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
//             if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
//             rev = rev * 10 + pop;
//         }
//         return rev;
//     }
// };

// cd 7-reverse-integer/
// to run -
// clang++-7 -pthread -std=c++17 -o 7 7-reverse-integer.cpp
// ./7
    
#include <stdio.h>
#include <limits.h>
#include <iostream>
using namespace std;

float round(float var)
{
	// we use array of chars to store number
	// as a string.
	char str[40];

	// Print in string the value of var
	// with two decimal point
	sprintf(str, "%.2f", var);

	// scan string value in var
	sscanf(str, "%f", &var);

	return var;
}

int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }

int main()
{
	float var = 37.8234;
	cout << reverse(var);
	return 0;
}


