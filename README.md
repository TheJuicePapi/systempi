-------------------------------------------------------------------------------------------------------------------------------------------

# systemPI - by TheJuicePapi

-------------------------------------------------------------------------------------------------------------------------------------------

![Screenshot_2023-12-15_16-13-59](https://github.com/TheJuicePapi/systempi/assets/134894632/b3a3917b-bf2e-43e7-bca4-8535f1edbac8)
![Screenshot_2023-12-15_16-14-22](https://github.com/TheJuicePapi/systempi/assets/134894632/c28f8b77-ea39-4201-871b-085ce1793053)
![Screenshot_2023-12-15_16-14-53](https://github.com/TheJuicePapi/systempi/assets/134894632/20f17a25-3039-409c-9a55-38b25644e3ee)


------------------------------


DEPENDANCIES

Right now this script is only compatible with RPI machines due to it using vcgencmd. It should work with Raspian OS or Kali linux assuming it's being run on the PI.
(more compatibility will be coming down the road)

This script also uses psutil which will be automatically installed using install.sh.

-------------------------------

DESCRIPTION

systempi is a Python script designed to provide real time monitoring of key system metrics on Raspberry Pi devices/Kali Pis. The script utilizes various tools, including vcgencmd and psutil, to retrieve and display the system stats for you. The script's output is presented in a clear and visually appealing format, with some color changing indicators to highlight critical values. It offers users a comprehensive view of their Raspberry Pi's performance, aiding in the assessment of resource utilization and system health.

-------------------------------

Features

1. CPU Load: Percentage of CPU usage.
2. CPU Temperature: Temperature of the CPU in degrees Celsius.
3. Memory Usage: Percentage of RAM usage.
4. Disk Usage: Percentage of disk space usage on the root file system.
5. Disk Read and Write Rates: Disk I/O rates in kilobytes per second.
6. ARM Frequency: Clock frequency of the ARM processor in Hertz.
7. Uptime: Total time the system has been running, displayed in hours, minutes, and seconds.
8. Load Average: Three load average values for the last 1, 5, and 15 minutes.
9. Swap Usage: Percentage of swap space usage.
10. Network Usage: Data transfer rates in kilobytes per second for both sent and received data. Total data transferred in kilobytes.

-------------------------------

INSTALLATION & USAGE


Git clone installation:

1. 'git clone https://github.com/TheJuicePapi/updateme.git'
2. 'cd updateme'
3. 'chmod +x install.sh'
4. 'sudo ./install.sh'
5. run the script with 'updateme'

 
-------------------------------

This script has been tested on an RPI 4b running a kali linux arm.
