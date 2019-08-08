import os
import sys
import time

print("""by SedSec


	""")
print("""Selecione sua Distribuicao Linux:



	""")
print("(1) kali Linux x64")
print("(2) kali Linux x86")
print("(3) Ubunto x64")
print("""(3) Ubunto x86
	""")
dist = raw_input("#: ")

if dist == 1:
	print("Instalando dependencias...")
	os.system("apt-get install linux-headers-4.19.0-kali5-all -y")
	os.system("apt-get install linux-image-cloud-amd64 -y")
	os.system("chmod 777 vbox.run && ./vbox.run")

else:
	print("Instalando dependencias...")
	os.system("apt-get install linux-headers-4.19.0-kali5-all-amd64 -y")
	os.system("apt-get install linux-image-4.19.0-kali5-amd64 -y")
	os.system("chmod 777 vbox.run && ./vbox.run")
	
os.system("clear")
print("Reinicie o Computador 2 Vezes")
time.sleep(7)
os.system("reboot now")
