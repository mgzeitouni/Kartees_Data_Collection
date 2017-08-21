def get_team(eventId):

    team = {9444003 : "dodgers", 9444030 : "dodgers", 9444079 : "dodgers", 9444101 : "dodgers", 9444421 : "dodgers", 9445362 : "cubs", 9445339: "cubs", 9445319: "cubs", 9445356: "cubs", 9445310: "cubs", 9445134: "mets", 9445028: "mets", 9445151: "mets", 9445089: "mets", 9445062: "mets", 9444843: "orioles", 9444850: "orioles", 9444836: "orioles", 9444835: "orioles", 9444794: "orioles", 9443093: "astros", 9443062: "astros", 9443091: "astros", 9443103: "astros", 9443054: "astros", 9370856: "knicks", 9370806: "knicks", 9370773: "knicks", 9370849: "knicks", 9370785: "knicks", 9370813: "knicks", 9370651: "warriors", 9370664: "warriors", 9370688: "warriors", 9370708: "warriors", 9370659: "warriors", 9371360: "trailblazers", 9371397: "trailblazers", 9371402: "trailblazers", 9371410: "trailblazers", 9371429: "trailblazers", 9371113: "hawks", 9371138: "hawks", 9371158: "hawks", 9371165: "hawks", 9371178: "hawks", 9371146: "grizzlies", 9371157: "grizzlies", 9371167: "grizzlies", 9371186: "grizzlies", 9371201: "grizzlies", 9341475: "rangers", 9341486: "rangers", 9341506: "rangers", 9341526: "rangers", 9341540: "rangers", 9341406: "bruins", 9341429: "bruins", 9341444: "bruins", 9341472: "bruins", 9341496: "bruins", 9341636: "stars", 9341649: "stars", 9341669: "stars", 9341682: "stars", 9341695: "stars", 9342365: "senators", 9342374: "senators", 9342393: "senators", 9342407: "senators", 9342419: "senators", 9342412: "bluejackets", 9342418: "bluejackets", 9342424: "bluejackets", 9342429: "bluejackets", 9342434: "bluejackets", 9454368: "patriots", 9298537: "broncos", 9454719: "broncos", 9298616: "panthers", 9454374: "panthers", 9298597: "cardinals", 9454380: "cardinals", 9298655: "bengals", 9454369: "bengals", 9371261: "raptors", 9371254: "raptors", 9371216: "raptors", 9371196: "raptors", 9371185: "raptors", 9371227: "raptors", 9371205: "raptors", 9371192: "raptors", 9371246: "raptors", 9371243: "raptors", 9371187: "raptors", 9371200: "raptors", 9371219: "raptors", 9371249: "raptors", 9371155: "celtics", 9371140: "celtics", 9371121: "celtics", 9371097: "celtics", 9371084: "celtics", 9371125: "celtics", 9371129: "celtics", 9371154: "celtics", 9371118: "celtics", 9371107: "celtics", 9371049: "celtics", 9371102: "celtics", 9370817: "knicks", 9370843: "knicks", 9370802: "knicks", 9370846: "knicks", 9370788: "knicks", 9370777: "knicks", 9370810: "knicks", 9370779: "knicks", 9370852: "knicks", 9370963: "nets", 9370992: "nets", 9370897: "nets", 9370907: "nets", 9370930: "nets", 9370970: "nets", 9371021: "nets", 9371011: "nets", 9371300: "76ers", 9371366: "76ers", 9371338: "76ers", 9371295: "76ers", 9371329: "76ers", 9371427: "76ers", 9371386: "76ers", 9371289: "76ers", 9371302: "76ers", 9371344: "76ers", 9371376: "76ers", 9371382: "76ers", 9371369: "76ers", 9370549: "cavaliers", 9370553: "cavaliers", 9370560: "cavaliers", 9370561: "cavaliers", 9370566: "cavaliers", 9370569: "cavaliers", 9370574: "cavaliers", 9370577: "cavaliers", 9370580: "cavaliers", 9370583: "cavaliers", 9370587: "cavaliers", 9370590: "cavaliers", 9370550: "bulls", 9370554: "bulls", 9370556: "bulls", 9370559: "bulls", 9370562: "bulls", 9370565: "bulls", 9370568: "bulls", 9370570: "bulls", 9370572: "bulls", 9371659: "bulls", 9371660: "bulls", 9371661: "bulls", 9370840: "pacers", 9370844: "pacers", 9370847: "pacers", 9370850: "pacers", 9370854: "pacers", 9370858: "pacers", 9370860: "pacers", 9370862: "pacers", 9370864: "pacers", 9370866: "pacers", 9370867: "pacers", 9370868: "pacers", 9370870: "pacers", 9370984: "pistons", 9370989: "pistons", 9370994: "pistons", 9370997: "pistons", 9371000: "pistons", 9371004: "pistons", 9371006: "pistons", 9371010: "pistons", 9371014: "pistons", 9371018: "pistons", 9371022: "pistons", 9371024: "pistons", 9371027: "pistons", 9370672: "bucks", 9370674: "bucks", 9370677: "bucks", 9370681: "bucks", 9370685: "bucks", 9370690: "bucks", 9370693: "bucks", 9370697: "bucks", 9370700: "bucks", 9370706: "bucks", 9370710: "bucks", 9370712: "bucks", 9370715: "bucks", 9370718: "bucks", 9370722: "bucks", 9370778: "heat", 9370781: "heat", 9370787: "heat", 9370793: "heat", 9370800: "heat", 9370805: "heat", 9370809: "heat", 9370815: "heat", 9370820: "heat", 9370824: "heat", 9370831: "heat", 9371161: "hawks", 9371166: "hawks", 9371168: "hawks", 9371171: "hawks", 9371173: "hawks", 9371176: "hawks", 9371181: "hawks", 9371184: "hawks", 9371188: "hawks", 9371034: "hornets", 9371036: "hornets", 9371038: "hornets", 9371041: "hornets", 9371044: "hornets", 9371047: "hornets", 9371050: "hornets", 9371055: "hornets", 9371060: "hornets", 9371064: "hornets", 9371073: "hornets", 9371076: "hornets", 9371080: "hornets", 9370591: "wizards", 9370593: "wizards", 9370595: "wizards", 9370599: "wizards", 9370602: "wizards", 9370607: "wizards", 9370610: "wizards", 9371900: "wizards", 9371901: "wizards", 9371902: "wizards", 9371903: "wizards", 9371241: "magic", 9371244: "magic", 9371250: "magic", 9371253: "magic", 9371255: "magic", 9371258: "magic", 9371263: "magic", 9371267: "magic", 9371269: "magic", 9371271: "magic", 9371563: "thunder", 9371565: "thunder", 9371567: "thunder", 9371568: "thunder", 9371570: "thunder", 9371572: "thunder", 9371574: "thunder", 9371576: "thunder", 9371578: "thunder", 9371416: "trailblazers", 9371418: "trailblazers", 9371422: "trailblazers", 9371425: "trailblazers", 9371433: "trailblazers", 9371435: "trailblazers", 9371438: "trailblazers", 9371442: "trailblazers", 9371448: "trailblazers", 9371378: "jazz", 9371381: "jazz", 9371384: "jazz", 9371387: "jazz", 9371389: "jazz", 9371393: "jazz", 9371396: "jazz", 9371398: "jazz", 9371400: "jazz", 9371403: "jazz", 9371480: "nuggets", 9371482: "nuggets", 9371483: "nuggets", 9371485: "nuggets", 9371486: "nuggets", 9371488: "nuggets", 9371492: "nuggets", 9371494: "nuggets", 9371496: "nuggets", 9371497: "nuggets", 9371499: "nuggets", 9371501: "nuggets", 9370675: "warriors", 9370694: "warriors", 9370638: "warriors", 9370699: "warriors", 9370626: "warriors", 9370576: "warriors", 9370592: "warriors", 9370666: "warriors", 9370714: "warriors", 9370720: "warriors", 9370725: "warriors", 9370702: "warriors", 9370731: "warriors", 9370584: "warriors", 9371035: "clippers", 9370941: "clippers", 9371037: "clippers", 9371039: "clippers", 9371045: "clippers", 9370913: "clippers", 9371033: "clippers", 9371051: "clippers", 9371057: "clippers", 9370968: "clippers", 9370789: "clippers", 9370828: "clippers", 9371569: "kings1", 9371571: "kings1", 9371573: "kings1", 9371575: "kings1", 9371577: "kings1", 9371579: "kings1", 9371580: "kings1", 9371581: "kings1", 9371582: "kings1", 9371583: "kings1", 9371584: "kings1", 9371585: "kings1", 9371604: "suns", 9371605: "suns", 9371607: "suns", 9371609: "suns", 9371614: "suns", 9371618: "suns", 9371620: "suns", 9371623: "suns", 9371627: "suns", 9370732: "lakers", 9370737: "lakers", 9370741: "lakers", 9370744: "lakers", 9370747: "lakers", 9370748: "lakers", 9370750: "lakers", 9370752: "lakers", 9370754: "lakers", 9370757: "lakers", 9370760: "lakers", 9370763: "lakers", 9370766: "lakers", 9370768: "lakers", 9370774: "lakers", 9370967: "spurs", 9370973: "spurs", 9370978: "spurs", 9370983: "spurs", 9370987: "spurs", 9370993: "spurs", 9370998: "spurs", 9371003: "spurs", 9371008: "spurs", 9371013: "spurs", 9371017: "spurs", 9371025: "spurs", 9371029: "spurs", 9371170: "grizzlies", 9371174: "grizzlies", 9371177: "grizzlies", 9371180: "grizzlies", 9371182: "grizzlies", 9371190: "grizzlies", 9371194: "grizzlies", 9371197: "grizzlies", 9371204: "grizzlies", 9371321: "mavericks", 9371327: "mavericks", 9371331: "mavericks", 9371335: "mavericks", 9371340: "mavericks", 9371346: "mavericks", 9371353: "mavericks", 9371358: "mavericks", 9371363: "mavericks", 9371367: "mavericks", 9371371: "mavericks", 9371375: "mavericks", 9370564: "rockets", 9370571: "rockets", 9370575: "rockets", 9370579: "rockets", 9370585: "rockets", 9372712: "rockets", 9372713: "rockets", 9372714: "rockets", 9372715: "rockets", 9372716: "rockets", 9372717: "rockets", 9372718: "rockets", 9371479: "pelicans", 9371481: "pelicans", 9371484: "pelicans", 9371487: "pelicans", 9371489: "pelicans", 9371491: "pelicans", 9371493: "pelicans", 9371495: "pelicans", 9371498: "pelicans", 9371500: "pelicans", 9371502: "pelicans", 9371503: "pelicans", 9342037: "panthers", 9342040: "panthers", 9342045: "panthers", 9342051: "panthers", 9342053: "panthers", 9342055: "panthers", 9342057: "panthers", 9342066: "panthers", 9342376: "lightning", 9342379: "lightning", 9342383: "lightning", 9342387: "lightning", 9342392: "lightning", 9342400: "lightning", 9342403: "lightning", 9342406: "lightning", 9342409: "lightning", 9341685: "redwings", 9341691: "redwings", 9341697: "redwings", 9341703: "redwings", 9341711: "redwings", 9341715: "redwings", 9341722: "redwings", 9341726: "redwings", 9341745: "redwings", 9341448: "bruins", 9341458: "bruins", 9341462: "bruins", 9341467: "bruins", 9341477: "bruins", 9341483: "bruins", 9341489: "bruins", 9341501: "bruins", 9342199: "canadiens", 9342202: "canadiens", 9342208: "canadiens", 9342215: "canadiens", 9342220: "canadiens", 9342224: "canadiens", 9342230: "canadiens", 9342235: "canadiens", 9342240: "canadiens", 9342245: "canadiens", 9342396: "senators", 9342397: "senators", 9342402: "senators", 9342411: "senators", 9342413: "senators", 9342415: "senators", 9342417: "senators", 9342422: "senators", 9342222: "mapleleafs", 9342225: "mapleleafs", 9342229: "mapleleafs", 9342233: "mapleleafs", 9342237: "mapleleafs", 9342241: "mapleleafs", 9342244: "mapleleafs", 9342248: "mapleleafs", 9342250: "mapleleafs", 9342253: "mapleleafs", 9342254: "mapleleafs", 9342257: "mapleleafs", 9342259: "mapleleafs", 9342263: "mapleleafs", 9342156: "sabres", 9342160: "sabres", 9342165: "sabres", 9342168: "sabres", 9342171: "sabres", 9342174: "sabres", 9342178: "sabres", 9342180: "sabres", 9342184: "sabres", 9342187: "sabres", 9342015: "capitals", 9342054: "capitals", 9342056: "capitals", 9342059: "capitals", 9342062: "capitals", 9342064: "capitals", 9342068: "capitals", 9342071: "capitals", 9342074: "capitals", 9342012: "capitals", 9341509: "rangers", 9341511: "rangers", 9341516: "rangers", 9341522: "rangers", 9341529: "rangers", 9341532: "rangers", 9341537: "rangers", 9341545: "rangers", 9342210: "islanders", 9342214: "islanders", 9342223: "islanders", 9342227: "islanders", 9342232: "islanders", 9342238: "islanders", 9342242: "islanders", 9342246: "islanders", 9342252: "islanders", 9342194: "islanders", 9341878: "penguins", 9341882: "penguins", 9341886: "penguins", 9341891: "penguins", 9341893: "penguins", 9341897: "penguins", 9341902: "penguins", 9341906: "penguins", 9341911: "penguins", 9341916: "penguins", 9341346: "devils", 9341350: "devils", 9341356: "devils", 9341361: "devils", 9341366: "devils", 9341369: "devils", 9341372: "devils", 9341375: "devils", 9341378: "devils", 9342338: "hurricanes", 9342340: "hurricanes", 9342342: "hurricanes", 9342347: "hurricanes", 9342350: "hurricanes", 9342352: "hurricanes", 9342354: "hurricanes", 9342356: "hurricanes", 9341698: "flyers", 9341701: "flyers", 9341705: "flyers", 9341708: "flyers", 9341712: "flyers", 9341716: "flyers", 9341720: "flyers", 9341724: "flyers", 9341729: "flyers", 9341731: "flyers", 9341733: "flyers", 9342426: "bluejackets", 9342427: "bluejackets", 9342428: "bluejackets", 9342430: "bluejackets", 9342431: "bluejackets", 9342432: "bluejackets", 9342433: "bluejackets", 9342435: "bluejackets", 9341304: "blackhawks", 9341308: "blackhawks", 9341310: "blackhawks", 9341313: "blackhawks", 9341316: "blackhawks", 9341318: "blackhawks", 9341321: "blackhawks", 9341323: "blackhawks", 9341326: "blackhawks", 9341663: "stars", 9341665: "stars", 9341672: "stars", 9341676: "stars", 9341679: "stars", 9341686: "stars", 9341688: "stars", 9341692: "stars", 9341840: "blues", 9341844: "blues", 9341846: "blues", 9341850: "blues", 9341853: "blues", 9341856: "blues", 9341857: "blues", 9341539: "avalanche", 9341542: "avalanche", 9341546: "avalanche", 9341549: "avalanche", 9341552: "avalanche", 9341554: "avalanche", 9341556: "avalanche", 9341559: "avalanche", 9341560: "avalanche", 9341412: "predators", 9341415: "predators", 9341417: "predators", 9341418: "predators", 9341421: "predators", 9341423: "predators", 9341427: "predators", 9341430: "predators", 9341433: "predators", 9341436: "predators", 9342018: "wild", 9342022: "wild", 9342026: "wild", 9342027: "wild", 9342030: "wild", 9342034: "wild", 9342036: "wild", 9342039: "wild", 9342042: "wild", 9342044: "wild", 9342047: "wild", 9341945: "jets", 9341947: "jets", 9341951: "jets", 9341954: "jets", 9341955: "jets", 9341958: "jets", 9341961: "jets", 9341965: "jets", 9341967: "jets", 9341976: "jets", 9341979: "jets", 9341963: "jets", 9341982: "jets", 9341684: "kings2", 9341670: "kings2", 9341689: "kings2", 9341693: "kings2", 9341696: "kings2", 9341699: "kings2", 9341702: "kings2", 9341709: "kings2", 9341677: "kings2", 9341662: "kings2", 9341718: "kings2", 9341721: "kings2", 9341531: "sharks", 9341536: "sharks", 9341541: "sharks", 9341544: "sharks", 9341547: "sharks", 9341551: "sharks", 9341555: "sharks", 9341557: "sharks", 9341494: "sharks", 9341499: "sharks", 9341431: "sharks", 9341538: "sharks", 9341561: "sharks", 9341520: "sharks", 9341374: "ducks", 9341383: "ducks", 9341386: "ducks", 9341388: "ducks", 9341390: "ducks", 9341392: "ducks", 9341395: "ducks", 9341327: "ducks", 9341399: "ducks", 9341402: "ducks", 9342221: "coyotes", 9342311: "coyotes", 9342296: "coyotes", 9342315: "coyotes", 9342216: "coyotes", 9342305: "coyotes", 9342320: "coyotes", 9342231: "coyotes", 9342323: "coyotes", 9341900: "canucks", 9341904: "canucks", 9341901: "canucks", 9341851: "canucks", 9341865: "canucks", 9341909: "canucks", 9341880: "canucks", 9341780: "canucks", 9341808: "canucks", 9341917: "canucks", 9341837: "canucks", 9341775: "canucks", 9342011: "flames", 9342063: "flames", 9342050: "flames", 9341971: "flames", 9342084: "flames", 9342094: "flames", 9341999: "flames", 9342035: "flames", 9341964: "flames", 9341810: "oilers", 9341814: "oilers", 9341817: "oilers", 9341820: "oilers", 9341823: "oilers", 9341827: "oilers", 9341831: "oilers", 9341834: "oilers", 9341838: "oilers", 9341848: "oilers", }

    return team[eventId]

def get_market_cap(eventId):


    market_cap = {'dodgers': 2400, 'cubs':1800, 'mets':1350, 'orioles':1000, 'astros':800,
                  'knicks': 2500, 'warriors':1300, 'trailblazers':940, 'hawks': 825, 'grizzlies':750,
                  'rangers':1200, 'bruins': 750, 'stars': 450, 'senators': 370, 'bluejackets': 226,
                  'patriots':3200, 'broncos':1940, 'panthers':1560, 'cardinals':1540, 'bengals':1445
                  }

    return market_cap[get_team(eventId)]

def get_sport(eventId):

        team = get_team(int(eventId))

        sport = { 'knicks': 'nba', 'warriors':'nba', 'trailblazers':'nba', 'hawks': 'nba', 'grizzlies':'nba',
                 'patriots':'nfl', 'broncos':'nfl', 'panthers':'nfl', 'cardinals':'nfl', 'bengals':'nfl',
                 'dodgers': 'mlb', 'cubs': 'mlb', 'mets': 'mlb', 'orioles': 'mlb', 'astros': 'mlb',
                 'rangers': 'nhl', 'bruins': 'nhl', 'stars': 'nhl', 'senators': 'nhl', 'bluejackets': 'nhl',
                 'raptors': 'nba', 'celtics': 'nba', 'nets': 'nba', '76ers': 'nba', 'cavaliers': 'nba', 'bulls': 'nba', 'pacers': 'nba', 'pistons': 'nba', 'bucks': 'nba', 'heat': 'nba', 'hornets': 'nba', 'wizards': 'nba', 'magic': 'nba', 'thunder': 'nba', 'jazz': 'nba', 'nuggets': 'nba', 'timberwolves': 'nba', 'clippers': 'nba', 'kings1': 'nba', 'suns': 'nba', 'lakers': 'nba', 'spurs': 'nba', 'mavericks': 'nba', 'rockets': 'nba', 'pelicans': 'nba',
                 'panthers': 'nhl', 'lightning': 'nhl', 'redwings': 'nhl', 'wings': 'nhl', 'canadiens': 'nhl', 'mapleleafs': 'nhl', 'sabres': 'nhl', 'capitals': 'nhl', 'islanders': 'nhl', 'penguins': 'nhl', 'devils': 'nhl', 'hurricanes': 'nhl', 'flyers': 'nhl', 'blackhawks': 'nhl', 'blues': 'nhl', 'avalanche': 'nhl', 'predators': 'nhl', 'wild': 'nhl', 'jets': 'nhl', 'kings2': 'nhl', 'sharks': 'nhl', 'ducks': 'nhl', 'coyotes': 'nhl', 'canucks': 'nhl', 'flames': 'nhl', 'oilers': 'nhl', }

        return sport[team]

def get_performer_id(event_id):

    team = get_team(int(event_id))

    performer_id = { "dodgers": 1061, "cubs": 5644, "mets": 5649, "orioles":4962, "astros": 4782,
                    "knicks":   2742, "warriors":136, "trailblazers":2562, "hawks": 6769, "grizzlies":  6772,
                    "rangers":  2764, "bruins": 2762, "stars":2766, "senators": 7551, "bluejackets":    6350,
                    "patriots": 31, "broncos":6050, "panthers": 6046, "cardinals":  329, "bengals": 6045
                     }

    return performer_id[team]

def get_full_team_name(team):

    full_name = {"dodgers": "Los Angeles Dodgers", "cubs": "Chicago Cubs", "mets": "New York Mets", "orioles": "Baltimore Orioles", "astros": "Houston Astros", "knicks": "New York Knicks", "warriors": "Golden State Warriors", "trailblazers": "Portland Trail Blazers", "hawks": "Atlanta Hawks", "grizzlies":"Memphis Grizzlies", "rangers": "New York Rangers", "bruins": "Boston Bruins", "stars": "Dallas Stars", "senators":"Ottawa Senators", "bluejackets":"Columbus Blue Jackets","dodgers": "Los Angeles Dodgers", "cubs": "Chicago Cubs", "mets": "New York Mets", "orioles": "Baltimore Orioles", "astros": "Houston Astros", "knicks": "New York Knicks", "warriors": "Golden State Warriors", "trailblazers": "Portland Trail Blazers", "hawks": "Atlanta Hawks", "grizzlies": "Memphis Grizzlies", "rangers": "New York Rangers", "bruins": "Boston Bruins", "stars": "Dallas Stars", "senators": "Ottawa Senators", "jackets": "Columbus Blue Jackets", "raptors": "Toronto Raptors", "celtics": "Boston Celtics", "nets": "Brooklyn Nets", "76ers": "Philadelphia 76ers", "cavaliers": "Cleveland Cavaliers", "bulls": "Chicago Bulls", "pacers": "Indiana Pacers", "pistons": "Detroit Pistons", "bucks": "Milwaukee Bucks", "heat": "Miami Heat", "hornets": "Charlotte Hornets", "wizards": "Washington Wizards", "magic": "Orlando Magic", "thunder": "Oklahoma City Thunder", "jazz": "Utah Jazz", "nuggets": "Denver Nuggets", "timberwolves": "Minnesota Timberwolves", "clippers": "Los Angeles Clippers", "kings1": "Sacramento Kings", "suns": "Phoenix Suns", "lakers": "Los Angeles Lakers", "spurs": "San Antonio Spurs", "mavericks": "Dallas Mavericks", "rockets": "Houston Rockets", "pelicans": "New Orleans Pelicans", "panthers": "Florida Panthers", "lightning": "Tampa Bay Lightning", "redwings": "Detroit Red Wings", "wings": "Detroit Red Wings", "canadiens": "Montreal Canadiens", "mapleleafs": "Toronto Maple Leafs", "sabres": "Buffalo Sabres", "capitals": "Washington Capitals", "islanders": "New York Islanders", "penguins": "Pittsburgh Penguins", "devils": "New Jersey Devils", "hurricanes": "Carolina Hurricanes", "flyers": "Philadelphia Flyers", "blackhawks": "Chicago Blackhawks", "blues": "St. Louis Blues", "avalanche": "Colorado Avalanche", "predators": "Nashville Predators", "wild": "Minnesota Wild", "jets": "Winnipeg Jets", "kings2": "Los Angeles Kings", "sharks": "San Jose Sharks", "ducks": "Anaheim Ducks", "coyotes": "Arizona Coyotes", "canucks": "Vancouver Canucks", "flames": "Calgary Flames", "oilers": "Edmonton Oilers", }
    return full_name[team]

def get_all_teams(sport):

    teams = {"mlb":[],"nba":[]}

    teams['mlb'] = ["Atlanta Braves", "Miami Marlins", "New York Mets", "Philadelphia Phillies", "Washington Nationals", "Chicago Cubs", "Cincinnati Reds", "Houston Astros", "Milwaukee Brewers", "Pittsburgh Pirates", "St. Louis Cardinals", "Arizona Diamondbacks", "Colorado Rockies", "Los Angeles Dodgers", "San Diego Padres", "San Francisco Giants", "Baltimore Orioles", "Boston Red", "New York Yankees", "Tampa Bay Rays", "Toronto Blue Jays", "Chicago White Sox", "Cleveland Indians", "Detroit Tigers", "Kansas City Royals", "Minnesota Twins", "Los Angeles Angels", "Oakland Athletics", "Seattle Mariners", "Texas Rangers"]
    teams['nba'] =["Atlanta Hawks","Boston Celtics","Brooklyn Nets","Charlotte Hornets","Chicago Bulls","Cleveland Cavaliers","Dallas Mavericks","Denver Nuggets","Detroit Pistons","Golden State Warriors","Houston Rockets","Indiana Pacers","LA Clippers","Los Angeles Lakers","Memphis Grizzlies","Miami Heat","Milwaukee Bucks","Minnesota Timberwolves","New Orleans Pelicans","New York Knicks","Oklahoma City Thunder","Orlando Magic","Philadelphia 76ers","Phoenix Suns","Portland Trail Blazers","Sacramento Kings","San Antonio Spurs","Toronto Raptors","Utah Jazz","Washington Wizards"]
    teams['nfl'] = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Los Angeles Rams', 'Los Angeles Chargers', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Redskins']
    teams['nhl'] = ['Anaheim Ducks', 'Arizona Coyotes', 'Boston Bruins', 'Buffalo Sabres', 'Calgary Flames', 'Carolina Hurricanes', 'Chicago Blackhawks', 'Colorado Avalanche', 'Columbus Blue Jackets', 'Dallas Stars', 'Detroit Red Wings', 'Edmonton Oilers', 'Florida Panthers', 'Los Angeles Kings', 'Minnesota Wild', 'Montreal Canadiens', 'Nashville Predators', 'New Jersey Devils', 'New York Islanders', 'New York Rangers', 'Ottawa Senators', 'Philadelphia Flyers', 'Pittsburgh Penguins', 'San Jose Sharks', 'St. Louis Blues', 'Tampa Bay Lightning', 'Toronto Maple Leafs', 'Vancouver Canucks', 'Vegas Golden Knights', 'Washington Capitals', 'Winnipeg Jets']

    return teams[sport]
