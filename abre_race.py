
def dico():   
    data_text = """
    KOBG Karayevia oblongella (Oestrup) M. Aboal 1 70,7 0,001
    EMIN Eunotia minor (Kützing) Grunow in Van Heurck 1 40,5 0,001
    ADHE Achnanthidium helveticum (Hustedt) Monnier Lange-Bertalot & Ector 1 39,9 0,001
    FCAP Fragilaria capucina Desmazieres var.capucina 1 38,8 0,001
    NAAN Navicula angusta Grunow 1 35,3 0,001
    FVIR Fragilaria virescens Ralfs 1 35,2 0,001
    EEXI Eunotia exigua (Brebisson ex Kützing) Rabenhorst 1 33,5 0,001
    TFLO Tabellaria flocculosa(Roth)Kützing 1 32,6 0,001
    ETEN Eunotia tenella(Grunow)Hustedt 1 31,8 0,001
    SRBA Surirella roba Leclercq 1 30,2 0,001
    EINC Eunotia incisa Gregory var.incisa 1 28,8 0,001
    ADMI Achnanthidium minutissimum (Kützing) Czarnecki 1 26,9 0,005
    GEXL Gomphonema exilissimum(Grun.) Lange-Bertalot & Reichardt 1 26,4 0,001
    ADSO Achnanthidium subatomoides (Hustedt) Monnier, Lange-Bertalot et Ector 1 25,1 0,001
    FRUM Fragilaria rumpens (Kütz.) G.W.F.Carlson 1 20,6 0,002
    EMUC Eunotia mucophila (Lange-Bert.&Norpel Schempp) Lange-Bertalot 1 19,9 0,001
    EIMP Eunotia implicata Nörpel. Lange-Bertalot & Alles 1 18,2 0,001
    ABRT Achnanthidium bioretii (Germain) Edlund 1 17,8 0,001
    FGRA Fragilaria gracilis Østrup 1 16,4 0,003
    PSEL Pinnularia subcapitata Gregory var. elongata Krammer 1 16,3 0,001
    FKRA Frustulia krammeri Lange-Bertalot & Metzeltin 1 14,9 0,001
    GPVL Gomphonema parvulius Lange-Bertalot & Reichardt 1 14,4 0,001
    ESUB Eunotia subarcuatoides Alles Nörpel & Lange-Bertalot 1 14,2 0,001
    ENNG Encyonema neogracile Krammer 1 13 0,001
    EUIN Eunotia intermedia (Krasske ex Hustedt) Nörpel & Lange-Bertalot 1 12,7 0,001
    FBID Fragilaria bidens Heiberg 1 7 0,018
    TVEN Tabellaria ventricosa Kützing 1 6,6 0,009
    EARC Eunotia arcus Ehrenberg var. arcus 1 6,4 0,011
    NNOT Navicula notha Wallace 1 6,4 0,01
    ADMS Adlafia minuscula (Grunow) Lange-Bertalot 1 5,7 0,027
    GCLA Gomphonema clavatum Ehr. 1 5,3 0,048
    EPEC Eunotia pectinalis (Dyllwyn) Rabenhorst var.pectinalis 1 4,6 0,017
    BVIT Brachysira vitrea (Grunow) Ross in Hartley 1 3,9 0,033
    NLAN Navicula lanceolata (Agardh) Ehrenberg 2 63,7 0,001
    PLFR Planothidium frequentissimum(Lange-Bertalot)Lange-Bertalot 2 57,6 0,001
    NCRY Navicula cryptocephala Kützing 2 40,8 0,001
    NGRE Navicula gregaria Donkin 2 39,4 0,001
    NPAL Nitzschia palea (Kützing) W.Smith 2 38,3 0,001
    ADSH Achnanthidium subhudsonis (Hustedt) H. Kobayasi 2 35,9 0,001
    NRHY Navicula rhynchocephala Kützing 2 35 0,001
    EOMI Eolimna minima(Grunow) Lange-Bertalot 2 33,1 0,001
    ESLE Encyonema silesiacum (Bleisch in Rabh.) D.G. Mann 2 31,4 0,003
    MVAR Melosira varians Agardh 2 27,3 0,001
    GPAR Gomphonema parvulum (Kützing) Kützing var. parvulum f. parvulum 2 26,8 0,001
    FCVA Fragilaria capucina Desmazieres var.vaucheriae(Kützing)Lange-Bertalot 2 26,1 0,001
    ENMI Encyonema minutum (Hilse in Rabh.) D.G. Mann 2 25,1 0,002
    AAMB Aulacoseira ambigua (Grunow) Simonsen 2 23,9 0,001
    SSVE Staurosira venter (Ehr.) Cleve & Moeller 2 23,6 0,001
    NGER Navicula germainii Wallace 2 23,4 0,001
    ADEU Achnanthidium eutrophilum (Lange-Bertalot)Lange-Bertalot 2 23,2 0,001
    PDAU Planothidium daui (Foged) Lange-Bertalot 2 21 0,001
    LGOE Luticola goeppertiana (Bleisch in Rabenhorst) D.G. Mann 2 19 0,001
    NINC Nitzschia inconspicua Grunow 2 18,2 0,006
    NANT Navicula antonii Lange-Bertalot 2 18,1 0,002
    DSTE Discostella stelligera (Cleve et Grun.) Houk & Klee 2 17,9 0,001
    PTPE Planothidium peragallii (Brun & Heribaud)Round & Bukhtiyarova 2 16 0,001
    ADRI Achnanthidium rivulare Potapova &Ponader 2 14,7 0,002
    NACD Nitzschia acidoclinata Lange-Bertalot 2 14,4 0,001
    KALA Karayevia laterostrata (Hustedt) Bukhtiyarova 2 14,1 0,001
    NPAD Nitzschia palea (Kützing) W.Smith var.debilis(Kützing)Grunow in Cl. & Grun 2 12,7 0,001
    SSEM Sellaphora seminulum (Grunow) D.G. Mann 2 12,6 0,005
    ESBM Eolimna subminuscula (Manguin) Moser Lange-Bertalot & Metzeltin 2 12,3 0,009
    NROS Navicula rostellata Kützing 2 12,3 0,001
    SPUP Sellaphora pupula (Kützing) Mereschkowksy 2 11,8 0,005
    GMIC Gomphonema micropus Kützing var. micropus 2 11,7 0,008
    SANG Surirella angusta Kützing 2 11,3 0,004
    SBRV Staurosira brevistriata (Grunow) Grunow 2 10,2 0,003
    HCAP Hippodonta capitata (Ehr.)Lange-Bert.Metzeltin & Witkowski 2 9,4 0,003
    PRST Planothidium rostratum (Oestrup) Lange-Bertalot 2 9,1 0,005
    PPRO Parlibellus protracta (Grunow) Witkowski Lange-Bertalot & Metzeltin 2 8,1 0,004
    ADCT Achnanthidium catenatum (Bily & Marvan) Lange-Bertalot 2 7,8 0,014
    CMLF Craticula molestiformis (Hustedt) Lange-Bertalot 2 7,8 0,011
    AUSB Aulacoseira subborealis (Nygaard) Denys, Muylaert & Krammer 2 7,2 0,005
    PCLT Placoneis clementis (Grun.) Cox 2 6,9 0,007
    FVUL Frustulia vulgaris (Thwaites) De Toni 2 6,8 0,005
    NSUA Nitzschia subacicularis Hustedt in A.Schmidt et al. 2 6,7 0,011
    NSHR Navicula schroeteri Meister var. schroeteri 2 6,6 0,011
    PGRN Planothidium granum (Hohn & Hellerman) Lange-Bertalot 2 6,6 0,004
    GITA Gomphonema italicum Kützing 2 5,4 0,009
    SEXG Stauroforma exiguiformis (Lange-Bertalot) Flower Jones et Round 2 4,8 0,027
    CPLI Cocconeis placentula Ehrenberg var.lineata (Ehr.)Van Heurck 3 73,3 0,001
    ADSU Achnanthidium subatomus (Hustedt) Lange-Bertalot 3 52,1 0,001
    PTLA Planothidium lanceolatum(Brebisson ex Kützing) Lange-Bertalot 3 36,5 0,001
    RSIN Reimeria sinuata (Gregory) Kociolek & Stoermer 3 34,7 0,001
    COPL Cocconeis pseudolineata (Geitler) Lange-Bertalot 3 28,1 0,001
    ADDA Achnanthidium daonense (Lange-Bertalot) Lange-Bertalot Monnier & Ector 3 21,8 0,001
    GRHB Gomphonema rhombicum M. Schmidt 3 21,8 0,001
    GACC Geissleria acceptata (Hust.) Lange-Bertalot & Metzeltin 3 20,9 0,001
    GCFU Gomphoneis calcifuga (Lange-Bertalot & Reichardt)Tuji 3 20,7 0,001
    DPER Diadesmis perpusilla (Grunow) D.G. Mann in Round & al. 3 18,5 0,001
    ADSP Adlafia sp. 3 16,9 0,001
    ADLS Adlafia suchlandtii (Hustedt) Moser Lange-Bertalot & Metzeltin 3 11,7 0,003
    DMES Diatoma mesodon (Ehrenberg) Kützing 3 11,5 0,027
    NULA Nupela lapidosa (Lange-Bertalot) Lange-Bertalot var.lapidosa 3 10,4 0,003
    NEXI Navicula exilis Kützing 3 9,9 0,012
    PSRE Psammothidium rechtensis (Leclercq) Lange-Bertalot 3 9,4 0,002
    NHAN Nitzschia hantzschiana Rabenhorst 3 8,5 0,006
    FARC Fragilaria arcus (Ehrenberg) Cleve var. arcus 3 7,9 0,04
    ADMM Adlafia minuscula var. muralis (Grunow) Lange-Bertalot 3 5,3 0,034
    NLUN Navicula lundii Reichardt 3 4,4 0,036
    NTPT Navicula tripunctata (O.F.Müller) Bory 4 82,7 0,001
    APED Amphora pediculus (Kützing) Grunow 4 79,5 0,001
    NCTE Navicula cryptotenella Lange-Bertalot 4 69,4 0,001
    CEUG Cocconeis euglypta Ehrenberg 4 50,3 0,001
    CPED Cocconeis pediculus Ehrenberg 4 44,3 0,001
    GMIN Gomphonema minutum(Ag.)Agardh f. minutum 4 40,6 0,001
    NDIS Nitzschia dissipata(Kützing)Grunow var.dissipata 4 39 0,001
    NRCH Navicula reichardtiana Lange-Bertalot var. reichardtiana 4 37,7 0,001
    FSBH Fallacia subhamulata (Grunow in V. Heurck) D.G. Mann 4 34,5 0,001
    CBAC Caloneis bacillum (Grunow) Cleve 4 33,2 0,001
    NCPR Navicula capitatoradiata Germain 4 33 0,001
    GSCI Gyrosigma sciotense (Sullivan et Wormley) Cleve 4 27,9 0,001
    RABB Rhoicosphenia abbreviata (C.Agardh) Lange-Bertalot 4 27,6 0,001
    AINA Amphora inariensis Krammer 4 27,3 0,001
    NFON Nitzschia fonticola Grunow in Cleve et Möller 4 26,6 0,002
    ACOP Amphora copulata (Kütz) Schoeman & Archibald 4 24,4 0,001
    NSOC Nitzschia sociabilis Hustedt 4 22,4 0,001
    GOLI Gomphonema olivaceum (Hornemann) Brébisson var. olivaceum 4 21,9 0,001
    CAEX Cymbella excisa Kützing var. excisa 4 19 0,002
    DVUL Diatoma vulgaris Bory 4 18,2 0,001
    RUNI Reimeria uniseriata Sala Guerrero & Ferrario 4 18,2 0,001
    SBRE Surirella brebissonii Krammer & Lange-Bertalot var.brebissonii 4 17,3 0,001
    DTEN Denticula tenuis Kützing 4 16,7 0,038
    NAMP Nitzschia amphibia Grunow f.amphibia 4 15,9 0,001
    ADLB Achnanthidium lauenburgianum (Hustedt) Monnier Lange-Bertalot & Ector 4 15,3 0,001
    GPRI Gomphonema pumilum var. rigidum Reichardt & Lange-Bertalot 4 15,2 0,001
    GYAT Gyrosigma attenuatum (Kützing) Rabenhorst 4 13,2 0,001
    KGES Kolbesia gessneri (Hustedt) Aboal 4 13 0,001
    DPST Discostella pseudostelligera (Hustedt) Houk et Klee 4 12,2 0,008
    FLEN Fallacia lenzi(Hustedt) Lange-Bertalot 4 11,6 0,001
    CEUO Cocconeis euglyptoides (Geitler) Lange-Bertalot 4 11,3 0,001
    NTRV Navicula trivialis Lange-Bertalot var. trivialis 4 10,7 0,002
    ENLB Encyonema lange-bertalotii Krammer morphotype 1 4 10 0,008
    SIDE Simonsenia delognei Lange-Bertalot 4 9,9 0,006
    DOCU Diploneis oculata (Brebisson) Cleve 4 9,8 0,002
    NREC Nitzschia recta Hantzsch in Rabenhorst 4 9,2 0,013
    DOBL Diploneis oblongella (Naegeli) Cleve-Euler 4 8,8 0,008
    CINV Cyclostephanos invisitatus(Hohn & Hellerman)Theriot Stoermer & Hakansson 4 8 0,005
    DSEP Diploneis separanda Lange-Bertalot 4 7,3 0,008
    ACAF Achnanthidium affine (Grun) Czarnecki 4 6,7 0,045
    NCTO Navicula cryptotenelloides Lange-Bertalot 4 6,6 0,033
    CMEN Cyclotella meneghiniana Kützing 4 6,2 0,017
    DMAR Diploneis marginestriata Hustedt 4 4,7 0,03
    ADPY Achnanthidium pyrenaicum (Hustedt) Kobayasi 5 78,2 0,001
    GELG Gomphonema elegans (Reichardt & Lange-Bertalot) Monnier & Ector 5 28,9 0,001
    GPUM Gomphonema pumilum (Grunow) Reichardt & Lange-Bertalot 5 27,2 0,001
    ACLI Achnanthidium lineare W.Smith 5 22,3 0,001
    DEHR Diatoma ehrenbergii Kützing 5 19,6 0,001
    ECPM Encyonopsis minuta Krammer & Reichardt 5 17,9 0,001
    GMPU Gomphonema micropumilum Reichardt 5 17,8 0,001
    CPAR Cymbella parva(W.Sm.)Kirchner in Cohn 5 16 0,001
    ENCM Encyonopsis microcephala (Grunow) Krammer 5 16 0,005
    CAFF Cymbella affinis Kützing var.affinis 5 14,6 0,001
    DTMO Diatoma tenuis Agardh var moniliformis Kützing 5 14,4 0,002
    GLAT Gomphonema lateripunctatum Reichardt & Lange-Bertalot 5 14 0,001
    GTER Gomphonema tergestinum Fricke 5 13,9 0,002
    SSTM Sellaphora stroemii (Hustedt) Mann 5 13,5 0,001
    ADAM Achnanthidium atomoides Monnier, Lange-Bertalot & Ector 5 12,8 0,013
    GOCU Gomphonema occultum Reichardt & Lange-Bertalot 5 11,1 0,002
    ESUM Encyonopsis subminuta Krammer & Reichardt 5 10,3 0,001
    ECKR Encyonopsis krammeri Reichardt 5 9,5 0,006
    DDEL Delicata delicatula (Kützing) Krammer var. delicatula 5 7,8 0,007
    GROS Gomphonema rosenstockianum Lange-Bertalot & Reichardt 5 7,8 0,037
    BMIC Brachysira microcephala (Grunow) Compère 5 7,7 0,015
    CEXF Cymbella excisiformis Krammer var.excisiformis 5 7,3 0,008
    CVUL Cymbella vulgata Krammer var.vulgata Krammer 5 7,1 0,014
    ADKR Achnanthidium kranzii (Lange-Bertalot) Round & Bukhtiyarova 5 6,6 0,023
    GAGV Gomphonema angustivalva E. Reichardt 5 6,6 0,018
    ADLA Amphora delicatissima
    ADMO Achnanthidium minutissimum
    ADRU Achnanthidium rivulare
    ADSB  Asterionella formosa
    AFOR  Amphora coffeaeformis
    AMID  Amphora ovalis
    AOVA  Aulacoseira valida
    AUGA  Aulacoseira granulata
    AUGR  Aulacoseira granulata
    AUPU  Aulacoseira pusilla
    AUSU  Aulacoseira subarctica
    CAGR  Cocconeis placentula
    CATO  Cavinula tenella
    CDUB  Cocconeis pediculus
    CLCT  Cymbella cistula
    CLNT  Cocconeis placentula
    CMED  Cyclotella meneghiniana
    CPLA  Cocconeis placentula
    CRAC  Cocconeis placentula
    CSLP  Cocconeis placentula
    CTPU  Cocconeis pediculus
    DCOF  Diatoma vulgare
    DMON  Diatoma moniliformis
    ECAE  Eunotia exigua
    EICD  Encyonema minutum
    ENVE  Encyonema ventricosum
    EOCO  Eunotia coarctata
    FCRO  Fragilaria crotonensis
    FFVI  Fragilaria virescens
    FMES  Fragilaria mesolepta
    FMOC  Fragilaria moelleri
    FNEV  Fragilaria nevadensis
    FPEC  Fragilaria pectinalis
    FPRU  Fragilaria pinnata
    FSAP  Fragilaria saprophila
    FSLU  Fragilaria capucina
    FVAU  Fragilaria vaucheriae
    GBOB  Gomphonema acuminatum
    GCLF  Gomphonema clevei
    GCUN  Gomphonema cuneatum
    GPLI  Gomphonema parvulum
    GTRU  Gomphonema truncatum
    HARC  Hannaea arcus
    HLMO  Hannaea arcus
    HVEN  Hannaea arcus
    KCLE  Karayevia clevei
    MCCO  Melosira varians
    MCIR  Melosira varians
    NACI  Navicula cincta
    NCPL  Navicula cryptocephala
    NCTV  Navicula cryptocephala
    NERI  Navicula erifuga
    NFIL  Navicula cryptocephala
    NHEU  Navicula heufleriana
    NIBU  Navicula ibérica
    NIPF  Navicula cryptocephala
    NIPU  Navicula pupula
    NLIN  Navicula linearis
    NMIC  Navicula minima
    NPAE  Navicula paucipunctata
    NRAD  Nitzschia adamsii
    NRCS  Nitzschia pusilla
    NSTS  Nitzschia sigma
    NVEN  Nitzschia veneta
    NYCO  Navicula cryptocephala
    NZSU  Nitzschia subcurvata
    PAPR  Pinnularia borealis
    PBIO  Pinnularia borealis
    PDAO  Pinnularia dohrnii
    PHEL  Pinnularia helleri
    PLAU  Pinnularia subcapitata
    PROH  Pinnularia robusta
    PSAT  Pseudo-nitzschia australis
    PSBR  Pseudo-nitzschia brasiliana
    PSXO  Pseudo-nitzschia delicatissima
    PTCO  Pseudo-nitzschia pseudodelicatissima
    PTDE  Pseudo-nitzschia delicatissima
    PTDU  Pseudo-nitzschia pseudodelicatissima
    PULA  Pseudo-nitzschia australis
    SBKU  Synedra biceps
    SBND  Synedra biceps
    SCON  Surirella constricta
    SHTE  Surirella tenera
    SKPO  Synedra kuetzingii
    SLAC  Synedra acus
    TAPI  Tabellaria fenestrata
    TFAS  Tabellaria fenestrata
    TGES  Tabellaria fenestrata
    THLA  Thalassiosira laevis
    TLEV  Thalassiosira levanderi
    UULN  Ulnaria ulna
    """
# le dictionnaire au dessus peut être completer de différente infromation ajouter juste une ligne est puis magie magie ;)
    dictionnaire_algue = {}

    lines = data_text.strip().split('\n')

    for line in lines:
        elements = line.split()
        code = elements[0]
        denomination_espece = ' '.join(elements[1:])
        dictionnaire_algue[code] = {
            'Denomination_espece': denomination_espece
        }

    return dictionnaire_algue
