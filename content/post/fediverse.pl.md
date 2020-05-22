---
title: Fediwersum jak miecz obosieczny
date: 2020-05-22T14:55:29+0200
---

Przez długie lata moim ulubionym portalem społecznościowym był [Twitter](https://twitter.com). Nie wiem, czy to przez krótkie wpisy, czy przez łatwe nawiązywanie znajomości, czy przez coś innego, ale tak było. Jednak od trzech lat moja uwaga dzieli się między Twittera a tak zwane *fediwersum*. Chciałbym krótko opowiedzieć, czym to *fediwersum* jest, jakie ma problemy i jak to się ma do Twittera.

## Rys historyczny

### Czym jest Fediwersum i dlaczego?

W kwietniu 2017 roku z czeluści Githuba do społecznego światka osób obytych z technologią (nie stricte programistów) przebił się [Mastodon](https://joinmastodon.org) – oprogramowanie do hostowania portali społecznościowych podobnych do Twittera. Różnica polegała na tym, że tak postawione serwery nie były osobnymi „zamkniętymi ogrodami”, ale mogły wymieniać między sobą wpisy swoich użytkowników.

Tak więc użytkownik [@michcio@om.nom.pl](https://om.nom.pl/michcio) mógł bez problemu porozumiewać się z [@fiskus@a.nom.pl](https://a.nom.pl/fiskus), a do wątku mógł się bez problemu włączyć również [@Michcioperz@niu.moe](https://niu.moe/@Michcioperz). (Na tym przykładzie widać, że nazwa użytkownika przypomina adres email.) Tak powstała sieć społecznościowa, z racji że serwery *były ze sobą w federacji*, nazwała się po angielsku *fediverse*, po polsku więc *fediwersum*, a zdrobniale *fedi*.

Sympatię twitterowej technolewicy Mastodon zaskarbił sobie możliwościami takimi jak dostosowywanie prywatności każdego wpisu (publiczny lub tylko dla znajomych) lub ukrycie treści wpisu i załączonych obrazków za wybranym *Content Warning*. Ważnym argumentem za ucieczką na Mastodon była też obietnica sieci społecznościowej wolnej od nazistów, cokolwiek miał na myśli autor Mastodona – o tym później.

### Dlaczego nie nazywamy tego Mastodon?

Pomysł federowania mini-twitterów nie był nowy, nawet sam protokół — OStatus — został zapożyczony z powstałego w 2008 roku oprogramowania StatusNet (obecnie [GNU social](https://gnu.io/social/)), natomiast Mastodon wyglądał dużo lepiej niż StatusNet <sup>\[potrzebny cytat\]</sup> i nie był napisany w PHP.

Wkrótce okazało się, że zastosowane pod maską Mastodona Ruby on Rails nie jest super wydajne, ale administratorzy większych *instancji* — bo tak mówi się o serwerach fediwersum — skądś znajdowali fundusze na więcej rdzeniów, a administratorzy mniejszych albo pisali skrypt restartujący Sidekiqa co kilka-kilkanaście godzin, albo przesiadali się z Mastodona na inne oprogramowanie serwerowe: Pleromę.

### Co poza Mastodonem?

[Pleroma](https://pleroma.social) również czerpała z bogatego PHPowego dziedzictwa kulturowego, jako że pierwszym jej napisanym komponentem był interfejs graficzny, który można było wgrać na swoją instancję StatusNet. W przeciwieństwie do oryginalnego interfejsu dawał większą interaktywność, np. odpytywał dynamicznie serwer o nowe wpisy i nie wymagał przełądowania strony przy każdym działaniu.

Później twórcy projektu uznali, że lepiej będzie napisać od podstaw własny serwer w memicznym języku programowania Elixir, dającym bogate narzędzia do budowania wysokowydajnych serwisów internetowych. Powstałe oprogramowanie miało drastycznie niższe zużycie pamięci, co ucementowało pozycję Pleromy wśród osób hostujących swoje instancje na płytkach Raspberry Pi.

Później do puli dostępnych serwerów zaczęły dołączać kolejne projekty, takie jak kulturowo silnie japoński [Misskey](https://github.com/syuilo/misskey) i radykalnie minimalistyczny (i ogólnie radykalny) [Honk](https://humungus.tedunangst.com/r/honk) ale też bardziej odbiegające od konwencji Twittera: portal do wymiany materiałów edukacyjnych [MoodleNet](https://moodle.net) czy oparty o WebTorrenty klon YouTube'a [PeerTube](https://joinpeertube.org). Zmianie uległ też najszerzej używany protokół wymiany wpisów – pozbyto się słabo udokumentowanego OStatusa, a w jego miejsce przyjęto [ActivityPub](https://activitypub.rocks), który doczekał się nawet uznania przez W3C za „rekomendowany standard”.

### To o co w końcu chodzi z tymi nazistami?

Jak wspomniałem wcześniej, twórca Mastodona spraszając lewicę i społeczności LGBT z Twittera mówił o tym, że budowana przez niego sieć będzie odporna na nazistów i środowiska takie jak GamerGate. Dla wielu osób dołączających do Mastodona było to o tyle ważne, że uważały moderację na Twitterze za zbyt spolegliwą, czuły się zagrożone.

Jednak oddolna moderacja była kusząca nie tylko dla tych, którym moderacji brakowało, ale też dla tych, dla których jakakolwiek moderacja była niepożądana. Nie dość, że od początku powstawały *free speech*-owe instancje Mastodona godzące w kreowany tak wizerunek sieci, to w pewnym momencie popularny wśród amerykańskiej *alt-prawicy* zamkniętoźródłowy portal Gab zmigrował się na kopię kodu źródłowego Mastodona. O ile miałbym poważne wątpliwości, czy Gab jest najbardziej jadowitą instancją, to jednak ok. 1 miliona użytkowników ma spory przemiał.

Skutkiem tych zajść z fediwersum wyrysowało się kilka podgrafów. Wyraźny podział jest trudny do wykonania, ale myślę, że da się wyłonić mniej więcej kategorie: zwolenników wolności słowa jako wartości najwyższej, zwolenników blokowania instancji z pierwszej grupy lub bezwładnie z nimi federujących, Japończyków ([chciałbym nie musieć tego wyjaśniać](https://en.wikipedia.org/wiki/Legal_status_of_drawn_pornography_depicting_minors)) oraz małe instancje zachowujące politykę równych odległości (por. polska polityka zagraniczna późnych lat 1930.).

Wśród grupy drugiej wykształciła się praktyka ogłaszania, kogo warto blokować. Powstawały nawet repozytoria na Githubie z bogatą argumentacją i dowodami, dlaczego warto. Przez pewien czas w grupie tej krążył też pogląd, że Pleroma jest oprogramowaniem nazistowskim, wynikający po części z tego, że wiele instancji z grupy pierwszej działało na Pleromie, bo była tania w utrzymaniu. Dla mnie osobiście był to pogląd o tyle zabawny, że Pleroma posiadała bogatsze niż na Mastodonie mechanizmy automatycznego moderowania wpisów z pozostałych instancji.

Istnieje też problem bardziej techniczny – protokół ActivityPub jest zaprojektowany w sposób dość naiwny, w szczególności sekcja specyfikacji dotycząca bezpieczeństwa jest oznaczona jako nienormatywna. Podczas transportu wpisów z instancji źródłową na instancje osób obserwujących wpisy otrzymują niezaprzeczalny podpis kryptograficzny. Taki wpis może zostać ujawniony przez wrogiego obserwującego razem z podpisem.

## Miecze obosieczne

Jak widać, fediwersum ma swoje problemy i sam czasem zastanawiam się, czy warto tam siedzieć mimo tych problemów.

Zwykle jednak dochodzę do wniosku, że warto, tylko trzeba mieć świadomość tych problemów, bo często wynikają one po prostu z zalet tej sieci:

### Możesz (musisz) moderować

To jest chyba ta zaleta, dla której sporo osób tutaj przyszło: jeżeli ktoś cię atakuje, to możesz zablokować jego albo całą jego instancję.

Z drugiej strony mam taką obserwację z instancji, na których byłem — jako administrator bądź użytkownik — że w pewnym momencie musisz przyjąć jakąś strategię moderacji, bo trafisz na takich ludzi, których zachowanie będzie ostro poza twoją strefą komfortu.

### Możesz samemu ustalić reguły swojej instancji (i nie musisz się ze wszystkimi zgadzać, a oni z tobą)

Możesz założyć instancję, na której nie ma zasad (jeżeli mieszkasz w kraju, w którym nie zostanie ci za to odebrany serwer lub adres IP).

Możesz założyć instancję, na której nie wolno przeklinać.

Możesz założyć [instancję, na której nie wolno używać litery E](https://oulipo.social) albo [taką, na której można używać tylko litery E](https://dolphin.town).

Musisz jednak mieć na uwadze, że z jednej strony ludzie patrzą na twoje reguły i na tej podstawie decydują, czy się z tobą kolegować, a z drugiej strony są ludzie, którzy nie będą patrzeć na twoje reguły, tylko powysyłają ci obraźliwe komentarze, aż ich zablokujesz (lub zaakceptujesz).

### Możesz łatwo tworzyć śmieszne boty (spamerzy też mogą)

Konta tworzy się łatwo. Ba, nawet instancje tworzy się dosyć łatwo. Dzięki temu możesz tworzyć [boty piszące śmieszne rzeczy](https://botsin.space/@jouns), [boty wrzucające śmieszne obrazki](https://botsin.space/@dogebot), [boty wrzucające prognozę pogody dla losowych miast](https://botsin.space/@randomweather) i wiele innych.

Niestety czasami (nie często, bo fedi jest nadal za mało popularne) zdarzają się fale spamu, więc pewnie prędzej czy później jakiś spambot zaproponuje ci dołączenie do *Don't Marry Movement*, opisując trzy najważniejsze reguły tego ruchu.

### Nie możesz łatwo przeszukiwać wszystkich postów (i mało kto może)

Wyszukiwanie czasem się przydaje, jednak przez osoby rozwijające Mastodona jest uważane za groźne, bo ułatwia nękanie. Zresztą nawet gdyby nie było ograniczone, to możesz przeszukiwać tylko bazę wpisów na tej konkretnej instancji – sieć jest rozproszona, więc ze sporym prawdopodobieństwem wiele wpisów nigdy do ciebie nie dotrze.

To jest coś co trudno jasno określić jako dobre lub złe. Ale da się z tym żyć.

## Nie odstraszyłeś mnie, gdzie mam podpisać?

Przede wszystkim, nawet jeśli rejestracja na flagowej instancji mastodon.social jest otwarta, nie idź tam. Moim zdaniem silne skupienie użytkowników na jednej instancji przyczyniło się po części do opisanego wcześniej spolaryzowania sieci.

Dwa lata temu uznałem, że fajnie byłoby mieć polską instancję Pleromy. Plan był dobry, domena też, tylko niedługo po tym naszedł mnie pierwszy kryzys zastanawiania się, czy na pewno chcę tu być. Koniec końców domenę i instancję oddałem [Rafałowi](http://kolucki.pl/), a on niedawno ją otworzył do rejestracji dla wszystkich. Tę instancję znajdziecie pod <https://a.nom.pl>. Została po mnie nawet część regulaminu: "Zabronione jest agresywne zachowanie wobec innych użytkowników, bez względu na to, kto zaczął. (...) Nalegamy na zachowanie kultury osobistej."

Jeżeli koniecznie musi być to moja jednoosobowa instancja, <https://om.nom.pl>, to w drodze wyjątku jestem skłonny przyjąć kilka osób, ale to trzeba ustalić prywatnie ze mną.

Poza tym dobrze czułem się na Pleromie na <https://kawen.space>. Dobrych znajomych mam na Mastodonach <https://nulled.red> i <https://mstdn.io> i administratorom tych instancji również osobiście ufam. Jest też jedna przyzwoita polska instancja Mastodona <https://101010.pl>, poza tym w kraju dość cicho.

A może chcesz samemu spróbować sił jako administrator? Darius Kazemi napisał bardzo fajny poradnik, przede wszystkim o aspektach społecznych, nie technicznych: <https://runyourown.social/>.


---

Mam nadzieję, że spotkamy się na fedi

[@michcio@om.nom.pl](https://om.nom.pl/michcio)
