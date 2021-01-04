# Description
THIS CLASS HELP US TO CONNECT REMOTE HOST BY USING KEY BASED AUTHENTICATION OR BY USERNAME AND PASSWORD THROUGH COMMAND LINE ARGUMENTS

# How to create .pem file
https://stackoverflow.com/questions/8382847/how-to-ssh-connect-through-python-paramiko-with-ppk-public-key

# Authentication Procedures
##  Key based authentication
Syntax: # python <file-name> --host <host name/ip> --empid <employee id> --key <private key file in .pem format>  
Example: python remote-login.py --host 120.16.40.7 --empid emp001 --key ./security-files/myServerKey.pem

## Password based authentication
Syntax: python <file-name> --host <host name/ip> --username <username> --password <password>  
Example: python remote-login.py --host 120.21.81.7 --username abc --password abc123

