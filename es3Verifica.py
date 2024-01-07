
ip_address = ["192.168.222.0/27", "192.168.100.0/24", "192.168.200.0/28", "192.168.50.0/22"]

file = open("mask.txt", "w")
for ip in ip_address:
    ip_add, sub_str = ip_address.split("/")
    sub = int(sub_str)
    binario = sub * '1' + '0' * (32 - sub)
    group1 = int(binario[0:8],2)
    group2 = int(binario[8:16],2)
    group3 = int(binario[16:24],2)
    group4 = int(binario[24:],2)

    lista = [group1, group2, group3, group4]
    lista = [str(elemento) for elemento in lista]
    
file.write("")

