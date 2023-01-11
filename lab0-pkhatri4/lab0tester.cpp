/****************************************************************/
/*                                                              */
/*   lab 0 tester file                                          */
/*                                                              */
/*   To compile: g++ lab0.cpp lab0tester.cpp -std=c++0x         */
/*                                                              */
/*                                                              */
/****************************************************************/
#include <iostream>
using namespace std;

unsigned long long factorial (unsigned int n);
unsigned long long power (unsigned int base, unsigned int n);
unsigned long long fibonacci (unsigned int n);

int main(void){

    unsigned long long correctFactorial[20]= {1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,
                                                6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 
                                                6402373705728000, 121645100408832000
                                            };
    bool hasBug=false;
    for(unsigned int i=0;i<20;i++){
        unsigned long long rc=factorial(i);
        if(rc !=correctFactorial[i]){
            cout << "Error: factorial (" << i << ") = " << correctFactorial[i] << endl;
            cout << "Your function returned: " << rc << endl;
            hasBug=true;
        }
    }
    if(hasBug){
        cout << "Your code has a bug.  please fix." << endl;
        return 1;
    }
    else{
        cout << "Congrats! your code is now working" << endl;
        return 0;
    }
}
