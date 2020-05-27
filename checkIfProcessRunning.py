# Function to check if a process is running
def checkIfProcessRunning(processName):
        '''Check if there are any running process that contains the given name processName.
        Iterate over the all the running process'''
        for proc in psutil.process_iter():
                try:
                        # Check if process name contains the given name string.
                        print('Checking if application is running...')
                        if processName.lower() in proc.name().lower():
                                return True
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                        pass
        return False;
        
# Example Usage
##        chromeRunning = True
##        while chromeRunning:
##                if checkIfProcessRunning('chrome'):
##                        print('Instance of Chrome is Running...waiting')
##                        time.sleep(20)
##                        print('Checking again...')
##                else:
##                        chromeRunning = False

