from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'bican',
     'default_range': 'string',
     'description': 'The BICAN Donor Metadata schema specifies the metadata '
                    'relating to donors in BICAN. These metadata reflect the '
                    'metadata needed to accurately track donors and related '
                    'entities from the brain banks through the specimen portal.',
     'id': 'https://w3id.org/brain-bican/donor',
     'imports': ['bican_biolink', 'bican_prov', 'linkml:types'],
     'name': 'Donor',
     'prefixes': {'NIMP': {'prefix_prefix': 'NIMP',
                           'prefix_reference': 'http://example.org/NIMP/'},
                  'bican': {'prefix_prefix': 'bican',
                            'prefix_reference': 'https://identifiers.org/brain-bican/vocab/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'ncbi': {'prefix_prefix': 'ncbi',
                           'prefix_reference': 'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi'},
                  'qudr': {'prefix_prefix': 'qudr',
                           'prefix_reference': 'http://qudt.org'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'spdx': {'prefix_prefix': 'spdx',
                           'prefix_reference': 'http://spdx.org/rdf/terms#'}},
     'source_file': 'donor.yaml',
     'subsets': {'Restricted': {'description': 'The data stored in this attribute '
                                               'is restricted to people with a '
                                               'required clearence.',
                                'from_schema': 'https://w3id.org/brain-bican/donor',
                                'name': 'Restricted'}},
     'title': 'Donor Schema'} )

class AgingType(str, Enum):
    pTau = "pTau"
    """
    A microtubule-associated protein tau that includes at least one phosphorylated residue.
    """
    pTDP_43 = "pTDP-43"
    """
    A protein that is a translation product of the human TARDBP gene or a 1:1 ortholog thereof.
    """
    atherosclerosis = "atherosclerosis"
    """
    Build-up of fatty material and calcium deposition in the arterial wall resulting in partial or complete occlusion of the arterial lumen.
    """
    arteriolosclerosis = "arteriolosclerosis"
    """
    The thickening of the wall of the small arteries and arterioles. It is caused by deposition of hyaline material in the wall or concentric smooth muscle wall hypertrophy. It results in lumen narrowing and tissue ischemia.
    """
    Other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "Other (specify)"


class ArtifactType(str, Enum):
    grossCOLON_brain_removalSOLIDUSdissection = "gross: brain removal/dissection"
    """
    A planned process that separates and isolates the brain or tissues thereof for surgical purposes, or for the analysis of their structures.
    """
    microscopicCOLON_autolysis = "microscopic: autolysis"
    """
    A programmed cell death process observed in bacteria and filamentous fungi and leading to spontaneous death by lysis. Examples are lysis of the mother cell during sporulation of Bacillus subtilis and self-degradation of fungal cells in Aspergillus nidulans. Autolysis is also involved in bacterial biofilm formation. [GO]
    """
    Other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "Other (specify)"


class BirthCountry(str, Enum):
    """
    Namibia
    """
    AF = "AF"
    """
    Afghanistan
    """
    AL = "AL"
    """
    Albania
    """
    DZ = "DZ"
    """
    Algeria
    """
    AS = "AS"
    """
    American Samoa
    """
    AD = "AD"
    """
    Andorra
    """
    AO = "AO"
    """
    Angola
    """
    AI = "AI"
    """
    Anguilla
    """
    AQ = "AQ"
    """
    Antarctica
    """
    AG = "AG"
    """
    Antigua and Barbuda
    """
    AR = "AR"
    """
    Argentina
    """
    AM = "AM"
    """
    Armenia
    """
    AW = "AW"
    """
    Aruba
    """
    AU = "AU"
    """
    Australia
    """
    AT = "AT"
    """
    Austria
    """
    AZ = "AZ"
    """
    Azerbaijan
    """
    BS = "BS"
    """
    Bahamas (the)
    """
    BH = "BH"
    """
    Bahrain
    """
    BD = "BD"
    """
    Bangladesh
    """
    BB = "BB"
    """
    Barbados
    """
    BY = "BY"
    """
    Belarus
    """
    BE = "BE"
    """
    Belgium
    """
    BZ = "BZ"
    """
    Belize
    """
    BJ = "BJ"
    """
    Benin
    """
    BM = "BM"
    """
    Bermuda
    """
    BT = "BT"
    """
    Bhutan
    """
    BO = "BO"
    """
    Bolivia (Plurinational State of)
    """
    BQ = "BQ"
    """
    Bonaire, Sint Eustatius and Saba
    """
    BA = "BA"
    """
    Bosnia and Herzegovina
    """
    BW = "BW"
    """
    Botswana
    """
    BV = "BV"
    """
    Bouvet Island
    """
    BR = "BR"
    """
    Brazil
    """
    IO = "IO"
    """
    British Indian Ocean Territory (the)
    """
    BN = "BN"
    """
    Brunei Darussalam
    """
    BG = "BG"
    """
    Bulgaria
    """
    BF = "BF"
    """
    Burkina Faso
    """
    BI = "BI"
    """
    Burundi
    """
    CV = "CV"
    """
    Cabo Verde
    """
    KH = "KH"
    """
    Cambodia
    """
    CM = "CM"
    """
    Cameroon
    """
    CA = "CA"
    """
    Canada
    """
    KY = "KY"
    """
    Cayman Islands (the)
    """
    CF = "CF"
    """
    Central African Republic (the)
    """
    TD = "TD"
    """
    Chad
    """
    CL = "CL"
    """
    Chile
    """
    CN = "CN"
    """
    China
    """
    CX = "CX"
    """
    Christmas Island
    """
    CC = "CC"
    """
    Cocos (Keeling) Islands (the)
    """
    CO = "CO"
    """
    Colombia
    """
    KM = "KM"
    """
    Comoros (the)
    """
    CD = "CD"
    """
    Congo (the Democratic Republic of the)
    """
    CG = "CG"
    """
    Congo (the)
    """
    CK = "CK"
    """
    Cook Islands (the)
    """
    CR = "CR"
    """
    Costa Rica
    """
    HR = "HR"
    """
    Croatia
    """
    CU = "CU"
    """
    Cuba
    """
    CW = "CW"
    """
    Curaçao
    """
    CY = "CY"
    """
    Cyprus
    """
    CZ = "CZ"
    """
    Czechia
    """
    CI = "CI"
    """
    Côte d'Ivoire
    """
    DK = "DK"
    """
    Denmark
    """
    DJ = "DJ"
    """
    Djibouti
    """
    DM = "DM"
    """
    Dominica
    """
    DO = "DO"
    """
    Dominican Republic (the)
    """
    EC = "EC"
    """
    Ecuador
    """
    EG = "EG"
    """
    Egypt
    """
    SV = "SV"
    """
    El Salvador
    """
    GQ = "GQ"
    """
    Equatorial Guinea
    """
    ER = "ER"
    """
    Eritrea
    """
    EE = "EE"
    """
    Estonia
    """
    SZ = "SZ"
    """
    Eswatini
    """
    ET = "ET"
    """
    Ethiopia
    """
    FK = "FK"
    """
    Falkland Islands (the) [Malvinas]
    """
    FO = "FO"
    """
    Faroe Islands (the)
    """
    FJ = "FJ"
    """
    Fiji
    """
    FI = "FI"
    """
    Finland
    """
    FR = "FR"
    """
    France
    """
    GF = "GF"
    """
    French Guiana
    """
    PF = "PF"
    """
    French Polynesia
    """
    TF = "TF"
    """
    French Southern Territories (the)
    """
    GA = "GA"
    """
    Gabon
    """
    GM = "GM"
    """
    Gambia (the)
    """
    GE = "GE"
    """
    Georgia
    """
    DE = "DE"
    """
    Germany
    """
    GH = "GH"
    """
    Ghana
    """
    GI = "GI"
    """
    Gibraltar
    """
    GR = "GR"
    """
    Greece
    """
    GL = "GL"
    """
    Greenland
    """
    GD = "GD"
    """
    Grenada
    """
    GP = "GP"
    """
    Guadeloupe
    """
    GU = "GU"
    """
    Guam
    """
    GT = "GT"
    """
    Guatemala
    """
    GG = "GG"
    """
    Guernsey
    """
    GN = "GN"
    """
    Guinea
    """
    GW = "GW"
    """
    Guinea-Bissau
    """
    GY = "GY"
    """
    Guyana
    """
    HT = "HT"
    """
    Haiti
    """
    HM = "HM"
    """
    Heard Island and McDonald Islands
    """
    VA = "VA"
    """
    Holy See (the)
    """
    HN = "HN"
    """
    Honduras
    """
    HK = "HK"
    """
    Hong Kong
    """
    HU = "HU"
    """
    Hungary
    """
    IS = "IS"
    """
    Iceland
    """
    IN = "IN"
    """
    India
    """
    ID = "ID"
    """
    Indonesia
    """
    IR = "IR"
    """
    Iran (Islamic Republic of)
    """
    IQ = "IQ"
    """
    Iraq
    """
    IE = "IE"
    """
    Ireland
    """
    IM = "IM"
    """
    Isle of Man
    """
    IL = "IL"
    """
    Israel
    """
    IT = "IT"
    """
    Italy
    """
    JM = "JM"
    """
    Jamaica
    """
    JP = "JP"
    """
    Japan
    """
    JE = "JE"
    """
    Jersey
    """
    JO = "JO"
    """
    Jordan
    """
    KZ = "KZ"
    """
    Kazakhstan
    """
    KE = "KE"
    """
    Kenya
    """
    KI = "KI"
    """
    Kiribati
    """
    KP = "KP"
    """
    Korea (the Democratic People's Republic of)
    """
    KR = "KR"
    """
    Korea (the Republic of)
    """
    KW = "KW"
    """
    Kuwait
    """
    KG = "KG"
    """
    Kyrgyzstan
    """
    LA = "LA"
    """
    Lao People's Democratic Republic (the)
    """
    LV = "LV"
    """
    Latvia
    """
    LB = "LB"
    """
    Lebanon
    """
    LS = "LS"
    """
    Lesotho
    """
    LR = "LR"
    """
    Liberia
    """
    LY = "LY"
    """
    Libya
    """
    LI = "LI"
    """
    Liechtenstein
    """
    LT = "LT"
    """
    Lithuania
    """
    LU = "LU"
    """
    Luxembourg
    """
    MO = "MO"
    """
    Macao
    """
    MG = "MG"
    """
    Madagascar
    """
    MW = "MW"
    """
    Malawi
    """
    MY = "MY"
    """
    Malaysia
    """
    MV = "MV"
    """
    Maldives
    """
    ML = "ML"
    """
    Mali
    """
    MT = "MT"
    """
    Malta
    """
    MH = "MH"
    """
    Marshall Islands (the)
    """
    MQ = "MQ"
    """
    Martinique
    """
    MR = "MR"
    """
    Mauritania
    """
    MU = "MU"
    """
    Mauritius
    """
    YT = "YT"
    """
    Mayotte
    """
    MX = "MX"
    """
    Mexico
    """
    FM = "FM"
    """
    Micronesia (Federated States of)
    """
    MD = "MD"
    """
    Moldova (the Republic of)
    """
    MC = "MC"
    """
    Monaco
    """
    MN = "MN"
    """
    Mongolia
    """
    ME = "ME"
    """
    Montenegro
    """
    MS = "MS"
    """
    Montserrat
    """
    MA = "MA"
    """
    Morocco
    """
    MZ = "MZ"
    """
    Mozambique
    """
    MM = "MM"
    """
    Myanmar
    """
    NR = "NR"
    """
    Nauru
    """
    NP = "NP"
    """
    Nepal
    """
    NL = "NL"
    """
    Netherlands (Kingdom of the)
    """
    NC = "NC"
    """
    New Caledonia
    """
    NZ = "NZ"
    """
    New Zealand
    """
    NI = "NI"
    """
    Nicaragua
    """
    NE = "NE"
    """
    Niger (the)
    """
    NG = "NG"
    """
    Nigeria
    """
    NU = "NU"
    """
    Niue
    """
    NF = "NF"
    """
    Norfolk Island
    """
    MK = "MK"
    """
    North Macedonia
    """
    MP = "MP"
    """
    Northern Mariana Islands (the)
    """
    NO = "NO"
    """
    Norway
    """
    OM = "OM"
    """
    Oman
    """
    PK = "PK"
    """
    Pakistan
    """
    PW = "PW"
    """
    Palau
    """
    PS = "PS"
    """
    Palestine, State of
    """
    PA = "PA"
    """
    Panama
    """
    PG = "PG"
    """
    Papua New Guinea
    """
    PY = "PY"
    """
    Paraguay
    """
    PE = "PE"
    """
    Peru
    """
    PH = "PH"
    """
    Philippines (the)
    """
    PN = "PN"
    """
    Pitcairn
    """
    PL = "PL"
    """
    Poland
    """
    PT = "PT"
    """
    Portugal
    """
    PR = "PR"
    """
    Puerto Rico
    """
    QA = "QA"
    """
    Qatar
    """
    RO = "RO"
    """
    Romania
    """
    RU = "RU"
    """
    Russian Federation (the)
    """
    RW = "RW"
    """
    Rwanda
    """
    RE = "RE"
    """
    Réunion
    """
    BL = "BL"
    """
    Saint Barthélemy
    """
    SH = "SH"
    """
    Saint Helena, Ascension and Tristan da Cunha
    """
    KN = "KN"
    """
    Saint Kitts and Nevis
    """
    LC = "LC"
    """
    Saint Lucia
    """
    MF = "MF"
    """
    Saint Martin (French part)
    """
    PM = "PM"
    """
    Saint Pierre and Miquelon
    """
    VC = "VC"
    """
    Saint Vincent and the Grenadines
    """
    WS = "WS"
    """
    Samoa
    """
    SM = "SM"
    """
    San Marino
    """
    ST = "ST"
    """
    Sao Tome and Principe
    """
    SA = "SA"
    """
    Saudi Arabia
    """
    SN = "SN"
    """
    Senegal
    """
    RS = "RS"
    """
    Serbia
    """
    SC = "SC"
    """
    Seychelles
    """
    SL = "SL"
    """
    Sierra Leone
    """
    SG = "SG"
    """
    Singapore
    """
    SX = "SX"
    """
    Sint Maarten (Dutch part)
    """
    SK = "SK"
    """
    Slovakia
    """
    SI = "SI"
    """
    Slovenia
    """
    SB = "SB"
    """
    Solomon Islands
    """
    SO = "SO"
    """
    Somalia
    """
    ZA = "ZA"
    """
    South Africa
    """
    GS = "GS"
    """
    South Georgia and the South Sandwich Islands
    """
    SS = "SS"
    """
    South Sudan
    """
    ES = "ES"
    """
    Spain
    """
    LK = "LK"
    """
    Sri Lanka
    """
    SD = "SD"
    """
    Sudan (the)
    """
    SR = "SR"
    """
    Suriname
    """
    SJ = "SJ"
    """
    Svalbard and Jan Mayen
    """
    SE = "SE"
    """
    Sweden
    """
    CH = "CH"
    """
    Switzerland
    """
    SY = "SY"
    """
    Syrian Arab Republic (the)
    """
    TW = "TW"
    """
    Taiwan (Province of China)
    """
    TJ = "TJ"
    """
    Tajikistan
    """
    TZ = "TZ"
    """
    Tanzania, the United Republic of
    """
    TH = "TH"
    """
    Thailand
    """
    TL = "TL"
    """
    Timor-Leste
    """
    TG = "TG"
    """
    Togo
    """
    TK = "TK"
    """
    Tokelau
    """
    TO = "TO"
    """
    Tonga
    """
    TT = "TT"
    """
    Trinidad and Tobago
    """
    TN = "TN"
    """
    Tunisia
    """
    TM = "TM"
    """
    Turkmenistan
    """
    TC = "TC"
    """
    Turks and Caicos Islands (the)
    """
    TV = "TV"
    """
    Tuvalu
    """
    TR = "TR"
    """
    Türkiye
    """
    UG = "UG"
    """
    Uganda
    """
    UA = "UA"
    """
    Ukraine
    """
    AE = "AE"
    """
    United Arab Emirates (the)
    """
    GB = "GB"
    """
    United Kingdom of Great Britain and Northern Ireland (the)
    """
    UM = "UM"
    """
    United States Minor Outlying Islands (the)
    """
    US = "US"
    """
    United States of America (the)
    """
    UY = "UY"
    """
    Uruguay
    """
    UZ = "UZ"
    """
    Uzbekistan
    """
    VU = "VU"
    """
    Vanuatu
    """
    VE = "VE"
    """
    Venezuela (Bolivarian Republic of)
    """
    VN = "VN"
    """
    Viet Nam
    """
    VG = "VG"
    """
    Virgin Islands (British)
    """
    VI = "VI"
    """
    Virgin Islands (U.S.)
    """
    WF = "WF"
    """
    Wallis and Futuna
    """
    EH = "EH"
    """
    Western Sahara*
    """
    YE = "YE"
    """
    Yemen
    """
    ZM = "ZM"
    """
    Zambia
    """
    ZW = "ZW"
    """
    Zimbabwe
    """
    AX = "AX"
    """
    Åland Islands
    """


class BrainTissueWeightType(str, Enum):
    Fresh_whole_brain = "Fresh whole brain"
    """
    A whole brain specimen that has not been frozen or fixed -- i.e., a whole brain that has not yet been treated by a preserving method.
    """
    Fixed_whole_brain = "Fixed whole brain"
    """
    A whole brain specimen that has been treated for preservation (typically by formalin).
    """
    Fresh_hemibrain = "Fresh hemibrain"
    """
    A hemibrain specimen that has not been frozen or fixed -- i.e., a whole brain that has not yet been treated by a preserving method.
    """
    Fixed_hemibrain = "Fixed hemibrain"
    """
    A hemibrain specimen that has been treated for preservation (typically by formalin).
    """
    Unknown = "Unknown"


class CauseOfDeath(str, Enum):
    All_Causes = "All Causes"
    Communicable_maternal_perinatal_and_nutritional_conditions = "Communicable, maternal, perinatal and nutritional conditions"
    Infectious_and_parasitic_diseases = "Infectious and parasitic diseases"
    Tuberculosis = "Tuberculosis"
    STDs_excluding_HIV = "STDs excluding HIV"
    Syphilis = "Syphilis"
    Chlamydia = "Chlamydia"
    Gonorrhoea = "Gonorrhoea"
    Other_STDs = "Other STDs"
    HIVSOLIDUSAIDS = "HIV/AIDS"
    Diarrhoeal_diseases = "Diarrhoeal diseases"
    Childhood_cluster_diseases = "Childhood-cluster diseases"
    Pertussis = "Pertussis"
    Poliomyelitis = "Poliomyelitis"
    Diphtheria = "Diphtheria"
    Measles = "Measles"
    Tetanus = "Tetanus"
    Meningitis = "Meningitis"
    Hepatitis_B = "Hepatitis B"
    Hepatitis_C = "Hepatitis C"
    Malaria = "Malaria"
    Tropical_cluster_diseases = "Tropical-cluster diseases"
    Trypanosomiasis = "Trypanosomiasis"
    Chagas_disease = "Chagas disease"
    Schistosomiasis = "Schistosomiasis"
    Leishmaniasis = "Leishmaniasis"
    Lymphatic_filariasis = "Lymphatic filariasis"
    Onchocerciasis = "Onchocerciasis"
    Leprosy = "Leprosy"
    Dengue = "Dengue"
    Japanese_encephalitis = "Japanese encephalitis"
    Trachoma = "Trachoma"
    Intestinal_nematode_infections = "Intestinal nematode infections"
    Ascariasis = "Ascariasis"
    Trichuriasis = "Trichuriasis"
    Hookworm_disease = "Hookworm disease"
    Other_intestinal_infections = "Other intestinal infections"
    Other_infectious_diseases = "Other infectious diseases"
    Respiratory_infections = "Respiratory infections"
    Lower_respiratory_infections = "Lower respiratory infections"
    COVID_19 = "COVID-19"
    Upper_respiratory_infections = "Upper respiratory infections"
    Otitis_media = "Otitis media"
    Maternal_conditions = "Maternal conditions"
    Maternal_haemorrhage = "Maternal haemorrhage"
    Maternal_sepsis = "Maternal sepsis"
    Hypertensive_disorders = "Hypertensive disorders"
    Obstructed_labour = "Obstructed labour"
    Abortion = "Abortion"
    Other_maternal_conditions = "Other maternal conditions"
    Perinatal_conditions = "Perinatal conditions"
    Low_birth_weight = "Low birth weight"
    Birth_asphyxia_and_birth_trauma = "Birth asphyxia and birth trauma"
    Other_perinatal_conditions = "Other perinatal conditions"
    Nutritional_deficiencies = "Nutritional deficiencies"
    Protein_energy_malnutrition = "Protein-energy malnutrition"
    Iodine_deficiency = "Iodine deficiency"
    Vitamin_A_deficiency = "Vitamin A deficiency"
    Iron_deficiency_anaemia = "Iron-deficiency anaemia"
    Other_nutritional_disorders = "Other nutritional disorders"
    Noncommunicable_diseases = "Noncommunicable diseases"
    Malignant_neoplasms = "Malignant neoplasms"
    Mouth_and_oropharynx_cancers = "Mouth and oropharynx cancers"
    aFULL_STOP_Lip_and_oral_cavity_cancers = "a. Lip and oral cavity cancers"
    bFULL_STOP_Nasopharynx_cancers = "b. Nasopharynx cancers"
    cFULL_STOP_Other_pharynx_cancer = "c. Other pharynx cancer"
    Oesophagus_cancer = "Oesophagus cancer"
    Stomach_cancer = "Stomach cancer"
    Colon_and_rectum_cancers = "Colon and rectum cancers"
    Liver_cancer = "Liver cancer"
    Pancreas_cancer = "Pancreas cancer"
    Trachea_bronchus_lung_cancers = "Trachea, bronchus, lung cancers"
    Melanoma_and_other_skin_cancers = "Melanoma and other skin cancers"
    aFULL_STOP_Malignant_skin_melanoma = "a. Malignant skin melanoma"
    bFULL_STOP_Non_melanoma_skin_cancer = "b. Non-melanoma skin cancer"
    Breast_cancer = "Breast cancer"
    Cervix_uteri_cancer = "Cervix uteri cancer"
    Corpus_uteri_cancer = "Corpus uteri cancer"
    Ovary_cancer = "Ovary cancer"
    Prostate_cancer = "Prostate cancer"
    Testicular_cancer = "Testicular cancer"
    Kidney_cancer = "Kidney cancer"
    Bladder_cancer = "Bladder cancer"
    Brain_and_nervous_system_cancers = "Brain and nervous system cancers"
    Gallbladder_and_biliary_tract_cancer = "Gallbladder and biliary tract cancer"
    Larynx_cancer = "Larynx cancer"
    Thyroid_cancer = "Thyroid cancer"
    Mesothelioma = "Mesothelioma"
    Lymphomas_multiple_myeloma = "Lymphomas, multiple myeloma"
    aFULL_STOP_Hodgkin_lymphoma = "a. Hodgkin lymphoma"
    bFULL_STOP_Non_Hodgkin_lymphoma = "b. Non-Hodgkin lymphoma"
    cFULL_STOP_Multiple_myeloma = "c. Multiple myeloma"
    Leukaemia = "Leukaemia"
    Ill_defined_malignant_neoplasms = "Ill-defined malignant neoplasms"
    Other_malignant_neoplasms = "Other malignant neoplasms"
    Other_neoplasms = "Other neoplasms"
    Diabetes_mellitus_and_endocrine_disorders = "Diabetes mellitus and endocrine disorders"
    Diabetes_mellitus = "Diabetes mellitus"
    Endocrine_disorders = "Endocrine disorders"
    Neuropsychiatric_conditions = "Neuropsychiatric conditions"
    Unipolar_depressive_disorders = "Unipolar depressive disorders"
    Bipolar_disorder = "Bipolar disorder"
    Schizophrenia = "Schizophrenia"
    Epilepsy = "Epilepsy"
    Alcohol_use_disorders = "Alcohol use disorders"
    Alzheimer_and_other_dementias = "Alzheimer and other dementias"
    Parkinson_disease = "Parkinson disease"
    Multiple_sclerosis = "Multiple sclerosis"
    Drug_use_disorders = "Drug use disorders"
    Post_traumatic_stress_disorder = "Post-traumatic stress disorder"
    Obsessive_compulsive_disorder = "Obsessive-compulsive disorder"
    Panic_disorder = "Panic disorder"
    Insomnia_LEFT_PARENTHESISprimaryRIGHT_PARENTHESIS = "Insomnia (primary)"
    Migraine = "Migraine"
    Mental_Retardation = "Mental Retardation"
    Other_neuropsychiatric_disorders = "Other neuropsychiatric disorders"
    Sense_organ_diseases = "Sense organ diseases"
    Glaucoma = "Glaucoma"
    Cataracts = "Cataracts"
    Vision_disorders_age_related = "Vision disorders, age-related"
    Hearing_loss_adult_onset = "Hearing loss, adult onset"
    Other_sense_organ_disorders = "Other sense organ disorders"
    Cardiovascular_diseases = "Cardiovascular diseases"
    Rheumatic_heart_disease = "Rheumatic heart disease"
    Hypertensive_heart_disease = "Hypertensive heart disease"
    Ischaemic_heart_disease = "Ischaemic heart disease"
    Cerebrovascular_disease = "Cerebrovascular disease"
    Inflammatory_heart_diseases = "Inflammatory heart diseases"
    Ill_defined_circulatory_diseases = "Ill-defined circulatory diseases"
    Other_circulatory_diseases = "Other circulatory diseases"
    Respiratory_diseases = "Respiratory diseases"
    Chronic_obstructive_pulmonary_disease = "Chronic obstructive pulmonary disease"
    Asthma = "Asthma"
    Other_respiratory_diseases = "Other respiratory diseases"
    Digestive_diseases = "Digestive diseases"
    Peptic_ulcer_disease = "Peptic ulcer disease"
    Cirrhosis_of_the_liver = "Cirrhosis of the liver"
    Appendicitis = "Appendicitis"
    Gastritis_and_duodenitis = "Gastritis and duodenitis"
    Paralytic_ileus_and_intestinal_obstruction = "Paralytic ileus and intestinal obstruction"
    Inflammatory_bowel_disease = "Inflammatory bowel disease"
    Gallbladder_and_biliary_diseases = "Gallbladder and biliary diseases"
    Pancreatitis = "Pancreatitis"
    Other_digestive_diseases = "Other digestive diseases"
    Genitourinary_diseases = "Genitourinary diseases"
    Nephritis_and_nephrosis = "Nephritis and nephrosis"
    Benign_prostatic_hypertrophy = "Benign prostatic hypertrophy"
    Other_genitourinary_system_diseases = "Other genitourinary system diseases"
    Skin_diseases = "Skin diseases"
    Musculoskeletal_diseases = "Musculoskeletal diseases"
    Rheumatoid_arthritis = "Rheumatoid arthritis"
    Osteoarthritis = "Osteoarthritis"
    Gout = "Gout"
    Back_pain = "Back pain"
    Other_musculoskeletal_disorders = "Other musculoskeletal disorders"
    Congenital_anomalies = "Congenital anomalies"
    Abdominal_wall_defect = "Abdominal wall defect"
    Anencephaly = "Anencephaly"
    Anorectal_atresia = "Anorectal atresia"
    Cleft_lip = "Cleft lip"
    Cleft_palate = "Cleft palate"
    Oesophageal_atresia = "Oesophageal atresia"
    Renal_agenesis = "Renal agenesis"
    Down_syndrome = "Down syndrome"
    Congenital_heart_anomalies = "Congenital heart anomalies"
    Spina_bifida = "Spina bifida"
    Other_Congenital_anomalies = "Other Congenital anomalies"
    Oral_conditions = "Oral conditions"
    Dental_caries = "Dental caries"
    Periodontal_disease = "Periodontal disease"
    Edentulism = "Edentulism"
    Other_oral_diseases = "Other oral diseases"
    Sudden_infant_death_syndrome = "Sudden infant death syndrome"
    Injuries = "Injuries"
    Unintentional_injuries = "Unintentional injuries"
    Road_traffic_accidents = "Road traffic accidents"
    Poisonings = "Poisonings"
    Falls = "Falls"
    Fires = "Fires"
    Drownings = "Drownings"
    Exposure_to_mechanical_forces = "Exposure to mechanical forces"
    Natural_disasters = "Natural disasters"
    Other_unintentional_injuries = "Other unintentional injuries"
    Intentional_injuries = "Intentional injuries"
    Self_inflicted_injuries = "Self-inflicted injuries"
    Violence = "Violence"
    War = "War"
    Other_intentional_injuries = "Other intentional injuries"
    Ill_defined_injuriesSOLIDUSaccidents = "Ill-defined injuries/accidents"
    Ill_defined_diseases = "Ill-defined diseases"


class ConditionType(str, Enum):
    Alzheimers_disease = "Alzheimers disease"
    """
    A progressive, neurodegenerative disease characterized by loss of function and death of nerve cells in several areas of the brain leading to loss of cognitive function such as memory and language.
    """
    amyotrophic_lateral_sclerosis_LEFT_PARENTHESISALSRIGHT_PARENTHESIS = "amyotrophic lateral sclerosis (ALS)"
    """
    Amyotrophic lateral sclerosis (ALS) is a neurodegenerative disease characterized by progressive muscular paralysis reflecting degeneration of motor neurons in the primary motor cortex, corticospinal tracts, brainstem and spinal cord.
    """
    ataxia = "ataxia"
    """
    A central nervous system disease that consists of gait impairment, unclear (“scanning”) speech, visual blurring due to nystagmus, hand incoordination, and tremor with movement.
    """
    autism = "autism"
    """
    Persistent deficits in social interaction and communication and interaction as well as a markedly restricted repertoire of activity and interest as well as repetitive patterns of behavior.
    """
    bi_polar_disorder = "bi-polar disorder"
    """
    A disorder of the brain that causes unusual shifts in mood, energy, activity levels and the ability to carry out day-to-day tasks. Often these moods range and shift from periods of elation and energized behavior to those of hopelessness and depression.
    """
    brain_aneurysm = "brain aneurysm"
    """
    A congenital or acquired aneurysm within the cranium.
    """
    cancer = "cancer"
    """
    A tumor composed of atypical neoplastic, often pleomorphic cells that invade other tissues. Malignant neoplasms often metastasize to distant anatomic sites and may recur after excision. The most common malignant neoplasms are carcinomas (adenocarcinomas or squamous cell carcinomas), Hodgkin and non-Hodgkin lymphomas, leukemias, melanomas, and sarcomas.
    """
    dementia = "dementia"
    """
    Loss of intellectual abilities interfering with an individual's social and occupational functions. Causes include Alzheimer's disease, brain injuries, brain tumors, and vascular disorders.
    """
    depression = "depression"
    """
    A melancholy feeling of sadness and despair.
    """
    diabetes_mellitus = "diabetes mellitus"
    """
    A metabolic disorder characterized by abnormally high blood sugar levels due to diminished production of insulin or insulin resistance/desensitization.
    """
    dystonia = "dystonia"
    """
    A movement disorder characterized by sustained or intermittent muscle contractions, resulting in abnormal movements and/or postures.
    """
    epilepsy = "epilepsy"
    """
    A brain disorder characterized by episodes of abnormally increased neuronal discharge resulting in transient episodes of sensory or motor neurological dysfunction, or psychic dysfunction. These episodes may or may not be associated with loss of consciousness or convulsions.
    """
    heart_disease = "heart disease"
    """
    A disease involving the heart and/or pericardium.
    """
    hypertension = "hypertension"
    """
    Persistently high systemic arterial blood pressure. Based on multiple readings (blood pressure determination), hypertension is currently defined as when systolic pressure is consistently greater than 140 mm Hg or when diastolic pressure is consistently 90 mm Hg or more.
    """
    memory_loss = "memory loss"
    """
    Systematic and extensive loss of memory caused by organic or psychological factors. The loss may be temporary or permanent, and may involve old or recent memories.
    """
    migraines = "migraines"
    """
    A common, severe type of vascular headache often associated with increased sympathetic activity, resulting in nausea, vomiting, and light sensitivity.
    """
    multiple_sclerosis = "multiple sclerosis"
    """
    A progressive autoimmune disorder affecting the central nervous system resulting in demyelination. Patients develop physical and cognitive impairments that correspond with the affected nerve fibers.
    """
    muscle_disease = "muscle disease"
    """
    A disease involving the muscle tissue.
    """
    ParkinsonAPOSTROPHEs_disease = "Parkinson's disease"
    """
    A progressive degenerative disorder of the central nervous system characterized by loss of dopamine producing neurons in the substantia nigra and the presence of Lewy bodies in the substantia nigra and locus coeruleus. Signs and symptoms include tremor which is most pronounced during rest, muscle rigidity, slowing of the voluntary movements, a tendency to fall back, and a mask-like facial expression.
    """
    schizophrenia = "schizophrenia"
    """
    A major psychotic disorder characterized by abnormalities in the perception or expression of reality. It affects the cognitive and psychomotor functions. Common clinical signs and symptoms include delusions, hallucinations, disorganized thinking, and retreat from reality.
    """
    stroke = "stroke"
    """
    A sudden loss of neurological function secondary to hemorrhage or ischemia in the brain parenchyma due to a vascular event. Stroke includes two main types, hemorrhagic and ischemic. Both types of stroke can cause acute seizures at the time of the acute event, as well as epilepsy as a long-term complication. In the elderly, cerebrovascular disease and stroke are the most common cause of acute seizures and epilepsy.
    """
    suicide_or_suicide_attempt = "suicide or suicide attempt"
    """
    Any behaviour related to suicide, including suicide ideation and self-harm
    """
    tourette_syndrome = "tourette syndrome"
    """
    A neurologic disorder caused by defective metabolism of the neurotransmitters in the brain. It is characterized by repeated involuntary movements (motor tics) and uncontrollable vocal sounds (vocal tics). The symptoms are usually manifested before the age of eighteen.
    """
    other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "other (specify)"


class ConfidenceLevel(str, Enum):
    confirmed_diagnosis = "confirmed diagnosis"
    """
    Sufficient evidence exists to: 1) make a clinical diagnosis based on medical history and neuropathological exam or genetic data or 2) make a clinical diagnosis by the consensus of expert clinicians or 3) confirm the absence of any brain-related diagnoses (i.e. Unaffected Control)
    """
    investigator_impression = "investigator impression"
    """
    Diagnosis is based on the clinical impressions of the clinician reviewing the available information but that information is insufficient to render a confirmed diagnosis
    """
    insufficient_data = "insufficient data"
    """
    The available information is insufficient to form a reasonable impression of or to exclude any brain-related diagnoses
    """


class DonorSource(str, Enum):
    BICAN_NBB = "BICAN-NBB"
    Donor_from_NIH_NeuroBioBank = "Donor from NIH NeuroBioBank"
    BICAN_UM1 = "BICAN-UM1"
    Other = "Other"


class DrugsFound(str, Enum):
    number_10_Hydroxycarbazepine = "10-Hydroxycarbazepine"
    number_2_Furanylfentanyl = "2-Furanylfentanyl"
    number_4_ANPP = "4-ANPP"
    number_6_Beta_Naltrexol___Free = "6-Beta-Naltrexol - Free"
    number_6_Monoacetylmorphine = "6-Monoacetylmorphine"
    number_7_Amino_Clonazepam = "7-Amino Clonazepam"
    number_7_Amino_Flunitrazepam = "7-Amino Flunitrazepam"
    number_9_Hydroxyrisperidone = "9-Hydroxyrisperidone"
    Acetaminophen = "Acetaminophen"
    Acetone = "Acetone"
    Acetyl_Fentanyl = "Acetyl Fentanyl"
    Acrylfentanyl = "Acrylfentanyl"
    Alfentanil = "Alfentanil"
    Alpha_Hydroxyalprazolam = "Alpha-Hydroxyalprazolam"
    Alpha_Hydroxyetizolam = "Alpha-Hydroxyetizolam"
    Alprazolam = "Alprazolam"
    Amitriptyline = "Amitriptyline"
    Amlodipine = "Amlodipine"
    Amoxapine = "Amoxapine"
    Amphetamine = "Amphetamine"
    Aripiprazole = "Aripiprazole"
    Atomoxetine = "Atomoxetine"
    Atropine = "Atropine"
    Barbiturates = "Barbiturates"
    Benzodiazepines = "Benzodiazepines"
    Benzoylecgonine = "Benzoylecgonine"
    Benztropine = "Benztropine"
    Bromazepam = "Bromazepam"
    Brompheniramine = "Brompheniramine"
    Buprenorphine = "Buprenorphine"
    Buprenorphine_SOLIDUS_Metabolite = "Buprenorphine / Metabolite"
    Bupropion = "Bupropion"
    Bupropion_Metabolite = "Bupropion Metabolite"
    Buspirone = "Buspirone"
    Butalbital = "Butalbital"
    Butorphanol = "Butorphanol"
    Butylone = "Butylone"
    Butyrylfentanyl = "Butyrylfentanyl"
    Caffeine = "Caffeine"
    Cannabinoids = "Cannabinoids"
    Carbamazepine = "Carbamazepine"
    Carbamazepine_1011_Epoxide = "Carbamazepine-10,11-Epoxide"
    Carfentanil = "Carfentanil"
    Carisoprodol = "Carisoprodol"
    Chlordiazepoxide = "Chlordiazepoxide"
    Chlorpheniramine = "Chlorpheniramine"
    Chlorpromazine = "Chlorpromazine"
    Citalopram_SOLIDUS_Escitalopram = "Citalopram / Escitalopram"
    Clobazam = "Clobazam"
    Clomipramine = "Clomipramine"
    Clonazepam = "Clonazepam"
    Clonazolam = "Clonazolam"
    Clonidine = "Clonidine"
    Clozapine = "Clozapine"
    Cocaethylene = "Cocaethylene"
    Cocaine = "Cocaine"
    Cocaine_SOLIDUS_Metabolites = "Cocaine / Metabolites"
    Codeine = "Codeine"
    Cotinine = "Cotinine"
    Cyclobenzaprine = "Cyclobenzaprine"
    Cyclopropylfentanyl = "Cyclopropylfentanyl"
    Delorazepam = "Delorazepam"
    Desalkylflurazepam = "Desalkylflurazepam"
    Descarboethoxyloratadine = "Descarboethoxyloratadine"
    Desipramine = "Desipramine"
    Desmethylcitalopram = "Desmethylcitalopram"
    Desmethylclomipramine = "Desmethylclomipramine"
    Desmethyldoxepin = "Desmethyldoxepin"
    Desmethylloperamide = "Desmethylloperamide"
    Desmethylmirtazapine = "Desmethylmirtazapine"
    Desmethylsertraline = "Desmethylsertraline"
    Desmethyltrimipramine = "Desmethyltrimipramine"
    Dextro_SOLIDUS_Levo_Methorphan = "Dextro / Levo Methorphan"
    Dextrorphan_SOLIDUS_Levorphanol = "Dextrorphan / Levorphanol"
    Diazepam = "Diazepam"
    Dibutylone = "Dibutylone"
    Dicyclomine = "Dicyclomine"
    Dihydrocodeine_SOLIDUS_Hydrocodol = "Dihydrocodeine / Hydrocodol"
    Diltiazem = "Diltiazem"
    Diphenhydramine = "Diphenhydramine"
    Donepezil = "Donepezil"
    Doxepin = "Doxepin"
    Doxylamine = "Doxylamine"
    Duloxetine = "Duloxetine"
    Duloxetine_Breakdown_Product = "Duloxetine Breakdown Product"
    EDDP = "EDDP"
    Ephedrine = "Ephedrine"
    Ephedrine_SOLIDUS_Pseudoephedrine = "Ephedrine / Pseudoephedrine"
    Estazolam = "Estazolam"
    Eszopiclone_SOLIDUS_Zopiclone = "Eszopiclone / Zopiclone"
    Eszopiclone_SOLIDUS_Zopiclone_Breakdown = "Eszopiclone / Zopiclone Breakdown"
    Ethanol = "Ethanol"
    Ethinamate = "Ethinamate"
    Ethosuximide = "Ethosuximide"
    Ethotoin = "Ethotoin"
    Ethylmorphine = "Ethylmorphine"
    Etizolam = "Etizolam"
    Felbamate = "Felbamate"
    Fentanyl = "Fentanyl"
    Flecainide = "Flecainide"
    Flubromazepam = "Flubromazepam"
    Flubromazolam = "Flubromazolam"
    Fluconazole = "Fluconazole"
    Flunitrazepam = "Flunitrazepam"
    Fluoxetine = "Fluoxetine"
    Fluphenazine = "Fluphenazine"
    Flurazepam = "Flurazepam"
    Fluvoxamine = "Fluvoxamine"
    Gabapentin = "Gabapentin"
    Gabapentin_Breakdown_Product = "Gabapentin Breakdown Product"
    Guaifenesin = "Guaifenesin"
    Haloperidol = "Haloperidol"
    Hexobarbital = "Hexobarbital"
    Hydrocodone = "Hydrocodone"
    Hydromorphone = "Hydromorphone"
    Hydroxybupropion = "Hydroxybupropion"
    Hydroxychloroquine = "Hydroxychloroquine"
    Hydroxyethylflurazepam = "Hydroxyethylflurazepam"
    Hydroxytriazolam = "Hydroxytriazolam"
    Hydroxyzine = "Hydroxyzine"
    Ibuprofen = "Ibuprofen"
    Iloperidone = "Iloperidone"
    Imipramine = "Imipramine"
    Isopropanol = "Isopropanol"
    Ketamine = "Ketamine"
    LSD = "LSD"
    Lacosamide = "Lacosamide"
    Lamotrigine = "Lamotrigine"
    Levamisole = "Levamisole"
    Levetiracetam = "Levetiracetam"
    Lidocaine = "Lidocaine"
    Loperamide = "Loperamide"
    Loratadine = "Loratadine"
    Lorazepam = "Lorazepam"
    Loxapine = "Loxapine"
    MDA = "MDA"
    MDEA = "MDEA"
    MDMA = "MDMA"
    Meclizine = "Meclizine"
    Memantine = "Memantine"
    Meperidine = "Meperidine"
    Mepivacaine = "Mepivacaine"
    Meprobamate = "Meprobamate"
    Mescaline = "Mescaline"
    Mesoridazine = "Mesoridazine"
    Metaxalone = "Metaxalone"
    Methadone = "Methadone"
    Methamphetamine = "Methamphetamine"
    Methanol = "Methanol"
    Methaqualone = "Methaqualone"
    Methocarbamol = "Methocarbamol"
    Methoxetamine = "Methoxetamine"
    Methylphenidate = "Methylphenidate"
    Metoprolol = "Metoprolol"
    Metronidazole = "Metronidazole"
    Midazolam = "Midazolam"
    Milnacipran = "Milnacipran"
    Mirtazapine = "Mirtazapine"
    Mitragynine = "Mitragynine"
    Monoethylglycinexylidide_LEFT_PARENTHESISMEGXRIGHT_PARENTHESIS = "Monoethylglycinexylidide (MEGX)"
    Morphine = "Morphine"
    N_Acetylprocainamide = "N-Acetylprocainamide"
    N_ethyl_Pentylone = "N-ethyl Pentylone"
    Nalbuphine = "Nalbuphine"
    Naloxone = "Naloxone"
    Naltrexone = "Naltrexone"
    Naltrexone___Free = "Naltrexone - Free"
    Naproxen = "Naproxen"
    Naproxen_Breakdown_Product = "Naproxen Breakdown Product"
    Nicotine = "Nicotine"
    Norbuprenorphine___Free = "Norbuprenorphine - Free"
    Norclozapine = "Norclozapine"
    Norcodeine = "Norcodeine"
    Norcyclobenzaprine = "Norcyclobenzaprine"
    Nordiazepam = "Nordiazepam"
    Norfentanyl = "Norfentanyl"
    Norflunitrazepam = "Norflunitrazepam"
    Norfluoxetine = "Norfluoxetine"
    Norhydroxyzine = "Norhydroxyzine"
    Norketamine = "Norketamine"
    Normeperidine = "Normeperidine"
    Norpropoxyphene = "Norpropoxyphene"
    Norpseudoephedrine = "Norpseudoephedrine"
    Norpseudoephedrine_SOLIDUS_Phenylpropanolamine = "Norpseudoephedrine / Phenylpropanolamine"
    Nortriptyline = "Nortriptyline"
    O_Desmethyltramadol = "O-Desmethyltramadol"
    O_Desmethylvenlafaxine = "O-Desmethylvenlafaxine"
    Olanzapine = "Olanzapine"
    Ondansetron = "Ondansetron"
    Opiates = "Opiates"
    Other_Findings = "Other Findings"
    Oxazepam = "Oxazepam"
    Oxycodone = "Oxycodone"
    Oxycodone_SOLIDUS_Oxymorphone = "Oxycodone / Oxymorphone"
    Oxymorphone = "Oxymorphone"
    Papaverine = "Papaverine"
    Paroxetine = "Paroxetine"
    Pentazocine = "Pentazocine"
    Pentobarbital = "Pentobarbital"
    Perphenazine = "Perphenazine"
    Phenazepam = "Phenazepam"
    Phencyclidine = "Phencyclidine"
    Pheniramine = "Pheniramine"
    Phenobarbital = "Phenobarbital"
    Phensuximide = "Phensuximide"
    Phentermine = "Phentermine"
    Phenylethylmalonamide_LEFT_PARENTHESISPEMARIGHT_PARENTHESIS = "Phenylethylmalonamide (PEMA)"
    Phenylpropanolamine = "Phenylpropanolamine"
    Phenyltoloxamine = "Phenyltoloxamine"
    Phenytoin = "Phenytoin"
    Primidone = "Primidone"
    Procainamide = "Procainamide"
    Prochlorperazine = "Prochlorperazine"
    Promazine = "Promazine"
    Promethazine = "Promethazine"
    Propofol = "Propofol"
    Propoxyphene = "Propoxyphene"
    Protriptyline = "Protriptyline"
    Pseudoephedrine = "Pseudoephedrine"
    Psilocin = "Psilocin"
    Pyrilamine = "Pyrilamine"
    Quetiapine = "Quetiapine"
    Quinidine = "Quinidine"
    Quinine = "Quinine"
    Risperidone = "Risperidone"
    Rufinamide = "Rufinamide"
    Salicylates = "Salicylates"
    Scope_Statement = "Scope Statement"
    Secobarbital = "Secobarbital"
    Sertraline = "Sertraline"
    Sildenafil = "Sildenafil"
    Strychnine = "Strychnine"
    Sufentanil = "Sufentanil"
    Tadalafil = "Tadalafil"
    Tapentadol = "Tapentadol"
    Temazepam = "Temazepam"
    Tetrahydrozoline = "Tetrahydrozoline"
    Theobromine = "Theobromine"
    Theophylline = "Theophylline"
    Thioridazine = "Thioridazine"
    Thiothixene = "Thiothixene"
    Ticlopidine = "Ticlopidine"
    Topiramate = "Topiramate"
    Topiramate_Breakdown_Product = "Topiramate Breakdown Product"
    Tramadol = "Tramadol"
    Tramadol_Metabolite = "Tramadol Metabolite"
    Trazodone = "Trazodone"
    Triazolam = "Triazolam"
    Trifluoperazine = "Trifluoperazine"
    Trimethoprim = "Trimethoprim"
    Trimipramine = "Trimipramine"
    Triprolidine = "Triprolidine"
    U_47700 = "U-47700"
    Valerylfentanyl = "Valerylfentanyl"
    Vardenafil = "Vardenafil"
    Venlafaxine = "Venlafaxine"
    Venlafaxine_Metabolite = "Venlafaxine Metabolite"
    Verapamil = "Verapamil"
    Warfarin = "Warfarin"
    Xylazine = "Xylazine"
    Yohimbine = "Yohimbine"
    Zaleplon = "Zaleplon"
    Ziprasidone = "Ziprasidone"
    Zolpidem = "Zolpidem"
    Zonisamide = "Zonisamide"
    alpha_PVP = "alpha-PVP"
    cis_3_Methylfentanyl = "cis-3-Methylfentanyl"
    mCPP = "mCPP"
    para_Fluoroisobutyrylfentanyl = "para-Fluoroisobutyrylfentanyl"
    trans_3_Methylfentanyl = "trans-3-Methylfentanyl"
    Other_findings_specify = "Other findings, specify"


class Ethnicity(str, Enum):
    Hispanic_or_Latino = "Hispanic or Latino"
    """
    A person of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race. The term, "Spanish origin" can be used in addition to "Hispanic or Latino".
    """
    Not_Hispanic_or_Latino = "Not Hispanic or Latino"
    """
    A person not of Cuban, Mexican, Puerto Rican, South or Central American, or other Spanish culture or origin, regardless of race.
    """
    Prefer_not_to_answer = "Prefer not to answer"
    """
    A response indicating that an individual prefers or preferred not to answer.
    """
    Unknown = "Unknown"
    """
    Not known, observed, recorded; or reported as unknown by the data contributor.
    """
    Not_reported = "Not reported"
    """
    Not provided or available.
    """


class Gender(str, Enum):
    male = "male"
    """
    The gender identity of male self-identified by the subject/participant.
    """
    female = "female"
    """
    The gender identity of female self-identified by the subject/participant.
    """
    transgender_male = "transgender male"
    """
    The gender identify of transgender male self-identified by the subject/participant.
    """
    transgender_female = "transgender female"
    """
    The gender identity of transgender female self-identified by the subject/participant.
    """
    non_binary = "non-binary"
    """
    The gender identity of non-binary self-identified by the subject/participant.
    """
    gender_fluid = "gender fluid"
    """
    The gender identity of gender fluid self-identified by the subject/participant.
    """
    other_specify = "other, specify"
    """
    A gender identity of a type not included in this list.
    """
    unknown = "unknown"
    """
    Not known, observed, recorded; or reported as unknown by the data contributor.
    """
    not_reported = "not reported"
    """
    Gender identity not reported.
    """


class Handedness(str, Enum):
    left = "left"
    """
    Handedness where the organism preferentially uses the left hand or foot for tasks requiring the use of a single hand or foot or a dominant hand or foot
    """
    right = "right"
    """
    Handedness where the organism preferentially uses the right hand or foot for tasks requiring the use of a single hand or foot or a dominant hand or foot.
    """
    either = "either"
    """
    Handedness where the organism exhibits no overall dominance in the use of right or left hand or foot in the performance of tasks that require one hand or foot or a dominant hand or foot.
    """


class Hemisphere(str, Enum):
    left = "left"
    """
    A cerebral hemisphere that is in the left side of a brain.
    """
    right = "right"
    """
    A cerebral hemisphere that is in the right side of a brain.
    """
    both = "both"
    """
    Part of the telencephalon consisting of both of the two smooth, elongated halves of the cerebrum.
    """
    unknown = "unknown"


class IncomeRange(str, Enum):
    Under_DOLLAR_SIGN15000 = "Under $15000"
    """
    Annual income under 15000 USD
    """
    DOLLAR_SIGN15000_to_DOLLAR_SIGN24999 = "$15000 to $24999"
    """
    Annual income between 15000 and 24999 USD
    """
    DOLLAR_SIGN25000_to_DOLLAR_SIGN34999 = "$25000 to $34999"
    """
    Annual income between 25000 and 34999 USD
    """
    DOLLAR_SIGN35000_to_DOLLAR_SIGN49999 = "$35000 to $49999"
    """
    Annual income between 35000 and 49999 USD
    """
    DOLLAR_SIGN50000_to_DOLLAR_SIGN74999 = "$50000 to $74999"
    """
    Annual income between 50000 and 74999 USD
    """
    DOLLAR_SIGN75000_to_DOLLAR_SIGN99999 = "$75000 to $99999"
    """
    Annual income between 75000 and 99999 USD
    """
    DOLLAR_SIGN100000_and_over = "$100000 and over"
    """
    Annual income greater than 100000 USD
    """
    Refused = "Refused"
    """
    Annual income disclosure refused.
    """
    Unknown = "Unknown"
    """
    Annual income unknown.
    """


class InformantRelationship(str, Enum):
    child = "child"
    """
    A person who is either the progeny of the subject or the adoptive child of the subject.
    """
    friendSOLIDUSneighbor = "friend/neighbor"
    """
    Either one of a friend of the subject or a person who lives near the subject.
    """
    parent = "parent"
    """
    A caretaker and/or immediate progenitor of a child.
    """
    professional_caregiver = "professional caregiver"
    """
    A person who bears the caretaker role for the subject.
    """
    themself = "themself"
    """
    A person who is identical to the subject, i.e., the subject themselves.
    """
    sibling = "sibling"
    """
    A person who shares a parent.
    """
    spouseSOLIDUSpartner = "spouse/partner"
    """
    A partner in marriage.
    """
    teammate = "teammate"
    """
    A person who is a member of a team whose membership includes the subject.
    """
    other_relative_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "other relative (specify)"
    other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "other (specify)"


class Language(str, Enum):
    aar = "aar"
    """
    Afar
    """
    abk = "abk"
    """
    Abkhazian
    """
    ace = "ace"
    """
    Achinese
    """
    ach = "ach"
    """
    Acoli
    """
    ada = "ada"
    """
    Adangme
    """
    ady = "ady"
    """
    Adyghe; Adygei
    """
    afa = "afa"
    """
    Afro-Asiatic languages
    """
    afh = "afh"
    """
    Afrihili
    """
    afr = "afr"
    """
    Afrikaans
    """
    ain = "ain"
    """
    Ainu
    """
    aka = "aka"
    """
    Akan
    """
    akk = "akk"
    """
    Akkadian
    """
    alb_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "alb (B)"
    """
    Albanian
    """
    sqi_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "sqi (T)"
    ale = "ale"
    """
    Aleut
    """
    alg = "alg"
    """
    Algonquian languages
    """
    alt = "alt"
    """
    Southern Altai
    """
    amh = "amh"
    """
    Amharic
    """
    ang = "ang"
    """
    English, Old (ca.450-1100)
    """
    anp = "anp"
    """
    Angika
    """
    apa = "apa"
    """
    Apache languages
    """
    ara = "ara"
    """
    Arabic
    """
    arc = "arc"
    """
    Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE)
    """
    arg = "arg"
    """
    Aragonese
    """
    arm_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "arm (B)"
    """
    Armenian
    """
    hye_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "hye (T)"
    arn = "arn"
    """
    Mapudungun; Mapuche
    """
    arp = "arp"
    """
    Arapaho
    """
    art = "art"
    """
    Artificial languages
    """
    arw = "arw"
    """
    Arawak
    """
    asm = "asm"
    """
    Assamese
    """
    ast = "ast"
    """
    Asturian; Bable; Leonese; Asturleonese
    """
    ath = "ath"
    """
    Athapascan languages
    """
    aus = "aus"
    """
    Australian languages
    """
    ava = "ava"
    """
    Avaric
    """
    ave = "ave"
    """
    Avestan
    """
    awa = "awa"
    """
    Awadhi
    """
    aym = "aym"
    """
    Aymara
    """
    aze = "aze"
    """
    Azerbaijani
    """
    bad = "bad"
    """
    Banda languages
    """
    bai = "bai"
    """
    Bamileke languages
    """
    bak = "bak"
    """
    Bashkir
    """
    bal = "bal"
    """
    Baluchi
    """
    bam = "bam"
    """
    Bambara
    """
    ban = "ban"
    """
    Balinese
    """
    baq_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "baq (B)"
    """
    Basque
    """
    eus_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "eus (T)"
    bas = "bas"
    """
    Basa
    """
    bat = "bat"
    """
    Baltic languages
    """
    bej = "bej"
    """
    Beja; Bedawiyet
    """
    bel = "bel"
    """
    Belarusian
    """
    bem = "bem"
    """
    Bemba
    """
    ben = "ben"
    """
    Bengali
    """
    ber = "ber"
    """
    Berber languages
    """
    bho = "bho"
    """
    Bhojpuri
    """
    bih = "bih"
    """
    Bihari languages
    """
    bik = "bik"
    """
    Bikol
    """
    bin = "bin"
    """
    Bini; Edo
    """
    bis = "bis"
    """
    Bislama
    """
    bla = "bla"
    """
    Siksika
    """
    bnt = "bnt"
    """
    Bantu languages
    """
    tib_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "tib (B)"
    """
    Tibetan
    """
    bod_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "bod (T)"
    bos = "bos"
    """
    Bosnian
    """
    bra = "bra"
    """
    Braj
    """
    bre = "bre"
    """
    Breton
    """
    btk = "btk"
    """
    Batak languages
    """
    bua = "bua"
    """
    Buriat
    """
    bug = "bug"
    """
    Buginese
    """
    bul = "bul"
    """
    Bulgarian
    """
    bur_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "bur (B)"
    """
    Burmese
    """
    mya_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "mya (T)"
    byn = "byn"
    """
    Blin; Bilin
    """
    cad = "cad"
    """
    Caddo
    """
    cai = "cai"
    """
    Central American Indian languages
    """
    car = "car"
    """
    Galibi Carib
    """
    cat = "cat"
    """
    Catalan; Valencian
    """
    cau = "cau"
    """
    Caucasian languages
    """
    ceb = "ceb"
    """
    Cebuano
    """
    cel = "cel"
    """
    Celtic languages
    """
    cze_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "cze (B)"
    """
    Czech
    """
    ces_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "ces (T)"
    cha = "cha"
    """
    Chamorro
    """
    chb = "chb"
    """
    Chibcha
    """
    che = "che"
    """
    Chechen
    """
    chg = "chg"
    """
    Chagatai
    """
    chi_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "chi (B)"
    """
    Chinese
    """
    zho_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "zho (T)"
    chk = "chk"
    """
    Chuukese
    """
    chm = "chm"
    """
    Mari
    """
    chn = "chn"
    """
    Chinook jargon
    """
    cho = "cho"
    """
    Choctaw
    """
    chp = "chp"
    """
    Chipewyan; Dene Suline
    """
    chr = "chr"
    """
    Cherokee
    """
    chu = "chu"
    """
    Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic
    """
    chv = "chv"
    """
    Chuvash
    """
    chy = "chy"
    """
    Cheyenne
    """
    cmc = "cmc"
    """
    Chamic languages
    """
    cnr = "cnr"
    """
    Montenegrin
    """
    cop = "cop"
    """
    Coptic
    """
    cor = "cor"
    """
    Cornish
    """
    cos = "cos"
    """
    Corsican
    """
    cpe = "cpe"
    """
    Creoles and pidgins, English based
    """
    cpf = "cpf"
    """
    Creoles and pidgins, French-based
    """
    cpp = "cpp"
    """
    Creoles and pidgins, Portuguese-based
    """
    cre = "cre"
    """
    Cree
    """
    crh = "crh"
    """
    Crimean Tatar; Crimean Turkish
    """
    crp = "crp"
    """
    Creoles and pidgins
    """
    csb = "csb"
    """
    Kashubian
    """
    cus = "cus"
    """
    Cushitic languages
    """
    wel_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "wel (B)"
    """
    Welsh
    """
    cym_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "cym (T)"
    dak = "dak"
    """
    Dakota
    """
    dan = "dan"
    """
    Danish
    """
    dar = "dar"
    """
    Dargwa
    """
    day = "day"
    """
    Land Dayak languages
    """
    del_ = "del"
    """
    Delaware
    """
    den = "den"
    """
    Slave (Athapascan)
    """
    ger_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "ger (B)"
    """
    German
    """
    deu_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "deu (T)"
    dgr = "dgr"
    """
    Dogrib
    """
    din = "din"
    """
    Dinka
    """
    div = "div"
    """
    Divehi; Dhivehi; Maldivian
    """
    doi = "doi"
    """
    Dogri
    """
    dra = "dra"
    """
    Dravidian languages
    """
    dsb = "dsb"
    """
    Lower Sorbian
    """
    dua = "dua"
    """
    Duala
    """
    dum = "dum"
    """
    Dutch, Middle (ca.1050-1350)
    """
    dut_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "dut (B)"
    """
    Dutch; Flemish
    """
    nld_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "nld (T)"
    dyu = "dyu"
    """
    Dyula
    """
    dzo = "dzo"
    """
    Dzongkha
    """
    efi = "efi"
    """
    Efik
    """
    egy = "egy"
    """
    Egyptian (Ancient)
    """
    eka = "eka"
    """
    Ekajuk
    """
    gre_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "gre (B)"
    """
    Greek, Modern (1453-)
    """
    ell_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "ell (T)"
    elx = "elx"
    """
    Elamite
    """
    eng = "eng"
    """
    English
    """
    enm = "enm"
    """
    English, Middle (1100-1500)
    """
    epo = "epo"
    """
    Esperanto
    """
    est = "est"
    """
    Estonian
    """
    ewe = "ewe"
    """
    Ewe
    """
    ewo = "ewo"
    """
    Ewondo
    """
    fan = "fan"
    """
    Fang
    """
    fao = "fao"
    """
    Faroese
    """
    per_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "per (B)"
    """
    Persian
    """
    fas_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "fas (T)"
    fat = "fat"
    """
    Fanti
    """
    fij = "fij"
    """
    Fijian
    """
    fil = "fil"
    """
    Filipino; Pilipino
    """
    fin = "fin"
    """
    Finnish
    """
    fiu = "fiu"
    """
    Finno-Ugrian languages
    """
    fon = "fon"
    """
    Fon
    """
    fre_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "fre (B)"
    """
    French
    """
    fra_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "fra (T)"
    frm = "frm"
    """
    French, Middle (ca.1400-1600)
    """
    fro = "fro"
    """
    French, Old (842-ca.1400)
    """
    frr = "frr"
    """
    Northern Frisian
    """
    frs = "frs"
    """
    Eastern Frisian
    """
    fry = "fry"
    """
    Western Frisian
    """
    ful = "ful"
    """
    Fulah
    """
    fur = "fur"
    """
    Friulian
    """
    gaa = "gaa"
    """
    Ga
    """
    gay = "gay"
    """
    Gayo
    """
    gba = "gba"
    """
    Gbaya
    """
    gem = "gem"
    """
    Germanic languages
    """
    geo_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "geo (B)"
    """
    Georgian
    """
    kat_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "kat (T)"
    gez = "gez"
    """
    Geez
    """
    gil = "gil"
    """
    Gilbertese
    """
    gla = "gla"
    """
    Gaelic; Scottish Gaelic
    """
    gle = "gle"
    """
    Irish
    """
    glg = "glg"
    """
    Galician
    """
    glv = "glv"
    """
    Manx
    """
    gmh = "gmh"
    """
    German, Middle High (ca.1050-1500)
    """
    goh = "goh"
    """
    German, Old High (ca.750-1050)
    """
    gon = "gon"
    """
    Gondi
    """
    gor = "gor"
    """
    Gorontalo
    """
    got = "got"
    """
    Gothic
    """
    grb = "grb"
    """
    Grebo
    """
    grc = "grc"
    """
    Greek, Ancient (to 1453)
    """
    grn = "grn"
    """
    Guarani
    """
    gsw = "gsw"
    """
    Swiss German; Alemannic; Alsatian
    """
    guj = "guj"
    """
    Gujarati
    """
    gwi = "gwi"
    """
    Gwich'in
    """
    hai = "hai"
    """
    Haida
    """
    hat = "hat"
    """
    Haitian; Haitian Creole
    """
    hau = "hau"
    """
    Hausa
    """
    haw = "haw"
    """
    Hawaiian
    """
    heb = "heb"
    """
    Hebrew
    """
    her = "her"
    """
    Herero
    """
    hil = "hil"
    """
    Hiligaynon
    """
    him = "him"
    """
    Himachali languages; Western Pahari languages
    """
    hin = "hin"
    """
    Hindi
    """
    hit = "hit"
    """
    Hittite
    """
    hmn = "hmn"
    """
    Hmong; Mong
    """
    hmo = "hmo"
    """
    Hiri Motu
    """
    hrv = "hrv"
    """
    Croatian
    """
    hsb = "hsb"
    """
    Upper Sorbian
    """
    hun = "hun"
    """
    Hungarian
    """
    hup = "hup"
    """
    Hupa
    """
    iba = "iba"
    """
    Iban
    """
    ibo = "ibo"
    """
    Igbo
    """
    ice_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "ice (B)"
    """
    Icelandic
    """
    isl_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "isl (T)"
    ido = "ido"
    """
    Ido
    """
    iii = "iii"
    """
    Sichuan Yi; Nuosu
    """
    ijo = "ijo"
    """
    Ijo languages
    """
    iku = "iku"
    """
    Inuktitut
    """
    ile = "ile"
    """
    Interlingue; Occidental
    """
    ilo = "ilo"
    """
    Iloko
    """
    ina = "ina"
    """
    Interlingua (International Auxiliary Language Association)
    """
    inc = "inc"
    """
    Indic languages
    """
    ind = "ind"
    """
    Indonesian
    """
    ine = "ine"
    """
    Indo-European languages
    """
    inh = "inh"
    """
    Ingush
    """
    ipk = "ipk"
    """
    Inupiaq
    """
    ira = "ira"
    """
    Iranian languages
    """
    iro = "iro"
    """
    Iroquoian languages
    """
    ita = "ita"
    """
    Italian
    """
    jav = "jav"
    """
    Javanese
    """
    jbo = "jbo"
    """
    Lojban
    """
    jpn = "jpn"
    """
    Japanese
    """
    jpr = "jpr"
    """
    Judeo-Persian
    """
    jrb = "jrb"
    """
    Judeo-Arabic
    """
    kaa = "kaa"
    """
    Kara-Kalpak
    """
    kab = "kab"
    """
    Kabyle
    """
    kac = "kac"
    """
    Kachin; Jingpho
    """
    kal = "kal"
    """
    Kalaallisut; Greenlandic
    """
    kam = "kam"
    """
    Kamba
    """
    kan = "kan"
    """
    Kannada
    """
    kar = "kar"
    """
    Karen languages
    """
    kas = "kas"
    """
    Kashmiri
    """
    kau = "kau"
    """
    Kanuri
    """
    kaw = "kaw"
    """
    Kawi
    """
    kaz = "kaz"
    """
    Kazakh
    """
    kbd = "kbd"
    """
    Kabardian
    """
    kha = "kha"
    """
    Khasi
    """
    khi = "khi"
    """
    Khoisan languages
    """
    khm = "khm"
    """
    Central Khmer
    """
    kho = "kho"
    """
    Khotanese; Sakan
    """
    kik = "kik"
    """
    Kikuyu; Gikuyu
    """
    kin = "kin"
    """
    Kinyarwanda
    """
    kir = "kir"
    """
    Kirghiz; Kyrgyz
    """
    kmb = "kmb"
    """
    Kimbundu
    """
    kok = "kok"
    """
    Konkani
    """
    kom = "kom"
    """
    Komi
    """
    kon = "kon"
    """
    Kongo
    """
    kor = "kor"
    """
    Korean
    """
    kos = "kos"
    """
    Kosraean
    """
    kpe = "kpe"
    """
    Kpelle
    """
    krc = "krc"
    """
    Karachay-Balkar
    """
    krl = "krl"
    """
    Karelian
    """
    kro = "kro"
    """
    Kru languages
    """
    kru = "kru"
    """
    Kurukh
    """
    kua = "kua"
    """
    Kuanyama; Kwanyama
    """
    kum = "kum"
    """
    Kumyk
    """
    kur = "kur"
    """
    Kurdish
    """
    kut = "kut"
    """
    Kutenai
    """
    lad = "lad"
    """
    Ladino
    """
    lah = "lah"
    """
    Lahnda
    """
    lam = "lam"
    """
    Lamba
    """
    lao = "lao"
    """
    Lao
    """
    lat = "lat"
    """
    Latin
    """
    lav = "lav"
    """
    Latvian
    """
    lez = "lez"
    """
    Lezghian
    """
    lim = "lim"
    """
    Limburgan; Limburger; Limburgish
    """
    lin = "lin"
    """
    Lingala
    """
    lit = "lit"
    """
    Lithuanian
    """
    lol = "lol"
    """
    Mongo
    """
    loz = "loz"
    """
    Lozi
    """
    ltz = "ltz"
    """
    Luxembourgish; Letzeburgesch
    """
    lua = "lua"
    """
    Luba-Lulua
    """
    lub = "lub"
    """
    Luba-Katanga
    """
    lug = "lug"
    """
    Ganda
    """
    lui = "lui"
    """
    Luiseno
    """
    lun = "lun"
    """
    Lunda
    """
    luo = "luo"
    """
    Luo (Kenya and Tanzania)
    """
    lus = "lus"
    """
    Lushai
    """
    mac_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "mac (B)"
    """
    Macedonian
    """
    mkd_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "mkd (T)"
    mad = "mad"
    """
    Madurese
    """
    mag = "mag"
    """
    Magahi
    """
    mah = "mah"
    """
    Marshallese
    """
    mai = "mai"
    """
    Maithili
    """
    mak = "mak"
    """
    Makasar
    """
    mal = "mal"
    """
    Malayalam
    """
    man = "man"
    """
    Mandingo
    """
    mao_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "mao (B)"
    """
    Maori
    """
    mri_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "mri (T)"
    map = "map"
    """
    Austronesian languages
    """
    mar = "mar"
    """
    Marathi
    """
    mas = "mas"
    """
    Masai
    """
    may_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "may (B)"
    """
    Malay
    """
    msa_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "msa (T)"
    mdf = "mdf"
    """
    Moksha
    """
    mdr = "mdr"
    """
    Mandar
    """
    men = "men"
    """
    Mende
    """
    mga = "mga"
    """
    Irish, Middle (900-1200)
    """
    mic = "mic"
    """
    Mi'kmaq; Micmac
    """
    min = "min"
    """
    Minangkabau
    """
    mis = "mis"
    """
    Uncoded languages
    """
    mkh = "mkh"
    """
    Mon-Khmer languages
    """
    mlg = "mlg"
    """
    Malagasy
    """
    mlt = "mlt"
    """
    Maltese
    """
    mnc = "mnc"
    """
    Manchu
    """
    mni = "mni"
    """
    Manipuri
    """
    mno = "mno"
    """
    Manobo languages
    """
    moh = "moh"
    """
    Mohawk
    """
    mon = "mon"
    """
    Mongolian
    """
    mos = "mos"
    """
    Mossi
    """
    mul = "mul"
    """
    Multiple languages
    """
    mun = "mun"
    """
    Munda languages
    """
    mus = "mus"
    """
    Creek
    """
    mwl = "mwl"
    """
    Mirandese
    """
    mwr = "mwr"
    """
    Marwari
    """
    myn = "myn"
    """
    Mayan languages
    """
    myv = "myv"
    """
    Erzya
    """
    nah = "nah"
    """
    Nahuatl languages
    """
    nai = "nai"
    """
    North American Indian languages
    """
    nap = "nap"
    """
    Neapolitan
    """
    nau = "nau"
    """
    Nauru
    """
    nav = "nav"
    """
    Navajo; Navaho
    """
    nbl = "nbl"
    """
    Ndebele, South; South Ndebele
    """
    nde = "nde"
    """
    Ndebele, North; North Ndebele
    """
    ndo = "ndo"
    """
    Ndonga
    """
    nds = "nds"
    """
    Low German; Low Saxon; German, Low; Saxon, Low
    """
    nep = "nep"
    """
    Nepali
    """
    new = "new"
    """
    Nepal Bhasa; Newari
    """
    nia = "nia"
    """
    Nias
    """
    nic = "nic"
    """
    Niger-Kordofanian languages
    """
    niu = "niu"
    """
    Niuean
    """
    nno = "nno"
    """
    Norwegian Nynorsk; Nynorsk, Norwegian
    """
    nob = "nob"
    """
    Bokmål, Norwegian; Norwegian Bokmål
    """
    nog = "nog"
    """
    Nogai
    """
    non = "non"
    """
    Norse, Old
    """
    nor = "nor"
    """
    Norwegian
    """
    nqo = "nqo"
    """
    N'Ko
    """
    nso = "nso"
    """
    Pedi; Sepedi; Northern Sotho
    """
    nub = "nub"
    """
    Nubian languages
    """
    nwc = "nwc"
    """
    Classical Newari; Old Newari; Classical Nepal Bhasa
    """
    nya = "nya"
    """
    Chichewa; Chewa; Nyanja
    """
    nym = "nym"
    """
    Nyamwezi
    """
    nyn = "nyn"
    """
    Nyankole
    """
    nyo = "nyo"
    """
    Nyoro
    """
    nzi = "nzi"
    """
    Nzima
    """
    oci = "oci"
    """
    Occitan (post 1500)
    """
    oji = "oji"
    """
    Ojibwa
    """
    ori = "ori"
    """
    Oriya
    """
    orm = "orm"
    """
    Oromo
    """
    osa = "osa"
    """
    Osage
    """
    oss = "oss"
    """
    Ossetian; Ossetic
    """
    ota = "ota"
    """
    Turkish, Ottoman (1500-1928)
    """
    oto = "oto"
    """
    Otomian languages
    """
    paa = "paa"
    """
    Papuan languages
    """
    pag = "pag"
    """
    Pangasinan
    """
    pal = "pal"
    """
    Pahlavi
    """
    pam = "pam"
    """
    Pampanga; Kapampangan
    """
    pan = "pan"
    """
    Panjabi; Punjabi
    """
    pap = "pap"
    """
    Papiamento
    """
    pau = "pau"
    """
    Palauan
    """
    peo = "peo"
    """
    Persian, Old (ca.600-400 B.C.)
    """
    phi = "phi"
    """
    Philippine languages
    """
    phn = "phn"
    """
    Phoenician
    """
    pli = "pli"
    """
    Pali
    """
    pol = "pol"
    """
    Polish
    """
    pon = "pon"
    """
    Pohnpeian
    """
    por = "por"
    """
    Portuguese
    """
    pra = "pra"
    """
    Prakrit languages
    """
    pro = "pro"
    """
    Provençal, Old (to 1500);Occitan, Old (to 1500)
    """
    pus = "pus"
    """
    Pushto; Pashto
    """
    qaa_qtz = "qaa-qtz"
    """
    Reserved for local use
    """
    que = "que"
    """
    Quechua
    """
    raj = "raj"
    """
    Rajasthani
    """
    rap = "rap"
    """
    Rapanui
    """
    rar = "rar"
    """
    Rarotongan; Cook Islands Maori
    """
    roa = "roa"
    """
    Romance languages
    """
    roh = "roh"
    """
    Romansh
    """
    rom = "rom"
    """
    Romany
    """
    rum_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "rum (B)"
    """
    Romanian; Moldavian; Moldovan
    """
    ron_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "ron (T)"
    run = "run"
    """
    Rundi
    """
    rup = "rup"
    """
    Aromanian; Arumanian; Macedo-Romanian
    """
    rus = "rus"
    """
    Russian
    """
    sad = "sad"
    """
    Sandawe
    """
    sag = "sag"
    """
    Sango
    """
    sah = "sah"
    """
    Yakut
    """
    sai = "sai"
    """
    South American Indian languages
    """
    sal = "sal"
    """
    Salishan languages
    """
    sam = "sam"
    """
    Samaritan Aramaic
    """
    san = "san"
    """
    Sanskrit
    """
    sas = "sas"
    """
    Sasak
    """
    sat = "sat"
    """
    Santali
    """
    scn = "scn"
    """
    Sicilian
    """
    sco = "sco"
    """
    Scots
    """
    sel = "sel"
    """
    Selkup
    """
    sem = "sem"
    """
    Semitic languages
    """
    sga = "sga"
    """
    Irish, Old (to 900)
    """
    sgn = "sgn"
    """
    Sign Languages
    """
    shn = "shn"
    """
    Shan
    """
    sid = "sid"
    """
    Sidamo
    """
    sin = "sin"
    """
    Sinhala; Sinhalese
    """
    sio = "sio"
    """
    Siouan languages
    """
    sit = "sit"
    """
    Sino-Tibetan languages
    """
    sla = "sla"
    """
    Slavic languages
    """
    slo_LEFT_PARENTHESISBRIGHT_PARENTHESIS = "slo (B)"
    """
    Slovak
    """
    slk_LEFT_PARENTHESISTRIGHT_PARENTHESIS = "slk (T)"
    slv = "slv"
    """
    Slovenian
    """
    sma = "sma"
    """
    Southern Sami
    """
    sme = "sme"
    """
    Northern Sami
    """
    smi = "smi"
    """
    Sami languages
    """
    smj = "smj"
    """
    Lule Sami
    """
    smn = "smn"
    """
    Inari Sami
    """
    smo = "smo"
    """
    Samoan
    """
    sms = "sms"
    """
    Skolt Sami
    """
    sna = "sna"
    """
    Shona
    """
    snd = "snd"
    """
    Sindhi
    """
    snk = "snk"
    """
    Soninke
    """
    sog = "sog"
    """
    Sogdian
    """
    som = "som"
    """
    Somali
    """
    son = "son"
    """
    Songhai languages
    """
    sot = "sot"
    """
    Sotho, Southern
    """
    spa = "spa"
    """
    Spanish; Castilian
    """
    srd = "srd"
    """
    Sardinian
    """
    srn = "srn"
    """
    Sranan Tongo
    """
    srp = "srp"
    """
    Serbian
    """
    srr = "srr"
    """
    Serer
    """
    ssa = "ssa"
    """
    Nilo-Saharan languages
    """
    ssw = "ssw"
    """
    Swati
    """
    suk = "suk"
    """
    Sukuma
    """
    sun = "sun"
    """
    Sundanese
    """
    sus = "sus"
    """
    Susu
    """
    sux = "sux"
    """
    Sumerian
    """
    swa = "swa"
    """
    Swahili
    """
    swe = "swe"
    """
    Swedish
    """
    syc = "syc"
    """
    Classical Syriac
    """
    syr = "syr"
    """
    Syriac
    """
    tah = "tah"
    """
    Tahitian
    """
    tai = "tai"
    """
    Tai languages
    """
    tam = "tam"
    """
    Tamil
    """
    tat = "tat"
    """
    Tatar
    """
    tel = "tel"
    """
    Telugu
    """
    tem = "tem"
    """
    Timne
    """
    ter = "ter"
    """
    Tereno
    """
    tet = "tet"
    """
    Tetum
    """
    tgk = "tgk"
    """
    Tajik
    """
    tgl = "tgl"
    """
    Tagalog
    """
    tha = "tha"
    """
    Thai
    """
    tig = "tig"
    """
    Tigre
    """
    tir = "tir"
    """
    Tigrinya
    """
    tiv = "tiv"
    """
    Tiv
    """
    tkl = "tkl"
    """
    Tokelau
    """
    tlh = "tlh"
    """
    Klingon; tlhIngan-Hol
    """
    tli = "tli"
    """
    Tlingit
    """
    tmh = "tmh"
    """
    Tamashek
    """
    tog = "tog"
    """
    Tonga (Nyasa)
    """
    ton = "ton"
    """
    Tonga (Tonga Islands)
    """
    tpi = "tpi"
    """
    Tok Pisin
    """
    tsi = "tsi"
    """
    Tsimshian
    """
    tsn = "tsn"
    """
    Tswana
    """
    tso = "tso"
    """
    Tsonga
    """
    tuk = "tuk"
    """
    Turkmen
    """
    tum = "tum"
    """
    Tumbuka
    """
    tup = "tup"
    """
    Tupi languages
    """
    tur = "tur"
    """
    Turkish
    """
    tut = "tut"
    """
    Altaic languages
    """
    tvl = "tvl"
    """
    Tuvalu
    """
    twi = "twi"
    """
    Twi
    """
    tyv = "tyv"
    """
    Tuvinian
    """
    udm = "udm"
    """
    Udmurt
    """
    uga = "uga"
    """
    Ugaritic
    """
    uig = "uig"
    """
    Uighur; Uyghur
    """
    ukr = "ukr"
    """
    Ukrainian
    """
    umb = "umb"
    """
    Umbundu
    """
    und = "und"
    """
    Undetermined
    """
    urd = "urd"
    """
    Urdu
    """
    uzb = "uzb"
    """
    Uzbek
    """
    vai = "vai"
    """
    Vai
    """
    ven = "ven"
    """
    Venda
    """
    vie = "vie"
    """
    Vietnamese
    """
    vol = "vol"
    """
    Volapük
    """
    vot = "vot"
    """
    Votic
    """
    wak = "wak"
    """
    Wakashan languages
    """
    wal = "wal"
    """
    Wolaitta; Wolaytta
    """
    war = "war"
    """
    Waray
    """
    was = "was"
    """
    Washo
    """
    wen = "wen"
    """
    Sorbian languages
    """
    wln = "wln"
    """
    Walloon
    """
    wol = "wol"
    """
    Wolof
    """
    xal = "xal"
    """
    Kalmyk; Oirat
    """
    xho = "xho"
    """
    Xhosa
    """
    yao = "yao"
    """
    Yao
    """
    yap = "yap"
    """
    Yapese
    """
    yid = "yid"
    """
    Yiddish
    """
    yor = "yor"
    """
    Yoruba
    """
    ypk = "ypk"
    """
    Yupik languages
    """
    zap = "zap"
    """
    Zapotec
    """
    zbl = "zbl"
    """
    Blissymbols; Blissymbolics; Bliss
    """
    zen = "zen"
    """
    Zenaga
    """
    zgh = "zgh"
    """
    Standard Moroccan Tamazight
    """
    zha = "zha"
    """
    Zhuang; Chuang
    """
    znd = "znd"
    """
    Zande languages
    """
    zul = "zul"
    """
    Zulu
    """
    zun = "zun"
    """
    Zuni
    """
    zxx = "zxx"
    """
    No linguistic content; Not applicable
    """
    zza = "zza"
    """
    Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki
    """


class MannerOfDeath(str, Enum):
    not_deceased = "not deceased"
    accidental = "accidental"
    """
    A manner of death in which death is caused by inadvertent chance happening(s).
    """
    homicide = "homicide"
    """
    A manner of death in which death is caused by a person's intentional action to kill or harm another.
    """
    suicide = "suicide"
    """
    A manner of death in which death is caused by self-inflicted injurty with evidence of intent to die.
    """
    natural = "natural"
    """
    A manner of death in which death is caused solely by disease or natural process.
    """
    manner_of_death_undetermined = "manner of death undetermined"
    """
    A manner of death where little information is known about the circumstances surrounding death or where information equally supports and/or conflicts with more than one manner of death.
    """
    unknown_if_subject_is_deceased_or_not = "unknown if subject is deceased or not"


class MaritalStatus(str, Enum):
    never_married = "never married"
    """
    A person who has never been married or whose only marriages have been annulled.
    """
    married = "married"
    """
    A person currently joined in matrimony. Classify common law marriage as married. Includes married couples living together and not living together.
    """
    domestic_partnership = "domestic partnership"
    """
    A person who is a member of an unmarried couple, including same sex couples, living together in longstanding relationships, that are registered or unregistered.
    """
    divorced = "divorced"
    """
    A person whose marriage has been legally dissolved and has not remarried.
    """
    separated = "separated"
    """
    A person living apart from his/her spouse by legal arrangement.
    """
    widowed = "widowed"
    """
    A person who is no longer married because of the death of his/her spouse and who has not remarried.
    """


class NeoplasticType(str, Enum):
    intrinsic = "intrinsic"
    """
    A disposition inhering in a tumour by virtue of the bearer's disposition not to invade surrounding tissues.
    """
    metastasis = "metastasis"
    """
    A disposition inhering in a tumour by virtue of the bearer's disposition to spread and invade distant tissues.
    """
    other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "other (specify)"
    """
    A structural quality which is held by a bearer when the latter's disposition the presence of abnormally proliferating masses of cells.
    """


class NeurodegenerativeType(str, Enum):
    beta_amyloid = "beta amyloid"
    """
    A peptide of 36-43 amino acids that is processed from the amyloid precursor protein. Appears to be the main constituent of amyloid plaques (deposits found in the brains of Alzheimer's disease patients).
    """
    pTau = "pTau"
    """
    A microtubule-associated protein tau that includes at least one phosphorylated residue.
    """
    pTDP_43 = "pTDP-43"
    """
    A protein that is a translation product of the human TARDBP gene or a 1:1 ortholog thereof.
    """
    alpha_synuclein = "alpha-synuclein"
    """
    A protein that is a translation product of the human SNCA gene or a 1:1 ortholog thereof.
    """
    Other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "Other (specify)"


class PerinatalEvent(str, Enum):
    subdural_hemorrhage = "subdural hemorrhage"
    """
    Bleeding into the subdural space, the potential space between the dura and arachnoid mater of the meninges around the brain.
    """
    subarachnoid_hemorrhage = "subarachnoid hemorrhage"
    """
    Intracranial hemorrhage into the subarachnoid space.
    """
    intraparenchymal_hemorrhage = "intraparenchymal hemorrhage"
    """
    Bleeding into the intraparenchymal space.
    """
    intraventricular_hemorrhage = "intraventricular hemorrhage"
    """
    Bleeding into the brain ventricles.
    """
    hypoxia = "hypoxia"
    """
    Reduced oxygenation of body tissues resulting in the decreased pressure of this component of body gases; commonly due to hypoxemia.
    """
    other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "other (specify)"
    none = "none"


class PostmortemMRI(str, Enum):
    cadaveric = "cadaveric"
    """
    A piece of tissue or a sample that is taken from a dead body (cadaver).
    """
    fresh_ex_vivo = "fresh ex vivo"
    """
    A piece of tissue or a sample that is taken from a living organism and not fixed.
    """
    fixed_ex_vivo = "fixed ex vivo"
    """
    A piece of tissue or a sample that is taken from a living organism and fixed.
    """


class Preparation(str, Enum):
    formalin_fixed = "formalin fixed"
    """
    A tissue sample that has been fixed with formalin.
    """
    number_4PERCENT_SIGN_paraformaldehyde_fixed = "4% paraformaldehyde fixed"
    """
    A tissue sample that has been fixed with 4% paraformaldehyde.
    """
    frozen = "frozen"
    """
    A tissue sample that has been frozen.
    """
    other = "other"
    """
    A tissue sample that has been fixed by some other method.
    """
    hemisphere_not_available = "hemisphere not available"


class Race(str, Enum):
    American_Indian_or_Alaska_Native = "American Indian or Alaska Native"
    """
    A person having origins in any of the original peoples of North and South America (including Central America) and who maintains tribal affiliation or community attachment.
    """
    Asian = "Asian"
    """
    A person having origins in any of the original peoples of the Far East, Southeast Asia, or the Indian subcontinent, including for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam.
    """
    Black_or_African_American = "Black or African American"
    """
    A person having origins in any of the Black racial groups of Africa. Terms such as "Haitian" or "Negro" can be used in addition to "Black or African American".
    """
    Native_Hawaiian_or_Other_Pacific_Islander = "Native Hawaiian or Other Pacific Islander"
    """
    A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands.
    """
    White = "White"
    """
    A person having origins in any of the original peoples of Europe, the Middle East, or North Africa.
    """
    More_than_one_race = "More than one race"
    """
    Having ancestors of several or various races.
    """
    Other_Race = "Other Race"
    """
    Individuals who do not necessarily identify with any particular race or others who do not wish to self select into a racial category(ies).
    """
    Prefer_not_to_Answer = "Prefer not to Answer"
    """
    A response indicating that an individual prefers or preferred not to answer.
    """
    Unknown = "Unknown"
    """
    Not known, observed, recorded; or reported as unknown by the data contributor.
    """


class RelativeType(str, Enum):
    biological_mother = "biological mother"
    """
    A female who contributes to the genetic makeup of her offspring from the fertilization of her ovum.
    """
    biological_father = "biological father"
    """
    A male who contributes to the genetic makeup of his offspring through the fertilization of an ovum by his sperm.
    """
    full_sibling = "full sibling"
    """
    A sibling with whom one shares both parents.
    """
    half_sibling = "half sibling"
    """
    A sibling with whom one shares a single parent.
    """
    child = "child"
    """
    A first-generation, biological descendant of any age.
    """
    maternal_grandmother = "maternal grandmother"
    """
    A female relative who is the biological mother of the biological mother.
    """
    paternal_grandmother = "paternal grandmother"
    """
    A female relative who is the biological mother of the biological father.
    """
    maternal_grandfather = "maternal grandfather"
    """
    A male relative who is the biological father of the biological mother.
    """
    paternal_grandfather = "paternal grandfather"
    """
    A male relative who is the biological father of the biological father.
    """
    maternal_aunt = "maternal aunt"
    """
    A female relative who is a sibling of the biological mother, and who both share a common ancestor.
    """
    paternal_aunt = "paternal aunt"
    """
    A female relative who is a sibling of the biological father, and who both share a common ancestor.
    """
    maternal_uncle = "maternal uncle"
    """
    A male relative who is a sibling of the biological mother, and who both share a common ancestor.
    """
    paternal_uncle = "paternal uncle"
    """
    A male relative who is a sibling of the biological father, and who both share a common ancestor.
    """
    maternal_nieceSOLIDUSnephew = "maternal niece/nephew"
    """
    A son or daughter of one's female biological sibling.
    """
    paternal_nieceSOLIDUSnephew = "paternal niece/nephew"
    """
    A son or daughter of one's male biological sibling.
    """
    maternal_cousin = "maternal cousin"
    """
    A relative who is the offspring of a sibling of the biological mother and thus sharing a common ancestor.
    """
    paternal_cousin = "paternal cousin"
    """
    A relative who is the offspring of a sibling of the biological father and thus sharing a common ancestor.
    """
    grandchild = "grandchild"
    """
    A child of one's son or daughter.
    """
    great_grandchild = "great-grandchild"
    """
    A child of one's grandchild.
    """
    other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "other (specify)"


class Repository(str, Enum):
    TBD = "TBD"
    Miami = "Miami"
    MtFULL_STOP_Sinai = "Mt. Sinai"
    Sepulveda = "Sepulveda"
    Harvard = "Harvard"
    Maryland_Psychiatric = "Maryland Psychiatric"
    HBCC = "HBCC"
    Maryland = "Maryland"
    Pittsburgh = "Pittsburgh"
    UCLA = "UCLA"


class Sex(str, Enum):
    male = "male"
    """
    A person who belongs to the sex that normally produces sperm. The term is used to indicate biological sex distinctions, cultural gender role distinctions, or both.
    """
    female = "female"
    """
    A person who belongs to the sex that normally produces ova. The term is used to indicate biological sex distinctions, or cultural gender role distinctions, or both.
    """
    intersex = "intersex"
    """
    A person (one of unisexual specimens) who is born with genitalia and/or secondary sexual characteristics of indeterminate sex, or which combine features of both sexes.
    """
    none_of_these_describe_me = "none of these describe me"
    """
    Suggested Definition: A response indicating that an individual feels that no option listed is a good description for them.
    """
    prefer_not_to_answer = "prefer not to answer"
    """
    A response indicating that an individual prefers or preferred not to answer.
    """
    unknown = "unknown"
    """
    Not known, observed, recorded; or reported as unknown by the data contributor.
    """


class SexualOrientation(str, Enum):
    bisexual = "bisexual"
    """
    Historically, bisexual referred to attraction to persons of two gender identities, typically, but not always, defined as male and female. In modern use, it is usually used to refer to persons who are sexually and/or romantically attracted to persons with a gender or genders like theirs and those with a gender or genders unlike theirs. Note that sometimes bisexual may be used as a synonym of pansexual.
    """
    homosexual_LEFT_PARENTHESISgaySOLIDUSlesbianRIGHT_PARENTHESIS = "homosexual (gay/lesbian)"
    """
    A person who is attracted solely or primarily to others of the same gender (or sex, depending on precise usage), i.e. being either a male androphile or a female gynephile.
    """
    heterosexual = "heterosexual"
    """
    Sexually attracted to a person defined as being of the "opposite" sex (i.e. male attracted to female or female attracted to male); more broadly, attracted to a gender that is not one's own.
    """
    not_reported = "not reported"
    """
    Not provided or available.
    """
    other = "other"
    """
    A sexual orientation that is not present in this list.
    """
    unknown = "unknown"
    """
    Not known, observed, recorded; or reported as unknown by the data contributor.
    """
    asexual = "asexual"
    """
    A person who identifies as asexual.
    """
    prefer_not_to_say = "prefer not to say"
    do_not_know = "do not know"


class TestName(str, Enum):
    Hepatitis_A = "Hepatitis A"
    Hepatitis_C_Antibody = "Hepatitis C Antibody"
    Hepatitis_B_Surface_Antigen = "Hepatitis B Surface Antigen"
    Hepatitis_B_Surface_Antibody = "Hepatitis B Surface Antibody"
    Hepatitis_B_Core_Antibody = "Hepatitis B Core Antibody"
    HIV_1SOLIDUSHIV_2_Plus_O_Antibody = "HIV-1/HIV-2 Plus O Antibody"
    HIV_1SOLIDUSHIV_2 = "HIV-1/HIV-2"
    HIV_1_Antibody = "HIV-1 Antibody"
    COVID_19_Virus_LEFT_PARENTHESISRT_PCRRIGHT_PARENTHESIS = "COVID-19 Virus (RT-PCR)"
    Other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "Other (specify)"


class TissueCollectionState(str, Enum):
    autopsy = "autopsy"
    """
    A postmortem examination of the body that includes an examination of the internal organs and structures after dissection to determine the cause of death and the nature of pathological changes.
    """
    surgery = "surgery"
    """
    Surgery is a medical procedure that uses operative manual and instrumental techniques on a patient to investigate and/or treat a pathological condition such as disease or injury, to help improve bodily function or appearance. The key difference between a surgery and a general procedure is the need for an incision. Making an incision, or cutting into the skin to gain access to the body’s deeper tissues or organs, is a defining characteristic of surgery.
    """


class Tissue(str, Enum):
    adipose = "adipose"
    """
    Portion of connective tissue composed of adipocytes enmeshed in areolar tissue.
    """
    adrenal = "adrenal"
    """
    Tissue that is part of some adrenal gland.
    """
    anus = "anus"
    """
    Orifice at the opposite end of an animal's digestive tract from the mouth. Its function is to expel feces, unwanted semi-solid matter produced during digestion, which, depending on the type of animal, may be one or more of: matter which the animal cannot digest, such as bones; food material after all the nutrients have been extracted, for example cellulose or lignin; ingested matter which would be toxic if it remained in the digestive tract; and dead or excess gut bacteria and other endosymbionts.
    """
    aorta = "aorta"
    """
    The main trunk of the systemic arterial system that carries blood from the heart to all the organs and other structures of the body, bringing oxygenated blood to all parts of the body in the systemic circulation.
    """
    appendix = "appendix"
    """
    A blind-ended tube connected to the cecum, from which it develops embryologically.
    """
    artery = "artery"
    """
    An epithelial tube or tree of tibes that transports blood away from the heart.
    """
    ascending_colon = "ascending colon"
    """
    Section of colon which is distal to the cecum and proximal to the transversecolon.
    """
    astrocytes = "astrocytes"
    """
    A class of large neuroglial (macroglial) cells in the central nervous system - the largest and most numerous neuroglial cells in the brain and spinal cord. Astrocytes (from 'star' cells) are irregularly shaped with many long processes, including those with 'end feet' which form the glial (limiting) membrane and directly and indirectly contribute to the blood-brain barrier. They regulate the extracellular ionic and chemical environment, and 'reactive astrocytes' (along with microglia) respond to injury. Astrocytes are reportedly CD68-negative, CD121a-positive, CD184-positive, CD192-positive, CRF-positive, EGFR-positive, GFAP-positive, GLUT1-positive, MBP-negative, and NGFR-positive.
    """
    bladder = "bladder"
    """
    Distensible musculomembranous organ situated in the anterior part of the pelvic cavity in which urine collects before excretion.
    """
    bone_rib = "bone rib"
    """
    An intersegmental rod-shaped bone that forms in the peritoneal membrane and attach to the vertebral parapophyses.
    """
    breast = "breast"
    """
    The upper ventral region of the torso of an organism.
    """
    bronchus = "bronchus"
    """
    The upper conducting airways of the lung; these airways arise from the terminus of the trachea.
    """
    cervical_spinal_cord = "cervical spinal cord"
    """
    A spinal cord segment that adjacent_to a cervical region.
    """
    colon_ascending = "colon ascending"
    """
    Section of colon which is distal to the cecum and proximal to the transversecolon.
    """
    colon_descending = "colon descending"
    """
    The portion of the colon between the left colic flexure and the sigmoid colon at the pelvic brim; the portion of the descending colon lying in the left iliac fossa is sometimes called the iliac colon.
    """
    CSF = "CSF"
    """
    A clear, colorless, bodily fluid, that occupies the subarachnoid space and the ventricular system around and inside the brain and spinal cord.
    """
    DRG_cervical = "DRG cervical"
    """
    A group of nerve cell bodies located on the dorsal spinal roots within the vertebral column at the level of the cervical vertebrae.
    """
    DRG_sacral = "DRG sacral"
    """
    A group of nerve cell bodies located on the dorsal spinal roots within the vertebral column at the level of the sacral vertebrae.
    """
    DRG_thoracic = "DRG thoracic"
    """
    A dorsal root ganglion that is part of a thorax.
    """
    diaphragm = "diaphragm"
    """
    A thin musculomebranous barrier that separates the abdominal and thoracic cavities. Often used for breathing control.
    """
    DNA = "DNA"
    """
    A long linear double-stranded polymer formed from nucleotides attached to a deoxyribose backbone and found in the nucleus of a cell; associated with the transmission of genetic information.
    """
    DRG_lumbar = "DRG lumbar"
    """
    The group of nerve cell bodies located on the dorsal spinal roots within the vertebral column at the level of the lumbar vertebrae.
    """
    duodenum = "duodenum"
    """
    The first part of the small intestine. At the junction of the stomach and the duodenum the alimentary canal is inflected. The duodenum first goes anteriorly for a short distance, turns dorsally, and eventually caudally, thus it is a U-shaped structure with two horizontal sections (a ventral and a dorsal one).
    """
    esophagus = "esophagus"
    """
    Tube that connects the pharynx to the stomach. In mammals, the oesophagus connects the buccal cavity with the stomach. The stratified squamous non-keratinised epithelium lining the buccal cavity is continued through the pharynx down into the oesophagus. The lowest part of the oesophagus (ca. 2 cm) is lined with gastric mucosa and covered by peritoneum. The main body of the oesophagus is lined with small, simple mucous glands. Each gland opens into the lumen by a long duct which pierces the muscularis mucosae (Wilson and Washington, 1989). A sphincter is situated at the point where the oesophagus enters the stomach to prevent gastro-oesophageal reflux, i.e. to prevent acidic gastric contents from reaching stratified epithelia of the oesophagus, where they can cause inflammation and irritation (Wilson and Washington, 1989; Brown et al., 1993).
    """
    eyes = "eyes"
    """
    An organ that detects light.
    """
    fallopian_tube = "fallopian tube"
    """
    Initial section of the oviduct through which the ova pass from the ovary to the uterus.
    """
    fibroblasts = "fibroblasts"
    """
    A connective tissue cell which secretes an extracellular matrix rich in collagen and other macromolecules. Flattened and irregular in outline with branching processes; appear fusiform or spindle-shaped. These cells may be vimentin-positive, fibronectin-positive, fsp1-positive, MMP-1-positive, collagen I-positive, collagen III-positive, and alpha-SMA-negative.
    """
    gallbladder = "gallbladder"
    """
    An organ that aids digestion and stores bile produced by the liver. Rats do not have a gallbladder, but produce bile. The bile flows directly from the liver through the (hepatic) bile duct into the small intestine (Hebel and Stromberg, 1988).
    """
    hair = "hair"
    """
    A filament, mostly protein, that grows from follicles found in the dermis.
    """
    heart = "heart"
    """
    A myogenic muscular circulatory organ found in the vertebrate cardiovascular system composed of chambers of cardiac muscle. It is the primary circulatory organ. Taxon notes:" the ascidian tube-like heart lacks chambers....The ascidian heart is formed after metamorphosis as a simple tube-like structure with a single-layered myoepithelium that is continuous with a single-layered pericar- dial wall. It lacks chambers and endocardium.... The innovation of the chambered heart was a key event in vertebrate evolution, because the chambered heart generates one-way blood flow with high pressure, a critical requirement for the efficient blood supply of large-body vertebrates... all extant vertebrates have hearts with two or more chambers (Moorman and Christoffels 2003)" DOI:10.1101/gad.1485706
    """
    ileum = "ileum"
    """
    The portion of the small intestine that extends from the jejunum to the colon.
    """
    jejunum = "jejunum"
    """
    The portion of the small intestine that extends from the duodenum to the ileum.
    """
    kidney = "kidney"
    """
    A paired organ of the urinary tract that produces urine and maintains bodily fluid homeostasis, blood pressure, pH levels, red blood cell production and skeleton mineralization.
    """
    liver = "liver"
    """
    An exocrine gland which secretes bile and functions in metabolism of protein and carbohydrate and fat, synthesizes substances involved in the clotting of the blood, synthesizes vitamin A, detoxifies poisonous substances, stores glycogen, and breaks down worn-out erythrocytes.
    """
    long_bone = "long bone"
    """
    A long bone is a bone that has a shaft and 2 ends and is longer than it is wide. Long bones have a thick outside layer of compact bone and an inner medullary cavity containing bone marrow. The ends of a long bone contain spongy bone and an epiphyseal plate or line depending on the stage of development. The epiphyseal plate is a hyaline cartilage, where new bone growth takes place, lengthening the bone prior to adulthood. Bone lengthening ceases when this cartilage is lost, leaving a remnant referred to as an epiphyseal line.
    """
    lumbar_spinal_cord = "lumbar spinal cord"
    lung = "lung"
    """
    Respiration organ that develops as an outpocketing of the esophagus.
    """
    lymph_node = "lymph node"
    """
    Any of the rounded masses of lymphoid tissue that are surrounded by a capsule of connective tissue, are distributed along the lymphatic vessels, and contain numerous lymphocytes which filter the flow of lymph.
    """
    middle_ear_bone = "middle ear bone"
    """
    One of 3 small bones contained within the middle ear space and serve to transmit sounds from the air to the fluid-filled labyrinth. The absence of the auditory ossicles would constitute a moderate-to-severe hearing loss. The term 'ossicles' literally means 'tiny bones' and commonly refers to the auditory ossicles, though the term may refer to any small bone throughout the body.
    """
    nail = "nail"
    """
    A horn-like keratin structure covering the dorsal aspect of the terminal phalanges of fingers and toes.
    """
    ovary = "ovary"
    """
    The gonad of a female organism which contains germ cells.
    """
    pancreas = "pancreas"
    """
    An endoderm derived structure that produces precursors of digestive enzymes and blood glucose regulating hormones.
    """
    peripheral_nerve = "peripheral nerve"
    """
    An enclosed, cable-like bundle of axons in the peripheral nervous system originating in a nerve root in the central nervous system (or a condensed nervous structure) connecting with peripheral structures.
    """
    pineal = "pineal"
    """
    A midline, cone like structure located in the dorso-caudal roof of the 3rd ventricle, attached by peduncles to the habenular and posterior commissures. The stalk contains nerve fibers, blood vessels, connective tissue and parenchymal cells (Paxinos, The Rat Central Nervous System, 2nd ed, pg 399).
    """
    pituitary = "pituitary"
    """
    The pituitary gland is an endocrine gland that secretes hormones that regulate many other glands.
    """
    placenta = "placenta"
    """
    Organ of metabolic interchange between fetus and mother, partly of embryonic origin and partly of maternal origin[GO]. The fetal portion of the placenta is known as the villous chorion. The maternal portion is known as the decidua basalis. The two portions are held together by anchoring villi that are anchored to the decidua basalis by the cytotrophoblastic shell. Marsupials possess only a rudimentary yolk-type placenta, with reduced nutrient and oxygen exchanging capabilities.
    """
    plasma = "plasma"
    """
    The liquid component of blood, in which erythrocytes are suspended.
    """
    prostate = "prostate"
    """
    The prostate gland is a partly muscular, partly glandular body that is situated near the base of the mammalian male urethra and secretes an alkaline viscid fluid which is a major constituent of the ejaculatory fluid.
    """
    psoas_muscle = "psoas muscle"
    """
    A powerful flexor of the thigh at the hip joint (psoas major) and a weak flexor of the trunk and lumbar spinal column (psoas minor). Psoas is derived from the Greek 'psoa', the plural meaning 'muscles of the loin'. It is a common site of infection manifesting as abscess (PSOAS ABSCESS). The psoas muscles and their fibers are also used frequently in experiments in muscle physiology.
    """
    RBC = "RBC"
    """
    A red blood cell. In mammals, mature erythrocytes are biconcave disks containing hemoglobin whose function is to transport oxygen.
    """
    RNA = "RNA"
    """
    High molecular weight, linear polymers, composed of nucleotides containing ribose and linked by phosphodiester bonds; RNA is central to the synthesis of proteins.
    """
    sacral_spinal_cord = "sacral spinal cord"
    """
    A spinal cord segment that adjacent_to a sacral region.
    """
    serum = "serum"
    """
    The portion of blood plasma that excludes clotting factors.
    """
    skin = "skin"
    """
    The organ covering the body that consists of the dermis and epidermis.
    """
    spleen = "spleen"
    """
    The organ that functions to filter blood and to store red corpuscles and platelets.
    """
    stomach = "stomach"
    """
    An expanded region of the vertebrate alimentary tract that serves as a food storage compartment and digestive organ. A stomach is lined, in whole or in part by a glandular epithelium.
    """
    systemic_tissue = "systemic tissue"
    """
    Tissue with cells that deposit non-polarized extracellular matrix including connective tissue fibers and ground substance.
    """
    temporalis_muscle = "temporalis muscle"
    """
    Pharyngeal arch 1 muscle that is innervated by the deep temporal branches of the trigeminal nerve and attaches to the wall of the braincase (including the cranial vault) and mandible.
    """
    testicle = "testicle"
    """
    A typically paired male reproductive gland that produces sperm and that in most mammals is contained within the scrotum at sexual maturity.
    """
    thoracic_spinal_cord = "thoracic spinal cord"
    """
    The thoracic nerves are the spinal nerves emerging from the thoracic vertebrae.
    """
    thymus = "thymus"
    """
    Anatomical structure of largely lymphoid tissue that functions in cell-mediated immunity by being the site where T cells develop.
    """
    thyroid = "thyroid"
    """
    A two-lobed endocrine gland found in all vertebrates, located in front of and on either side of the trachea in humans, and producing various hormones, such as triiodothyronine and calcitonin.
    """
    tissue = "tissue"
    """
    Multicellular anatomical structure that consists of many cells of one or a few types, arranged in an extracellular matrix such that their long-range organisation is at least partly a repetition of their short-range organisation.
    """
    tissue_other = "tissue-other"
    tongue = "tongue"
    """
    A fleshy movable process of the floor of the mouths of most vertebrates that bears sensory end organs and small glands and functions especially in taking and swallowing food and in humans as a speech organ.
    """
    tonsil = "tonsil"
    """
    Either of the two small almond-shaped masses of lymph tissue found on either side of the oropharynx.
    """
    trachea = "trachea"
    """
    The trachea is the portion of the airway that attaches to the bronchi as it branches.
    """
    umbilical_cord = "umbilical cord"
    """
    The connecting cord from the developing embryo to the placenta.
    """
    ureter = "ureter"
    """
    Muscular duct that propels urine from the kidneys to the urinary bladder, or related organs.
    """
    urinary_bladder = "urinary bladder"
    """
    Distensible musculomembranous organ situated in the anterior part of the pelvic cavity in which urine collects before excretion.
    """
    urine = "urine"
    """
    Excretion that is the output of a kidney.
    """
    uterus = "uterus"
    """
    The female muscular organ of gestation in which the developing embryo or fetus is nourished until birth.
    """
    vein = "vein"
    """
    Any of the tubular branching vessels that carry blood from the capillaries toward the heart.
    """
    vitreous = "vitreous"
    vitreous_humor = "vitreous humor"
    """
    A transparent, semigelatinous substance that fills the cavity behind the crystalline lens of the eye and in front of the retina.
    """
    whole_blood = "whole blood"
    """
    An achromatic cell of the myeloid or lymphoid lineages capable of ameboid movement, found in blood or other tissue.
    """


class TissueSource(str, Enum):
    whole_blood = "whole blood"
    """
    A fluid that is composed of blood plasma and erythrocytes.
    """
    plasma = "plasma"
    """
    The liquid component of blood, in which erythrocytes are suspended.
    """
    brain = "brain"
    """
    The brain is the center of the nervous system in all vertebrate, and most invertebrate, animals. Some primitive animals such as jellyfish and starfish have a decentralized nervous system without a brain, while sponges lack any nervous system at all. In vertebrates, the brain is located in the head, protected by the skull and close to the primary sensory apparatus of vision, hearing, balance, taste, and smell.
    """
    nasal_swab = "nasal swab"
    """
    A specimen obtained using a cotton swab on a stick, passed up the nostril to obtain a sample of exudate and epithelial debris for microbiological or cellular examination.
    """
    serum = "serum"
    """
    The portion of blood plasma that excludes clotting factors.
    """
    other = "other"
    unknown = "unknown"


class TraumaticType(str, Enum):
    contusion = "contusion"
    """
    An injury to biological tissue in which the capillaries are damaged, allowing blood to seep into the surrounding tissue
    """
    chronic_traumatic_encephalopathy = "chronic traumatic encephalopathy"
    """
    A tauopathy that is characterized by an abundance of hyperphosphorylated tau protein in neurons, astrocytes and cell processes around blood vessels and that is associated with repetitive head impacts or exposure to blast waves.
    """
    other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "other (specify)"


class VascularType(str, Enum):
    acute_infarct = "acute infarct"
    """
    Tissue necrosis in any area of the brain, including the cerebral hemispheres, the cerebellum, and the brain stem. Brain infarction is the result of a cascade of events initiated by inadequate blood flow through the brain that is followed by hypoxia and hypoglycemia in brain tissue. Damage may be temporary, permanent, selective or pan-necrosis.
    """
    chronic_infarct = "chronic infarct"
    """
    Tissue necrosis in any area of the brain, including the cerebral hemispheres, the cerebellum, and the brain stem. Brain infarction is the result of a cascade of events initiated by inadequate blood flow through the brain that is followed by hypoxia and hypoglycemia in brain tissue. Damage may be temporary, permanent, selective or pan-necrosis.
    """
    hemorrhage = "hemorrhage"
    """
    Loss of blood from the vascular compartment to the exterior or into nonvascular body space as a result of rupture or severance of the blood vessels.
    """
    other_LEFT_PARENTHESISspecifyRIGHT_PARENTHESIS = "other (specify)"



class OntologyClass(ConfiguredBaseModel):
    """
    a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:OntologyClass',
         'comments': ["This is modeled as a mixin. 'ontology class' should not be the "
                      'primary type of a node in the KG. Instead you should use an '
                      'informative bioloink category, such as AnatomicalEntity (for '
                      'Uberon classes), ChemicalSubstance (for CHEBI or CHEMBL), etc',
                      'Note that formally this is a metaclass. Instances of this class '
                      "are instances in the graph, but can be the object of 'type' "
                      'edges. For example, if we had a node in the graph representing '
                      'a specific brain of a specific patient (e.g brain001), this '
                      'could have a category of bl:Sample, and by typed more '
                      'specifically with an ontology class UBERON:nnn, which has as '
                      'category bl:AnatomicalEntity'],
         'definition_uri': 'https://w3id.org/biolink/vocab/OntologyClass',
         'exact_mappings': ['owl:Class', 'schema:Class'],
         'examples': [{'description': "the class 'brain' from the Uberon anatomy "
                                      'ontology',
                       'value': 'UBERON:0000955'}],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['MESH', 'UMLS', 'KEGG.BRITE'],
         'mixin': True,
         'see_also': ['https://github.com/biolink/biolink-model/issues/486']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })


class Annotation(ConfiguredBaseModel):
    """
    Biolink Model root class for entity annotations.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:Annotation',
         'definition_uri': 'https://w3id.org/biolink/vocab/Annotation',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    pass


class QuantityValue(Annotation):
    """
    A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:QuantityValue',
         'definition_uri': 'https://w3id.org/biolink/vocab/QuantityValue',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    has_unit: Optional[str] = Field(default=None, description="""connects a quantity value to a unit""", json_schema_extra = { "linkml_meta": {'close_mappings': ['EFO:0001697', 'UO-PROPERTY:is_unit_of'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_unit',
         'domain': 'quantity value',
         'domain_of': ['quantity value'],
         'exact_mappings': ['qud:unit', 'IAO:0000039'],
         'in_subset': ['samples'],
         'narrow_mappings': ['SNOMED:has_concentration_strength_denominator_unit',
                             'SNOMED:has_concentration_strength_numerator_unit',
                             'SNOMED:has_presentation_strength_denominator_unit',
                             'SNOMED:has_presentation_strength_numerator_unit',
                             'SNOMED:has_unit_of_presentation'],
         'slot_uri': 'biolink:has_unit'} })
    has_numeric_value: Optional[float] = Field(default=None, description="""connects a quantity value to a number""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/has_numeric_value',
         'domain': 'quantity value',
         'domain_of': ['quantity value'],
         'exact_mappings': ['qud:quantityValue'],
         'in_subset': ['samples'],
         'slot_uri': 'biolink:has_numeric_value'} })


class Entity(ConfiguredBaseModel):
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:Entity',
         'definition_uri': 'https://w3id.org/biolink/vocab/Entity',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Entity","biolink:Entity"]] = Field(default=["biolink:Entity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })


class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:NamedThing',
         'definition_uri': 'https://w3id.org/biolink/vocab/NamedThing',
         'exact_mappings': ['BFO:0000001',
                            'WIKIDATA:Q35120',
                            'UMLSSG:OBJC',
                            'STY:T071',
                            'dcid:Thing'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'slot_usage': {'category': {'name': 'category', 'required': True}}})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/NamedThing","biolink:NamedThing"]] = Field(default=["biolink:NamedThing"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })


class Attribute(NamedThing, OntologyClass):
    """
    A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Attribute',
         'definition_uri': 'https://w3id.org/biolink/vocab/Attribute',
         'exact_mappings': ['SIO:000614'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['EDAM-DATA', 'EDAM-FORMAT', 'EDAM-OPERATION', 'EDAM-TOPIC'],
         'in_subset': ['samples'],
         'mixins': ['ontology class'],
         'slot_usage': {'name': {'description': "The human-readable 'attribute name' "
                                                'can be set to a string which reflects '
                                                'its context of interpretation, e.g. '
                                                'SEPIO evidence/provenance/confidence '
                                                'annotation or it can default to the '
                                                "name associated with the 'has "
                                                "attribute type' slot ontology term.",
                                 'name': 'name'}}})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Attribute","biolink:Attribute"]] = Field(default=["biolink:Attribute"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    name: Optional[str] = Field(default=None, description="""The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    has_attribute_type: str = Field(default=..., description="""connects an attribute to a class that describes it""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute_type',
         'domain': 'attribute',
         'domain_of': ['attribute'],
         'in_subset': ['samples'],
         'narrow_mappings': ['LOINC:has_modality_type', 'LOINC:has_view_type'],
         'slot_uri': 'biolink:has_attribute_type'} })
    has_quantitative_value: Optional[list[QuantityValue]] = Field(default=None, description="""connects an attribute to a value""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/has_quantitative_value',
         'domain': 'attribute',
         'domain_of': ['attribute'],
         'exact_mappings': ['qud:quantityValue'],
         'in_subset': ['samples'],
         'narrow_mappings': ['SNOMED:has_concentration_strength_numerator_value',
                             'SNOMED:has_presentation_strength_denominator_value',
                             'SNOMED:has_presentation_strength_numerator_value'],
         'slot_uri': 'biolink:has_quantitative_value'} })
    has_qualitative_value: Optional[str] = Field(default=None, description="""connects an attribute to a value""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/has_qualitative_value',
         'domain': 'attribute',
         'domain_of': ['attribute'],
         'in_subset': ['samples'],
         'slot_uri': 'biolink:has_qualitative_value'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })


class TaxonomicRank(OntologyClass):
    """
    A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:TaxonomicRank',
         'definition_uri': 'https://w3id.org/biolink/vocab/TaxonomicRank',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['TAXRANK'],
         'mappings': ['WIKIDATA:Q427626']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })


class OrganismTaxon(NamedThing):
    """
    A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['taxon', 'taxonomic classification'],
         'class_uri': 'biolink:OrganismTaxon',
         'definition_uri': 'https://w3id.org/biolink/vocab/OrganismTaxon',
         'exact_mappings': ['WIKIDATA:Q16521', 'STY:T001', 'bioschemas:Taxon'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['NCBITaxon', 'MESH', 'UMLS'],
         'in_subset': ['model_organism_database'],
         'narrow_mappings': ['dcid:BiologicalSpecies'],
         'slot_usage': {'has taxonomic rank': {'mappings': ['WIKIDATA:P105'],
                                               'multivalued': False,
                                               'name': 'has taxonomic rank',
                                               'range': 'taxonomic rank'}},
         'values_from': ['NCBITaxon']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/OrganismTaxon","biolink:OrganismTaxon"]] = Field(default=["biolink:OrganismTaxon"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    has_taxonomic_rank: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/has_taxonomic_rank',
         'domain': 'named thing',
         'domain_of': ['organism taxon'],
         'is_a': 'node property',
         'mappings': ['WIKIDATA:P105'],
         'slot_uri': 'biolink:has_taxonomic_rank'} })
    exact_match: Optional[list[str]] = Field(default=None, description="""An external concept that is interchangeable with this entity. Symmetric and transitive, so it chains through third-party mappings. NOTE: this slot was added by bican (utils/bican_biolink_edit.py); it is not part of the Biolink Model.""", json_schema_extra = { "linkml_meta": {'domain_of': ['organism taxon'], 'slot_uri': 'skos:exactMatch'} })


class InformationContentEntity(NamedThing):
    """
    a piece of information that typically describes some topic of discourse or is used as support.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'aliases': ['information', 'information artefact', 'information entity'],
         'class_uri': 'biolink:InformationContentEntity',
         'definition_uri': 'https://w3id.org/biolink/vocab/InformationContentEntity',
         'exact_mappings': ['IAO:0000030'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['doi'],
         'narrow_mappings': ['UMLSSG:CONC',
                             'STY:T077',
                             'STY:T078',
                             'STY:T079',
                             'STY:T080',
                             'STY:T081',
                             'STY:T082',
                             'STY:T089',
                             'STY:T102',
                             'STY:T169',
                             'STY:T171',
                             'STY:T185']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/InformationContentEntity","biolink:InformationContentEntity"]] = Field(default=["biolink:InformationContentEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    license: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/license',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:license'],
         'is_a': 'node property',
         'narrow_mappings': ['WIKIDATA_PROPERTY:P275'],
         'slot_uri': 'biolink:license'} })
    rights: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/rights',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:rights'],
         'is_a': 'node property',
         'slot_uri': 'biolink:rights'} })
    format: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/format',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:format', 'WIKIDATA_PROPERTY:P2701'],
         'is_a': 'node property',
         'slot_uri': 'biolink:format'} })
    creation_date: Optional[date] = Field(default=None, description="""date on which an entity was created. This can be applied to nodes or edges""", json_schema_extra = { "linkml_meta": {'aliases': ['publication date', 'date started'],
         'definition_uri': 'https://w3id.org/biolink/vocab/creation_date',
         'domain': 'named thing',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:createdOn', 'WIKIDATA_PROPERTY:P577'],
         'is_a': 'node property',
         'slot_uri': 'biolink:creation_date'} })


class StudyResult(InformationContentEntity):
    """
    A collection of data items from a study that are about a particular study subject or experimental unit (the 'focus' of the Result) - optionally with context/provenance metadata that may be relevant to the interpretation of this data as evidence.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'biolink:StudyResult',
         'definition_uri': 'https://w3id.org/biolink/vocab/StudyResult',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'notes': ['The data/metadata included in a Study Result object are typically '
                   'a subset of data from a larger study data set, that are selected '
                   'by a curator because they may be useful as evidence for deriving '
                   'knowledge about a specific focus of the study. The notion of a '
                   "'study' here is defined broadly to include any research activity "
                   'at any scale that is aimed at generating knowledge or hypotheses. '
                   'This may include a single assay or computational analyses, or a '
                   'larger scale clinical trial or experimental research '
                   'investigation.']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/StudyResult","biolink:StudyResult"]] = Field(default=["biolink:StudyResult"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    license: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/license',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:license'],
         'is_a': 'node property',
         'narrow_mappings': ['WIKIDATA_PROPERTY:P275'],
         'slot_uri': 'biolink:license'} })
    rights: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/rights',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:rights'],
         'is_a': 'node property',
         'slot_uri': 'biolink:rights'} })
    format: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/format',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:format', 'WIKIDATA_PROPERTY:P2701'],
         'is_a': 'node property',
         'slot_uri': 'biolink:format'} })
    creation_date: Optional[date] = Field(default=None, description="""date on which an entity was created. This can be applied to nodes or edges""", json_schema_extra = { "linkml_meta": {'aliases': ['publication date', 'date started'],
         'definition_uri': 'https://w3id.org/biolink/vocab/creation_date',
         'domain': 'named thing',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:createdOn', 'WIKIDATA_PROPERTY:P577'],
         'is_a': 'node property',
         'slot_uri': 'biolink:creation_date'} })


class RelativeFrequencyAnalysisResult(StudyResult):
    """
    A result of a relative frequency analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:RelativeFrequencyAnalysisResult',
         'definition_uri': 'https://w3id.org/biolink/vocab/RelativeFrequencyAnalysisResult',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/RelativeFrequencyAnalysisResult","biolink:RelativeFrequencyAnalysisResult"]] = Field(default=["biolink:RelativeFrequencyAnalysisResult"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    license: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/license',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:license'],
         'is_a': 'node property',
         'narrow_mappings': ['WIKIDATA_PROPERTY:P275'],
         'slot_uri': 'biolink:license'} })
    rights: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/rights',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:rights'],
         'is_a': 'node property',
         'slot_uri': 'biolink:rights'} })
    format: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/format',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:format', 'WIKIDATA_PROPERTY:P2701'],
         'is_a': 'node property',
         'slot_uri': 'biolink:format'} })
    creation_date: Optional[date] = Field(default=None, description="""date on which an entity was created. This can be applied to nodes or edges""", json_schema_extra = { "linkml_meta": {'aliases': ['publication date', 'date started'],
         'definition_uri': 'https://w3id.org/biolink/vocab/creation_date',
         'domain': 'named thing',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:createdOn', 'WIKIDATA_PROPERTY:P577'],
         'is_a': 'node property',
         'slot_uri': 'biolink:creation_date'} })


class Dataset(InformationContentEntity):
    """
    an item that refers to a collection of data from a data source.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Dataset',
         'definition_uri': 'https://w3id.org/biolink/vocab/Dataset',
         'exact_mappings': ['IAO:0000100',
                            'dctypes:Dataset',
                            'schema:dataset',
                            'dcid:Dataset'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema'})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Dataset","biolink:Dataset"]] = Field(default=["biolink:Dataset"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    license: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/license',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:license'],
         'is_a': 'node property',
         'narrow_mappings': ['WIKIDATA_PROPERTY:P275'],
         'slot_uri': 'biolink:license'} })
    rights: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/rights',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:rights'],
         'is_a': 'node property',
         'slot_uri': 'biolink:rights'} })
    format: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/format',
         'domain': 'information content entity',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:format', 'WIKIDATA_PROPERTY:P2701'],
         'is_a': 'node property',
         'slot_uri': 'biolink:format'} })
    creation_date: Optional[date] = Field(default=None, description="""date on which an entity was created. This can be applied to nodes or edges""", json_schema_extra = { "linkml_meta": {'aliases': ['publication date', 'date started'],
         'definition_uri': 'https://w3id.org/biolink/vocab/creation_date',
         'domain': 'named thing',
         'domain_of': ['information content entity',
                       'study result',
                       'relative frequency analysis result',
                       'dataset'],
         'exact_mappings': ['dct:createdOn', 'WIKIDATA_PROPERTY:P577'],
         'is_a': 'node property',
         'slot_uri': 'biolink:creation_date'} })


class PhysicalEssenceOrOccurrent(ConfiguredBaseModel):
    """
    Either a physical or processual entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:PhysicalEssenceOrOccurrent',
         'definition_uri': 'https://w3id.org/biolink/vocab/PhysicalEssenceOrOccurrent',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class PhysicalEssence(PhysicalEssenceOrOccurrent):
    """
    Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:PhysicalEssence',
         'definition_uri': 'https://w3id.org/biolink/vocab/PhysicalEssence',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class PhysicalEntity(PhysicalEssence, NamedThing):
    """
    An entity that has material reality (a.k.a. physical essence).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:PhysicalEntity',
         'definition_uri': 'https://w3id.org/biolink/vocab/PhysicalEntity',
         'exact_mappings': ['STY:T072'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixins': ['physical essence'],
         'narrow_mappings': ['STY:T073']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/PhysicalEntity","biolink:PhysicalEntity"]] = Field(default=["biolink:PhysicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })


class Occurrent(PhysicalEssenceOrOccurrent):
    """
    A processual entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Occurrent',
         'definition_uri': 'https://w3id.org/biolink/vocab/Occurrent',
         'exact_mappings': ['BFO:0000003'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class ActivityAndBehavior(Occurrent):
    """
    Activity or behavior of any independent integral living, organization or mechanical actor in the world
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:ActivityAndBehavior',
         'definition_uri': 'https://w3id.org/biolink/vocab/ActivityAndBehavior',
         'exact_mappings': ['UMLSSG:ACTI'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class Activity(ActivityAndBehavior, NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Activity',
         'definition_uri': 'https://w3id.org/biolink/vocab/Activity',
         'exact_mappings': ['prov:Activity', 'NCIT:C43431', 'STY:T052'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixins': ['activity and behavior'],
         'narrow_mappings': ['STY:T056',
                             'STY:T057',
                             'STY:T064',
                             'STY:T066',
                             'STY:T062',
                             'STY:T065',
                             'STY:T058']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Activity","biolink:Activity"]] = Field(default=["biolink:Activity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })


class Procedure(ActivityAndBehavior, NamedThing):
    """
    A series of actions conducted in a certain order or manner
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Procedure',
         'definition_uri': 'https://w3id.org/biolink/vocab/Procedure',
         'exact_mappings': ['UMLSSG:PROC', 'dcid:MedicalProcedure'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['CPT'],
         'mixins': ['activity and behavior'],
         'narrow_mappings': ['STY:T059', 'STY:T060', 'STY:T061', 'STY:T063']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Procedure","biolink:Procedure"]] = Field(default=["biolink:Procedure"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })


class SubjectOfInvestigation(ConfiguredBaseModel):
    """
    An entity that has the role of being studied in an investigation, study, or experiment
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:SubjectOfInvestigation',
         'definition_uri': 'https://w3id.org/biolink/vocab/SubjectOfInvestigation',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class MaterialSample(SubjectOfInvestigation, PhysicalEntity):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['biospecimen', 'sample', 'biosample', 'physical sample'],
         'class_uri': 'biolink:MaterialSample',
         'definition_uri': 'https://w3id.org/biolink/vocab/MaterialSample',
         'exact_mappings': ['OBI:0000747', 'SIO:001050'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['BIOSAMPLE', 'GOLD.META'],
         'mixins': ['subject of investigation']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/MaterialSample","biolink:MaterialSample"]] = Field(default=["biolink:MaterialSample"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })


class ThingWithTaxon(ConfiguredBaseModel):
    """
    A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:ThingWithTaxon',
         'definition_uri': 'https://w3id.org/biolink/vocab/ThingWithTaxon',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })


class BiologicalEntity(ThingWithTaxon, NamedThing):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'aliases': ['bioentity'],
         'class_uri': 'biolink:BiologicalEntity',
         'definition_uri': 'https://w3id.org/biolink/vocab/BiologicalEntity',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixins': ['thing with taxon'],
         'narrow_mappings': ['WIKIDATA:Q28845870',
                             'STY:T050',
                             'SIO:010046',
                             'STY:T129']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/BiologicalEntity","biolink:BiologicalEntity"]] = Field(default=["biolink:BiologicalEntity"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })


class GenomicEntity(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:GenomicEntity',
         'definition_uri': 'https://w3id.org/biolink/vocab/GenomicEntity',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'in_subset': ['translator_minimal'],
         'mixin': True,
         'narrow_mappings': ['STY:T028', 'GENO:0000897']})

    has_biological_sequence: Optional[str] = Field(default=None, description="""connects a genomic feature to its sequence""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/has_biological_sequence',
         'domain': 'named thing',
         'domain_of': ['genomic entity', 'gene', 'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:has_biological_sequence'} })


class ChemicalEntityOrGeneOrGeneProduct(ConfiguredBaseModel):
    """
    A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:ChemicalEntityOrGeneOrGeneProduct',
         'definition_uri': 'https://w3id.org/biolink/vocab/ChemicalEntityOrGeneOrGeneProduct',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True})

    pass


class MacromolecularMachineMixin(ConfiguredBaseModel):
    """
    A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:MacromolecularMachineMixin',
         'definition_uri': 'https://w3id.org/biolink/vocab/MacromolecularMachineMixin',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'mixin': True,
         'slot_usage': {'name': {'description': 'genes are typically designated by a '
                                                'short symbol and a full name. We map '
                                                'the symbol to the default display '
                                                'name and use an additional slot for '
                                                'full name',
                                 'name': 'name',
                                 'range': 'symbol type'}}})

    name: Optional[str] = Field(default=None, description="""genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })


class GeneOrGeneProduct(MacromolecularMachineMixin):
    """
    A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:GeneOrGeneProduct',
         'definition_uri': 'https://w3id.org/biolink/vocab/GeneOrGeneProduct',
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['CHEMBL.TARGET', 'IUPHAR.FAMILY'],
         'mixin': True})

    name: Optional[str] = Field(default=None, description="""genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })


class Gene(GeneOrGeneProduct, ChemicalEntityOrGeneOrGeneProduct, GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['NCIT:C45822'],
         'class_uri': 'biolink:Gene',
         'definition_uri': 'https://w3id.org/biolink/vocab/Gene',
         'exact_mappings': ['SO:0000704', 'SIO:010035', 'WIKIDATA:Q7187', 'dcid:Gene'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'id_prefixes': ['NCBIGene',
                         'ENSEMBL',
                         'HGNC',
                         'MGI',
                         'ZFIN',
                         'dictyBase',
                         'WB',
                         'WormBase',
                         'FB',
                         'RGD',
                         'SGD',
                         'PomBase',
                         'OMIM',
                         'KEGG.GENES',
                         'UMLS',
                         'Xenbase',
                         'AspGD',
                         'PHARMGKB.GENE'],
         'in_subset': ['translator_minimal', 'model_organism_database'],
         'mixins': ['gene or gene product',
                    'genomic entity',
                    'chemical entity or gene or gene product',
                    'physical essence',
                    'ontology class'],
         'narrow_mappings': ['bioschemas:gene']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'macromolecular machine mixin',
         'domain_of': ['macromolecular machine mixin', 'gene or gene product'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'is_a': 'name',
         'is_usage_slot': True,
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label',
         'usage_slot_name': 'name'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Gene","biolink:Gene"]] = Field(default=["biolink:Gene"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })
    symbol: Optional[str] = Field(default=None, description="""Symbol for a particular thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/symbol',
         'domain': 'named thing',
         'domain_of': ['gene'],
         'exact_mappings': ['AGRKB:symbol', 'gpi:DB_Object_Symbol'],
         'is_a': 'node property',
         'slot_uri': 'biolink:symbol'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    has_biological_sequence: Optional[str] = Field(default=None, description="""connects a genomic feature to its sequence""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/has_biological_sequence',
         'domain': 'named thing',
         'domain_of': ['genomic entity', 'gene', 'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:has_biological_sequence'} })


class Genome(GenomicEntity, BiologicalEntity, PhysicalEssence, OntologyClass):
    """
    A genome is the sum of genetic material within a cell or virion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'biolink:Genome',
         'close_mappings': ['dcid:GenomeAssemblyUnit'],
         'definition_uri': 'https://w3id.org/biolink/vocab/Genome',
         'exact_mappings': ['SO:0001026', 'SIO:000984', 'WIKIDATA:Q7020'],
         'from_schema': 'https://w3id.org/biolink/bican-biolink-schema',
         'in_subset': ['model_organism_database'],
         'mixins': ['genomic entity', 'physical essence', 'ontology class']})

    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    name: Optional[str] = Field(default=None, description="""A human-readable name for an attribute or entity.""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['gff3:Name', 'gpi:DB_Object_Name'],
         'in_subset': ['translator_minimal', 'samples'],
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    xref: Optional[list[str]] = Field(default=None, description="""A database cross reference or alternative identifier for a NamedThing or edge between two NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'in_subset': ['translator_minimal'],
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://w3id.org/biolink/vocab/Genome","biolink:Genome"]] = Field(default=["biolink:Genome"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })
    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })
    has_biological_sequence: Optional[str] = Field(default=None, description="""connects a genomic feature to its sequence""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/has_biological_sequence',
         'domain': 'named thing',
         'domain_of': ['genomic entity', 'gene', 'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:has_biological_sequence'} })


class ProvActivity(ConfiguredBaseModel):
    """
    An activity is something that occurs over a period of time and acts upon or with entities;  it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Activity',
         'from_schema': 'https://identifiers.org/brain-bican/bican-prov-schema',
         'mixin': True})

    used: Optional[str] = Field(default=None, description="""Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize this entity and could not have been affected by the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProvActivity'], 'slot_uri': 'prov:used'} })


class ProvEntity(ConfiguredBaseModel):
    """
    An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects;  entities may be real or imaginary.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'prov:Entity',
         'from_schema': 'https://identifiers.org/brain-bican/bican-prov-schema',
         'mixin': True})

    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProvEntity'], 'slot_uri': 'prov:wasDerivedFrom'} })
    was_generated_by: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProvEntity'], 'slot_uri': 'prov:wasGeneratedBy'} })


class Donor(ProvEntity, ThingWithTaxon, PhysicalEntity):
    """
    A person or organism that is the source of a biological sample for scientific study.  Many biological samples are generated from a single donor.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['NIMP:Donor'],
         'from_schema': 'https://w3id.org/brain-bican/donor',
         'mixins': ['thing with taxon', 'ProvEntity'],
         'slot_usage': {'name': {'description': 'Donor identifier given by the brain '
                                                'bank or the institution that holds '
                                                'the brain',
                                 'exact_mappings': ['bican:f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf',
                                                    'NIMP:PD-QLQLFB34'],
                                 'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                                        'local_name_value': 'donor_local_name'},
                                                 'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                                        'local_name_value': 'Donor'}},
                                 'name': 'name'},
                        'xref': {'description': 'NIMP generated globally unique '
                                                'identifier for a Donor',
                                 'exact_mappings': ['bican:98b28574-f97f-4436-b723-10a6508431b5',
                                                    'NIMP:PD-DEXRDO36'],
                                 'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                                        'local_name_value': 'donor_nhash_id'},
                                                 'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                                        'local_name_value': 'Donor'}},
                                 'name': 'xref'}}})

    name: Optional[str] = Field(default=None, description="""Donor identifier given by the brain bank or the institution that holds the brain""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'display name', 'title'],
         'definition_uri': 'https://w3id.org/biolink/vocab/name',
         'domain': 'entity',
         'domain_of': ['attribute',
                       'entity',
                       'macromolecular machine mixin',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome',
                       'Donor'],
         'exact_mappings': ['bican:f8af20f7-e8b8-47b5-8a68-9ec1f913ffdf',
                            'NIMP:PD-QLQLFB34'],
         'in_subset': ['translator_minimal', 'samples'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'donor_local_name'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'Donor'}},
         'mappings': ['rdfs:label'],
         'narrow_mappings': ['dct:title', 'WIKIDATA_PROPERTY:P1476'],
         'slot_uri': 'rdfs:label'} })
    xref: Optional[list[str]] = Field(default=None, description="""NIMP generated globally unique identifier for a Donor""", json_schema_extra = { "linkml_meta": {'aliases': ['dbxref', 'Dbxref', 'DbXref', 'record_url', 'source_record_urls'],
         'definition_uri': 'https://w3id.org/biolink/vocab/xref',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'gene',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'genome',
                       'Donor'],
         'exact_mappings': ['bican:98b28574-f97f-4436-b723-10a6508431b5',
                            'NIMP:PD-DEXRDO36'],
         'in_subset': ['translator_minimal'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'donor_nhash_id'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'Donor'}},
         'narrow_mappings': ['gff3:Dbxref', 'gpi:DB_Xrefs'],
         'slot_uri': 'biolink:xref'} })
    repository: Optional[Repository] = Field(default=None, description="""If the brain is from NBB the NBB repository the brain belongs to""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:408682ed-0e27-41e2-b9fa-f05674366d6e',
                            'NIMP:PD-NYNYAR61'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'repository'}}} })
    donor_source: Optional[DonorSource] = Field(default=None, description="""The source of the donor brain e.g. NBB/UM1 project/other""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:0d0cf732-0f76-409d-9a73-7a96d829d3d3',
                            'NIMP:PD-TPTPPS27'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'donor_source'}}} })
    ethnicity: Optional[Ethnicity] = Field(default=None, description="""Ethnicity of the donor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:918370df-49f6-4361-9c52-f46b16412980',
                            'NIMP:PD-JEJECK48'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'ethnicity'}}} })
    race: Optional[Race] = Field(default=None, description="""Race of the donor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:e515c009-550e-4f9c-b1b6-fc876a6fb2a8',
                            'NIMP:PD-PRPRRP41'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'race'}}} })
    secondary_race: Optional[Race] = Field(default=None, description="""Second race if available for the donor""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:192fe5b1-c812-4767-86fb-3178f9914705',
                            'NIMP:PD-SESEQB42'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'second_race'}}} })
    sex: Optional[Sex] = Field(default=None, description="""Donor's sex at birth""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:c819b9d5-2fde-40b2-bf0d-e07b56f96ac9',
                            'NIMP:PD-LXUBTM45'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'sex'}}} })
    gender: Optional[Gender] = Field(default=None, description="""Donor's gender at death""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:1c71e775-65aa-442b-a392-1cf9a44e326e',
                            'NIMP:PD-KLKLJH33'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'gender'}}} })
    sex_orientation: Optional[SexualOrientation] = Field(default=None, description="""Donor's sexual orientation at death""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:e47e8a2f-72fb-4036-b288-f4580dc2aa4e',
                            'NIMP:PD-HKHGTM45'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'sex_orientation'}}} })
    age_of_death: Optional[int] = Field(default=None, description="""Donor's age at death in years""", ge=0, le=200, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:14eb923a-161d-45e2-889d-81fea7b632b6',
                            'NIMP:PD-FTEMQD38'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'age_of_death'}},
         'unit': {'ucum_code': 'a'}} })
    birth_country_name: Optional[BirthCountry] = Field(default=None, description="""Donor's birth country""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:9c27fd29-b512-492f-a32f-b615c7585ff7',
                            'NIMP:PD-SQSQDF25'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'birth_country_name'}}} })
    primary_language: Optional[Language] = Field(default=None, description="""Donor's primary language""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:abe9edc7-96ca-4c6a-a1ed-c008548cc373',
                            'NIMP:PD-ATEVEV39'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'primary_language'}}} })
    secondary_language: Optional[Language] = Field(default=None, description="""Donor's secondary language""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:37b7495f-b010-4d1c-ae32-9cb19c680950',
                            'NIMP:PD-OBIUQB42'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'secondary_language'}}} })
    marital_status: Optional[MaritalStatus] = Field(default=None, description="""Donor's marital or partner status""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:4f0e41c9-dd15-4a37-ae6b-11b7131d7cba',
                            'NIMP:PD-JCYJCN35'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'marital_status'}}} })
    education_years_number: Optional[int] = Field(default=None, description="""Number of years of education the donor had""", ge=0, le=30, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:add3f7fe-ae60-4cc1-bb2e-72bbbe9a1a7d',
                            'NIMP:PD-SJSJRC41'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'education_years_number'}},
         'unit': {'ucum_code': 'a'}} })
    handedness: Optional[Handedness] = Field(default=None, description="""Donor's handedness""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:82a4087c-d0e3-48ca-8bea-a81eefc683a0',
                            'NIMP:PD-WGWGTM45'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'handedness'}}} })
    confirmed_hbcac: Optional[str] = Field(default=None, description="""Confirmation status of meeting inclusion criteria of the Human Brain Cell Atlas Collection at NBB""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:b6cdddf7-6f0b-4855-a0fa-16c2ab29f219',
                            'NIMP:PD-YBLATM45'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'confirmed_hbcac'}}} })
    age_at_death_value: Optional[float] = Field(default=None, description="""Donor's age at death value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:57e24d3c-c9c7-4ef3-9809-a35802d563ec',
                            'NIMP:PD-FTFTCP24'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'age_at_death_value'}}} })
    age_at_death_unit: Optional[str] = Field(default=None, description="""The unit of the value mentioned under \"age_at_death_value\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:b5436e99-f0a7-4c30-825d-56b88ee2ac1d',
                            'NIMP:PD-AVAVEV39'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'age_at_death_unit'}}} })
    age_at_death_reference_point: Optional[str] = Field(default=None, description="""Reference point from which the donor's age at death was calculated""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:3bed1f94-9d82-4ed7-afdf-79d896b24dbb',
                            'NIMP:PD-RARAGG39'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'age_at_death_reference_point'}}} })
    donor_species: Optional[str] = Field(default=None, description="""NCBI Taxonomy code of the donor species""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:6837cb02-6bd7-4fb8-838c-9062ead96ba4',
                            'NIMP:PD-HEHERP41'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'donor_species'}}} })
    consent_status: Optional[str] = Field(default=None, description="""Whether the type of consent is open or controlled""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:1a53e733-276f-421a-850d-eb46e50db972',
                            'NIMP:PD-CBCBWQ40'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'consent_status'}}} })
    positive_test_result: Optional[str] = Field(default=None, description="""Whether the donor has had a positive serology test result""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:0ef73629-5172-4517-a1f8-295be1603b80',
                            'NIMP:PD-PDZDNL63'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'positive_test_result'}}} })
    donor_project: Optional[str] = Field(default=None, description="""Donor Project""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:cd772fb0-a2fe-4df3-b2dd-b62370be37fc',
                            'NIMP:PD-HEHEQB42'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'donor_project'}}} })
    donor_labs: Optional[str] = Field(default=None, description="""Donor Labs""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:b97c384f-a556-42a2-a3c2-c31e5771f481',
                            'NIMP:PD-APAPRP41'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'donor_labs'}}} })
    death_causes_data_available: Optional[str] = Field(default=None, description="""NIMP indicator for availability of the cause of death""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:e46e9d58-d982-4800-b7de-67f608951211',
                            'NIMP:PD-FYUCNY46'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'death_causes_data_available'}}} })
    rins_data_available: Optional[str] = Field(default=None, description="""NIMP indicator for availability of RNA Integrity Number""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:d05825e6-b785-42a3-9bdf-c34b30e698b8',
                            'NIMP:PD-JRJCAR61'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'rins_data_available'}}} })
    rines_data_available: Optional[str] = Field(default=None, description="""NIMP indicator for availability of RNA Integrity Number equivalent""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:28a5e912-570b-4a7f-87f2-36bd5db92090',
                            'NIMP:PD-CJRWAR61'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'rines_data_available'}}} })
    hemisphere: Optional[Hemisphere] = Field(default=None, description="""Hemisphere of the brain""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:68b7a28b-d695-4ec9-800b-6a27ca206081',
                            'NIMP:PD-JRJRFQ31'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'hemisphere'}}} })
    post_mortem_interval: Optional[float] = Field(default=None, description="""Post Mortem Interval in hours""", ge=0, le=8888, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:6fd5c5ac-b128-4a4a-ae98-09eaeba22f92',
                            'NIMP:PD-CHCHLC46'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'post_mortem_interval'}},
         'unit': {'ucum_code': 'h'}} })
    left_hemisphere_preparation: Optional[Preparation] = Field(default=None, description="""The method of which the left hemisphere of the brain was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:57d5378f-a451-4bf5-a472-cc88d0d29586',
                            'NIMP:PD-JSJSUS44'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'left_hemisphere_preparation'}}} })
    left_hemisphere_prep_2: Optional[str] = Field(default=None, description="""The second method used to prepare the left hemisphere""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:d76753fb-b30b-419b-b853-d341510d8034',
                            'NIMP:PD-ZMPWIB34'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'left_hemisphere_prep_2'}}} })
    right_hemisphere_preparation: Optional[Preparation] = Field(default=None, description="""The method of which the right hemisphere of the brain was prepared""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:477c2600-f979-43c5-9c61-ab61fd771584',
                            'NIMP:PD-MLMLPG50'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'right_hemisphere_preparation'}}} })
    right_hemisphere_prep_2: Optional[str] = Field(default=None, description="""The second method used to prepare the right hemisphere""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:b0a52336-fe31-4ac4-8914-b0bb76a8ef5a',
                            'NIMP:PD-FWUVWQ40'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'right_hemisphere_prep_2'}}} })
    rin: Optional[float] = Field(default=None, description="""RNA Integrity Number""", ge=0, le=99, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:cd472c0d-0b64-45c9-a38e-e54d15cea953',
                            'NIMP:PD-LPLPSK50'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'rin'}}} })
    rine: Optional[float] = Field(default=None, description="""RNA Integrity Number equivalent""", ge=0, le=99, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:1210148d-d8fb-45aa-b51a-4b19b6d09bec',
                            'NIMP:PD-XCXCRC41'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'rine'}}} })
    ph: Optional[float] = Field(default=None, description="""pH value""", ge=0, le=99, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:9e67af02-c081-43e1-a42c-bf9603cae616',
                            'NIMP:PD-FXFXDK42'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'ph'}}} })
    brain_weight: Optional[int] = Field(default=None, description="""The weight of the brain in grams""", ge=0, le=9998, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:546fc32d-f8a2-4c00-924a-8c4730f11f51',
                            'NIMP:PD-WUASWQ40'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'brain_weight'}},
         'unit': {'ucum_code': 'g'}} })
    weighed_type: Optional[BrainTissueWeightType] = Field(default=None, description="""The type of the brain tissue weighed based on the preparation""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:a7463e3f-0c61-4718-a7d0-60fd2116908a',
                            'NIMP:PD-FGHMDF25'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'weighed_type'}}} })
    photo_2d_available: Optional[str] = Field(default=None, description="""Is a 2D photograph is available?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:611beda8-1ac6-4183-a284-04a30bb474f3',
                            'NIMP:PD-NINIEV39'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'photo_2d_available'}}} })
    scan_3d_available: Optional[str] = Field(default=None, description="""Is a 3D scan is available?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:658e8a80-e232-438f-8c1e-d5f38724dc55',
                            'NIMP:PD-RBRBQB42'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'scan_3d_available'}}} })
    antemortem_mri_available: Optional[str] = Field(default=None, description="""Is an Antemortem MRI is available?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:43a04caa-4f28-47ac-8a9d-74c40f10776f',
                            'NIMP:PD-RCRCRC24'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'antemortem_mri_available'}}} })
    postmortem_mri_available: Optional[str] = Field(default=None, description="""Is a Postmortem MRI Available""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:0badd072-0c25-48c6-9357-44d5b5bc0818',
                            'NIMP:PD-YNYNEV39'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'postmortem_mri_available'}}} })
    postmortem_mri_type: Optional[PostmortemMRI] = Field(default=None, description="""The type of postmortem MRI if it is available.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:64a607a9-21e6-4c73-8f2e-2d67b0dc51c8',
                            'NIMP:PD-BEBEEV39'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'postmortem_mri_type'}}} })
    non_brain_specimen_data_available: Optional[str] = Field(default=None, description="""NIMP indicator for availability of non-brain Specimen data""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:e537aacd-040a-423b-9920-9ce5adecf111',
                            'NIMP:PD-JSFGYJ57'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'non_brain_specimen_data_available'}}} })
    neurologic_events_data_available: Optional[str] = Field(default=None, description="""NIMP indicator for availability of perinatal neurologic events data""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:27a7df05-5aec-4060-85b9-2b4658ecd1e8',
                            'NIMP:PD-SLCHJH85'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'neurologic_events_data_available'}}} })
    infectious_testings_data_available: Optional[str] = Field(default=None, description="""NIMP indicator for availability of infectious Disease/Serology testing data""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:af034af4-9a8d-49ed-a100-1e87ebe962f5',
                            'NIMP:PD-AATACA52'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'infectious_testings_data_available'}}} })
    tox_screening_data_available: Optional[str] = Field(default=None, description="""NIMP indicator for availability of toxicology screening data""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:3730c096-5524-43f4-a3c0-010ccdf80ae1',
                            'NIMP:PD-LELMNL63'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'tox_screening_data_available'}}} })
    nn_diagnoses_data_available: Optional[str] = Field(default=None, description="""NIMP indicator for availability of non-neuropathological diagnoses data""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:87a4e421-4586-4938-91cc-6ae4e6e95dde',
                            'NIMP:PD-JXZWYJ57'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'nn_diagnoses_data_available'}}} })
    non_brain_tissue_available: Optional[str] = Field(default=None, description="""Are any non-brain tissues available?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:3a064c96-a956-4cf3-8b77-056b8e392f99',
                            'NIMP:PD-LGLGRZ37'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'non_brain_tissue_available'}}} })
    tissue_type: Optional[Tissue] = Field(default=None, description="""The type of non-brain tissues""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:33ccbc85-ae35-44d6-8bc6-c2fb91116cf7',
                            'NIMP:PD-JLJLCT43'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'tissue_type'}}} })
    clinical_brain_diagnosis: Optional[str] = Field(default=None, description="""The ICD-10 code of the clinical brain diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:b7a34c73-ae08-43d3-80d2-d5ef8436e449',
                            'NIMP:PD-CLCLXT26'],
         'in_subset': ['Restricted'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'clinical_brain_diagnosis_code'}}} })
    clinical_brain_diagnosis_confidence_level: Optional[ConfidenceLevel] = Field(default=None, description="""The confidence level of the clinical brain diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:2e72b4b9-d5fb-4f0d-897c-1f977ed4fabd',
                            'NIMP:PD-LCLCJH33'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'clinical_brain_diagnosis_confidence_level'}}} })
    genetic_diagnosis_code: Optional[str] = Field(default=None, description="""The ICD-10 code of the genetic diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:7a7916e0-ff79-4426-b49f-58e2f2a8a367',
                            'NIMP:PD-KRKRBX30'],
         'in_subset': ['Restricted'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'genetic_diagnosis_code'}}} })
    genetic_diagnosis_confidence_level: Optional[ConfidenceLevel] = Field(default=None, description="""The confidence level of the genetic diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:cb2b0108-8c07-40e8-92a3-b693b6dc64b4',
                            'NIMP:PD-NONORZ37'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'genetic_diagnosis_confidence_level'}}} })
    non_brain_diagnosis_code: Optional[str] = Field(default=None, description="""The ICD-10 code of the non-brain diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:65e8824e-01d2-44cf-9f47-9962461a65c9',
                            'NIMP:PD-DNDNPI37'],
         'in_subset': ['Restricted'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'non_brain_diagnosis_code'}}} })
    non_brain_diagnosis_confidence_level: Optional[ConfidenceLevel] = Field(default=None, description="""The confidence level of the non-brain diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:2a7ff937-287b-40a3-a1f6-ebf598683774',
                            'NIMP:PD-FGFGUS44'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'non_brain_diagnosis_confidence_level'}}} })
    birth_weight_lbs: Optional[float] = Field(default=None, description="""Birth weight in pounds""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:69d9a60d-32d5-4c3a-a26a-802d8f030c8d',
                            'NIMP:PD-YOVEEV39'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'birth_weight_lbs'}},
         'unit': {'ucum_code': '[lb_av]'}} })
    birth_weight_oz: Optional[float] = Field(default=None, description="""Birth weight in ounces""", ge=0, le=100, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:b6f30050-f762-4427-8533-31738e737ea2',
                            'NIMP:PD-CANPLC46'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'birth_weight_oz'}},
         'unit': {'ucum_code': '[oz_av]'}} })
    apgar_5_minute_score: Optional[int] = Field(default=None, description="""The APGAR Five Minute Score. This is a test given to newborns just after birth""", ge=1, le=10, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:3a10dabf-39b0-4eb7-8399-85fd325c5646',
                            'NIMP:PD-GLPDCP24'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'apgar_5_minute_score'}}} })
    apgar_10_minute_score: Optional[int] = Field(default=None, description="""The APGAR Ten Minute Score. This is a test given to newborns just after birth""", ge=1, le=10, json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:09d512b6-7c20-4693-8894-77824ad7f04d',
                            'NIMP:PD-YKRCCP24'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'apgar_10_minute_score'}}} })
    neuropathology_diagnosis_code: Optional[str] = Field(default=None, description="""The ICD-10 codes for the neuropathological diagnoses""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:784e9cc1-7258-4535-a6d5-f7f9a4c2da4b',
                            'NIMP:PD-NCMNSS51'],
         'in_subset': ['Restricted'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'neuropathology_diagnosis_code'}}} })
    artifacts_type: Optional[ArtifactType] = Field(default=None, description="""The type of artifacts""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:dc217b9b-ed6b-48e2-93b4-4f648dc395f7',
                            'NIMP:PD-NCNCRC24'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'artifacts_type'}}} })
    developmental_type_specify: Optional[str] = Field(default=None, description="""The developmental neuropathology diagnoses specified""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:bee7d477-2dec-4bf5-878e-a105a0054366',
                            'NIMP:PD-TYTYOO47'],
         'in_subset': ['Restricted'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'developmental_type_specify'}}} })
    inflammatory_type_specify: Optional[str] = Field(default=None, description="""The inflammatory neuropathology diagnoses specified""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:616ba8d8-ced3-4f3e-b1ca-7103eb7a2c94',
                            'NIMP:PD-MAMATE52'],
         'in_subset': ['Restricted'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'inflammatory_type_specify'}}} })
    infectious_type_specify: Optional[str] = Field(default=None, description="""The infectious neuropathology diagnoses specified""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:c73cea5e-44d1-4dd9-b55e-3c6ef5dd2ef2',
                            'NIMP:PD-TYTYTE52'],
         'in_subset': ['Restricted'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'infectious_type_specify'}}} })
    traumatic_type: Optional[TraumaticType] = Field(default=None, description="""The type of traumatic neuropathology diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:01d2f488-f30b-40e0-913f-c9adc6b39b97',
                            'NIMP:PD-DRDRCT43'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'traumatic_type'}}} })
    vascular_type: Optional[VascularType] = Field(default=None, description="""The type of vascular neuropathology diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:5beafa90-ffdb-4cce-a78c-a3b3175210b6',
                            'NIMP:PD-RIRITM45'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'vascular_type'}}} })
    neoplastic_type: Optional[NeoplasticType] = Field(default=None, description="""The type of neoplastic neuropathology diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:a58be8f4-2756-4a66-9d05-1fbf44b4e810',
                            'NIMP:PD-NENERZ37'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'neoplastic_type'}}} })
    aging_type: Optional[AgingType] = Field(default=None, description="""The type of aging-related neuropathology diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:5e31b66f-131e-4d5e-8760-ddd85f5634d5',
                            'NIMP:PD-WNWNRC24'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'aging_type'}}} })
    neurodegenerative_type: Optional[NeurodegenerativeType] = Field(default=None, description="""The type of neurodegenerative neuropathology diagnosis""", json_schema_extra = { "linkml_meta": {'domain_of': ['Donor'],
         'exact_mappings': ['bican:b150b62c-a968-4f5d-9aa3-d1ab5207ff83',
                            'NIMP:PD-PEPERZ37'],
         'local_names': {'NIMP_resource_type': {'local_name_source': 'NIMP_resource_type',
                                                'local_name_value': 'Donor'},
                         'NIMP_variable_name': {'local_name_source': 'NIMP_variable_name',
                                                'local_name_value': 'neurodegenerative_type'}}} })
    in_taxon: Optional[list[str]] = Field(default=None, description="""connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'""", json_schema_extra = { "linkml_meta": {'aliases': ['instance of',
                     'is organism source of gene product',
                     'organism has gene',
                     'gene found in organism',
                     'gene product has organism source'],
         'annotations': {'canonical_predicate': {'tag': 'canonical_predicate',
                                                 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['RO:0002162', 'WIKIDATA_PROPERTY:P703'],
         'in_subset': ['translator_minimal'],
         'inherited': True,
         'is_a': 'related to at instance level',
         'narrow_mappings': ['RO:0002160'],
         'slot_uri': 'biolink:in_taxon'} })
    in_taxon_label: Optional[str] = Field(default=None, description="""The human readable scientific name for the taxon of the entity.""", json_schema_extra = { "linkml_meta": {'annotations': {'denormalized': {'tag': 'denormalized', 'value': True}},
         'definition_uri': 'https://w3id.org/biolink/vocab/in_taxon_label',
         'domain': 'thing with taxon',
         'domain_of': ['thing with taxon', 'biological entity', 'gene', 'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P225'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'slot_uri': 'biolink:in_taxon_label'} })
    was_derived_from: Optional[str] = Field(default=None, description="""A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProvEntity'], 'slot_uri': 'prov:wasDerivedFrom'} })
    was_generated_by: Optional[str] = Field(default=None, description="""Generation is the completion of production of a new entity by an activity. This entity did not exist before generation and becomes available for usage after this generation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['ProvEntity'], 'slot_uri': 'prov:wasGeneratedBy'} })
    id: str = Field(default=..., description="""A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/id',
         'domain': 'entity',
         'domain_of': ['ontology class',
                       'entity',
                       'attribute',
                       'named thing',
                       'taxonomic rank',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['AGRKB:primaryId', 'gff3:ID', 'gpi:DB_Object_ID'],
         'in_subset': ['translator_minimal'],
         'slot_uri': 'biolink:id'} })
    iri: Optional[str] = Field(default=None, description="""An IRI for an entity. This is determined by the id using expansion rules.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/iri',
         'domain_of': ['attribute',
                       'entity',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['WIKIDATA_PROPERTY:P854'],
         'in_subset': ['translator_minimal', 'samples'],
         'slot_uri': 'biolink:iri'} })
    type: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/type',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['gff3:type', 'gpi:DB_Object_Type'],
         'mappings': ['rdf:type'],
         'slot_uri': 'rdf:type'} })
    description: Optional[str] = Field(default=None, description="""a human-readable description of an entity""", json_schema_extra = { "linkml_meta": {'aliases': ['definition'],
         'definition_uri': 'https://w3id.org/biolink/vocab/description',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['IAO:0000115', 'skos:definitions'],
         'in_subset': ['translator_minimal'],
         'mappings': ['dct:description'],
         'narrow_mappings': ['gff3:Description'],
         'slot_uri': 'dct:description'} })
    has_attribute: Optional[list[str]] = Field(default=None, description="""connects any entity to an attribute""", json_schema_extra = { "linkml_meta": {'close_mappings': ['OBI:0001927'],
         'definition_uri': 'https://w3id.org/biolink/vocab/has_attribute',
         'domain': 'entity',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['SIO:000008'],
         'in_subset': ['samples'],
         'narrow_mappings': ['OBAN:association_has_subject_property',
                             'OBAN:association_has_object_property',
                             'CPT:has_possibly_included_panel_element',
                             'DRUGBANK:category',
                             'EFO:is_executed_in',
                             'HANCESTRO:0301',
                             'LOINC:has_action_guidance',
                             'LOINC:has_adjustment',
                             'LOINC:has_aggregation_view',
                             'LOINC:has_approach_guidance',
                             'LOINC:has_divisor',
                             'LOINC:has_exam',
                             'LOINC:has_method',
                             'LOINC:has_modality_subtype',
                             'LOINC:has_object_guidance',
                             'LOINC:has_scale',
                             'LOINC:has_suffix',
                             'LOINC:has_time_aspect',
                             'LOINC:has_time_modifier',
                             'LOINC:has_timing_of',
                             'NCIT:R88',
                             'NCIT:eo_disease_has_property_or_attribute',
                             'NCIT:has_data_element',
                             'NCIT:has_pharmaceutical_administration_method',
                             'NCIT:has_pharmaceutical_basic_dose_form',
                             'NCIT:has_pharmaceutical_intended_site',
                             'NCIT:has_pharmaceutical_release_characteristics',
                             'NCIT:has_pharmaceutical_state_of_matter',
                             'NCIT:has_pharmaceutical_transformation',
                             'NCIT:is_qualified_by',
                             'NCIT:qualifier_applies_to',
                             'NCIT:role_has_domain',
                             'NCIT:role_has_range',
                             'INO:0000154',
                             'HANCESTRO:0308',
                             'orphanet:C016',
                             'orphanet:C017',
                             'RO:0000053',
                             'RO:0000086',
                             'RO:0000087',
                             'SNOMED:has_access',
                             'SNOMED:has_clinical_course',
                             'SNOMED:has_count_of_base_of_active_ingredient',
                             'SNOMED:has_dose_form_administration_method',
                             'SNOMED:has_dose_form_release_characteristic',
                             'SNOMED:has_dose_form_transformation',
                             'SNOMED:has_finding_context',
                             'SNOMED:has_finding_informer',
                             'SNOMED:has_inherent_attribute',
                             'SNOMED:has_intent',
                             'SNOMED:has_interpretation',
                             'SNOMED:has_laterality',
                             'SNOMED:has_measurement_method',
                             'SNOMED:has_method',
                             'SNOMED:has_priority',
                             'SNOMED:has_procedure_context',
                             'SNOMED:has_process_duration',
                             'SNOMED:has_property',
                             'SNOMED:has_revision_status',
                             'SNOMED:has_scale_type',
                             'SNOMED:has_severity',
                             'SNOMED:has_specimen',
                             'SNOMED:has_state_of_matter',
                             'SNOMED:has_subject_relationship_context',
                             'SNOMED:has_surgical_approach',
                             'SNOMED:has_technique',
                             'SNOMED:has_temporal_context',
                             'SNOMED:has_time_aspect',
                             'SNOMED:has_units',
                             'UMLS:has_structural_class',
                             'UMLS:has_supported_concept_property',
                             'UMLS:has_supported_concept_relationship',
                             'UMLS:may_be_qualified_by'],
         'slot_uri': 'biolink:has_attribute'} })
    deprecated: Optional[bool] = Field(default=None, description="""A boolean flag indicating that an entity is no longer considered current or valid.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/deprecated',
         'domain_of': ['entity',
                       'attribute',
                       'named thing',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'exact_mappings': ['oboInOwl:ObsoleteClass'],
         'slot_uri': 'biolink:deprecated'} })
    provided_by: Optional[list[str]] = Field(default=None, description="""The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/provided_by',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:provided_by'} })
    full_name: Optional[str] = Field(default=None, description="""a long-form human readable name for a thing""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/full_name',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:full_name'} })
    synonym: Optional[list[str]] = Field(default=None, description="""Alternate human-readable names for a thing""", json_schema_extra = { "linkml_meta": {'aliases': ['alias'],
         'definition_uri': 'https://w3id.org/biolink/vocab/synonym',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'in_subset': ['translator_minimal'],
         'is_a': 'node property',
         'narrow_mappings': ['skos:altLabel',
                             'gff3:Alias',
                             'AGRKB:synonyms',
                             'gpi:DB_Object_Synonyms',
                             'HANCESTRO:0330',
                             'IAO:0000136',
                             'RXNORM:has_tradename'],
         'slot_uri': 'biolink:synonym'} })
    information_content: Optional[float] = Field(default=None, description="""Information content (IC) value for a term, primarily from Automats.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/information_content',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'slot_uri': 'biolink:information_content'} })
    equivalent_identifiers: Optional[list[str]] = Field(default=None, description="""A set of identifiers that are considered equivalent to the primary identifier of the entity. This attribute is used to represent a collection of identifiers that are considered equivalent to the primary identifier of an entity. These equivalent identifiers may come from different databases, ontologies, or naming conventions, but they all refer to the same underlying concept or entity. This attribute is particularly useful in data integration and interoperability scenarios, where it is important to recognize and link different representations of the same entity across various sources.""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/equivalent_identifiers',
         'domain': 'named thing',
         'domain_of': ['named thing',
                       'attribute',
                       'organism taxon',
                       'study result',
                       'relative frequency analysis result',
                       'information content entity',
                       'dataset',
                       'physical entity',
                       'activity',
                       'procedure',
                       'material sample',
                       'biological entity',
                       'gene',
                       'genome'],
         'is_a': 'node property',
         'see_also': ['biolink:xref', 'biolink:synonyms'],
         'slot_uri': 'biolink:equivalent_identifiers'} })
    category: list[Literal["https://identifiers.org/brain-bican/vocab/Donor","bican:Donor"]] = Field(default=["bican:Donor"], description="""Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag. In an RDF database it should be a biolink model class URI. This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`. In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}""", json_schema_extra = { "linkml_meta": {'definition_uri': 'https://w3id.org/biolink/vocab/category',
         'designates_type': True,
         'domain': 'entity',
         'domain_of': ['entity'],
         'in_subset': ['translator_minimal'],
         'is_a': 'type',
         'is_class_field': True,
         'slot_uri': 'biolink:category'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
OntologyClass.model_rebuild()
Annotation.model_rebuild()
QuantityValue.model_rebuild()
Entity.model_rebuild()
NamedThing.model_rebuild()
Attribute.model_rebuild()
TaxonomicRank.model_rebuild()
OrganismTaxon.model_rebuild()
InformationContentEntity.model_rebuild()
StudyResult.model_rebuild()
RelativeFrequencyAnalysisResult.model_rebuild()
Dataset.model_rebuild()
PhysicalEssenceOrOccurrent.model_rebuild()
PhysicalEssence.model_rebuild()
PhysicalEntity.model_rebuild()
Occurrent.model_rebuild()
ActivityAndBehavior.model_rebuild()
Activity.model_rebuild()
Procedure.model_rebuild()
SubjectOfInvestigation.model_rebuild()
MaterialSample.model_rebuild()
ThingWithTaxon.model_rebuild()
BiologicalEntity.model_rebuild()
GenomicEntity.model_rebuild()
ChemicalEntityOrGeneOrGeneProduct.model_rebuild()
MacromolecularMachineMixin.model_rebuild()
GeneOrGeneProduct.model_rebuild()
Gene.model_rebuild()
Genome.model_rebuild()
ProvActivity.model_rebuild()
ProvEntity.model_rebuild()
Donor.model_rebuild()
