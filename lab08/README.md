# Vaja 8: Načrtovanje in razvoj varnih sistemov elektronskega poslovanja

V tej vaji boste spoznali, kako že v fazi načrtovanja zagotoviti varnost sistema za elektronsko poslovanje. Prepoznali boste tipične napake arhitektur, analizirali primer obstoječega sistema in pripravili svoj načrt varne arhitekture.

---

# 🧪 Načrtovanje in razvoj varnih sistemov

Mnogi napadi na spletne trgovine in druge sisteme e-poslovanja so posledica slabe zasnove in pomanjkanja varnostnih mehanizmov že v fazi načrtovanja.  
»Security by design« pomeni načrtovati sistem tako, da je varen že od začetka, ne pa da se kasneje varnost dodaja kot popravek.

---

## 1️⃣ Uvod: Cilji

✅ razumeti pomen varnosti v fazi načrtovanja  
✅ analizirati tipične napake v arhitekturah  
✅ pripraviti načrt za varen sistem elektronskega poslovanja  

---

## 2️⃣ Aktivnost: Analiza arhitekture

Analizirajte arhitekturo obstoječega (izmišljenega) sistema spletne trgovine.  
Primer naj vsebuje:  
- spletni strežnik  
- podatkovno bazo  
- administrativni portal  
- uporabnike  
- zunanji ponudnik plačil


Podjetje Shopko upravlja spletno trgovino, ki strankam omogoča nakup izdelkov prek spleta. Uporabniki do sistema dostopajo z uporabo spletnega brskalnika ali mobilne naprave. Vsa komunikacija poteka prek spletnega strežnika, ki hkrati streže uporabniški vmesnik in aplikacijski programski vmesnik (API), preko katerega se izvajajo vse funkcionalnosti sistema, kot so prijava uporabnikov, oddaja naročil in pregled zgodovine nakupov.

Spletni strežnik je povezan s podatkovno bazo, v kateri so shranjeni podatki o uporabnikih, izdelkih, naročilih in plačilih. Podatkovna baza se nahaja v notranjem omrežju in ni neposredno dostopna iz interneta, vendar ima aplikacija do nje poln dostop. 

Administrativni portal je namenjen zaposlenim, ki upravljajo spletno trgovino. Preko njega administratorji urejajo izdelke, obdelujejo naročila, potrjujejo vračila in dostopajo do podatkov o strankah. Portal je dostopen prek posebnega naslova, s prijavo uporabniškega imena in gesla.

Plačila v spletni trgovini se izvajajo prek zunanjega ponudnika plačilnih storitev. Ko uporabnik odda naročilo, je preusmerjen na plačilno stran ponudnika, po uspešno izvedenem plačilu pa ponudnik pošlje povratno obvestilo (t. i. webhook) nazaj v sistem spletne trgovine. Sistem ob prejemu tega obvestila naročilo označi kot plačano. 


### Naloga

🔷 1️⃣ Analizirajte arhitekturo in odgovorite:  
- Katera področja so ranljiva?  
- Ali so gesla varno shranjena?  
- Kako je urejen dostop za administratorje?  
- Ali je zagotovljena zaupnost, celovitost, razpoložljivost?

🔷 2️⃣ Označite ključne šibkosti (npr. podatkovna baza neposredno dostopna iz interneta, gesla v čistopisu …)

---

## 3️⃣ Aktivnost: Načrt varnega sistema

Pripravite osnovni načrt arhitekture varnega sistema:  
✅ kako zaščititi podatke uporabnikov (šifriranje, dostop)  
✅ kako zaščititi komunikacijo (HTTPS, TLS)  
✅ kako ločiti cone zaupanja (DMZ, notranje omrežje)  
✅ kako obvladovati dostop (vloge, najmanjša potrebna pravica)

---

## 4️⃣ Refleksija in poročilo

### 📝 Navodila za poročilo

- Opišite glavne pomanjkljivosti obstoječe arhitekture.  
- Pripravite osnovno skico varne arhitekture s pojasnili.  
- Katere varnostne standarde bi upoštevali (npr. GDPR, PCI-DSS)?  
- Kako bi zagotovili skladnost in preverjanje varnosti skozi čas?

---

📑 Poročilo oddajte v pisni obliki (priporočeno: 2–3 strani).  
📣 Pomembno: dokument naj bo razumljiv tudi ne-tehničnim deležnikom (vodstvo podjetja).