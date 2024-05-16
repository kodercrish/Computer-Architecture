#include <stdio.h>

int n_power_n(int n)
{
        int final=1;
        for(int i=0;i<n;i++)
        {
                final=final*n;
        }
        return final;
}

int main()
{
        printf("This a code for calculating summation of n^n for n natural numbers:\n\n");
        int input;
        printf("Enter the value of n: ");
        scanf("%d", &input);
        int res=0;

        for(int i=1;i<=input;i++)
        {
                res=res+ n_power_n(i);
        }
        printf("Summation of n^n is %d.\n", res);
        return 0;
}
