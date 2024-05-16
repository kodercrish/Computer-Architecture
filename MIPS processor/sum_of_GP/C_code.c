#include<stdio.h>
#include<math.h>

int power(int r,int n)
{
    int pow=1;
    for(int i=0;i<n;i++)
    {
        pow=pow*r;
    }
    return pow;
}

int main()
{
    int a,r,n;
    printf("Enter the first term: ");
    scanf("%d",&a);

    printf("Enter the common ratio: ");
    scanf("%d", &r);

    printf("Enter the number of terms of GP: ");
    scanf("%d",&n);

    int sum;
    sum=(a*((power(r,n))-1.0))/(r-1);
    printf("Sum of first %d terms of GP formula: %d",n,sum);

    return 0;
}
