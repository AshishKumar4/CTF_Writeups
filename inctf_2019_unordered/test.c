#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "stdint.h"

int main()
{
    int array[] = {0x33323130, 0x62613534, 0x66656463, 0x6a696867, 0x6e6d6c6b, \
                    0x7271706f, 0x76757473, 0x7a797877, 0x4342415f, 0x47464544, \
                    0x4b4a4948, 0x4f4e4d4c, 0x53525150, 0x57565554, 0x7b5a5958, \
                    0x7d, 0x5c4d564b, 0x564b7e4e, 0x4658464c, 0x52436558, 0x4549654f, \
                    0x554b444c, 0x7946, 0};
    uint8_t* ptr = array;

    char str[30];
    char tstack[27];
    char *s2;
    scanf("%s", str);
    s2 = str;
    int ln = printf("%s", s2);
    printf("==>%d", ln);
    for(int i = 0; i < ln; i++)
    {
        int j = 0;
        for(j = 0; str[i] != ((char*)ptr)[j]; j++);
        printf("\n-->[%d, %d]", j, j^0x45);
        tstack[i] = j ^ 0x45;
    }

    char* a = 0x0;
    int b = 0;
    do {
        if(ln <= (int)(a))
        {
            lbl:
            if(a == (char*)0x1a)
            {
                printf("\nGreat! Got the flag!");
            }
            else 
            {
                printf("\nThe end!");
            }
            return 0;
        }
        // b = (int)s2[(int)&]
    }while(1);
    return 0;
}