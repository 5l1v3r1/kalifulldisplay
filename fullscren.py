import os
import sys

print("""


	""")
print("""Selecione sua Distribuicao Linux:



	""")
print("(1) kali Linux x64")
print("(2) kali Linux x86")
print("(3) Ubunto x64")
print("""(3) Ubunto x86
	""")
dist = raw_imput("#: ")

if dist == 1:
	print("Instalando dependencias...")
	os.system("apt-get install linux-headers-4.19.0-kali5-all-amd64")
	os.system("apt-get install linux-image-4.19.0-kali5-amd64")
	os.system("chmod 777 vbox.run && ./vbox.run")

elif dist == 2:
	print("Instalando dependencias...")
	os.system("apt-get install linux-headers-4.19.0-kali5-all")
	os.system("apt-get install linux-image-cloud-amd64")
	os.system("chmod 777 vbox.run && ./vbox.run")

print("Reinicie o Computador 2 Vezes")

os.system("reboot now")