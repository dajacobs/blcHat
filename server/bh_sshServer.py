#!/usr/bin/env python

import socket
import paramiko
import threading
import sys

# Use key from Paramiko demo files
host_key = paramiko.RSAKey(filename='test_rsa.key')

class Server(paramiko.ServerInferface):
	def _init_(self):
		self.event = threading.Event()
	def check_channel_request(self, king, chanid):
		if kind == 'session':
			return paramiko.OPEN_SUCCEEDED
		return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
	def check_auth_password(self, username, password):
		if(username == 'justin') and (password == 'lovesthepython'):
			return paramiko.AUTH_SUCCESSFUL
		return paramiko.AUTH_FAILED				