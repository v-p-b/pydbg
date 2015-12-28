from pydbg import *
from pydbg.defines import *
from utils import crash_binning

def handle_crash(dbg):
    if dbg.dbg.u.Exception.dwFirstChance:
        return DBG_EXCEPTION_NOT_HANDLED
    print "Exception handling..."
    crash_bin=crash_binning()
    print "Record crash"
    crash_bin.record_crash(dbg)
    print "Synopsis"
    print crash_bin.crash_synopsis()
    dbg.terminate_process()
    return DBG_EXCEPTION_NOT_HANDLED

dbg=pydbg()
pid=raw_input("PID: ")
dbg.attach(int(pid))
dbg.set_callback(EXCEPTION_STACK_OVERFLOW,handle_crash)
dbg.set_callback(EXCEPTION_ACCESS_VIOLATION,handle_crash)
dbg.run()