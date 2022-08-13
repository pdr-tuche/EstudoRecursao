#include <iostream>
using namespace std;

int fatorialRecursivo (int n);

int main (){

    int numero;
    cout << "digite um numero \n";
    cin >> numero;

    cout << fatorialRecursivo(numero);
    return 0;
}

int fatorialRecursivo (int n){
    if(n <=1 )
        return 1;
    else
        return n * fatorial(n-1);
}
