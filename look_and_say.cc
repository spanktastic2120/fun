/*

This is just a short program that outputs the the next line in the look-and-say
sequence. It lets you pick a starting value, though it turns out that doesnt 
matter unless you start it at 1. For more info on that, try it out.

http://en.wikipedia.org/wiki/Look-and-say_sequence

*/



using namespace std;
#include <iostream>

class sequence {

private:
  
  int index;
  int size;
  int * value;

public:
  
  sequence() {
    index = 0;
    size = 5;
    value = new int[size];
  }
  
  ~sequence() {
    delete [] value;
  }
  
  void Grow() {
    size = size + 5;
    int * bigger = new int[size];
    for (int i = 0; i < index; i++) {
      bigger[i] = value[i];
    }
    delete [] value;
    value = bigger;    
  }
  
  void Shrink() {
    size = 5;
    int * smaller = new int[size];
    delete [] value;
    value = smaller;
  }
  
  void Clear() {
    index = 0;
    Shrink();
  }
  
  void Add(int n) {
    value[index] = n;
    index++;
    if (index == size) Grow();
  }
  
  void GetValue() {
    for (int i = 0; i < index; i++) {
      cout << value[i] << " ";
      //cout << endl << "index = " << index << endl;
      //cout << "i = " << i << endl;
    }
  }
  
  void Next() {
    sequence temp;
    
    for (int i = 0; i < index;) {
      int count = 1;
      int num = value[i];
      
      while ( num == value[i+1] ) {
        count++;
        i++;
        if (i + 1 == index) break;
      }
      
      temp.Add(count);
      temp.Add(num);
      i++;
    }
    Clear();
    for (int i = 0; i < temp.index; i++)
      Add(temp.value[i]);
  }
  
};

main() {
  sequence ls;
  
  cout << "Enter starting number (0-9): ";
  int start = 0;
  cin >> start;
  if (start > 9 || start < 0) {
    start = 1;
    cout << "Learn to follow directions. Using 1.\n";
  }
  
  ls.Add(start);
  
  cout << "\nPress enter to see the next sequence\n";
  cout << "Enter 'x' to exit" << endl;

  cin.ignore(1000, '\n');  
  char input = cin.get();
  do {
    cin.clear();
    ls.GetValue();
    input = cin.get();
    ls.Next();
  } while (input != 'x' && input != 'X');
  return 0;
}