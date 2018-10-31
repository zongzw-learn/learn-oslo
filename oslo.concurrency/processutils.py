from oslo_concurrency import processutils

limit = processutils.ProcessLimits(cpu_time=1, memory_locked=512, stack_size=512)

try:
    (out, err) = processutils.execute("pwd", prlimit=limit)
    print(out, err)
except processutils.ProcessExecutionError as e:
    print(e)

#processutils.ssh_execute(<ssh connection object>, cmd ...)