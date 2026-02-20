# Django To-Do -sovellus

Tämä on yksinkertainen To-Do-lista, joka on rakennettu Pythonilla ja Django-sovelluskehyksellä. Projekti on tehty osana HAMK:n AI Expert-kurssin harjoitustehtävää, ja sen tarkoituksena on oppia Djangon perusteita (Models, Views, Templates) sekä tekoälyn hyödyntämistä koodauksessa.

## Ominaisuudet
* Tehtävien tarkastelu listana
* Uusien tehtävien lisääminen
* Tehtävien poistaminen
* Yksinkertainen käyttöliittymä (CSS & Google Fonts)
* Djangon sisäänrakennettu hallintapaneeli (Admin)

## Käytetyt teknologiat
* **Backend:** Python 3, Django
* **Frontend:** HTML, CSS
* **Tietokanta:** SQLite (Djangon oletus)

## Miten käynnistää projekti paikallisesti
Varmista, että koneellasi on Python asennettuna.

1. Kloonaa tämä repositorio koneellesi.
2. Siirry projektikansioon terminaalissa.
3. Aja migraatiot (tietokannan luonti):
   `python manage.py migrate`
4. Käynnistä paikallinen palvelin:
   `python manage.py runserver`
5. Avaa selain ja mene osoitteeseen `http://127.0.0.1:8000/`