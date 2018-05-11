# Käyttöohje
Lataa tiedosto _nbodysim-final.whl_ ja _random__input__file.dat_ [lopullisesta releasesta](https://github.com/LeeviT/otm-harjoitustyo/releases/tag/v1.0-beta).
## Ohjelman käynnistäminen
Voit käynnistää ohjelman komennolla 
```
python3.6 nbodysim-final.whl
```
## Parametrien syöttäminen
Ohjelma käynnistyy seuraavanlaiseen näkymään
<img src=https://i.imgur.com/6QRLhTR.png?1>
_Choose a input file_-nappulasta aukeaa tiedostoselain jonka kautta voit valita input-tiedoston, eli esimerkiksi _random__input__file.dat_ jonka juuri latasit. _Number of timesteps_-tekstin oikealla puolella olevaan kenttään voit syöttää aika-askelten määrän, eli positiivisen kokonaisluvun. _Accuracy of simulation_-slaiderista säädetään simulaation tarkkuutta (1=epätarkin, 10=tarkin). _Pass values to simulation_-napista parametrit annetaan ohjelmalle, minkä jälkeen voikin käynnistää varsinaisen laskemisvaiheen _Calculate!_-napista. Tällöin aukeaa seuraava näkymä
<img src=https://i.imgur.com/fKAE6Qr.jpg?1>
Näkymä näyttää mitä aika-askelta ohjelma parhaillaan suorittaa ja aika-askelten kokonaismäärän. Odota kunnes ohjelma saa laskettua ja avautuu seuraava näkymä
<img src=https://i.imgur.com/a9jL5rL.jpg?1>
jossa on output-tiedoston nimi. Output-tiedosto tallentuu samaan kansioon kuin missä suoritit ohjelman. Voit nyt sulkea molemmat ikkunat ja tarkastella generoitunutta output-tiedostoa.
