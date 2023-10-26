import os
import sys
import random


def main_parent(n: int):
    count_children = 0
    for i in range(n):
        if do_fork() != 0:
            count_children += 1
    while count_children > 0:
        child_pid, wait_status = os.wait()
        exit_code = os.waitstatus_to_exitcode(wait_status)
        print('Parent[', os.getpid(), ']: Child with PID ', child_pid, ' terminated. Exit Status ', exit_code, '.')
        count_children -= 1
        if exit_code != 0:
            if do_fork() != 0:
                count_children += 1


def do_fork():
    try:
        pid = os.fork()
        if pid != 0:
            print('Parent[', os.getpid(), ']: I ran children process with PID ', pid, '.')
        else:
            start_child()
        return pid
    except OSError:
        sys.exit(1)

def start_child():
    s = str(random.randint(5, 10))
    os.execl(sys.executable, sys.executable, "./child.py", s)


main_parent(int(sys.argv[1]))
