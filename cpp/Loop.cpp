#include <iostream>
using namespace std;

int fatorialLoop (int n);

int main (){

    int numero;
    cout << "digite um numero \n";
    cin >> numero;

    cout << fatorialLoop(numero);
    return 0;
}

int fatorialLoop (int n){
    int fatorial = 1;
    for(int i = n; i>0; i--){
        fatorial*=i;
    }
    return fatorial;
}
