// Donovan Carr
/* BAC formula: B = -0.015 * t +(2.84 * N / W * g)
 t = time, N = number of drinks, W = weight, g = gender: 
 male is 0.68, female is 0.55. Use double for variables*/
#include <iostream>
using namespace std;

int main() {
	double time, numDrink, weight, // I needed to define all these as double so the calculation does not error out
		gender = 0, male, female, BAC; // I split gender into two variables char gen and double gender.

	male = 0.68;
	female = 0.55;

	char gen, loop; // loop controls main loop

	while (true) { // main loop
		cout << "We are police officers checking your Blood Alcohol Content" << endl;
		cout << "Please cooperate and answer our question as we calculate your BAC" << endl;
		cout << "What gender are you(m for male, f for female): ";
		cin >> gen;
		while (gen != 'm' && gen != 'f') { // made some progress added input validation for gender
			cout << "ERROR: NO DATA ON INPUT" << endl; // I have to say when its not(!) m && f, to loop until they are.
			cout << "Please enter in your gender again: ";
			cin >> gen;
		}
		switch (gen) // I learned I can use switch case for  gender
		{
		case 'm':
			gender = male;
			cout << "You are a male." << endl;
			break;

		case 'f':
			gender = female;
			cout << "You are a female." << endl;
			break;
		}
		
		cout << "How much have you had to drink?: "; // The IDE at first seen every thing as error until I compiled
		//cin >> numDrink;                             // it, do to me using cin in the input validation for number
		while (!(cin >> numDrink)) {
			cout << "ERROR: Enter a number: ";
			cin.clear(); // this clears my last input
			cin.ignore(256, '\n'); // tells it to ignore the last 123 characters
		}
		cout << "You drinked " << numDrink << " beers." << endl;

		cout << "How long ago was your last drink?: "; // the same goes for all the other inputs
		//cin >> time;
		while (!(cin >> time)) { 
			cout << "ERROR: Enter a number: ";
			cin.clear();
			cin.ignore(256, '\n');
		} 
		cout << "You drinked " << time << " hours ago." << endl;

		cout << "How much do you weight in pounds?: ";
		//cin >> weight;
		while (!(cin >> weight)) {				// I first used this on friday morning and it worked but now on
			cout << "ERROR: Enter a number: ";  // saturday morning it ignores the input then askes again for no reason
			cin.clear();
			cin.ignore(256, '\n');
		}
		cout << "You weight " << weight << " pounds." << endl;

		BAC = -0.015 * time + ((2.84 * numDrink) / (weight * gender));
		cout << "Your BAC is " << BAC << endl;
		if (BAC >= 0.08) {
			cout << "Over the legal limit for driving" << endl;
		}
		if (BAC < 0.03) {
			cout << "Normal behavior, no impairment" << endl;
		}
		else // when doing the compairson I was using || instead of && so it treated ever answer as the same.
		{
			if (BAC >= 0.03 && BAC < 0.06) {
				cout << "Mild euphoria and impairment" << endl; // when using || every thing was this response
			}
			else
			{
				if (BAC >= 0.06 && BAC < 0.10) {
					cout << "Euphoric, increased impairment" << endl; // and at one point this one
				}
				else 
				{
					if (BAC >= 0.10 && BAC < 0.20) {
						cout << "Drunk, loss of motor control" << endl;
					}
					else 
					{
						if (BAC >= 0.20 && BAC < 0.30) {
							cout << "Confused, possible blackout" << endl;
						}
						else
						{
							if (BAC >= 0.30 && BAC < 0.40) {
								cout << "Possibly unconscious" << endl;
							}
							else 
							{
								if (BAC >= 0.40) {
									cout << "Unconscious, risk of death" << endl;
								}// final if // these where put here so I dont get confused
							} // final else
						} // 5 else
					} // 4 else
				} // 3 else
			} // 2 else
		}// 1 else
		cout << "would you like to continue?" << endl; // code to end or continue loop
		cout << "press any key or press q to quite: ";
		cin >> loop;
		if (loop == 'q' || loop == 'Q') {
			cout << "Thank you, have a good night." << endl;
			break;
		}
	}// end of while
	return 0;
} // main