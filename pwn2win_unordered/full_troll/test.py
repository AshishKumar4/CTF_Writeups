def test(param_1):
    abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/-_.'
    bVar1 = 0
    sVar2 = 0
    local_1c = 0
    local_24 = 0
    while True:
        sVar2 = len(param_1)
        if (sVar2 <= local_24):
            return 1
        bVar1 = False 
        local_1c = 0
        sVar2 = len(abc)
        while local_1c < sVar2:
            if abc[local_1c] == param_1[local_24]:
                bVar1 = True 
                break 
            local_1c += 1
        if bVar1 == 0:
            return 0
        local_24 += 1


  # do {
  #   sVar2 = strlen(param_1);
  #   if (sVar2 <= (ulong)(long)local_24) {
  #     return 1;
  #   }
  #   bVar1 = false;
  #   local_1c = 0;
  #   while (sVar2 = strlen(s_abcdefghijklmnopqrstuvwxyzABCDEF_00302020),
  #         (ulong)(long)local_1c < sVar2) {
  #     if (s_abcdefghijklmnopqrstuvwxyzABCDEF_00302020[local_1c] == param_1[local_24]) {
  #       bVar1 = true;
  #       break;
  #     }
  #     local_1c = local_1c + 1;
  #   }
  #   if (!bVar1) {
  #     return 0;
  #   }
  #   local_24 = local_24 + 1;
  # } while( true );