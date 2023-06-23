# -*- coding: utf-8 -*-
#python C:\Users\zaheer.shaik\Downloads\python\auto.py ["ssimhppfas2980v"]
"""
Created on Mon Jul 19 20:23:33 2021

@author: zaheer.shaik
"""
#!/usr/bin/env python2
import sys
import paramiko


class ConnectSim:
    def __init__(self, hostname):
        self.hostname = hostname
        self.username = 'dev\svcldrn'
        self.password = 'svc0ldrn!'
        try:
            print("Establishing connection to .....%s" % self.hostname)
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname,username=self.username,password=self.password)
            print("Connection established")
        except Exception as e:
            print( e.__class__, "occurred.")
            exit(2)

    def Check_Simprocess(self, process_name):
        self.cmd='tasklist /v /fi "imagename EQ {}.exe" /FO LIST'.format(process_name)
        try:
            self.stdin, self.stdout, self.stderr = self.ssh.exec_command(self.cmd)
        except Exception as e:
            print(e.message)
        err = ''.join(self.stderr.readlines())
        out = ''.join([line for line in self.stdout.readlines() if "PID:" in line])
        final_output = str(out).rstrip()+str(err).rstrip()
        print(final_output)

    def kill_Simprocess(self, process_name):
        self.cmd='taskkill /IM "{}.exe" /F'.format(process_name)
        try:
            self.stdin, self.stdout, self.stderr = self.ssh.exec_command(self.cmd)
        except Exception as e:
            print(e.message)
        err = ''.join(self.stderr.readlines())
        out = ''.join(self.stdout.readlines())
        final_output = str(out).rstrip()+str(err).rstrip()
        print(final_output)


    def start_Sim(self, process_name):
        self.cmd=r'D:\ClientSim_MQ_30\{}.exe'.format(process_name)
        self.chec_cmd='tasklist /v /fi "imagename EQ {}.exe" /FO LIST'.format(process_name)
        try:
            self.ssh.exec_command(self.cmd)
            self.stdin, self.stdout, self.stderr = self.ssh.exec_command(self.chec_cmd)
        except Exception as e:
            print(e.message)
        err = ''.join(self.stderr.readlines())
        out = ''.join(self.stdout.readlines()[0:3])
        final_output = str(out).rstrip()+str(err).rstrip()
        print(final_output)




if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Error!! Some Issue in getting the arguments")
        sys.exit(1)
def startProcess(hosts):
    for i in hosts:
        w = ConnectSim(i)
        #w.Check_Simprocess('ServerSim')
        w.kill_Simprocess("ClientSim")
        #w.start_Sim("ClientSim")
n = len(sys.argv[1])
hostnames = sys.argv[1][1:n-1]
hostnames=hostnames.split(',')
startProcess(hostnames)



