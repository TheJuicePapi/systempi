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

def main():
    boot_time = psutil.boot_time()

    while True:
        temperature = get_temperature()
        frequency = get_frequency()
        cpu_load = psutil.cpu_percent(interval=1)
        mem_percent = psutil.virtual_memory().percent

        color_code_temp = "\033[92m" if temperature < TEMP_THRESHOLD_LOW else ("\033[93m" if temperature < TEMP_THRESHOLD_MEDIUM else "\033[91m")
        color_code_freq = "\033[96m"
        color_code_mem = "\033[94m"
        color_code_systemp = "\033[91;1m"  # Bright red

        uptime = time.time() - boot_time
        hours = int(uptime // 3600)
        minutes = int((uptime % 3600) // 60)
        seconds = int(uptime % 60)

        # Get network usage
        sent_per_sec, recv_per_sec = get_network_usage()

        # Calculate the total sent and received at the same time
        total_current = sent_per_sec + recv_per_sec

        os.system("clear")
        print(f"{color_code_systemp}  SYSTEMP - TheJuicePapi\033[0m")
        print(f"                      ")
        print(f"CPU load = {cpu_load}%")
        print(f"CPU temp = {color_code_temp}{temperature}\033[0m °C")
        print(f"MEM usage = {color_code_mem}{mem_percent}%\033[0m")
        print(f"ARM freq = {color_code_freq}{frequency}\033[0m Hz")
        print(f"Uptime = {hours}h {minutes}m {seconds}s")
        print(f"Network:")
        print(f"  Sent = {sent_per_sec:.2f} KiB/s")
        print(f"  Received = {recv_per_sec:.2f} KiB/s")
        print(f"  Total = {total_current:.2f} KiB")

        time.sleep(1)

if __name__ == "__main__":
    main()
