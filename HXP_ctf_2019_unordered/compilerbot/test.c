int main()
{
    __asm__(".global custom\n\
            .custom:\n\
                .global flag_area\n\
                flag_area:\n\
                    .macro flag\n\
                        .include \"test.txt\"\n\
                    .endmacro\n\
                    .ifdef flag\n\
                    .err\n\
                    flag\n\
                flag_area_end:\n\
                .ifdef FLAG\n\
                .err\n\
                .endif\n\
                custom_end:");
    return 0;
}
//.incbin \"test.txt\"