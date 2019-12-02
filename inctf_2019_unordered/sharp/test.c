#include "stdint.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

int gotHere(int x)
{
  printf("[[%d GOT HERE]] ", x);
  fflush(stdout);
}

uint64_t main(void)
{
  uint8_t bVar1;
  long in_FS_OFFSET;
  uint8_t local_291;
  int local_290;
  int local_28c;
  int local_288;
  int local_284;
  int local_280;
  uint8_t local_278[4];
  char local_274;
  uint8_t abStack627[6];
  char local_26d;
  uint8_t abStack620[52];
  uint64_t local_238;
  uint64_t local_230;
  uint64_t local_228;
  uint64_t local_220;
  uint64_t local_218;
  uint64_t local_210;
  uint16_t local_208;
  uint8_t abStack504[5];
  uint8_t abStack499[59];
  uint64_t local_1b8;
  uint64_t local_1b0;
  uint64_t local_1a8;
  uint64_t local_1a0;
  uint64_t local_198;
  uint64_t local_190;
  uint16_t local_188;
  uint8_t abStack376[5];
  uint8_t abStack371[59];
  uint64_t local_138;
  uint64_t local_130;
  uint64_t local_128;
  uint64_t local_120;
  uint64_t local_118;
  uint64_t local_110;
  uint16_t local_108;
  uint64_t local_f8;
  uint64_t local_f0;
  uint64_t local_e8;
  uint64_t local_e0;
  uint64_t local_d8;
  uint64_t local_d0;
  uint16_t local_c8;
  char local_b8[64];
  uint64_t local_78;
  uint64_t local_70;
  uint64_t local_68;
  uint64_t local_60;
  uint64_t local_58;
  uint64_t local_50;
  uint64_t local_48;
  uint64_t local_40;
  uint64_t local_38;
  uint64_t local_30;
  uint64_t local_28;
  uint64_t local_20;
  uint32_t local_18;
  long local_10;

  // local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_238 = 0x7331743465623072;
  local_230 = 0x703072707364306e;
  local_228 = 0x796c3433;
  local_220 = 0;
  local_218 = 0;
  local_210 = 0;
  local_208 = 0;
  local_1b8 = 0x79697d3534333231;
  local_1b0 = 0x6d6f6f;
  local_1a8 = 0;
  local_1a0 = 0;
  local_198 = 0;
  local_190 = 0;
  local_188 = 0;
  local_138 = 0x796b746b63346871;
  local_130 = 0x66647361706f6975;
  local_128 = 0x63787a6c6b6a6867;
  local_120 = 0x333231306d6e6276;
  local_118 = 0x393837363534;
  local_110 = 0;
  local_108 = 0;
  local_f8 = 0x6f67656c;
  local_f0 = 0;
  local_e8 = 0;
  local_e0 = 0;
  local_d8 = 0;
  local_d0 = 0;
  local_c8 = 0;
  local_78 = 0x254841755d5c5554;
  local_70 = 0x5958515069612749;
  local_68 = 0x4f4e474679787170;
  local_60 = 0x65644d4c45446f66;
  local_58 = 0x213d3c3534356d6c;
  local_50 = 0x392d2f2638302928;
  local_48 = 0x40;
  local_40 = 0;
  local_38 = 0;
  local_30 = 0;
  local_28 = 0;
  local_20 = 0;
  local_18 = 0;
  local_290 = 0;
  
  gotHere(1);

  for(int i = 0xc; i < 0x14; i++)
  {
    printf("[%c]", *(uint8_t *)((long)&local_238 + (long)i));
  }

  char* t = (char*)&local_1b8;

  for(int i = 0x5; i < 0xb; i++)
  {
    printf("[%c, %d]", t[i], t[i]);
  }

  scanf("%s", local_278);
  strcpy(local_b8, (char *)local_278);
  printf("\n[%c, %c; %s]",local_274, local_26d, local_278);
  printf("\n%x, %x %x; [%d, %d, %d]", local_278, &local_274, &local_280, local_278[4], local_274, local_280);
  if ((local_274 == '_') && (local_26d == '_'))
  {
    printf("\nheree!!!");
    local_28c = 0xc;
    while (local_28c < 0x14)
    {
      if (local_278[local_28c] == *(uint8_t *)((long)&local_238 + (long)local_28c))
      {
        printf(">>>%d", local_28c);
        local_290 = local_290 + 1;
      }
      local_28c = local_28c + 1;
    }
    printf("\n{%x}", local_290);
    local_288 = 5;
    while (local_288 < 0xb)
    {
      local_284 = 0;
      while (local_284 < 0x34)
      {
        abStack504[local_288] = local_278[local_288] & 0x76;
        abStack376[local_288] = abStack504[local_288] | 0x69;
        if ((abStack376[local_288] == *(uint8_t *)((long)&local_1b8 + (long)local_288)) &&
            (local_278[local_288] != *(uint8_t *)((long)&local_78 + (long)local_284)))
        {
          local_290 = local_290 + 1;
        }
        local_284 = local_284 + 1;
      }
      local_288 = local_288 + 1;
    }
    local_280 = 0;
    while (local_280 < 4)
    {
      bVar1 = local_278[local_280];
      if (('`' < (char)bVar1) && ((char)bVar1 < '{'))
      {
        local_291 = bVar1 + 4;
        if ('z' < (char)local_291)
        {
          local_291 = bVar1 - 0x16;
        }
        local_278[local_280] = local_291;
      }
      if (local_278[local_280] == *(uint8_t *)((long)&local_f8 + (long)local_280))
      {
        local_290 = local_290 + 1;
      }
      local_280 = local_280 + 1;
    }
    if (local_290 == 0x144)
    {
      printf("YO! The flag is - inctf{%s}", local_b8);
    }
    else
    {
      puts("Commonsense daa!");
    }
  }
  else
  {
    puts("Commonsense daa!");
  }
  // if (local_10 != *(long *)(in_FS_OFFSET + 0x28))
  // {
  //   /* WARNING: Subroutine does not return */
  //   __stack_chk_fail();
  // }
  return 0;
}
