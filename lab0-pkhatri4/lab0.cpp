unsigned long long factorial (unsigned int n){
    unsigned long f;

    if(n == 0 || n == 1)
        return 1;
    else
        f = n* factorial(n-1);
    return f;
}
