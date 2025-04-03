# project_work_sistemi_informativi
Il dataset riporta informazioni riguardanti delle case nella regione di Sindian, Nuova Taipei, Taiwan. 
Le variabili in esso presenti sono:
X1, data della transazione;
X2, età della casa (in anni);
X3, distanza dalla stazione MRT più vicina (in metri);
X4, numero di minimarket vicini;
X5, latitudine;
X6, longitudine;
Y, prezzo in 10000 New Taiwan Dollar/Ping.
Dopo aver convertito la variabile target in TWD/mq, si applicano due modelli, entrambi con il prezzo al mq come target, uno con longitudine e latitudine come predittori, l'altro con le variabili X2, X3 e X4 come covariate. Potranno essere usati entrambi nella web app per stimare il prezzo della casa, a seconda delle informazioni che si hanno a disposizione.
Per eseguire l'applicazione basta runnare il codice sul terminale tramite il comando "streamlit run project_trematerra.py".
Infine è stata creata una mappa interattiva delle case presenti nel dataset per poterne visualizzare la posizione e le caratteristiche.
La mappa è visualizzabile al seguente link: https://public.tableau.com/app/profile/raffaele.trematerra3300/viz/mappa_prezzi_case_Sindian/Foglio1
