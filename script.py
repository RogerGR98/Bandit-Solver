import paramiko 

host = "bandit.labs.overthewire.org"
port = "2220"
user_input = input("Which Bandit level are you doing (1-13)? ")
level_instructions = {
        "bandit1":"cat readme", 
        "bandit2":"cat <-", 
        "bandit3":"cat 'spaces in this filename'", 
        "bandit4":"cd inhere/; ls -a > /dev/null; cat .hidden", 
        "bandit5":"cd inhere; for x in {0..9}; do file ./-file0$x > /dev/null; done; cat <-file07", 
        "bandit6":"cd inhere; find -type f -size 1033c ! -executable > /dev/null; cd maybehere07; cat <.file2", 
        "bandit7":"find / -user bandit7 -group bandit6 -size 33c 2>/dev/null; cd /var/lib/dpkg/info; cat bandit7.password", 
        "bandit8":"cat data.txt | grep millionth", 
        "bandit9":"sort data.txt | uniq -u", 
        "bandit10":"cat data.txt | strings | grep ^'&='", 
        "bandit11":"cat data.txt | base64 --decode", 
        "bandit12":"cat data.txt | tr '[A-Za-z]' '[N-ZA-Mn-za-m]'", 
        "bandit13":"mkdir -p /tmp/test; cp data.txt /tmp/test; cd /tmp/test; xxd -r data.txt > passwd; mv passwd passwd.gz; gunzip passwd.gz; mv passwd passwd.bz2; bzip2 -d passwd.bz2; mv passwd passwd.gz; gunzip passwd.gz; mv passwd passwd.tar; tar -xf passwd.tar; mv data5.bin data5.tar; tar -xf data5.tar; mv data6.bin data6.bz2; bzip2 -d data6.bz2; mv data6 data6.tar; tar -xf data6.tar; mv data8.bin data8.gz; gunzip data8.gz; cat data8 ", 
        }

pass_dict = {
        "bandit1":"bandit0", 
        "bandit2":"boJ9jbbUNNfktd78OOpsqOltutMc3MY1", 
        "bandit3":"CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9", 
        "bandit4":"UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK", 
        "bandit5":"pIwrPrtPN36QITSp3EQaw936yaFoFgAB", 
        "bandit6":"koReBOKuIDDepwhWk7jZC0RTdopnAYKh", 
        "bandit7":"DXjZPULLxYr17uwoI01bNLQbtFemEgo7", 
        "bandit8":"HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs", 
        "bandit9":"cvX2JJa4CFALtqS87jk27qwqGhBM9plV", 
        "bandit10":"UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR", 
        "bandit11":"truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk", 
        "bandit12":"IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR", 
        "bandit13":"5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu", 
        }

### Modified Parameters
user_value = 'bandit' + user_input
pass_used = pass_dict[user_value]
level_instruction = level_instructions[user_value]

### Create a new variable with the level input - 1 bc the value they input is the level they want to solve, not the one they are in; and to solve it we need to login with the previous level credentials 
user_input_modified = str(int(user_input) - 1)
user_used = 'bandit' + user_input_modified

###Functions
def my_function(user, passw, instruction):
    
    #setting connection
    ssh = paramiko.SSHClient()
    #paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG) - debug line
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, passw)
    
    #passing instructions
    stdin, stdout, stderr = ssh.exec_command(instruction)
    output = stdout.read()
    print(output[0:33].decode('ascii'))

my_function(user_used, pass_used, level_instruction)
