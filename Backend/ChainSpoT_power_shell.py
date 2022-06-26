import subprocess
import sys
import ctypes
from time import sleep

#check if the script run as administrator or not if not  it'll restart the script with admin rights
def run_as_admin(argv=None, debug=False):
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # Support pyinstaller wrapped program.
        arguments = map(str, argv[1:])
    else:
        arguments = map(str, argv)
    argument_line = u' '.join(arguments)
    executable = str(sys.executable)
    if debug:
        print ('Command line: ', executable, argument_line)
    ret = shell32.ShellExecuteW(None, u"runas", executable, argument_line, None, 1)
    if int(ret) <= 32:
        return False
    return None

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

#check if you open hotspot or not return True or False
def check_hotspot(prev_check=0):

    power_shell_cmd='''$connectionProfile = [Windows.Networking.Connectivity.NetworkInformation,Windows.Networking.Connectivity,ContentType=WindowsRuntime]::GetInternetConnectionProfile()
$tetheringManager = [Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager,Windows.Networking.NetworkOperators,ContentType=WindowsRuntime]::CreateFromConnectionProfile($connectionProfile)
$tetheringManager.TetheringOperationalState
    '''
    power_shell_output = run(power_shell_cmd)
    power_shell_output = power_shell_output.stdout.decode()
    power_shell_output = power_shell_output.replace("\r","")
    power_shell_output = power_shell_output.replace("\n","")
     
    if power_shell_output =="InTransition" and prev_check == 0 :
        sleep(5)
        return check_hotspot(1) 
    elif power_shell_output == "On":
        return True
    elif power_shell_output == "Off":
        return False
    else:
        return -1

#check if user's device support hotspot or not
def support_hotspot():
    power_shell_cmd='''$connectionProfile = [Windows.Networking.Connectivity.NetworkInformation,Windows.Networking.Connectivity,ContentType=WindowsRuntime]::GetInternetConnectionProfile()
$tetheringManager = [Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager,Windows.Networking.NetworkOperators,ContentType=WindowsRuntime]::CreateFromConnectionProfile($connectionProfile)
    '''
    power_shell_output = run(power_shell_cmd)

    if power_shell_output.returncode != 0:
        #print("An error occured: %s", completed.stderr) # Just if You want to print the error
        return False
    return True

#return MAC addresses of connected devices to your hotspot
def connected_devices():
    power_shell_cmd='''$connectionProfile = [Windows.Networking.Connectivity.NetworkInformation,Windows.Networking.Connectivity,ContentType=WindowsRuntime]::GetInternetConnectionProfile()
$tetheringManager = [Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager,Windows.Networking.NetworkOperators,ContentType=WindowsRuntime]::CreateFromConnectionProfile($connectionProfile)
$tetheringManager.GetTetheringClients()
    '''
    power_shell_output = run(power_shell_cmd)

    if power_shell_output.returncode != 0:
        #print("An error occured: %s", completed.stderr) # Just if You want to print the error
        return -1
    
    power_shell_output = power_shell_output.stdout.decode()
    power_shell_output = power_shell_output.replace("\r","")
    power_shell_output = power_shell_output.split("\n")
    mac_list=[]
    for i in power_shell_output:
        if "System.__ComObject " in i and ":" in i:
            mac_list.append(i[19:])
    return mac_list





#start hotspot networf if it works return True else return False
#input only hotspot name and password of hotspot
def start_hotspot(hotspot_name,password):

    if len(password) <8 or len(password) > 32 or'"' in password: #If password less than 8 char or bigger than 32 char or there's double quote in password retturn -1
        return -1

    power_shell_cmd= '''Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | ? { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
Function Await($WinRtTask, $ResultType) {
    $asTask = $asTaskGeneric.MakeGenericMethod($ResultType)
    $netTask = $asTask.Invoke($null, @($WinRtTask))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}
Function AwaitAction($WinRtAction) {
    $asTask = ([System.WindowsRuntimeSystemExtensions].GetMethods() | ? { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and !$_.IsGenericMethod })[0]
    $netTask = $asTask.Invoke($null, @($WinRtAction))
    $netTask.Wait(-1) | Out-Null
}
$connectionProfile = [Windows.Networking.Connectivity.NetworkInformation,Windows.Networking.Connectivity,ContentType=WindowsRuntime]::GetInternetConnectionProfile()
$tetheringManager = [Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager,Windows.Networking.NetworkOperators,ContentType=WindowsRuntime]::CreateFromConnectionProfile($connectionProfile)
$accessPointConfiguration = $tetheringManager.GetCurrentAccessPointConfiguration()
$accessPointConfiguration.Ssid = ''' + '"'+ hotspot_name+'"'+" \n$accessPointConfiguration.Passphrase ="+'"'+password+'"' +''' \nAwaitAction ($tetheringManager.ConfigureAccessPointAsync($accessPointConfiguration)) ([Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult])
Await ($tetheringManager.StartTetheringAsync()) ([Windows.Networking.NetworkOperators.NetworkOperatorTetheringOperationResult])
'''
    
    power_shell_output = run(power_shell_cmd)
    
    if power_shell_output.returncode != 0:
        #print("An error occured: %s", completed.stderr) # Just if You want to print the error
        return False
    return True

#check if you open hotspot or not then stop hotspot network if it done return True else return False
#input only hotspot name and password of hotspot
def stop_hotspot():
    power_shell_cmd='''$connectionProfile = [Windows.Networking.Connectivity.NetworkInformation,Windows.Networking.Connectivity,ContentType=WindowsRuntime]::GetInternetConnectionProfile()
$tetheringManager = [Windows.Networking.NetworkOperators.NetworkOperatorTetheringManager,Windows.Networking.NetworkOperators,ContentType=WindowsRuntime]::CreateFromConnectionProfile($connectionProfile)
$tetheringManager.StopTetheringAsync()
'''
    power_shell_output = run(power_shell_cmd)
    check = check_hotspot()
    if check == False:
        return True 
    elif check == True:
        return False
    else:
        return -1


if __name__ == '__main__':
    run_as_admin()
    print(check_hotspot())
    ret  = start_hotspot("Hello","Heellllo")
    print(ret)
    print(support_hotspot())
    print(check_hotspot())
    print(connected_devices())
    print(stop_hotspot())
    