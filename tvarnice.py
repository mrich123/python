print("Konfigurátor zdícího systému")
print("****************************")
uzivatelske_jmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")

uzivatel_jmeno_kontrola = "stavebnik"
heslo_kontrola = "stavba"

if uzivatelske_jmeno == uzivatel_jmeno_kontrola and heslo == heslo_kontrola:
    print("Vítejte")
    sirka_steny=float(input("Zadejte délku stěny: "))
    vyska_steny=float(input("Zadej výšku stěny: "))
    vyska_okna=float(input("Zadej výšku okna: "))
    sirka_okna=float(input("Zadej šířku okna: "))
    
    plocha_okna=vyska_okna*sirka_okna
    print(f"Plocha okna: {plocha_okna}")
    plocha_zdi_bez_okna=-1*(plocha_okna-vyska_steny*sirka_steny)
    print(f"Plocha stěny bez okna: {plocha_zdi_bez_okna}")
    plocha_zdi_s_oknem=vyska_steny*sirka_steny
    print(f"Plocha stěny včetně okna: {plocha_zdi_s_oknem}")
    pocet_tvarnic = plocha_zdi_bez_okna/0.1
    print(f"Počet tvárnic potřebných k vyzdění plochy stěny: {pocet_tvarnic}")

    seznam_pobocek = [ 
    [" Praha", "tvárnice", "500"],
    [" Brno", "tvárnice", "300"],
    [" Ostrava", "tvárnice", "700"]
    ]
    print("|**********************************************************|")
    print("| Město         | Druh materiálu  | Počet kusů na pobočce  |")
    print("|**********************************************************|")
    for mesto, druh_mat, pocet_kusu_na_pobocce in seznam_pobocek:
        veta = "|{:<15}|  {:<15}|  {:<22}|".format(mesto, druh_mat, pocet_kusu_na_pobocce)
        print(veta)
else:
    print("Zdali jste chybně užívatelské jméno nebo heslo")