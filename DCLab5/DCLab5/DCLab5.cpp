// Donovan Carr
/* solve for the diagonal of a rectanguler box and which size
sphere will they fit into: 4, 6, 8, 10, 12. If the box is too big
the value is to be returned as 0, and if the user enters 0 as one of
the dimensions the program ends. Make the calculations in a separate
function from main, that also tells witch sphere the box can go into.
the returning data type needs to be a floating point number.
formula: D = square root of L^2 + W^2 + H^2 */

#include <iostream>
#include <cmath> // has the square root function
#include <iomanip> // this lets me use the setprecision function
using namespace std;

double calculateSphere(double, double, double); // I dont know if it matters if its double or float, it gives me
												// a of warnings when converting double to float even though I 
												// turned them all into doubles in the program.
int main() {
	double dfunc, leng, // dfunc is the dimension value returning from the function
		width, height;
	while (true) {
		cout << "Sort the boxes into the appropriate spheres" << endl;
		cout << "Sphere 4, Sphere 6, Sphere 8 Sphere 10, Sphere 12" << endl;
		cout << "Calculate the box size to place it into the right sphere." << endl;
		cout << "give box length: ";
		cin >> leng;
		if (leng == 0) { // it will also treat any other input other than a number as 0
			cout << "You entered a zero" << endl;
			cout << "Ending now" << endl;
			exit(EXIT_SUCCESS);
		}
		// the while loop below is suppose to start if the user input is anything other than a number
		/*	while(!(cin >> leng)){
				cout << "ERROR: Please enter a number!: ";
				cin.clear();
				cin.ignore(123, '\n');
			} */
		// in reference to comment on line 16
		// which is why this while loop will not work in this program since I will not try to make it do so.
		cout << "the length is " << leng << endl;

		cout << "give box width: ";
		cin >> width;
		if (width == 0) {
			cout << "You entered a zero" << endl;
			cout << "Ending now" << endl;
			exit(EXIT_SUCCESS);
		}
		cout << " the width is " << width << endl;

		cout << "give box height: ";
		cin >> height;
		if (height == 0) {
			cout << "You entered a zero" << endl;
			cout << "Ending now" << endl;
			exit(EXIT_SUCCESS);
		}
		cout << "the height is " << height << endl;

		calculateSphere(leng, width, height); // at first I tried to send these to the function separatly
		dfunc = calculateSphere(leng, width, height); // they are also brought back together in one line too, I learned
		cout << "The box dimension is " << setprecision(3) << dfunc << endl;
		cout << "" << endl; // this was added so it will make each instance look as a separate paragraph
		if (dfunc == 0) {
			cout << "The value is zero" << endl;
			cout << "Ending now" << endl;
			exit(EXIT_SUCCESS);
		}
	} // end of while
	return 0;
}

double calculateSphere(double lgth, double wid, double heig) { // I gave them short versions of their original names
	double diag;
	diag = sqrt(pow(lgth, 2.0) + pow(wid, 2.0) + pow(heig, 2.0)); // I learned I can call pow individualy for each
	if (diag <= 4) { // these end up printing twice do to it appearing in this function and being returned with diag value
		cout << "Sphere 4 will fit" << endl;
	}
	else {
		if (diag > 4  && diag <= 6) {
			cout << "Sphere 6 will fit" << endl;
		}
		else {
			if (diag > 6 && diag <= 8) {
				cout << "Sphere 8 will fit" << endl;
			}
			else {
				if (diag > 8 && diag <= 10) {
					cout << "Sphere 10 will fit" << endl;
				}
				else {
					if (diag > 10 && diag <= 12) {
						cout << "Sphere 12 will fit" << endl;
					}
					else {
						if (diag > 12) {
							cout << "Its too big to fit in any sphere" << endl;
							return 0; // this will also end the main loop
						}
					} // else 5
				} // else 4
			} // else 3
		} // else 2
	} // else 1
	return diag;
}