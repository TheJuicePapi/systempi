import os
import subprocess
import time
import psutil

# Constants
TEMP_THRESHOLD_LOW = 40
TEMP_THRESHOLD_MEDIUM = 50

# Global variables to store previous network stats
prev_sent = 0
prev_recv = 0
prev_disk_read = 0
prev_disk_write = 0

def get_temperature():
    try:
        result_temp = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True, text=True, check=True)
        temperature = float(result_temp.stdout.strip().split("=")[1][:-2])
        return temperature
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Error retrieving temperature: {e}")
        return None

def get_frequency():
    try:
        result_freq = subprocess.run(["vcgencmd", "measure_clock", "arm"], capture_output=True, text=True, check=True)
        frequency = int(result_freq.stdout.strip().split("=")[1])
        return frequency
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Error retrieving frequency: {e}")
        return None

def get_network_usage():
    global prev_sent, prev_recv

    try:
        network_stats = psutil.net_io_counters(pernic=True)
        
        # Assume wlan0 as the default interface
        interface = 'wlan0'

        # Get the current network usage for the interface
        interface_stats = network_stats.get(interface, None)

        if interface_stats:
            # Calculate KiBps
            kb_sent_per_sec = (interface_stats.bytes_sent - prev_sent) / 1024
            kb_recv_per_sec = (interface_stats.bytes_recv - prev_recv) / 1024

            # Update previous values for the next iteration
            prev_sent = interface_stats.bytes_sent
            prev_recv = interface_stats.bytes_recv

            return kb_sent_per_sec, kb_recv_per_sec
        else:
            print(f"No network stats available for {interface}")
            return None, None

    except Exception as e:
        print(f"Error retrieving network usage: {e}")
        return None, None

def get_disk_io():
    global prev_disk_read, prev_disk_write

    try:
        disk_stats = psutil.disk_io_counters()
        disk_read_per_sec = (disk_stats.read_bytes - prev_disk_read) / 1024
        disk_write_per_sec = (disk_stats.write_bytes - prev_disk_write) / 1024

        # Update previous values for the next iteration
        prev_disk_read = disk_stats.read_bytes
        prev_disk_write = disk_stats.write_bytes

        return disk_read_per_sec, disk_write_per_sec

    except Exception as e:
        print(f"Error retrieving disk I/O stats: {e}")
        return None, None

def get_system_load_average():
    try:
        load_avg = os.getloadavg()
        return load_avg
    except Exception as e:
        print(f"Error retrieving system load average: {e}")
        return None

def get_swap_usage():
    try:
        swap = psutil.swap_memory()
        swap_percent = swap.percent
        return swap_percent
    except Exception as e:
        print(f"Error retrieving swap usage: {e}")
        return None

def main():
    boot_time = psutil.boot_time()

    while True:
        temperature = get_temperature()
        frequency = get_frequency()
        cpu_load = psutil.cpu_percent(interval=1)
        mem_percent = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent  # Monitor root disk usage
        disk_read_per_sec, disk_write_per_sec = get_disk_io()
        network_sent_per_sec, network_recv_per_sec = get_network_usage()
        system_load_avg = get_system_load_average()
        swap_percent = get_swap_usage()

        color_code_temp = "\033[92m" if temperature < TEMP_THRESHOLD_LOW else ("\033[93m" if temperature < TEMP_THRESHOLD_MEDIUM else "\033[91m")
        color_code_freq = "\033[96m"
        color_code_mem = "\033[94m"
        color_code_disk = "\033[95m"
        color_code_net = "\033[97m"
        color_code_systemp = "\033[91;1m"  # Bright red
        color_code_load_avg = "\033[0m"  # Default color
        color_code_numbers = "\033[91m"  # Red color for numbers

        uptime = time.time() - boot_time
        hours = int(uptime // 3600)
        minutes = int((uptime % 3600) // 60)
        seconds = int(uptime % 60)

        os.system("clear")

        # ASCII Box
        box_top = f"{color_code_systemp}{'='*30}\033[0m"
        box_bottom = f"{color_code_systemp}{'='*30}\033[0m"

        print(box_top)
        print(f"{color_code_systemp}    SYSTEMP - TheJuicePapi\033[0m")
        print(box_top)

        # Color code for CPU load
        color_code_cpu = "\033[93m" if cpu_load >= 45 and cpu_load < 75 else ("\033[91m" if cpu_load >= 75 else "\033[92m")

        print(f"  CPU load = {color_code_cpu}{cpu_load}%\033[0m")
        print(f"  CPU temp = {color_code_temp}{temperature}\033[0m °C")
        print(f"  MEM usage = {color_code_mem}{mem_percent}%\033[0m")
        print(f"  Disk usage = {color_code_disk}{disk_usage}%\033[0m")
        print(f"  Disk Read = {color_code_disk}{disk_read_per_sec:.2f} KiB/s\033[0m")
        print(f"  Disk Write = {color_code_disk}{disk_write_per_sec:.2f} KiB/s\033[0m")
        print(f"  ARM freq = {color_code_freq}{frequency}\033[0m Hz")
        print(f"  Uptime = {hours}h {minutes}m {seconds}s")
        
        # Modified line for load average
        load_avg_str = f"  Load Average:\n    1m: {color_code_numbers}{round(system_load_avg[0], 2)}\033[0m\n    5m: {color_code_numbers}{round(system_load_avg[1], 2)}\033[0m\n    15m: {color_code_numbers}{round(system_load_avg[2], 2)}\033[0m"
        print(f"{color_code_load_avg}{load_avg_str}")
        
        print(f"  Swap Usage = {color_code_disk}{swap_percent}%\033[0m")
        print(f"  Network:")
        print(f"    Sent = {color_code_net}{network_sent_per_sec:.2f} KiB/s\033[0m")
        print(f"    Received = {color_code_net}{network_recv_per_sec:.2f} KiB/s\033[0m")
        print(f"    Total = {color_code_net}{network_sent_per_sec + network_recv_per_sec:.2f} KiB\033[0m")

        print(box_bottom)

        time.sleep(1)

if __name__ == "__main__":
    main()
