// Donovan Carr, class COSC-1436
/*Write a program that has a jar of 40 cookies
and the user enters the number how ever many they eat and
measure how much calories they consumed. 10 cookies
is one serving and one serving is 300 calories.*/

#include <iostream>
using namespace std;

int main() {
	int Serving = 10;
	int ServingCal = 300;
	int ACookie = ServingCal / Serving; // The amount of calories in one cookie
	int Amount; // set limit if amount is over 40
	int NumOfCal;
	int bag = 40; // display how many cookies are still in bag
	int leftover;

	cout << "How many cookies would you like: "; // enter in amount and conditon if bigger than bag
	cin >> Amount;
	if (Amount > bag) {
		cout << "OWCH! YOU BIT MY HAND!\n";
		cout << "Please pick whats in the bag: ";
		cin >> Amount;
	}

	NumOfCal = Amount * ACookie; // Calculations and display
	cout << "You have eaten " << Amount << " cookies\n";
	cout << "Which is " << NumOfCal << " calories.\n";

	leftover = bag - Amount; // Shows how many remain
	if (leftover == 0)
		cout << "All out of cookies.\n";
	cout << "There are " << leftover << " cookies in the bag.\n";

	return 0;

}