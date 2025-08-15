#include<stdio.h>

int main(){
    int arr[5], x;
    int sum = 0;
    for(int i = 0;i<5;i++){
        scanf("%d",&x);
        arr[i] = x;
        sum = sum+x;
    }
    printf("%d",sum/5);
}
