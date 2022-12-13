import pickle
import numpy as np
from flask import Flask
from flask import request
from flask import render_template 



# create flask app
app = Flask(__name__)


# Function that takes a string and returns the corresponding integer
def string_to_make(s):
    make_list = {'ABARTH': 0, 'ALFA ROMEO': 1, 'ALPINE': 2, 'ASTON MARTIN': 3, 'AUDI': 4, 'AUSTIN': 5, 'BENTLEY': 6, 'BMW': 7, 'CADILLAC': 8, 'CHEVROLET': 9, 'CHRYSLER': 10, 'CITROEN': 11, 'CORVETTE': 12, 'CUPRA': 13, 'DACIA': 14, 'DAEWOO': 15, 'DAIHATSU': 16, 'DFSK': 17, 'DODGE': 18, 'DS': 19, 'FERRARI': 20, 'FIAT': 21, 'FORD': 22, 'GALLOPER': 23, 'HONDA': 24, 'HUMMER': 25, 'HYUNDAI': 26, 'INFINITI': 27, 'ISUZU': 28, 'IVECO': 29, 'IVECO-PEGASO': 30, 'JAGUAR': 31, 'JEEP': 32, 'KIA': 33, 'LAMBORGHINI': 34, 'LANCIA': 35, 'LAND-ROVER': 36, 'LDV': 37, 'LEXUS': 38, 'LOTUS': 39, 'MAHINDRA': 40, 'MASERATI': 41, 'MAXUS': 42, 'MAZDA': 43, 'MERCEDES-BENZ': 44, 'MG': 45, 'MINI': 46, 'MITSUBISHI': 47, 'MORGAN': 48, 'NISSAN': 49, 'OPEL': 50, 'PEUGEOT': 51, 'PIAGGIO': 52, 'PONTIAC': 53, 'PORSCHE': 54, 'RENAULT': 55, 'ROVER': 56, 'SAAB': 57, 'SANTANA': 58, 'SEAT': 59, 'SKODA': 60, 'SMART': 61, 'SSANGYONG': 62, 'SUBARU': 63, 'SUZUKI': 64, 'TATA': 65, 'TESLA': 66, 'TOYOTA': 67, 'UMM': 68, 'VOLKSWAGEN': 69, 'VOLVO': 70}
    if s in make_list:
        return make_list[s]
    else:
        return None

# Function that takes a string and returns the corresponding integer
def string_to_model(s):
    model_list = {'100': 0, '1007': 1, '100D': 2, '106': 3, '107': 4, '108': 5, '124 Spider': 6, '140D': 7, '147': 8, '156': 9, '159': 10, '164': 11, '19': 12, '190': 13, '200': 14, '2008': 15, '205': 16, '206': 17, '206 +': 18, '206 SW': 19, '207': 20, '207 +': 21, '208': 22, '208 XAD': 23, '220': 24, '230': 25, '240': 26, '25': 27, '260': 28, '2CV': 29, '300': 30, '300 GT': 31, '300 ZX': 32, '3008': 33, '3008 Hybrid': 34, '300C': 35, '300M': 36, '306': 37, '307': 38, '307 SW': 39, '308': 40, '309': 41, '323': 42, '33': 43, '350': 44, '350Z': 45, '355': 46, '360': 47, '370Z': 48, '4007': 49, '4008': 50, '406': 51, '407': 52, '407 SW': 53, '45': 54, '458': 55, '488': 56, '4Runner': 57, '500': 58, '5008': 59, '500C': 60, '500L': 61, '500X': 62, '505': 63, '508': 64, '508 Hybrid': 65, '580': 66, '599': 67, '600': 68, '607': 69, '626': 70, '718': 71, '740': 72, '75': 73, '806': 74, '807': 75, '812': 76, '9-3': 77, '9-5': 78, '90': 79, '911': 80, '928': 81, '944': 82, '960': 83, '968': 84, 'A1': 85, 'A110': 86, 'A2': 87, 'A3': 88, 'A4': 89, 'A4 Allroad Quattro': 90, 'A5': 91, 'A6': 92, 'A6 allroad quattro': 93, 'A7': 94, 'A8': 95, 'ALTEA': 96, 'AMG GT': 97, 'ASX': 98, 'AX': 99, 'Accent': 100, 'Accord': 101, 'Across': 102, 'Actyon': 103, 'Adam': 104, 'Agila': 105, 'Alhambra': 106, 'Allroad Quattro': 107, 'Almera': 108, 'Almera Tino': 109, 'Altea Freetrack': 110, 'Altea XL': 111, 'Alto': 112, 'Amarok': 113, 'Ampera': 114, 'Anibal': 115, 'Antara': 116, 'Aria': 117, 'Arona': 118, 'Arosa': 119, 'Arteon': 120, 'Astra': 121, 'Ateca': 122, 'Atos': 123, 'Atos Prime': 124, 'Auris': 125, 'Avenger': 126, 'Avensis': 127, 'Avensis Verso': 128, 'Aventador': 129, 'Aveo': 130, 'Aygo': 131, 'B-MAX': 132, 'BLS': 133, 'BRZ': 134, 'BX': 135, 'Barchetta': 136, 'Beetle': 137, 'Bentayga': 138, 'Berlingo': 139, 'Bipper': 140, 'Bora': 141, 'Boxer': 142, 'Boxster': 143, 'Brava': 144, 'Bravo': 145, 'Brera': 146, 'C-15': 147, 'C-Crosser': 148, 'C-Elysée': 149, 'C-HR': 150, 'C-Max': 151, 'C-Zero': 152, 'C1': 153, 'C2': 154, 'C3': 155, 'C3 Aircross': 156, 'C3 Picasso': 157, 'C3 Pluriel': 158, 'C30': 159, 'C4': 160, 'C4 Aircross': 161, 'C4 Cactus': 162, 'C4 Picasso': 163, 'C4 Sedán': 164, 'C4 Spacetourer': 165, 'C5': 166, 'C5 Aircross': 167, 'C5 Aircross Hybrid': 168, 'C6': 169, 'C70': 170, 'C8': 171, 'CC': 172, 'CLA': 173, 'CLS': 174, 'CLUBMAN': 175, 'CR-V': 176, 'CR-Z': 177, 'CRX': 178, 'CT': 179, 'CTS': 180, 'CUBE': 181, 'CX-3': 182, 'CX-30': 183, 'CX-5': 184, 'CX-7': 185, 'CX-9': 186, 'Cabrio': 187, 'Cabriolet': 188, 'Cabstar': 189, 'Cabstar E': 190, 'Caddy': 191, 'Caliber': 192, 'California': 193, 'Camaro': 194, 'Camry': 195, 'Capri': 196, 'Captiva': 197, 'Captur': 198, 'Caravelle': 199, 'Carens': 200, 'Carisma': 201, 'Carnival': 202, 'Cayenne': 203, 'Cayenne Coupé': 204, 'Cayman': 205, 'Ceed Tourer': 206, 'Celica': 207, 'Cerato': 208, 'Cherokee': 209, 'Citan': 210, 'Citigo': 211, 'Civic': 212, 'Clase A': 213, 'Clase B': 214, 'Clase C': 215, 'Clase CL': 216, 'Clase CLA': 217, 'Clase CLC': 218, 'Clase CLK': 219, 'Clase CLS': 220, 'Clase E': 221, 'Clase G': 222, 'Clase GL': 223, 'Clase GLA': 224, 'Clase GLC': 225, 'Clase GLE': 226, 'Clase GLE Coupé': 227, 'Clase GLK': 228, 'Clase GLS': 229, 'Clase M': 230, 'Clase R': 231, 'Clase S': 232, 'Clase SL': 233, 'Clase SL R129': 234, 'Clase SLC': 235, 'Clase SLK': 236, 'Clase V': 237, 'Clase X': 238, 'Clio': 239, 'Clio 4': 240, 'Clio Campus': 241, 'Clio III': 242, 'Colt': 243, 'Combo': 244, 'Combo Life': 245, 'Commander': 246, 'Compact': 247, 'Compass': 248, 'Connect': 249, 'Continental': 250, 'Continental Flying Spur': 251, 'Continental GT': 252, 'Continental GTC': 253, 'Corolla': 254, 'Corolla Sedán': 255, 'Corolla Verso': 256, 'Corrado': 257, 'Corsa': 258, 'Corsa Van': 259, 'Corsa-e': 260, 'Corvette': 261, 'Corvette Stingray': 262, 'Countryman': 263, 'Coupe': 264, 'Coupé': 265, 'Courier': 266, 'Crafter': 267, 'Croma': 268, 'Crossfire': 269, 'Crossland': 270, 'Crossland X': 271, 'Cruze': 272, 'Córdoba': 273, 'D-Max': 274, 'DB9': 275, 'DS 3': 276, 'DS 3 Crossback': 277, 'DS 3 Crossback E-Tense': 278, 'DS 4': 279, 'DS 4 Crossback': 280, 'DS 5': 281, 'DS 7 Crossback': 282, 'DS 7 Crossback E-Tense': 283, 'DS 9': 284, 'DS3': 285, 'DS4': 286, 'DS5': 287, 'Daily': 288, 'Defender': 289, 'Delta': 290, 'Discovery': 291, 'Discovery 4': 292, 'Discovery Sport': 293, 'Doblò': 294, 'Doblò Cargo': 295, 'Doblò Panorama': 296, 'Dokker': 297, 'Ducato': 298, 'Duster': 299, 'Dyna': 300, 'E-Pace': 301, 'EQC': 302, 'ES': 303, 'EVALIA': 304, 'EX': 305, 'Eclipse': 306, 'Eclipse Cross': 307, 'EcoSport': 308, 'Edge': 309, 'El Dorado': 310, 'Elantra': 311, 'Elise': 312, 'Eos': 313, 'Epica': 314, 'Escalade': 315, 'Escort': 316, 'Espace': 317, 'Evanda': 318, 'Evasión': 319, 'Exceed': 320, 'Exeo': 321, 'Expert': 322, 'Explorer': 323, 'Express': 324, 'F-Pace': 325, 'F-Type': 326, 'F355': 327, 'F430': 328, 'FF': 329, 'FR-V': 330, 'FX': 331, 'Fabia': 332, 'Felicia': 333, 'Fengon 5': 334, 'Fiesta': 335, 'Fiesta Van': 336, 'Fiorino': 337, 'Firebird': 338, 'Fluence': 339, 'Flying Spur': 340, 'Focus': 341, 'Focus C-MAX': 342, 'Forester': 343, 'Formentor': 344, 'Freelander': 345, 'Freemont': 346, 'Frontera': 347, 'Fullback': 348, 'Fusion': 349, 'G': 350, 'G3X Justy': 351, 'GLA': 352, 'GLB': 353, 'GLC Coupé': 354, 'GLE': 355, 'GLE Coupé': 356, 'GLS': 357, 'GR Yaris': 358, 'GS': 359, 'GS300': 360, 'GS450h': 361, 'GT': 362, 'GT-R': 363, 'GT86': 364, 'GTC': 365, 'GTC4': 366, 'Galant': 367, 'Galaxy': 368, 'Gallardo': 369, 'Genesis': 370, 'Getz': 371, 'Ghibli': 372, 'Giulia': 373, 'Giulietta': 374, 'Goa': 375, 'Goa Pik Up Plus': 376, 'Golf': 377, 'Golf Plus': 378, 'Golf Sportsvan': 379, 'GranCabrio': 380, 'GranTurismo': 381, 'Grand C-Max': 382, 'Grand C4 Picasso': 383, 'Grand C4 Spacetourer': 384, 'Grand California': 385, 'Grand Cherokee': 386, 'Grand Espace': 387, 'Grand Kangoo Combi': 388, 'Grand Modus': 389, 'Grand Safari': 390, 'Grand Santa Fe': 391, 'Grand Scénic': 392, 'Grand Tourneo Connect': 393, 'Grand Vitara': 394, 'Grand Vitara XL-7': 395, 'Grand Voyager': 396, 'Grande Punto': 397, 'Grandis': 398, 'Grandland X': 399, 'Grandland X PHEV': 400, 'H-1': 401, 'H-1 Travel': 402, 'H2': 403, 'H350': 404, 'HR-V': 405, 'Hilux': 406, 'Honda e': 407, 'Huracán': 408, 'ID.3': 409, 'INDICA': 410, 'IONIQ': 411, 'IS': 412, 'IS200': 413, 'IS220d': 414, 'IS250': 415, 'IS300': 416, 'Ibiza': 417, 'Idea': 418, 'Ignis': 419, 'Impreza': 420, 'Inca': 421, 'Insight': 422, 'Insignia': 423, 'Interstar': 424, 'JUKE': 425, 'Jazz': 426, 'Jetta': 427, 'Jimny': 428, 'Journey': 429, 'Jumper': 430, 'Jumpy': 431, 'KA': 432, 'KUV100': 433, 'Ka+': 434, 'Kadett': 435, 'Kadjar': 436, 'Kalos': 437, 'Kamiq': 438, 'Kangoo': 439, 'Kangoo Combi': 440, 'Kangoo Express': 441, 'Kangoo Furgón': 442, 'Kangoo Z.E.': 443, 'Karl': 444, 'Karoq': 445, 'Kodiaq': 446, 'Koleos': 447, 'Kona': 448, 'Korando': 449, 'Korando KJ': 450, 'Kubistar': 451, 'Kuga': 452, 'Kyron': 453, 'L200': 454, 'LEAF': 455, 'LEVORG': 456, 'LS': 457, 'LS460': 458, 'LT': 459, 'Lacetti': 460, 'Laguna': 461, 'Lancer': 462, 'Land Cruiser': 463, 'Land Cruiser 100': 464, 'Land Cruiser 200': 465, 'Land Cruiser 80': 466, 'Land Cruiser 90': 467, 'Lanos': 468, 'Lantra': 469, 'Latitude': 470, 'Legacy': 471, 'Leganza': 472, 'Legend': 473, 'Levante': 474, 'León': 475, 'Liana': 476, 'Linea': 477, 'Lodgy': 478, 'Logan': 479, 'Lupo': 480, 'Lybra': 481, 'M': 482, 'MGF': 483, 'MINI': 484, 'MX-30': 485, 'MX-5': 486, 'Macan': 487, 'Malibu': 488, 'Manta': 489, 'Marbella': 490, 'Mascott': 491, 'Massif': 492, 'Master': 493, 'Master Propulsión': 494, 'Matiz': 495, 'Matrix': 496, 'Maverick': 497, 'Maxima QX': 498, 'Maxity': 499, 'Maxus': 500, 'Mazda2': 501, 'Mazda3': 502, 'Mazda5': 503, 'Mazda6': 504, 'Mercedes-AMG GT': 505, 'Meriva': 506, 'MiTo': 507, 'Micra': 508, 'Mii': 509, 'Mini': 510, 'Model 3': 511, 'Model S': 512, 'Model X': 513, 'Modus': 514, 'Mokka': 515, 'Mokka X': 516, 'Mondeo': 517, 'Mondial': 518, 'Monterey': 519, 'Montero': 520, 'Montero Sport': 521, 'Montero iO': 522, 'Movano': 523, 'Multipla': 524, 'Multivan': 525, 'Murano': 526, 'Musa': 527, 'Musso': 528, 'Mustang': 529, 'Mégane': 530, 'NOTE': 531, 'NP300 Navara': 532, 'NT400': 533, 'NT400 Cabstar': 534, 'NV200': 535, 'NV250': 536, 'NV300': 537, 'NV400': 538, 'NX': 539, 'Navara': 540, 'Nemo': 541, 'Neon': 542, 'New Beetle': 543, 'Niro': 544, 'Niro Hïbrido Enchufable': 545, 'Niro PHEV': 546, 'Nitro': 547, 'Nubira': 548, 'Octavia': 549, 'Omega': 550, 'Optima': 551, 'Optima PHEV': 552, 'Optima SW': 553, 'Orlando': 554, 'Outback': 555, 'Outlander': 556, 'PT Cruiser': 557, 'PULSAR': 558, 'Paceman': 559, 'Panamera': 560, 'Panda': 561, 'Panda Classic': 562, 'Partner': 563, 'Partner Origin': 564, 'Passat': 565, 'Passat CC': 566, 'Pathfinder': 567, 'Patriot': 568, 'Patrol': 569, 'Patrol GR': 570, 'Phaeton': 571, 'Phedra': 572, 'Picanto': 573, 'Pick-up': 574, 'Pixo': 575, 'Plus 4': 576, 'Polo': 577, 'Porter': 578, 'Pregio': 579, 'Prelude': 580, 'Premacy': 581, 'Previa': 582, 'Primastar': 583, 'Primera': 584, 'Prius': 585, 'Prius+': 586, 'Pro Ceed': 587, 'ProCeed': 588, 'Proace': 589, 'Proace City Verso': 590, 'Proace Verso': 591, 'Probe': 592, 'Puma': 593, 'Punto': 594, 'Punto EVO': 595, 'Q2': 596, 'Q3': 597, 'Q3 Sportback': 598, 'Q30': 599, 'Q5': 600, 'Q50': 601, 'Q60': 602, 'Q7': 603, 'Q70': 604, 'Q8': 605, 'QASHQAI': 606, 'QASHQAI+2': 607, 'QX30': 608, 'QX70': 609, 'Quanto': 610, 'Quattroporte': 611, 'Qubo': 612, 'R11': 613, 'R21': 614, 'R4': 615, 'R5': 616, 'R6': 617, 'R8': 618, 'RC': 619, 'RCZ': 620, 'RS Q3': 621, 'RS3': 622, 'RS4': 623, 'RS5': 624, 'RS6': 625, 'RS7': 626, 'RX': 627, 'RX-8': 628, 'RX300': 629, 'RX350': 630, 'RX400h': 631, 'Range Rover': 632, 'Range Rover Evoque': 633, 'Range Rover Sport': 634, 'Range Rover Velar': 635, 'Ranger': 636, 'Rapid': 637, 'Rapide': 638, 'Rav4': 639, 'Renegade': 640, 'Rexton': 641, 'Rexton II': 642, 'Rifter': 643, 'Rio': 644, 'Rodius': 645, 'Roomster': 646, 'S-MAX': 647, 'S-Type': 648, 'S2000': 649, 'S3': 650, 'S4': 651, 'S40': 652, 'S5': 653, 'S6': 654, 'S60': 655, 'S7': 656, 'S8': 657, 'S80': 658, 'S90': 659, 'SC430': 660, 'SCross': 661, 'SLS AMG': 662, 'SQ5': 663, 'SQ7': 664, 'SRX': 665, 'SX4': 666, 'SX4 S-Cross': 667, 'Safari': 668, 'Safrane': 669, 'Samurai': 670, 'Sandero': 671, 'Santa Fe': 672, 'Santamo': 673, 'Santana': 674, 'Saxo': 675, 'Scala': 676, 'Scirocco': 677, 'Scout': 678, 'Scudo': 679, 'Scénic': 680, 'Sebring': 681, 'Sebring 200C': 682, 'Sedici': 683, 'Seicento': 684, 'Sephia II': 685, 'Serena': 686, 'Serie 1': 687, 'Serie 2': 688, 'Serie 2 Active Tourer': 689, 'Serie 2 Gran Tourer': 690, 'Serie 3': 691, 'Serie 4': 692, 'Serie 5': 693, 'Serie 6': 694, 'Serie 7': 695, 'Serie 8': 696, 'Serie C': 697, 'Serie K': 698, 'Serie N': 699, 'Serie XJ': 700, 'Serie XK': 701, 'Sharan': 702, 'Shuma': 703, 'Sierra': 704, 'Signum': 705, 'Sonata': 706, 'Sorento': 707, 'Soul': 708, 'Soul EV': 709, 'Space Gear': 710, 'Space Star': 711, 'Space Wagon': 712, 'Spaceback': 713, 'Spacetourer': 714, 'Spark': 715, 'Spider': 716, 'Splash': 717, 'Sportage': 718, 'Sports Pick Up': 719, 'Sprinter': 720, 'Spyder': 721, 'Stelvio': 722, 'Stilo': 723, 'Stinger': 724, 'Stonic': 725, 'Stratus': 726, 'Stream': 727, 'Sunny': 728, 'Super Exceed': 729, 'Superb': 730, 'Supra': 731, 'Swace': 732, 'Swift': 733, 'T-Cross': 734, 'T-Roc': 735, 'TRANS AM': 736, 'TT': 737, 'TT RS': 738, 'TTS': 739, 'TUCSON': 740, 'Tahoe': 741, 'Talento': 742, 'Talisman': 743, 'Tarraco': 744, 'Taycan': 745, 'Terios': 746, 'Terracan': 747, 'Terrano': 748, 'Terrano II': 749, 'Thema': 750, 'Tigra': 751, 'Tiguan': 752, 'Tiguan Allspace': 753, 'Tiida': 754, 'Tipo': 755, 'Tivoli': 756, 'Toledo': 757, 'Touareg': 758, 'Touran': 759, 'Tourneo Connect': 760, 'Tourneo Courier': 761, 'Tourneo Custom': 762, 'Trade': 763, 'Trafic': 764, 'Trajet': 765, 'Transit': 766, 'Transit Connect': 767, 'Transit Courier': 768, 'Transit Custom': 769, 'Transporter': 770, 'Traveller': 771, 'Trax': 772, 'Tribeca': 773, 'Twingo': 774, 'UX': 775, 'Ulysse': 776, 'Uno': 777, 'Urban Cruiser': 778, 'V40': 779, 'V40 Cross Country': 780, 'V50': 781, 'V60': 782, 'V60 Cross Country': 783, 'V70': 784, 'V70 XC': 785, 'V8 Vantage': 786, 'V80': 787, 'V90': 788, 'V90 Cross Country': 789, 'Vanette Cargo': 790, 'Vantage': 791, 'Vantage V8': 792, 'Vectra': 793, 'Vel Satis': 794, 'Veloster': 795, 'Venga': 796, 'Verso': 797, 'Viano': 798, 'Viper': 799, 'Vitara': 800, 'Vito': 801, 'Vivaro': 802, 'Volt': 803, 'Voyager': 804, 'WRX STI': 805, 'Wind': 806, 'Wrangler': 807, 'Wrangler Unlimited': 808, 'X-TRAIL': 809, 'X-Type': 810, 'X1': 811, 'X2': 812, 'X3': 813, 'X4': 814, 'X5': 815, 'X6': 816, 'X7': 817, 'XC40': 818, 'XC60': 819, 'XC70': 820, 'XC90': 821, 'XCeed': 822, 'XE': 823, 'XF': 824, 'XG': 825, 'XJ': 826, 'XLV': 827, 'XUV500': 828, 'XV': 829, 'Xantia': 830, 'Xsara': 831, 'Xsara Picasso': 832, 'Y': 833, 'Y10': 834, 'Yaris': 835, 'Yeti': 836, 'Ypsilon': 837, 'Z1': 838, 'Z3': 839, 'Z4': 840, 'ZR': 841, 'ZX': 842, 'Zafira': 843, 'Zafira Life': 844, 'Zafira Tourer': 845, 'Zafira-e Life': 846, 'Zoe': 847, 'ceed': 848, 'ceed Sportswagon': 849, 'ceed Sporty Wagon': 850, 'e-2008': 851, 'e-208': 852, 'e-NV200': 853, 'e-NV200 EVALIA': 854, 'e-Niro': 855, 'e-Soul': 856, 'e-tron': 857, 'e-tron Sportback': 858, 'e-up!': 859, 'forfour': 860, 'fortwo': 861, 'i-Pace': 862, 'i10': 863, 'i20': 864, 'i20 Active': 865, 'i3': 866, 'i30': 867, 'i40': 868, 'i8': 869, 'iQ': 870, 'ion': 871, 'ix20': 872, 'ix35': 873, 'ix55': 874, 'pro_ceed GT': 875, 'roadster': 876, 'smart': 877, 'up!': 878, 'ë-C4': 879}
    if s in model_list:
        return model_list[s]
    else:
        return None 

# Function that takes a string and returns the corresponding integer
def string_to_fuel(s):
    fuel_list = {'Diésel': 0, 'Eléctrico': 1, 'Gas licuado (GLP)': 2, 'Gas natural (CNG)': 3, 'Gasolina': 4, 'Híbrido': 5, 'Híbrido enchufable': 6}
    if s in fuel_list:
        return fuel_list[s]
    else:
        return None

# Function that takes a string and returns the corresponding integer
def string_to_shift(s):
    shift_list = {'Automático': 0, 'Manual': 1}
    if s in shift_list:
        return shift_list[s]
    else:
        return None

# Function that takes a string and returns the corresponding integer
def string_to_province(s):
    province_list = {'A Coruña': 0, 'Albacete': 1, 'Alicante': 2, 'Almería': 3, 'Asturias': 4, 'Badajoz': 5, 'Baleares': 6, 'Barcelona': 7, 'Burgos': 8, 'Cantabria': 9, 'Castellón': 10, 'Ceuta': 11, 'Ciudad Real': 12, 'Cuenca': 13, 'Cáceres': 14, 'Cádiz': 15, 'Córdoba': 16, 'Girona': 17, 'Granada': 18, 'Guadalajara': 19, 'Guipúzcoa': 20, 'Huelva': 21, 'Huesca': 22, 'Jaén': 23, 'La Rioja': 24, 'Las Palmas': 25, 'León': 26, 'Lleida': 27, 'Lugo': 28, 'Madrid': 29, 'Melilla': 30, 'Murcia': 31, 'Málaga': 32, 'Navarra': 33, 'Orense': 34, 'Palencia': 35, 'Pontevedra': 36, 'Salamanca': 37, 'Segovia': 38, 'Sevilla': 39, 'Soria': 40, 'Tarragona': 41, 'Tenerife': 42, 'Teruel': 43, 'Toledo': 44, 'Valencia': 45, 'Valladolid': 46, 'Vizcaya': 47, 'Zamora': 48, 'Zaragoza': 49, 'Álava': 50, 'Ávila': 51}
    if s in province_list:
        return province_list[s]
    else:
        return None




# prediction function
def ValuePredictor(to_predict_list):

    to_predict_list = np.array(to_predict_list).reshape(1, 12)
    loaded_model = pickle.load(open("model.pkl", "rb"))

    print(to_predict_list)
    result = loaded_model.predict(to_predict_list)

    return result[0]

@app.route('/')
def index():
 return render_template('index.html') 
 
@app.route('/result', methods = ['POST'])
def result():

    if request.method == 'POST':

        to_predict_list = request.form.to_dict()

        to_predict_list['make'] = string_to_make(to_predict_list.get('make'))
        to_predict_list['model'] = string_to_model(to_predict_list.get('model'))
        to_predict_list['fuel']= string_to_fuel(to_predict_list.get('fuel'))
        to_predict_list['shift'] = string_to_shift(to_predict_list.get('shift'))
        to_predict_list['province'] = string_to_province(to_predict_list.get('province'))

        if (to_predict_list.get('is_professional') == 'True'):
            to_predict_list['is_professional'] = 1
        else: 
            to_predict_list['is_professional'] = 0 

        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)           
        return render_template("result.html", prediction = result)