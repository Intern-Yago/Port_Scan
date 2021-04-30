import socket, argparse, datetime, sys
horário = f'{datetime.datetime.today().hour}:{datetime.datetime.today().minute}:{datetime.datetime.today().second}'
data = f'{datetime.date.today().day}/{datetime.date.today().month}/{datetime.date.today().year}'

parser = argparse.ArgumentParser(description='teste arg')
parser.add_argument('Ip')
parser.add_argument('--portas',"-p")
args = parser.parse_args()

print(f'Realzado em {data}\n{horário}')
print(f'Scan em: {args.Ip}\n\n')
try:
    portas = int(args.portas)
except:
    portas = 200

door = {}
todas = []
t = 0
for porta in range(1, portas+1):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    try:
        codigo = cliente.connect_ex((args.Ip, porta))
    except:
        print('ERROR HOST [desligado/bloqueado/inexistente]')
        exit(-1)
    else:
        todas.append(porta)
        if codigo == 0:
            codigo = 'open'
            door[f'{str(porta)}'] = codigo
            t =1
        else:
            codigo = 'closed'
            door[f'{str(porta)}'] = codigo

if len(todas) > 30 and t==1:
    print(f'{"PORTA":<10} STATE')
    for k,v in door.items():
        if v == 'open':
            print(f'{k:<10} {v}')
elif len(todas) != 0 and t==1:
    print(f'{"PORTA":<10} STATE')
    for k,v in door.items():
        print(f'{k:<10} {v}')
else:
    print(f'All {portas} ports are closed')