import paramiko
import time

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.116.1.229","8080","mdmsadmin","monaco1234")
_stdin,_stdout,_stderr=ssh.exec_command("echo monaco1234 | sudo -S service process_manager status")
time.sleep(0.5)
result=_stdout.readlines()
ssh.close()