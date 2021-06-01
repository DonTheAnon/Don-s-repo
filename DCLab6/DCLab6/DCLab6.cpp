// Donovan Carr
#include <iostream>
#include <string>
using namespace std;

double calcRainFall(const double[], int);
double lowestRainFall(const double[], int);
double highestRainFall(const double[], int);
string getLowMonth(string[], const double[], int); // I need three peramaters for these two fuctions to work
string getHighestMonth(string[], const double[], int);

int main() {
	const int year = 12; // learned you cant declare const double for an array
	double month[year], average, total, min = 0, max;
	string lowMonth, highMonth,
		month_name[year] = { "January", "February", "March","April", "May", "June",
		 "July", "August", "September", "October", "November", "December"};
	int count;

	calcRainFall(month, year);
	lowestRainFall(month, year);
	highestRainFall(month, year);
	getLowMonth(month_name, month, year);
	getHighestMonth(month_name, month, year);

	for (count = 0; count < year; count++) {
		cout << "enter amount of rain fall for each month " << (count + 1) << ": ";
		cin >> month[count];
		while (month[count] < 0) { // need to keep it from crashing if I enter a negative value backwords (1-)
			cout << "Error: Please enter in a number greater than 0: ";
			cin >> month[count];
		}
	}

	cout << "Here is the rain fall for each month: " << endl;
	for (count = 0; count < year; count++)
		cout << month_name[count]<< ": " << month[count] << endl;

	cout << endl;
	total = calcRainFall(month, year);
	cout << "The total rain fall this year is " << total << endl;
	average = total / year; // I decided to get the average in the main instead of giving it its own function
	cout << "The average rain fall this year is " << average << endl;

	min = lowestRainFall(month, year);
	lowMonth = getLowMonth(month_name, month, year);
	max = highestRainFall(month, year);
	highMonth = getHighestMonth(month_name, month, year);

	cout << "The highest is: " << highMonth << ": " << max << endl;
	cout << "The lowest is: " << lowMonth << ": " << min << endl;
	return 0;
}

double calcRainFall(const double sum[], int level) { // I almost left out the const, the program would not start
	double total = 0, aveg = 0;
	int count;
	for (count = 0; count < level; count++) { // to get the total
		total += sum[count];
	}
	return total;
}

double lowestRainFall(const double low[], int level) {
	double lowest;
	int count;
	lowest = low[0];

	for (count = 0; count < level; count++) {
		if (low[count] < lowest)
			lowest = low[count];
	}
	return lowest;
}

 string getLowMonth(string mon[], const double low[], int level){
	 int index = 0, count;
	 string date;

	 for (count = 0; count < level; count++) {
		 if (low[count] < low[index]) // I took the index of the lowest to get the right month name
			 index = count;
	 }
	 date = mon[index];
	 return date;
}
 // these two functions are the same as the two above, except they solve for the highest
double highestRainFall(const double high[], int level) {
	double highest;
	int count;
	highest = high[0];

	for (count = 0; count < level; count++) {
		if (high[count] > highest)
			highest = high[count];
	}
	return highest;
}

string getHighestMonth(string mon[], const double high[], int level) {
	int index = 0, count;
	string date;

	for (count = 0; count < level; count++) {
		if (high[count] > high[index])
			index = count;
	}
	date = mon[index];
	return date;
}