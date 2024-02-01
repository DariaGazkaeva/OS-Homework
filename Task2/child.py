import sys
import os
import time
import random


def main_child():
    s = int(sys.argv[1])
    pid = os.getpid()
    ppid = os.getppid()
    print('Child[', pid, ']: I am started. My PID ', pid, '. Parent PID ', ppid, '.')
    time.sleep(s)
    print('Child[', pid, ']: I am ended. PID ', pid, 'Parent PID ', ppid, '.')
    sys.exit(round(random.random()))


main_child()
