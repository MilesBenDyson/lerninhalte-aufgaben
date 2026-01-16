open_ports = [
    135,
    445,
    1337,
    3240,
    5040,
    5354,
    7680,
    13331,
    13344,
    49664,
    49665,
    49666,
    49667,
    49668,
    49670,
    49671,
    49708,
    49713,
    54235,
    63342]

#Code von ChatGPT
import subprocess
import re

def port_zu_prozess(port):
    # netstat ausführen
    out = subprocess.check_output(["netstat", "-ano"], text=True, errors="ignore")

    for line in out.splitlines():
        if f":{port} " in line or f":{port}\r" in line:
            parts = re.split(r"\s+", line.strip())
            if len(parts) >= 5:
                pid = parts[-1]

                # Prozessname zur PID holen
                task_out = subprocess.check_output(
                    ["tasklist", "/FI", f"PID eq {pid}"],
                    text=True,
                    errors="ignore"
                )

                for tline in task_out.splitlines():
                    if ".exe" in tline:
                        name = tline.split()[0]
                        return pid, name

                return pid, "unbekannt"

    return None, "kein Eintrag"


for p in open_ports:
    pid, name = port_zu_prozess(p)
    print(f"Port {p:5} → PID {pid} → {name}")

#mehr Detail:

import subprocess

def pid_details(pid: str) -> tuple[str, str]:
    # Name
    name_cmd = f"(Get-Process -Id {pid}).ProcessName"
    # Pfad (kann leer sein, je nach Rechten/Prozess)
    path_cmd = f"(Get-Process -Id {pid}).Path"

    name = subprocess.check_output(["powershell", "-NoProfile", "-Command", name_cmd],
                                   text=True, errors="ignore").strip()
    path = subprocess.check_output(["powershell", "-NoProfile", "-Command", path_cmd],
                                   text=True, errors="ignore").strip()

    return name or "unbekannt", path or "(kein Pfad / keine Rechte)"

unbekannte_pid = [6812, 4]
for p in unbekannte_pid:
    name, path = pid_details(p)
    print(f"PID {p} -> {name}")
    print(f"    Pfad: {path}")
