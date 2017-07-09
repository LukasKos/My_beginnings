from sys import exit

name = raw_input("Zadejte sve jmeno: ")

name = list(name)

def names(who):

    if who[-1] == 'a':
        who[-1] = 'o'
        return ''.join(who)
    elif who[-1] == 'A':
        who[-1] = 'O'
        return ''.join(who)
    else:
        return ''.join(who)

class Room(object):

    def enter(self):
        print "."
        exit(0)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('hotovo')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Dead(Room):

    def enter(self):
        print "\t%s to nedokazala. Uz nikdy se nedozvi, proc se zde objevila." \
        % ''.join(name)
        exit(0)

class FirstRoom(Room):

    def enter(self):
        print """\n\t%s se objevila v mistnosti, kterou nepoznavala. Sla """ \
        """vecer spat
    \ta rano se probudila zde. "Co se to deje?" pomyslela si a podivala
    \tse kolem sebe. Vypadalo to jako na nejakem starem hrade ci tvrzi,
    \tvsude sede kameny a plno pavucin. A vlevo a vpravo dvere.
    \tRozhodla se tedy, ze jednemi z nich pujde dal...""" % ''.join(name)

        choice = raw_input("""\n1) Vpravo\n2) Vlevo\n> """)

        if choice ==  '1':
            return 'golem_room'
        elif choice == '2':
            return 'spider_room'
        else:
            print "\tTak dlouho se %s rozhlizela a premyslela, az nemela silu" \
            " nikam jit." % ''.join(name)
            return 'dead'

class GolemRoom(Room):

    def enter(self):
            print "\tV mistnosti stoji nehnute golem."
            print "\tVypada presne jako z pohadky Cisaruv pekar/Pekaruv cisar."
            print "\tVedle tebe je na stolku golemuv sem."
            print "\tCo udelas?"

            choice = raw_input("""\n\r1) Priblizis se ke golemovi a vlozis""" \
            """ mu do cela sem
            \r2) Skocis na golema a zacnes ho mlatit
            \r3) Projdes pomalu kolem golema
            > """)

            if '1' in choice:
                print """\tGolem zafunel, zacaly mu zarit oci a zacal se k""" \
                """ tobe priblizovat.
        "Poslouchej me, goleme!" kricis, ale golem jako by te neslysel...""" \
        """ protoze te opravdu
        neslysi. Nikdo mu neudelal usi. Jak si toho nemohl nekdo v te""" \
        """ pohadce nevsimnout?
        Golem se k tobe prikoleba a rozdrti te."""
                return 'dead'
            elif '2' in choice:
                print """\tSkocila jsi na golema a mlatis ho hlava nehlava.""" \
                """ Nasazujes mu
        kravatu, ale nic se nedeje. Golem jen nehnute stoji. Mno, ale stalo""" \
        """ to za to... asi."""
                print "\tDo kterych dveri nyni?"


                choc = raw_input("\n1) Dolu\n2) Vlevo\n> ")

                if choc == '1':
                    return 'evans_room'
                elif choc == '2':
                    return 'spider_room'
                else:
                    print "\tZkus to napsat jeste jednou :)"
                    return 'golem_room'


            elif '3' in choice:
                print "\tProsla jsi kolem golema."
                print "\tZe by se nic nedelo?"
                print "\tAle nahle!!!"
                print "\tNe, opravdu se nic nestalo."
                print "\tHmm, to bylo lehci nez sis puvodne myslela, ze?"
                print "\tDo kterych dveri nyni?"

                choci = raw_input("\n1) Dolu\n2) Vlevo\n> ")

                if choci == '1':
                    return 'evans_room'
                elif choci == '2':
                    return 'spider_room'
                else:
                    print "\tZkus to napsat jeste jednou :)"
                    return 'golem_room'
            else:
                print "\tZkus to napsat jeste jednou :)"
                return 'golem_room'

class SpiderRoom(Room):

    def enter(self):
        print "\tJsi v podivne zatuchle mistnosti."
        print "\tVsude jsou pavuciny a mas podivny pocit, jako by te " \
        "nekdo sledoval."
        print "\tMraz ti beha po zadech, ale nemas jinou moznost, nez " \
        "pokracovat dal."
        print "\tKdyz tu se ozvou jako by cupitave kroky."
        print """\t"Co to bylo?" pomyslis si a jdes pomalicku dal."""
        print "\tNahle podivny hlas zaskrehota: 'Ztatila ses, holubicko?'"
        print "\tRychle se otocis. 'Odkud ten hlas prisel?' leti ti hlavou."
        print "\tAle nikdo nikde."
        print "\t'Me neuvidis, dokud nebudu chtit, holubicko, he heh he,' " \
        "zaskrehotal hlas"
        print "\t'Ukaz se,' kricis a zpet se ozve: 'Jak si prejes.'"
        print "\tZ temnoty mistnsti se zjevi temny stin. Ne vlastne, to " \
        "neni stin."
        print "\tJe to obrovsky pavouk, jenz te hladove pozoruje."
        print "\tCo ted udelas?"

        choice = raw_input("\n1) Zacnes utikat po mistnosti\n2) Zautocis\n3) " \
        "Znehybnis strachy\n> ")

        if str(1) in choice:
            print "\tPavouk se smeje. Je to jak kdyz motorova pila reze" \
            " stromy. A pak skoci a je konec."
            return 'dead'
        elif str(2) in choice:
            print "\tPavoukovi jsi dala pravy hak a levy hak. HA! To by bylo," \
            " abys neporazila pavouka!\n\tA pak pavouk kousne a je konec."
            return 'dead'
        elif str(3) in choice:
            print "\tNic nedelas a nic se nedeje. Strachy se nemuzes ani" \
            " pohnout."
            print "\tPavouk se na tebe diva."
            print "\tTakhle proti sobe stojite cca 5 minut."
            print "\tPak pavouk rekne: 'Tohle je nuda, bez radsi dal.'"
            print "\tZazrak, prezila jsi setkani s obrim pavoukem!"
            print "\tAle do kterych dveri pujdes nyni?"

            choc = raw_input("\n1) Dolu\n2) Vlevo\n> ")

            if choc == str(1):
                return 'tabak_room'
            elif choc == str(2):
                return 'evans_room'
            else:
                print "\tZkus to napsat jeste jednou :)"
                return 'spider_room'
        else:
            print "\tZkus to napsat jeste jednou :)"
            return 'spider_room'

class EvansRoom(Room):

    def enter(self):
        print "\tVesla jsi do mistnosti, ktera je podivne studena."
        print "\tRozhlizis se kolem a nahle spatris na konci mistnosti" \
        " nehnutou postavu."
        print "\tPoradne zaostris a hlesnes: 'Ne.'"
        print "\tAle ano. Poznavas jej. Je to on."
        print "\tLuke Evans!"
        print "\tChces se k nemu rozebehnout, protoze uz asi chapes, ze tu" \
        " jsi kvuli nemu."
        print "\tAle pak si vsimnes, ze neco neni uplne v poradku."
        print "\t'U vsech skotu!' pomyslis si. 'Luke Evans je zombie!'"
        print "\tJe to tak, Luke Evans je skutecne zombie. Co nyni udelas?"

        choice = raw_input("\n1) Zkusis Evanse polibit, treba je to jak s " \
        "tou zabou a bude z nej zas krasny princ\n2) Striknes zombie-Evansovi" \
        " peprak do ksichtu\n> ")

        if choice == str(1):
            print "\tAc je to pokekud nechutne, polibila jsi jeho " \
            "rozpadajici se rty."
            print "\tA nahle. Co to bylo? Spatrila jsi snad jiskricku zivota" \
            " v jeho ocich?"
            print "\tLuke Evans te kousne!"
            print "\tSakra! Kdo by to byl cekal, ze te zombie kousne?"
            print "\tJojo. Temto zombie-krasavcum se neda verit."
            return 'dead'

        elif choice == str(2):
            print "\tNastrikalas zombie-Evansovi peprak do tvare."
            print "\tAuu! AAAAAAUUUUUUUUUUU! krici a chyta se za oblices."
            print "\tRadsi to neriskujes a vystrikas celej obsah. " \
            "Jistota je jistota."
            print "\tZombie-Evans se sviji na zemi a breci."
            print "\tPro jistotu ho jeste kopnes do hlavy."
            print "\tPred sebou mas opet dvere, kam nyni?"

            choc = raw_input("\n1) Dolu\n2) Vpravo\n> ")

            if choc == str(1):
                return 'ending_room'
            elif choc == str(2):
                return 'tabak_room'
            else:
                print "Zkus to napsat jeste jednou :)"
                return 'evans_room'
        else:
            print "\tZkus to napsat jeste jednou :)"
            return 'evans_room'

class TabakRoom(Room):

    def enter(self):
        print "\tVsude jsou vodnice a tabak!!!"
        print "\tA vino tece z fontany! Sladoucke bile vino!"
        print "\tVypada to, ze jsi se dostala do raje. Tohle je urcite" \
        " konec tve cesty."
        print "\tVzadu zahlednes nejake dvere, ale to je stejne jedno, " \
        "vdyt tady je fajn."
        print "\tKonecne klid a mir."
        print "\tUz zadna monstra, jen vodnice a sklenka vina."
        print "\tJak se rozhodnes?"

        choc = raw_input("\n1) Uz na to kaslu, tady je hezky! Zde zustanu!\n2)"\
        " Moc se mi nechce, vdyt tady je fajn, ale podivam se jeste kousek " \
        "dal.\n> ")

        if choc == str(1):
            print "\tTady tva cesta konci. Dosla jsi klidu a miru, ale" \
            " skoncila jsi jen krucek pred odpovedi na tvou otazku, proc" \
            " jsi se zde objevila"
            return "dead"
        elif choc == str(2):
            return 'ending_room'
        else:
            print "\tZkus to napsat jeste jednou :)"
            return 'tabak_room'

class EndingRoom(Room):

    def enter(self):
        print "\tDokazala jsi to. Dosla jsi na konec sve cesty."
        print "\tVidis jak na posteli lezi spici muz, jenz je ti dle vzhledu" \
        " tuze mily."
        print "\tNevis, co s nim je. Ale citis, ze jej musis zachranit."
        print "\tNeni preci zdrave cely den polehavat v posteli a nic nedelat."
        print "\tCo s tim podivne povedomym a mirne korpulentnim muzem udelas?"

        choice = raw_input("\n1) Polibis jej\n2) Rozsvitis svetlo\n3) " \
        "Nechas jej spat\n> ")

        if choice == str(1):
            print "\tLukas pomalu otevre oci a ty opet vis jak se jmenuje."
            print "\tJsi stastna, ze jsi jej vysvobodila z jeho prokleti."
            print "\tJsi hrdinka, kdyz jsi jej probudila z jeho spanku a " \
            "proto jsi vyhrala!"
            print "\tNyni se spolu vydate do mistnosti divu a date si spolu" \
            " vodnici."
            print "\tDobra prace %s." % names(name)
            exit(0)
        elif choice == str(2):
            print "\tNemas chut se s tim spicim obtloustlym muzem babrat."
            print "\tPrudce rozsvitis a tim probudis toho spiciho (ne)tvora."
            print "\t'Tak kvuli tobe jsem tu musela projit peklem? No to je" \
            " tedy neco!' \n\tzakricis a das se sama na cestu zpet. Konec " \
            "nekde musi byt"
            print "\tTo nebyl ten nejhezci konec."
            return 'dead'
        elif choice == str(3):
            print "\tNechas ho spat."
            print "\tNevis kdo to je ci co to je, a nemas zadnou chut to " \
            "zjistovat."
            print "\tVe vedlejsi mistnosti je vodnice, ta je zajimavejsi nez " \
            "ten chraploun."
            print "\tTo nebyl ten nejhezci konec."
            return 'dead'
        else:
            print "\tZkus to napsat jeste jednou :)"
            return 'ending_room'

class Finish():
    def enter(self):
        print "\tZvitezila jsi."
        return 'hotovo'

class Map(object):

    scenes = {
        'first_room': FirstRoom(),
        'dead': Dead(),
        'golem_room': GolemRoom(),
        'spider_room': SpiderRoom(),
        'evans_room': EvansRoom(),
        'tabak_room': TabakRoom(),
        'ending_room': EndingRoom(),
        'hotovo': Finish(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('first_room')
game = Engine(a_map)
game.play()
