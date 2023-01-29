
#include <stdio.h>

int main(){
    int n;
    int a;
    scanf("%d",&n);
    for(int i;i<n;i++){
       scanf("%d",&a);
        if(a%4==0){
            printf("BOB\n");
        }else{
            printf("ALICE\n");
        }
    }
    return 0;
}