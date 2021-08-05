# clean-my-logs

## Description
A CLI tool to clean and display the important (anamoly) logs from a log file.

## How to Run - 
1. Download the repository to your local device
```bash
$git clone https://github.com/ArpitFalcon/clean-my-logs.git
```

2. Change directory to into the root folder and install the package
```bash
$cd ./clean-my-logs
$pip install .
```

3. Run the CLI app with path to the log file
```bash
$cleanlogs <path to the log file>
```

## Example
```bash
$cleanlogs --help
usage: cleanlogs [-h] [-m MAX_DIST] [-s {desc,asc}] [file [file ...]]

Clean Logs: An anamoly detection CLI tool

positional arguments:
  file                  File name (log file) to use. Default: stdin

optional arguments:
  -h, --help            show this help message and exit
  -m MAX_DIST, --max-dist MAX_DIST
                        This controls how granular cluster should be. Lower value will generate more clusters.      
                        Default: 0.35
  -s {desc,asc}, --sorted {desc,asc}
                        Sort the cluster on the count of members. Default: desc

$cleanlogs ./docker.logs
4 INFO: Finished DockerContainerWatchdog Asynchronous Periodic Work. ---- ms
4 INFO: Started DockerContainerWatchdog Asynchronous Periodic Work
4 INFO: Docker Container Watchdog has been triggered
4 <date> <time> com.nirima.jenkins.plugins.docker.DockerContainerWatchdog$Statistics writeStatisticsToLog
4 INFO: Watchdog Statistics: Number of overall executions:<date>, Executions with processing timeout: 0, Containers 
removed gracefully: 0, Containers removed w
4 ith force: 0, Containers removal failed: 0, Nodes removed successfully: 0, Nodes removal failed: 0, Container removal average duration (gracefully): 0 ms,
4 Container removal average duration (force): 0 ms, Average overall runtime of watchdog: 0 ms, Average runtime of container retrieval: 0 ms
6 INFO: We currently have 0 nodes assigned to this Jenkins instance, which we will check
6 INFO: Docker Container Watchdog check has been completed
10 <date> <time> hudson.model.AsyncPeriodicWork$1 run
16 <date> <time> com.nirima.jenkins.plugins.docker.DockerContainerWatchdog ----
```

## Implementation
The implementation is outlined is much details [here](https://www.cs.unm.edu/~mueen/Papers/LogMine.pdf).
