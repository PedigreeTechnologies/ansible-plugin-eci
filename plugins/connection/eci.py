DOCUMENTATION = '''
    connection: eci
    short_description: use ec2-instance-connect to support the ansible ssh module
    description:
        - This connection plugin extends the ssh module and uses ec2-instance-connect to handle access permissions
    author: mpieters3
    options:
      aws_access_key:
          description: AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.
          ini:
            - section: defaults
              key: aws_access_key
          env:
            - name: ANSIBLE_AWS_ACCESS_KEY
          vars:
            - name: aws_access_key
      aws_secret_key:
          description: AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.
          ini:
            - section: defaults
              key: aws_secret_key
          env:
            - name: ANSIBLE_AWS_SECRET_KEY
          vars:
            - name: aws_secret_key
      region:
          description: The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region
          ini:
            - section: defaults
              key: region
          env:
            - name: AWS_REGION
            - name: EC2_REGION
          vars:
            - name: ansible_region
            - name: aws_region
            - name: ec2_region
      instance_id:
          description: ec2-instance-id to connect to
          ini:
            - section: defaults
              key: instance_id
          vars:
            - name: ansible_instance_id
      host:
          description: Hostname/IP to connect to.
          default: inventory_hostname
          vars:
               - name: inventory_hostname
               - name: ansible_host
               - name: ansible_ssh_host
               - name: delegated_vars['ansible_host']
               - name: delegated_vars['ansible_ssh_host']
      host_key_checking:
          description: Determines if SSH should check host keys.
          default: True
          type: boolean
          ini:
              - section: defaults
                key: 'host_key_checking'
              - section: ssh_connection
                key: 'host_key_checking'
                version_added: '2.5'
          env:
              - name: ANSIBLE_HOST_KEY_CHECKING
              - name: ANSIBLE_SSH_HOST_KEY_CHECKING
                version_added: '2.5'
          vars:
              - name: ansible_host_key_checking
                version_added: '2.5'
              - name: ansible_ssh_host_key_checking
                version_added: '2.5'
      password:
          description: Authentication password for the C(remote_user). Can be supplied as CLI option.
          vars:
              - name: ansible_password
              - name: ansible_ssh_pass
              - name: ansible_ssh_password
      sshpass_prompt:
          description:
              - Password prompt that sshpass should search for. Supported by sshpass 1.06 and up.
              - Defaults to C(Enter PIN for) when pkcs11_provider is set.
          default: ''
          ini:
              - section: 'ssh_connection'
                key: 'sshpass_prompt'
          env:
              - name: ANSIBLE_SSHPASS_PROMPT
          vars:
              - name: ansible_sshpass_prompt
          version_added: '2.10'
      ssh_args:
          description: Arguments to pass to all SSH CLI tools.
          default: '-C -o ControlMaster=auto -o ControlPersist=60s'
          ini:
              - section: 'ssh_connection'
                key: 'ssh_args'
          env:
              - name: ANSIBLE_SSH_ARGS
          vars:
              - name: ansible_ssh_args
                version_added: '2.7'
      ssh_common_args:
          description: Common extra args for all SSH CLI tools.
          ini:
              - section: 'ssh_connection'
                key: 'ssh_common_args'
                version_added: '2.7'
          env:
              - name: ANSIBLE_SSH_COMMON_ARGS
                version_added: '2.7'
          vars:
              - name: ansible_ssh_common_args
          cli:
              - name: ssh_common_args
          default: ''
      ssh_executable:
          default: ssh
          description:
            - This defines the location of the SSH binary. It defaults to C(ssh) which will use the first SSH binary available in $PATH.
            - This option is usually not required, it might be useful when access to system SSH is restricted,
              or when using SSH wrappers to connect to remote hosts.
          env: [{name: ANSIBLE_SSH_EXECUTABLE}]
          ini:
          - {key: ssh_executable, section: ssh_connection}
          #const: ANSIBLE_SSH_EXECUTABLE
          version_added: "2.2"
          vars:
              - name: ansible_ssh_executable
                version_added: '2.7'
      sftp_executable:
          default: sftp
          description:
            - This defines the location of the sftp binary. It defaults to C(sftp) which will use the first binary available in $PATH.
          env: [{name: ANSIBLE_SFTP_EXECUTABLE}]
          ini:
          - {key: sftp_executable, section: ssh_connection}
          version_added: "2.6"
          vars:
              - name: ansible_sftp_executable
                version_added: '2.7'
      scp_executable:
          default: scp
          description:
            - This defines the location of the scp binary. It defaults to C(scp) which will use the first binary available in $PATH.
          env: [{name: ANSIBLE_SCP_EXECUTABLE}]
          ini:
          - {key: scp_executable, section: ssh_connection}
          version_added: "2.6"
          vars:
              - name: ansible_scp_executable
                version_added: '2.7'
      scp_extra_args:
          description: Extra exclusive to the C(scp) CLI
          vars:
              - name: ansible_scp_extra_args
          env:
            - name: ANSIBLE_SCP_EXTRA_ARGS
              version_added: '2.7'
          ini:
            - key: scp_extra_args
              section: ssh_connection
              version_added: '2.7'
          cli:
            - name: scp_extra_args
          default: ''
      sftp_extra_args:
          description: Extra exclusive to the C(sftp) CLI
          vars:
              - name: ansible_sftp_extra_args
          env:
            - name: ANSIBLE_SFTP_EXTRA_ARGS
              version_added: '2.7'
          ini:
            - key: sftp_extra_args
              section: ssh_connection
              version_added: '2.7'
          cli:
            - name: sftp_extra_args
          default: ''
      ssh_extra_args:
          description: Extra exclusive to the SSH CLI.
          vars:
              - name: ansible_ssh_extra_args
          env:
            - name: ANSIBLE_SSH_EXTRA_ARGS
              version_added: '2.7'
          ini:
            - key: ssh_extra_args
              section: ssh_connection
              version_added: '2.7'
          cli:
            - name: ssh_extra_args
          default: ''
      reconnection_retries:
          description: Number of attempts to connect.
          default: 0
          type: integer
          env:
            - name: ANSIBLE_SSH_RETRIES
          ini:
            - section: connection
              key: retries
            - section: ssh_connection
              key: retries
          vars:
            - name: ansible_ssh_retries
              version_added: '2.7'
      port:
          description: Remote port to connect to.
          type: int
          ini:
            - section: defaults
              key: remote_port
          env:
            - name: ANSIBLE_REMOTE_PORT
          vars:
            - name: ansible_port
            - name: ansible_ssh_port
          keyword:
            - name: port
      remote_user:
          description:
              - User name with which to login to the remote server, normally set by the remote_user keyword.
              - If no user is supplied, Ansible will let the SSH client binary choose the user as it normally.
          ini:
            - section: defaults
              key: remote_user
          env:
            - name: ANSIBLE_REMOTE_USER
          vars:
            - name: ansible_user
            - name: ansible_ssh_user
          cli:
            - name: user
          keyword:
            - name: remote_user
      pipelining:
          description:
            - Pipelining settings
          env:
            - name: ANSIBLE_PIPELINING
            - name: ANSIBLE_SSH_PIPELINING
          ini:
            - section: defaults
              key: pipelining
            - section: connection
              key: pipelining
            - section: ssh_connection
              key: pipelining
          vars:
            - name: ansible_pipelining
            - name: ansible_ssh_pipelining
      private_key_file:
          description:
              - Path to private key file to use for authentication.
          ini:
            - section: defaults
              key: private_key_file
          env:
            - name: ANSIBLE_PRIVATE_KEY_FILE
          vars:
            - name: ansible_private_key_file
            - name: ansible_ssh_private_key_file
          cli:
            - name: private_key_file
              option: '--private-key'
      control_path:
        description:
          - This is the location to save SSH's ControlPath sockets, it uses SSH's variable substitution.
          - Since 2.3, if null (default), ansible will generate a unique hash. Use ``%(directory)s`` to indicate where to use the control dir path setting.
          - Before 2.3 it defaulted to ``control_path=%(directory)s/ansible-ssh-%%h-%%p-%%r``.
          - Be aware that this setting is ignored if C(-o ControlPath) is set in ssh args.
        env:
          - name: ANSIBLE_SSH_CONTROL_PATH
        ini:
          - key: control_path
            section: ssh_connection
        vars:
          - name: ansible_control_path
            version_added: '2.7'
      control_path_dir:
        default: ~/.ansible/cp
        description:
          - This sets the directory to use for ssh control path if the control path setting is null.
          - Also, provides the ``%(directory)s`` variable for the control path setting.
        env:
          - name: ANSIBLE_SSH_CONTROL_PATH_DIR
        ini:
          - section: ssh_connection
            key: control_path_dir
        vars:
          - name: ansible_control_path_dir
            version_added: '2.7'
      sftp_batch_mode:
        default: 'yes'
        description: 'TODO: write it'
        env: [{name: ANSIBLE_SFTP_BATCH_MODE}]
        ini:
        - {key: sftp_batch_mode, section: ssh_connection}
        type: bool
        vars:
          - name: ansible_sftp_batch_mode
            version_added: '2.7'
      ssh_transfer_method:
        description:
            - "Preferred method to use when transferring files over ssh"
            - Setting to 'smart' (default) will try them in order, until one succeeds or they all fail
            - Using 'piped' creates an ssh pipe with C(dd) on either side to copy the data
        choices: ['sftp', 'scp', 'piped', 'smart']
        env: [{name: ANSIBLE_SSH_TRANSFER_METHOD}]
        ini:
            - {key: transfer_method, section: ssh_connection}
        vars:
            - name: ansible_ssh_transfer_method
              version_added: '2.12'
      scp_if_ssh:
        deprecated:
              why: In favor of the "ssh_transfer_method" option.
              version: "2.17"
              alternatives: ssh_transfer_method
        default: smart
        description:
          - "Preferred method to use when transferring files over SSH."
          - When set to I(smart), Ansible will try them until one succeeds or they all fail.
          - If set to I(True), it will force 'scp', if I(False) it will use 'sftp'.
          - This setting will overridden by ssh_transfer_method if set.
        env: [{name: ANSIBLE_SCP_IF_SSH}]
        ini:
        - {key: scp_if_ssh, section: ssh_connection}
        vars:
          - name: ansible_scp_if_ssh
            version_added: '2.7'
      use_tty:
        version_added: '2.5'
        default: 'yes'
        description: add -tt to ssh commands to force tty allocation.
        env: [{name: ANSIBLE_SSH_USETTY}]
        ini:
        - {key: usetty, section: ssh_connection}
        type: bool
        vars:
          - name: ansible_ssh_use_tty
            version_added: '2.7'
      timeout:
        default: 10
        description:
            - This is the default amount of time we will wait while establishing an SSH connection.
            - It also controls how long we can wait to access reading the connection once established (select on the socket).
        env:
            - name: ANSIBLE_TIMEOUT
            - name: ANSIBLE_SSH_TIMEOUT
              version_added: '2.11'
        ini:
            - key: timeout
              section: defaults
            - key: timeout
              section: ssh_connection
              version_added: '2.11'
        vars:
          - name: ansible_ssh_timeout
            version_added: '2.11'
        cli:
          - name: timeout
        type: integer
      pkcs11_provider:
        version_added: '2.12'
        default: ""
        description:
          - "PKCS11 SmartCard provider such as opensc, example: /usr/local/lib/opensc-pkcs11.so"
          - Requires sshpass version 1.06+, sshpass must support the -P option.
        env: [{name: ANSIBLE_PKCS11_PROVIDER}]
        ini:
          - {key: pkcs11_provider, section: ssh_connection}
        vars:
          - name: ansible_ssh_pkcs11_provider
'''

import importlib
import tempfile
from datetime import datetime
import os
import time

try:
  from ansible.utils.display import Display
  HAS_ANSIBLE = True
except ImportError:
  HAS_ANSIBLE = False

try:
    import boto3
    HAS_BOTO = True
except ImportError:
    HAS_BOTO = False
    
try:
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.serialization.ssh import load_ssh_private_key
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
    HAS_CRYPTOGRAPHY = True
except ImportError:
    HAS_CRYPTOGRAPHY = False

ssh = importlib.import_module('ansible.plugins.connection.ssh')

## we're going to base our connector off the basic SSH connector, as we want nearly all its behavior
display = Display()

ECI_PUSH_EXPIRY = 45
ECI_KEY_SIZE = 2048
ECI_KEY_EXPONENT = 65537

class Connection(ssh.Connection):
    """ SSH connection that uses EC2 Instance Connect to connect """

    transport = 'eci'
    has_pipelining = True

    def __init__(self, *args, **kwargs):
        ssh.Connection.__init__(self, *args, **kwargs)
        self._load_name = self.__module__.split('.')[-1]
        self.set_options()

        if self._play_context.private_key_file:
          display.vvv("EXISTING PRIVATE KEY FILE AVAILABLE, USING IT")
          self._private_key = load_ssh_private_key(open(self._play_context.private_key_file, 'rb').read(), None, default_backend())
        else:
          display.vvv("NO PRIVATE KEY FILE, GENERATING ON DEMAND")
          (self._play_context.private_key_file, self._private_key) = self._create_temporary_key()

        self._public_key = self._private_key.public_key().public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH
        ).decode('utf-8')

        self._last_key_push = datetime.min
    
    def _create_temporary_key(self):
      key = rsa.generate_private_key(
          public_exponent=ECI_KEY_EXPONENT,
          key_size=ECI_KEY_SIZE,
          backend=default_backend()
      )
      pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
      )
      file = tempfile.NamedTemporaryFile(delete=False)
      with file as pem_out:
          pem_out.write(pem)
      display.vvv("TEMPORARY KEY LOCATION: {0}".format(file.name))
      return (file.name, key)

    def exec_command(self, cmd, in_data=None, sudoable=True):
      self.set_option('private_key_file', self._play_context.private_key_file)
      self.set_option('sshpass_prompt', '')
      self.set_option('password', None)
      return ssh.Connection.exec_command(self, cmd=cmd, in_data=in_data, sudoable=sudoable)

    def _bare_run(self, cmd, in_data, sudoable=True, checkrc=True):
      if((datetime.now() - self._last_key_push).total_seconds() > ECI_PUSH_EXPIRY):
          display.vvv("ECI PUB KEY EXPIRING/NOT SENT, PUSHING NOW")
          ##For some reason, playcontext not fully initialized
          ##in testing before barerun, so only getting these arguments now
          _push_key(self._get_boto_args(), self._get_eci_args())
          self._last_key_push = datetime.now()

      return ssh.Connection._bare_run(self, cmd=cmd, in_data=in_data, sudoable=sudoable, checkrc=checkrc)

    def _get_eci_args(self):
      ##TODO Make this cleaner, build once then always return
      if(not hasattr(self, '_instance_id') and self.get_option('instance_id')):
        self._instance_id = self.get_option('instance_id')
      else:
        client = boto3.client('ec2', **self._get_boto_args())
        lookup_address = self._play_context.remote_addr
        display.vvv("NO INSTANCE_ID PROVIDED, ATTEMPTING LOOKUP")
        for filter_name in ('ip-address', 'private-ip-address', 'private-dns-name'):
          filter = [{'Name': filter_name,'Values': [lookup_address ]}]
          response = client.describe_instances(Filters=filter)
          for r in response['Reservations']:
            for i in r['Instances']:
              self._instance_id = i['InstanceId']
              self._availability_zone = i['Placement']['AvailabilityZone']
          ##We've found it, so stop
          if(hasattr(self, '_instance_id')):
            break

      if(not hasattr(self, '_instance_id')):
        raise Exception('No instance_id found')

      if(not hasattr(self, '_availability_zone')):
        client = boto3.client('ec2', **self._get_boto_args())
        response = client.describe_instances(InstanceIds=[self._instance_id])
        for r in response['Reservations']:
          for i in r['Instances']:
            self._availability_zone = i['Placement']['AvailabilityZone']
      return {
            "InstanceId": self._instance_id, 
            "InstanceOSUser": self._play_context.remote_user,
            "SSHPublicKey": self._public_key,
            "AvailabilityZone": self._availability_zone
      }

    def _get_boto_args(self):
      if not hasattr(self, '_boto_args'):
        self._boto_args = {
            "region_name": self.get_option('region'),
            "aws_secret_access_key": self.get_option('aws_secret_key'),
            "aws_access_key_id": self.get_option('aws_access_key')
          }
      return self._boto_args

def _push_key(aws_client_args, eci_args):
  client = boto3.client('ec2-instance-connect', **aws_client_args)
  client.send_ssh_public_key(**eci_args)
