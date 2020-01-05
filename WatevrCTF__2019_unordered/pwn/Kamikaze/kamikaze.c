
undefined8 main(void)

{
  char local_a [2];
  
  signal(0xe,sig);
  alarm(0x28);
  puts("Hello and welcome to \x1b[3mour\x1b[23m voting application!");
  puts("Today\'s vote will be regarding the administration of");
  puts("watevr CTF.");
  puts("the voting range is 0 to 10. 0 being the worst possible and 10 being the best possible.");
  puts("Thanks!");
  printf("Vote: ");
  fflush(stdout);
  gets(local_a);
  puts("Thanks for voting!");
  return 0;
}

