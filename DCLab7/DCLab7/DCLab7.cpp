// Donovan Carr
/*Create a program that sorts the months by higest rainfall to lowest rainfall*/
#include <iostream>
#include <string>
using namespace std;

void weatherSort(string[], double[], const int);
void swapNum(double&, double&);
void swapMonth(string&, string&); // I also needed to sort the months
void displaySort(string[], double[], const int); // I needed a seporate function to display the sorted info

int main() {
	const int year = 12;
	double month[year];
	string month_name[year] = { "January", "February", "March","April", "May", "June",
		 "July", "August", "September", "October", "November", "December" };
	int count;

	for (count = 0; count < year; count++) {
		cout << "enter amount of rain fall for " << month_name[count] << ": ";
		cin >> month[count];
		while (month[count] < 0) { // need to keep it from crashing if I enter a negative value backwords (1-)
			cout << "Error: Please enter in a number greater than 0: ";
			cin >> month[count];
		}
	}

	cout << "Here is the rain fall for each month: " << endl;
	for (count = 0; count < year; count++)
		cout << month_name[count] << ": " << month[count] << endl;

	cout << endl; // I used the first half of my code from assignment 6

	weatherSort(month_name, month, year); /* I thought calling this function above where I display the unsorted data 
										   would automaticly sort it, but no I needed another function to do so.*/
	displaySort(month_name, month, year);
	
	return 0;
}

void weatherSort(string month[], double list[], const int time){
	int start, maxindex;
	string date;
	double value;
	
	for (start = 0; start < (time - 1); start++) { // get first item in array
		maxindex = start;
		value = list[start];
		date = month[start];
		for (int index = start + 1; index < time; index++) { // compare first item to next item or get the largest
			if (list[index] > value) {
				value = list[index];
				date = month[index];
				maxindex = index;
			}
		}
		swapNum(list[maxindex], list[start]);
		swapMonth(month[maxindex], month[start]);
	}
} // weatherSort function end

void swapNum(double &num1, double &num2) {
	double test = num1;
	num1 = num2;
	num2 = test;
}

void swapMonth(string& mon1, string& mon2) { // code to swap the months the same for the numbers above
	string test = mon1;
	mon1 = mon2;
	mon2 = test;
}

void displaySort(string month[], double list[], const int time) { // code to display sorted data
	cout << "Sorted Months and rainfall" << endl;
	for (int index = 0; index < time; index++) {
		cout << month[index] << ": " << list[index] << endl;
	}
	cout << endl;
}