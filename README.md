-------------------------------------------------------------------------------------------------------------------------------------------

# systemPI - by TheJuicePapi

-------------------------------------------------------------------------------------------------------------------------------------------
![Screenshot_2023-12-15_16-13-59](https://github.com/TheJuicePapi/systempi/assets/134894632/29b66419-4856-4a18-b057-007d0f94a5a0)
![Screenshot_2023-12-15_16-14-22](https://github.com/TheJuicePapi/systempi/assets/134894632/014276be-1178-4102-9533-600d1b1e11d9)
![Screenshot_2023-12-15_16-14-53](https://github.com/TheJuicePapi/systempi/assets/134894632/f989887d-dbf3-4846-a375-28ff1fd5b0de)



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

1. 'git clone https://github.com/TheJuicePapi/systempi.git'
2. 'cd systempi'
3. 'sudo chmod +x install.sh systempi.py'
4. 'sudo ./install.sh'
5. Exit and open a new terminal to use 'systempi' shortcut

 
-------------------------------

This script has been tested on an RPI 4b running a kali linux arm.
