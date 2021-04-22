### Minu lahendus

Et lahendada seda ülesanne ma implementeerisin 2 meetodi. Esimene meetod _train_topic_ ma kasutan et tehisintellekti 
treenida. See meetod kogub informatsioon artiklitest. Teine meetod _define_topic_ kasutab esimene meetodi ja siis
selle andmete põhjal teeb otsuse. Alguses mõlemad meetodid viskavad ära kõik sõnad mis on väiksem kui 4 sümbolit,
pärast seda _train_topic_ kogub kõik vajalikud andmed (artiklite koguarv, kui palju artikleid kuulub erinevatele
teemadele, sõnade esinemised igas teemas, palju sõnu kokku, palju unikaalseid sõnu) ja _define_topic_ kasutab 
need andmed (paneb valemisse ja arvutab tõenäosused), siis _define_topic_ valib teema kõige suurema tõenäosusega
ja peetab seda õigeks. Kõik andmed mul hoitakse dictionary'des, minu arvates see on kõige mudav viis andmete 
hoidmiseks. Minu algoritmi täpsus on 96%.  