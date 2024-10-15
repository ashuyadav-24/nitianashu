#include<stdio.h>
int main(){
    int day;
    printf("enter the day\n");
    scanf("%d",&day);

    switch(day){
        case 1: printf("monday");
        break;
        case 2: printf("tuesday");
        break;
        default:printf("not a valid day");
        break;
    }
    return 0;

}