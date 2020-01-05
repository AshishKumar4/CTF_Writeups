#!/usr/bin/python

import random
import string
from random import randint, choice, sample
from os import system

def random_string(N):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def generate():
    with open('/home/ctf/template.c', 'r') as f:
        template = f.read()

    options = {
        'USELESS_FUNCTIONS': '',
        'USELESS_CALLS': '',
        'BUFFER_SIZE': str(randint(1, 50)),
        'USELESS_BUFFERS_1': '',
        'USELESS_BUFFERS_2': '',
        'GREETING': choice(['Hello', 'Greetings', 'Welcome', 'Good day', 'Nice to meet you', 'It\'s a pleasure']),
        'GOOD_BYE': choice(['See you later', 'Bye', 'Bye bye', 'Good bye', 'Have a good day', 'See ya', 'Good day'])
    }

    decl_template = "{} {}()"
    body_template = "\n {} {} \n"
    instr_list    = [
            "int a = 5; a *= 2; a -= 15; a /= 3;",
            "float b, c, d; b = 123; c = b * 100; d = (c + b) / 2;",
            "int x0 = 0, x1 = 1, x2; for (int i = 0; i < 100; i++) { x2 = x0 + x1; x0 = x1; x1 = x2; }",
            "int k = 12345678; int sum0; while (k) {sum0 += k % 10; k /= 10; int x999 = k + k * 123;}"
    ]
    types = [
        ("int", "return {};".format(randint(1, 1000000))),
        ("float", "return 543.123;"),
        ("double", "return 12312543.4543;"),
        ("char", "return {};".format(randint(1, 127))),
        ("void", "return ;")
    ]

    #functions = []
    for i in range(randint(1, 100)):
        func_name = "func_{}".format(randint(1, 1000000000000000))
        func_type = choice(types)
        func_instr = ''.join(sample(instr_list, randint(0, len(instr_list))))

        options['USELESS_FUNCTIONS'] += decl_template.format(func_type[0], func_name)
        options['USELESS_FUNCTIONS'] += "{" + body_template.format(func_instr, func_type[1]) + "}\n"

        options['USELESS_CALLS'] += "{}();\n".format(func_name)

    bufs = randint(1, 10)
    for i in range(bufs):
        options['USELESS_BUFFERS_1'] += 'char buffer{}[{}];\n'.format(randint(1, 5000), randint(1, 50))

    bufs = randint(1, 10)
    for i in range(bufs):
        options['USELESS_BUFFERS_2'] += 'char buffer{}[{}];\n'.format(randint(1, 5000), randint(1, 50))

    for k in options:
        template = template.replace(k, options[k])

    src_name = "random{}.c".format(random_string(64))
    exe_name = src_name.replace('.c', '.elf')
    with open('/tmp/' + src_name, 'w') as f:
        f.write(template)

    system('gcc -w /tmp/{} -o /tmp/{} -fno-stack-protector -no-pie >/dev/null 2>&1'.format(src_name, exe_name))
    system('strip --strip-all /tmp/{}'.format(exe_name))
    system('rm /tmp/{}'.format(src_name))

    return exe_name

