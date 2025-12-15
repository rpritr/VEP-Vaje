# Vaja: Enkripcija datotek in varna izmenjava z GPG Suite

## Namen vaje
Namen vaje je, da spoznamo:
✅  osnovne koncepte asimetrične kriptografije,
✅  uporabo GPG (OpenPGP) za zaščito podatkov,
✅  generiranje kriptografskih ključev,
✅  enkripcijo in dekripcijo datotek,
✅  varno izmenjavo podatkov med pošiljateljem in prejemnikom.

Vaja simulira realen scenarij varnega pošiljanja občutljive datoteke po elektronski pošti.

---

## Orodja in zahteve
- Nameščeno orodje: **GPG Suite**
  - https://gpgtools.org
- Elektronska pošta (simulacija pošiljanja datoteke)
- Tekstovni urejevalnik (npr. TextEdit, VS Code)

---

## Opis scenarija
Podjetje *SecureTrade d.o.o.* mora zunanjemu sodelavcu poslati datoteko, ki vsebuje zaupne podatke (npr. pogodbo ali finančno poročilo).

Zaradi varnostnih zahtev:
- datoteka ne sme biti poslana v nešifrirani obliki,
- vsebino sme prebrati samo predvideni prejemnik,
- komunikacija poteka preko običajne e-pošte.

---

## Naloga 1: Generiranje GPG ključev
1. Odprite **GPG Keychain**.
2. Ustvarite nov GPG ključ:
   - ime in priimek (ali psevdonim),
   - e-poštni naslov,
   - močno geslo za zaščito zasebnega ključa.
3. Preverite, da imate:
   - **javni ključ (public key)**,
   - **zasebni ključ (private key)**.

### Razmislek
- Zakaj zasebnega ključa nikoli ne delimo z drugimi?
- Kaj se zgodi, če izgubimo geslo zasebnega ključa?

---

## Naloga 2: Izvoz in izmenjava javnega ključa
1. Izvozite svoj **javni ključ** v datoteko.
2. Javni ključ izmenjajte s sošolcem (simulacija prejemnika).
3. Uvozite javni ključ prejemnika v svoj GPG Keychain.

### Razmislek
- Zakaj je varno deliti javni ključ?
- Kako lahko preverimo, da javni ključ res pripada pravi osebi?

---

## Naloga 3: Enkripcija datoteke
1. Ustvarite testno datoteko (npr. `zaupno.txt`).
2. Datoteka naj vsebuje kratko zaupno sporočilo.
3. Enkriptirajte datoteko z uporabo **javnega ključa prejemnika**.
4. Preverite, da nastane enkriptirana datoteka (npr. `.gpg`).

### Razmislek
- Zakaj pošiljatelj ne potrebuje zasebnega ključa prejemnika?
- Ali lahko pošiljatelj sam dekriptira datoteko?

---

## Naloga 4: Pošiljanje in dekripcija
1. Enkriptirano datoteko posredujte prejemniku (simulacija e-pošte).
2. Prejemnik datoteko dekriptira s svojim **zasebnim ključem**.
3. Preverite, da je vsebina pravilno obnovljena.

### Razmislek
- Kaj se zgodi, če enkriptirano datoteko prestreže tretja oseba?
- Kako pomembna je zaščita naprave, kjer hranimo zasebni ključ?

---

## Naloga 5: Analiza varnosti
Odgovorite na naslednja vprašanja:
- Kakšne vrste napadov preprečuje uporaba GPG?
- Ali enkripcija zagotavlja tudi avtentičnost pošiljatelja?
- Kako bi dodali še digitalni podpis?
- Kakšne so omejitve uporabe GPG v realnem poslovnem okolju?

---

## Oddaja naloge
Oddajte kratko poročilo, ki vsebuje:
  - opis izvedbe nalog,
  - posnetke zaslona ključnih korakov,
  - odgovore na vprašanja za razmislek,
  - osebno refleksijo o uporabnosti GPG v e-poslovanju.

---

## Dodatna vprašanja (za refleksijo)
- Zakaj večina uporabnikov še vedno ne uporablja PGP/GPG za e-pošto?
- Kakšna je razlika med TLS zaščito e-pošte in end-to-end enkripcijo?
- Kako se GPG primerja z modernimi orodji (npr. Signal, ProtonMail)?

---