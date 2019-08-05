#include <iostream>
#include <vector>
using namespace std;
/* Head ends here */
void displayPathtoPrincess(int n, vector <string> grid){
    //your logic here
    
    int distToEdge = (n-1)/2;
    
    // locate princess
    int location = 0;
    if (grid[0].at(0) == 'p') location = 1; //top left
    if (grid[0].at(n-1) == 'p') location = 2; //top right
    if (grid[n-1].at(0) == 'p') location = 3; //bottom left
    if (grid[n-1].at(n-1) == 'p') location = 4; //bottom right
    
    // go to princess
    switch (location) {
        case 1: {
            for (int i=0; i<distToEdge; i++) {
                cout << "LEFT" << endl << "UP" << endl;
            }
                break;
        }
        case 2: {
            for (int i=0; i<distToEdge; i++) {
                cout << "RIGHT" << endl << "UP" << endl;
            }
                break;   
        }
        case 3: {
            for (int i=0; i<distToEdge; i++) {
                cout << "LEFT" << endl << "DOWN" << endl;
            }
                break;   
        }
        case 4: {
            for (int i=0; i<distToEdge; i++) {
                cout << "RIGHT" << endl << "DOWN" << endl;
            }
                break;   
        }
    }
}
/* Tail starts here */
int main(void) {

    int m;
    vector <string> grid;

    cin >> m;

    for(int i=0; i<m; i++) {
        string s; cin >> s;
        grid.push_back(s);
    }

    displayPathtoPrincess(m,grid);

    return 0;
}