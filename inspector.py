#!usr/bin/env	python


import os,sys
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class inspector(object):

	def __init__(self):
		self.kernel_version = ""
		self.start_dir = ""
		self.environnement = ""
		self.kernel_version = ""
		self.history_pattern = [
			{"search":"ssh","content":"possible SSH login"},
			{"search":"mysql ","content":"MySQL database connexion found"},
			{"search":"ftp ","content":"Possible FTP login"}
		]
		self.history_listing = ['.bash_history','.mysql_history','.bashrc','.zshrc','.zsh_history']
		self.kernel_exploit = [
		{"name":'w00t', "version":['2.4.10','2.4.16','2.4.17','2.4.18','2.4.19','2.4.20','2.4.21']},
		{"name":"brk", "version":['2.4.10','2.4.18','2.4.19','2.4.20','2.4.21','2.4.22']},
		{"name":'pp_key', "version":['3.8.0', '3.8.1', '3.8.2', '3.8.3', '3.8.4', '3.8.5', '3.8.6', '3.8.7', '3.8.8', '3.8.9', '3.9', '3.10', '3.11', '3.12', '3.13', '3.4.0', '3.5.0', '3.6.0', '3.7.0', '3.8.0', '3.8.5', '3.8.6', '3.8.9', '3.9.0', '3.9.6', '3.10.0', '3.10.6', '3.11.0', '3.12.0', '3.13.0', '3.13.1']},
		{"name":'overlayfs', "version":['3.8.0','3.8.1', '3.8.2', '3.8.3', '3.8.4', '3.8.5', '3.8.6', '3.8.7', '3.8.8', '3.8.9', '3.9', '3.10', '3.11', '3.12', '3.13', '3.4.0', '3.5.0', '3.6.0', '3.7.0', '3.8.0', '3.8.5', '3.8.6', '3.8.9', '3.9.0', '3.9.6', '3.10.0', '3.10.6', '3.11.0', '3.12.0', '3.13.0', '3.13.1']},
		{"name":'rawmodePTY', "version":['2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36', '2.6.37', '2.6.38', '2.6.39', '3.14', '3.15']},
		{"name":'timeoutpwn', "version":['3.4 ', '3.5 ', '3.6 ', '3.7 ', '3.8 ', '3.8.9 ', '3.9 ', '3.10 ', '3.11 ', '3.12 ', '3.13 ', '3.4.0 ', '3.5.0 ', '3.6.0 ', '3.7.0 ', '3.8.0 ', '3.8.5 ', '3.8.6 ', '3.8.9 ', '3.9.0 ', '3.9.6 ', '3.10.0 ', '3.10.6 ', '3.11.0 ', '3.12.0 ', '3.13.0 ', '3.13.1']},
		{"name":'perf_swevent', "version":['3.0.0', '3.0.1', '3.0.2', '3.0.3', '3.0.4', '3.0.5', '3.0.6', '3.1.0', '3.2', '3.3', '3.4.0', '3.4.1', '3.4.2', '3.4.3', '3.4.4', '3.4.5', '3.4.6', '3.4.8', '3.4.9', '3.5', '3.6', '3.7', '3.8.0', '3.8.1', '3.8.2', '3.8.3', '3.8.4', '3.8.5', '3.8.6', '3.8.7', '3.8.8', '3.8.9']},
		{"name":'msr', "version":['2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36', '2.6.37', '2.6.38', '2.6.39', '3.0.0', '3.0.1', '3.0.2', '3.0.3', '3.0.4', '3.0.5', '3.0.6', '3.1.0', '3.2', '3.3', '3.4', '3.5', '3.6', '3.7.0', '3.7.6']},
		{"name":'memodipper', "version":['2.6.39', '3.0.0', '3.0.1', '3.0.2', '3.0.3', '3.0.4', '3.0.5', '3.0.6', '3.1.0']},
		{"name":'american-sign-language', "version":['2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36']},
		{"name":'full-nelson', "version":['2.6.31', '2.6.32', '2.6.35', '2.6.37']},
		{"name":'half_nelson', "version":['2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36']},
		{"name":'rds', "version":['2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36']},
		{"name":'pktcdvd', "version":['2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36']},
		{"name":'ptrace_kmod2', "version":['2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34']},
		{"name":'video4linux', "version":['2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33']},
		{"name":'can_bcm', "version":['2.6.18','2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34', '2.6.35', '2.6.36']},
		{"name":'reiserfs', "version":['2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31', '2.6.32', '2.6.33', '2.6.34']},
		{"name":'do_pages_move', "version":['2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31']},
		{"name":'pipe.c_32bit', "version":['2.4.4', '2.4.5', '2.4.6', '2.4.7', '2.4.8', '2.4.9', '2.4.10', '2.4.11', '2.4.12', '2.4.13', '2.4.14', '2.4.15', '2.4.16', '2.4.17', '2.4.18', '2.4.19', '2.4.20', '2.4.21', '2.4.22', '2.4.23', '2.4.24', '2.4.25', '2.4.26', '2.4.27', '2.4.28', '2.4.29', '2.4.30', '2.4.31', '2.4.32', '2.4.33', '2.4.34', '2.4.35', '2.4.36', '2.4.37', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30', '2.6.31']},
		{"name":'udp_sendmsg_32bit', "version":['2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19']},
		{"name":'sock_sendpage', "version":['2.4.4', '2.4.5', '2.4.6', '2.4.7', '2.4.8', '2.4.9', '2.4.10', '2.4.11', '2.4.12', '2.4.13', '2.4.14', '2.4.15', '2.4.16', '2.4.17', '2.4.18', '2.4.19', '2.4.20', '2.4.21', '2.4.22', '2.4.23', '2.4.24', '2.4.25', '2.4.26', '2.4.27', '2.4.28', '2.4.29', '2.4.30', '2.4.31', '2.4.32', '2.4.33', '2.4.34', '2.4.35', '2.4.36', '2.4.37', '2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30']},
		{"name":'sock_sendpage2', "version":['2.4.4', '2.4.5', '2.4.6', '2.4.7', '2.4.8', '2.4.9', '2.4.10', '2.4.11', '2.4.12', '2.4.13', '2.4.14', '2.4.15', '2.4.16', '2.4.17', '2.4.18', '2.4.19', '2.4.20', '2.4.21', '2.4.22', '2.4.23', '2.4.24', '2.4.25', '2.4.26', '2.4.27', '2.4.28', '2.4.29', '2.4.30', '2.4.31', '2.4.32', '2.4.33', '2.4.34', '2.4.35', '2.4.36', '2.4.37', '2.6.0', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29', '2.6.30']},
		{"name":'exit_notify', "version":['2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29']},
		{"name":'udev', "version":['2.6.25', '2.6.26', '2.6.27', '2.6.28', '2.6.29']},
		{"name":'ftrex', "version":['2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22']},
		{"name":'vmsplice2', "version":['2.6.23', '2.6.24']},
		{"name":'vmsplice1', "version":['2.6.17', '2.6.18', '2.6.19', '2.6.20', '2.6.21', '2.6.22', '2.6.23', '2.6.24', '2.6.24.1']},
		{"name":'h00lyshit', "version":['2.6.8', '2.6.10', '2.6.11', '2.6.12', '2.6.13', '2.6.14', '2.6.15', '2.6.16']},
		{"name":'raptor_prctl', "version":[ '2.6.13', '2.6.14', '2.6.15', '2.6.16', '2.6.17']},
		{"name":'elflbl', "version":['2.4.29']},
		{"name":'caps_to_root', "version":['2.6.34', '2.6.35', '2.6.36']},
		{"name":'mremap_pte', "version":['2.4.20', '2.2.24', '2.4.25', '2.4.26', '2.4.27']},
		{"name":'krad3', "version":['2.6.5', '2.6.7', '2.6.8', '2.6.9', '2.6.10', '2.6.11']}
		]
		self.logo()
		self.load_inspection()

	def logo(self):
		os.system('clear')
		print """  _____                           _             
  \_   \_ __  ___ _ __   ___  ___| |_ ___  _ __ 
   / /\/ '_ \/ __| '_ \ / _ \/ __| __/ _ \| '__|
/\/ /_ | | | \__ \ |_) |  __/ (__| || (_) | |   
\____/ |_| |_|___/ .__/ \___|\___|\__\___/|_|   
                 |_|                            
"""

	def information(self):
		kernel_version = os.popen('uname -r').read()
		uname = os.popen('uname -a').read()
		process_list = os.popen('ps axco user,command | grep root').read()
		print "========="
		print "= [!] User  : "+os.popen('whoami').read().strip()
		print "= [!] Group : "+os.popen('id -Gn').read().strip()[:20]  
		print "= [!] Shell : "+self.environnement
		print "= [!] "+uname.strip()
		print "========"

	def check_exploit(self):
		for line in self.kernel_exploit:
			vulnerable = False
			print bcolors.OKBLUE + "* "+bcolors.ENDC + "Checking : " + line['name']
			for version in line['version']:
				if version == self.kernel_version:
					vulnerable = True
			if vulnerable == True:
				print bcolors.OKGREEN + "* Success" + bcolors.ENDC
			else:
				print bcolors.FAIL + "* Not vulnerable" + bcolors.ENDC
			time.sleep(0.3)

	def history_file(self):
		find = []
		possible = []
		print bcolors.WARNING + "* Checking history file" + bcolors.ENDC
		try:
			for line in self.history_listing:
				if self.start_dir[-1:] != "/":
					read_path = self.start_dir + "/" + line.strip()
				else:
					read_path = self.start_dir + line.strip()
				if os.path.exists(read_path):
					find.append(read_path)
			if len(find) > 0:
				for file in find:
					count = 0
					print bcolors.OKGREEN + "* reading : " + file + bcolors.ENDC
					content_file = open(file).read().split('\n')
					print bcolors.WARNING + "* total line : " + str(len(content_file)) + bcolors.ENDC
					for file_line in content_file:
						count += 1
						for line_search in self.history_pattern:
							if line_search['search'] in file_line:
								if line_search['content'] not in possible:
									possible.append(line_search['content'])
					for line in possible:
						print bcolors.OKBLUE + "* "+ line + bcolors.ENDC

			else:
				print bcolors.FAIL + "* Can't get history file..." + bcolors.ENDC
		except:
			print bcolors.FAIL + "* Can't read history file."

	def load_inspection(self):
		error = False
		print "* Get user directory..."
		try:
			home = os.path.expanduser("~")
			self.start_dir = home
			print bcolors.OKGREEN + "* success : " + bcolors.BOLD + str(home) + bcolors.ENDC
		except:
			print bcolors.OKRED + "* Fail : can't get users directory!" + bcolors.ENDC
			error = True
		print "* Get shell environnement..."
		try:
			shell_environement = os.environ['SHELL']
			shell_environement = shell_environement.rsplit("/", 1)[1]
			self.environnement = shell_environement
			print bcolors.OKGREEN + "* success : "+bcolors.BOLD + str(self.environnement) + bcolors.ENDC
		except:
			print bcolors.OKRED + "* Fail : can't get shell environnement!" + bcolors.ENDC

		print "* Get kernel version..."
		try:
			kernel_version = os.popen('uname -r').read().strip()
			self.kernel_version = kernel_version
			print bcolors.OKGREEN + "* success : " + bcolors.BOLD + str(self.kernel_version) + bcolors.ENDC
		except:
			print bcolors.OKRED + "* Fail : can't get kernel!" + bcolors.ENDC
		if error == False:
			self.information()
			print bcolors.WARNING + "* Checking exploit for : " + str(self.kernel_version) + "..." + bcolors.ENDC
			time.sleep(1)
			self.check_exploit()
			self.history_file()



inspector = inspector()