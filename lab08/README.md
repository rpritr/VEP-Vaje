# Vaja 8: Načrtovanje in razvoj varnih sistemov elektronskega poslovanja

📅 **Trajanje: 4 ure**

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

Predavatelj bo posredoval shemo arhitekture obstoječega (izmišljenega) sistema spletne trgovine.  
Primer bo vseboval:  
- spletni strežnik  
- podatkovno bazo  
- administrativni portal  
- uporabnike  
- zunanji ponudnik plačil

### Naloga

🔷 1️⃣ V skupinah analizirajte arhitekturo in odgovorite:  
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