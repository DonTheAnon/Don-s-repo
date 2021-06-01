// Donovan Carr
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
// I ran out of time and gave up.
int main() {
//	const int SCORE = 11;
	ifstream readfile;
	string team1, team2, team3;
	string score1[11], score2[11], score3[11];
	const int SCORE = 11;
	int num1 = 0, num2 = 0, num3 = 0, total1 = 0, total2 = 0, total3 = 0;
	int sco1[SCORE], sco2[SCORE], sco3[SCORE];

	readfile.open("C:\\scores.txt");
	if (!readfile) {
		cout << "Error: File Open Failure!" << endl;
	}

	getline(readfile, team1);
	cout << team1 << endl;

	getline(readfile, score1[num1], '\n'); // I put the scores into arrays
	cout << score1[num1] << endl;
	sco1[SCORE] = stoi(score1[num1]); // I tried to turn them into integers here I might need to make them into vectors
	//for (int count = 0; count < SCORE; count++)
	//	total1 += sco1[count];
//	cout << " total 1: " << total1 << endl;

	getline(readfile, team2);
	cout << team2 << endl;

	getline(readfile, score2[num2], '\n');
	cout << score2[num2] << endl;
	sco2[SCORE] = stoi(score2[num2]);

	getline(readfile, team3);
	cout << team3 << endl;

	getline(readfile, score3[num3], '\n');
	cout << score3[num3] << endl;
	sco3[SCORE] = stoi(score3[num3]);

	readfile.close();

	return 0;
}
