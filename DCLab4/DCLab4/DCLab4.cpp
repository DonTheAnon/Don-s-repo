// Donovan Carr
/* Write program displaying a table of celsius tempertures
 converted to fahrenheit from 0 to 20. Use a loop to display
 the info; the formulat to convert celsius to fahrenheit:
  f = (9/5)c + 32 */

#include <iostream>
using namespace std;

int main() {
	int min = 0, max = 20;
	double cel; // it gave me a warning because I tried defining cel as int
				// then did the math with a double leading to arithmatic overflow.
	cout << "Celsius \t Fahrenheit" << endl;
	cout << "###########################" << endl;

	for (cel = min; cel <= max; cel++) {
		double fah;
		fah = (cel * 9/5) + 32; // I also got errors with the formula because I did not make it a double
		cout << cel <<"\t\t"<<fah << endl; // (9/5 * cel) will give the wrong answer, (celsius * 9/5) + 32 is right
	}
	return 0;
}