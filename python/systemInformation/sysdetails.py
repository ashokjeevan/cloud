import psutil
import platform
from datetime import datetime as dt

uname = platform.uname()

def getMachineDetails():
    print("="*40, "Machine Details", "="*40)
    print(f'System: {uname.system}')
    print(f'Node: {uname.node}')
    print(f'Release: {uname.release}')
    print(f'Version: {uname.version}')
    print(f'Processor: {uname.processor}')
    print(f'Machine: {uname.machine}')

def getTimeElapsedAfterBoot():
    print("="*40, "Time after Boot", "="*40)
    timestamp = psutil.boot_time()
    print(f'Time elapsed since boot: {dt.fromtimestamp(timestamp)}')
    
def cpuInformation():
    print("="*40, "CPU Information", "="*40)
    physicalCores = psutil.cpu_count(logical=False)
    totalCores = psutil.cpu_count(logical=True)
    print(f'Physical core count: {physicalCores} and total no of cores: {totalCores}')

def memoryInformation():
    print("="*40, "Memory Information", "="*40)
    virtualMem = psutil.virtual_memory()
    # should convert the bytes into KB or MB
    # print(f'Total memory: {get_size(virtualMem.total)}')
    print(f'Total memory: {virtualMem.total}')

getMachineDetails()
getTimeElapsedAfterBoot()
cpuInformation()
memoryInformation()

