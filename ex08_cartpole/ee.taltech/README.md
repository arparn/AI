### Minu Lahendus:

Ma tegin mitu meetodit et lahendada seda ülesanne. Mul on play() meetod kus kõik toimub. 
Kõigepealt ma panen käima meetodi: fill_q_table(), kus ma initsialiseerin training_map ja panen sisse kõik andmed,
mis on vaja, et seda tabeli täitma. Siis panen käima environmenti. Peale seda, kui algab simulatsioon, iga tspkli
iteratsioonis mul on kontroll, et kui training_map'is on juba selle olukorda jaaoks sobivad tegevused, siis minu
tehisintellekt kasutab need, muul juhul ta teeb juhuslikud liikumised. Kui käik oli õige, ehk varras ei ole kukkunud
tehisintellekt saab positiivse auhinna. Kui kukkub, siis saab negatiivse auhinna. Siis, kui käik on tehtud,
minu koodis käivitatakse meetod train_q_table(), mis on vaja, et tehisintellekti treenida.
train_q_table() ma annan parameetritena praegune observation, jargmine observation, auhinna ja käigu.
Siis ma muutan praeguse oservation'i jargmise observation'i peale ja iteratsioon kordub uute teadmistega.
