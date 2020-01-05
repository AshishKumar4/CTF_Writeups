int main()
{
    asm volatile("test_message:\n.incbin \"flag\"\ntest_message_end:");
}
