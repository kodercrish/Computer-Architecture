#include<stdio.h>

int recurse(int n)
{
     if(n==1)
    {
        return 0;
    }
    else if(n==2)
    {
        return 0;
    }
    else if (n==3)
    {
        return 1;
    }
    else{
        return recurse(n-1)+recurse(n-2)+recurse(n-3);
    }
}

int main()
{
    int n;
    printf("Enter the nth term of tribonacci series which you want to find: ");
    scanf("%d", &n);

    int nth_value=recurse(n);
    printf("%dth term of tribonacci series is %d",n,nth_value);
    return 0;
   
}
