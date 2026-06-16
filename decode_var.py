import base64 as b64
import os
import subprocess


def decode_cred(cred):
    '''
    This function takes an base64 encoded string and decodes it.
    This is used so that database passwords aren't stored as plain text in environment variables.

    Parameters:
        cred (str): Base64 encoded string

    Returns:
        decoded_cred (str): Decoded plain text string
    '''
    return b64.b64decode(cred).decode('ascii')


def powershell_cd():
    proc= subprocess.run("where powershell", shell=True, text=True, capture_output= True)
    return proc.stdout.strip('\n')


def run_powershell_command(command):
    pws_path= '{}'.format(powershell_cd())
    subprocess.call("{} {}".format(pws_path,command), shell=True)