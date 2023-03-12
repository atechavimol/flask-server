
#include <stdio.h>

int isFactor(int number, int factor);

int isPrime(int num);

void findPrimeFactors(int num);

int main()
{
    const int SIZE = 3;
    int nums[SIZE] = {1081, 28579110, 30030};

    for (int i = 0; i < SIZE; i++)
    {
        findPrimeFactors(nums[i]);
    }

    return 0;
}

void findPrimeFactors(int num)
{
    printf("Finding prime factors of %d \n", num);

    for (int i = 1; i <= num; ++i)
    {
        if (isFactor(num, i) == 1)
        {
            if (isPrime(i) == 1)
            {
                printf("%d is a prime factor of %d \n", i, num);
            }
        }
    }

    printf("\n");
}

int isFactor(int number, int factor)
{
    if (number % factor == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isPrime(int num)
{
    int count = 0;
    for (int i = 1; i < num; ++i)
    {
        if (num % i == 0)
        {
            count++;
        }
    }

    if (count == 1)
    {
        return 1;
    }

    return 0;
}
