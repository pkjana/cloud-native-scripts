import sys
import os
import argparse

import paramiko

'''
THIS IS CLASS HELP US TO CONNECT REMOTE HOST
BY USING KEY BASED AUTHENTICATION OR BY USERNAME AND PASSWORD
THROUGH COMMAND LINE ARGUMENTS
'''

class Main(object):

    def __init__(self, args):
        self.args = args
        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        

    def open_ssh_client(self):
        if self.args.empid:
            pkey = paramiko.RSAKey.from_private_key_file(self.args.key)
            self._ssh_client.connect(
                hostname=self.args.host,
                username=self.args.empid,
                pkey=pkey
            )
        else:
            self._ssh_client.connect(
                self.args.host,
                username=self.args.username,
                password=self.args.password
            )


    def close_ssh_client(self):
        self._ssh_client.close()

    def run(self):
        self.open_ssh_client()
        print "Conected"
        self.close_ssh_client()
		
		
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--empid', default=None,
        help='Engineer\'s empid'
    )
    parser.add_argument(
        '--host', dest='host', type=str, required=True,
        help='Host ip or hostname is required'
    )
    parser.add_argument(
        '--username', dest='username', type=str,
        help='Host username is required'
    )
    parser.add_argument(
        '--password', dest='password', type=str,
        help='Host password is required'
    )
    parser.add_argument(
        '--key', dest='key', type=str,
        help='User private key is required'
    )

Main(parser.parse_args()).run()
