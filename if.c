#include<stdio.h>
int main(){
    int marks;
    printf("enter the marks:\n");
    scanf("%d",&marks);
    if(marks >= 0 && marks <= 30){
        printf("failed");}
        else if( marks > 30 && marks <= 100 ) {
            printf("passed\n");
            return 0;
            }
            else {
                printf("wrong input");
                }
        return 0;
    }
