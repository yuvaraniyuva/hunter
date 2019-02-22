#include<stdio.h>
int main()
{
long int arr[100000],N,i;
int f=0;
scanf("%ld",&N);
for(i=0;i<N;i++)
	{
scanf("%ld",&arr[i]);
}
for(i=0;i<N;i++)
{
if(arr[i]==i)		
{
f=1;
printf(" %d ",i);
}
}	
if(f==0)
printf("-1");
}
