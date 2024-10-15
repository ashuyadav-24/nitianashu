#include<stdio.h>
int main(){
    int n;
    do{
        printf("enter the number:");
        scanf("%d",&n);
    }
    while(n%7!=0);
    printf("thank you");
    return 0;
}