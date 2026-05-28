#!/usr/bin/env python3

#Author: John Marques
#Author ID: jfpessoa-marques-fil
#Date Created: 2026/05/28

import subprocess
 
def free_space():
    p = subprocess.Popen(['df', '-h', '/'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    # Use awk to get the 4th field (free space) from the line matching '/'
    p2 = subprocess.Popen('df -h | grep \'/$\' | awk \'{print $4}\'', stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output2 = p2.communicate()
    stdout2 = output2[0].decode('utf-8').strip()
    return stdout2
 
if __name__ == '__main__':
    print(free_space())
