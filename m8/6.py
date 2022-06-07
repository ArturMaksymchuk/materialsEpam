#---------6------------
# Write program, that will show basic PC information (OS, RAM amount, HDD’s, and etc.)
import platform
import psutil
import cpuinfo
pl=platform.uname()

def gb(a):
    return a/1024/1024/1024
# ---OS info---
print("-----OS info-----")
print("System: "+pl.system)
print("Node name: "+pl.node)
print("Release: "+pl.release)
print("Versiion: "+pl.version)
print("Machine: "+pl.machine)


# ---CPU info---
print("-----CPU info-----")
# print("Model CPU: ", cpuinfo.get_cpu_info()['brand_raw'])
print("Base speed: ", psutil.cpu_freq().max , "Mhz")
print("CPU cores: ", psutil.cpu_count(logical=False))
print("Logical cores: ", psutil.cpu_count(logical=True))


# ---RAM info---
print("-----RAM info-----")
print("Total RAM: ", round(gb(psutil.virtual_memory().total),1),"GB")
print("Used RAM: ",round(gb(psutil.virtual_memory().used),1),"GB")
print("Free RAM: ",round(gb(psutil.virtual_memory().free),1),"GB")

# ---GPU info---
print("-----GPU info-----")
print("Model CPU: "+pl.system)
print("Base speed: "+pl.system)
print("CPU cores: "+pl.system)
print("Logical cores: "+pl.system)


# ---Disk info---
print("-----Disk info-----")

# ---NET info---
print("-----Net info-----")



