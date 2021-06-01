// Donovan Carr
/* Create a program that asks for the weight of a
package the user wants to ship then display the charges
for the shipment. */
#include <iostream>
using namespace std;

int main() {
	int weight; // I decided to give the prices their own variables
	double cheap = 1.50, afordable = 3.25, medprice = 5.15, expensive = 7.45;
	cout << "What is the weight of your package?: ";
	cin >> weight;
	if (weight <= 3) {
		cout << "your total is $"<< cheap << endl; // I need to format this one for the zero
	}
	else {
		if (weight <= 7) {
			cout << "your total is $"<< afordable << endl;
		}
		else {
			if (weight <= 12) {
				cout << "your total is $"<< medprice << endl;
			}
			else {
				if (weight > 12) {
					cout << "your total is $"<< expensive << endl;
				}
			} // else 3

		} // else 2
	} // else 1
	return 0;
} // end of main
