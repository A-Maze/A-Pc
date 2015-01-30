from django.db import models

from mongoengine import *
from APc.settings import DBNAME

connect(DBNAME)



class Views(Document):

    Id = StringField(max_length=500)
    Categorie = StringField(max_length=500)
    Aantal = StringField(max_length=50)

class ViewsPerDatum(Document):
    Aantal = StringField(max_length=500)
    Datum = StringField(max_length=50)

class Select(Document):

    Id = StringField(max_length=500)
    Categorie = StringField(max_length=500)
    Aantal = StringField(max_length=50)

class Moederborden(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = DecimalField()
    Afbeelding = StringField(max_length=500)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    Merk = StringField(max_length=200)
    Serie = StringField(max_length=200)
    Uitvoering = StringField(max_length=200)
    Afbeelding = StringField(max_length=200)
    Product = StringField(max_length=200)
    Socket = StringField(max_length=200)
    Aantal_socket = StringField(max_length=200)
    Form_Factor = StringField(max_length=200)
    BIOS_of_UEFI = StringField(max_length=200)
    Dual_of_Single_BIOS_UEFI = StringField(max_length=200)
    Moederbordchipset = StringField(max_length=200)
    Geheugentype = StringField(max_length=200)
    Maximum_geheugengrootte  = StringField(max_length=200)
    Hardeschijf_bus = StringField(max_length=200)
    Raid_modi = StringField(max_length=200)
    Card_Interface = StringField(max_length=200)
    Aantal_PCIe = StringField(max_length=200)
    Link_Interface  = StringField(max_length=200)
    Verbinding_Ethernet = StringField(max_length=200)
    Netwerkchip = StringField(max_length=200)
    Bluetooth_aanwezig = StringField(max_length=200)
    Verbinding_USB = StringField(max_length=200)
    Video_uit = StringField(max_length=200)
    Verbinding = StringField(max_length=200)
    Audio_kanalen = StringField(max_length=200)
    Audio_uitgangen = StringField(max_length=200)
    Audiochip = StringField(max_length=200)

class Processoren(Document):
    
    herkomst = StringField(max_length=200)
    categorie = StringField(max_length=120)
    Uitvoering = StringField(max_length=500)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    prijs = DecimalField()
    stock = StringField(max_length=500)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
    Merk = StringField(max_length=200)
    Serie = StringField(max_length=200)
    Product = StringField(max_length=200)
    Afbeelding = StringField(max_length=200)
    Socket = StringField(max_length=200)
    Aantal_cores = StringField(max_length=200)
    CPU_sSpec_Number = StringField(max_length=200)
    Snelheid = StringField(max_length=200)
    Maximale_turbo_frequentie = StringField(max_length=200)
    Geheugen_Specificatie = StringField(max_length=200)
    Bus_snelheid = StringField(max_length=200)
    Procestechnologie = StringField(max_length=200)
    Thermal_Design_Power = StringField(max_length=200)
    Geintegreerde_graphics = StringField(max_length=200)
    Gpu = StringField(max_length=200)
    Nominale_snelheid_videochip = StringField(max_length=200)
    Maximale_snelheid_videochip = StringField(max_length=200)
    CPU_Cache_Level_1 = StringField(max_length=200)
    CPU_Cache_Level_2 = StringField(max_length=200)
    CPU_Cache_Level_3 = StringField(max_length=200)
    Threads_oud = StringField(max_length=200)
    Threads = StringField(max_length=200)
    Threads_nieuw = StringField(max_length=200)
    Virtualisatie = StringField(max_length=200)
    Virtualisatie_type = StringField(max_length=200)
    CPU_Multiplier = StringField(max_length=200)
    CPU_stepping = StringField(max_length=200)
    CPU_Instructieset = StringField(max_length=200)
    Type_koeling = StringField(max_length=200)
    Verkoopstatus_CPU = StringField(max_length=200)
    Fabrieksgarantie = StringField(max_length=200)
    Bijzonderheden = StringField(max_length=200)


class Koeling(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = DecimalField()
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    Merk = StringField(max_length=200)
    Uitvoering = StringField(max_length=200)
    Afbeelding = StringField(max_length=200)
    Socket = StringField(max_length=200)
    Aansluiting_processorkoeling = StringField(max_length=200)
    Heatpipes = StringField(max_length=200)
    Geluidssterkte = StringField(max_length=200)
    Rotatiesnelheid_min = StringField(max_length=200)
    Rotatiesnelheid_max = StringField(max_length=200)
    Type_koeling = StringField(max_length=200)
    Hoogte = StringField(max_length=200)
    Diameter = StringField(max_length=200)
    Kleuren = StringField(max_length=200)
    Materialen = StringField(max_length=200)
    Fabrieksgarantie = StringField(max_length=200)
    Bijzonderheden = StringField(max_length=200)

class Behuizingen(Document):
    
    categorie = StringField(max_length=120)
    Product = StringField(max_length=500)
    naam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = DecimalField()
    Afbeelding = StringField(max_length=500)
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    Merk = StringField(max_length=200)
    Uitvoering = StringField(max_length=200)
    Barebonetype = StringField(max_length=200)
    Socket = StringField(max_length=200)
    CPU_SoC = StringField(max_length=200)
    Geheugentype_moederbord = StringField(max_length=200)
    Form_Factor = StringField(max_length=200)
    Aansluitingen = StringField(max_length=200)
    Hardeschijf_bus = StringField(max_length=200)
    Videochip = StringField(max_length=200)
    Behuizing_Voeding = StringField(max_length=200)
    Verbinding_Ethernet = StringField(max_length=200)
    Verbinding_wlan = StringField(max_length=200)
    Bluetooth_versie = StringField(max_length=200)
    Verbinding_USB_FW = StringField(max_length=200)
    Audio_uitgangen = StringField(max_length=200)
    Video_uit = StringField(max_length=200)
    Aansluitingen_voorzijde = StringField(max_length=200)
    Materialen = StringField(max_length=200)
    Kleuren = StringField(max_length=200)
    Behuizing_bay_intern = StringField(max_length=200)
    Hoogte = StringField(max_length=200)
    Breedte = StringField(max_length=200)
    Diepte = StringField(max_length=200)
    Bijzonderheden = StringField(max_length=200)

class Grafische(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = DecimalField()
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
    Merk = StringField(max_length=200)
    Product = StringField(max_length=200)
    Uitvoering = StringField(max_length=200)
    Afbeelding = StringField(max_length=200)
    Videochip = StringField(max_length=200)
    Chipset_generatie = StringField(max_length=200)
    Videochipfabrikant = StringField(max_length=200)
    Nominale_snelheid_videochip = StringField(max_length=200)
    Maximale_turbo_frequentie = StringField(max_length=200)
    Rekenkernen = StringField(max_length=200)
    Geheugengrootte = StringField(max_length=200)
    Geheugen_Type = StringField(max_length=200)
    Geheugen_Nominale_snelheid_videochip = StringField(max_length=200)
    Geheugen_Busbreedte = StringField(max_length=200)
    Card_Interface = StringField(max_length=200)
    Video_uit = StringField(max_length=200)
    Hoogste_HDMI_versie = StringField(max_length=200)
    Hoogste_DisplayPort_versie = StringField(max_length=200)
    Video_Adapter = StringField(max_length=200)
    DirectX_versie = StringField(max_length=200)
    OpenGL_versie = StringField(max_length=200)
    Shader_model = StringField(max_length=200)
    Lengte = StringField(max_length=200)
    Hoogte = StringField(max_length=200)
    Breedte = StringField(max_length=200)
    Aantal_slots = StringField(max_length=200)
    Aantal_pins = StringField(max_length=200)
    Aantal_6_pins = StringField(max_length=200)
    Aantal_8_pins = StringField(max_length=200)
    Stroomverbruik = StringField(max_length=200)
    Type_koeling = StringField(max_length=200)
    Link_Interface = StringField(max_length=200)

class Harde(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = DecimalField()
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    Merk = StringField(max_length=200)
    Serie = StringField(max_length=200)
    Product = StringField(max_length=200)
    Uitvoering = StringField(max_length=200)
    Afbeelding = StringField(max_length=200)
    Opslagcapaciteit = StringField(max_length=200)
    Hardeschijf_bus = StringField(max_length=200)
    Behuizing_bay_intern = StringField(max_length=200)
    Hoogte = StringField(max_length=200)
    Rotatiesnelheid = StringField(max_length=200)
    Drive_cache = StringField(max_length=200)
    Command_Queuing = StringField(max_length=200)
    Stroomverbruik_lezen = StringField(max_length=200)
    Stroomverbruik_schrijven = StringField(max_length=200)
    Prijs_per_GB = StringField(max_length=200)
    Fabrieksgarantie = StringField(max_length=200)
    SSD_type = StringField(max_length=200)
    SSD_controller = StringField(max_length=200)
    SSD_eigenschappen = StringField(max_length=200)
    Hardeschijf_bus_intern = StringField(max_length=200)
    HDD_SSD_aansluiting = StringField(max_length=200)
    Lezen_sequentieel = StringField(max_length=200)
    Schrijven_sequentieel = StringField(max_length=200)
    Lezen_random_4K = StringField(max_length=200)
    Schrijven_random_4K = StringField(max_length=200)
    Verkoopstatus = StringField(max_length=200)

class Dvd(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = DecimalField()
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
    Merk = StringField(max_length=200)
    Uitvoering = StringField(max_length=200) 
    Afbeelding = StringField(max_length=200)      
    Drive_Bay = StringField(max_length=200)
    Optisch_stationtype = StringField(max_length=200)
    Hardeschijf_bus = StringField(max_length=200)
    DVD_Leessnelheid = StringField(max_length=200)
    DVD_Schrijfsnelheid_SL = StringField(max_length=200)
    DVD_Schrijfsnelheid_DL = StringField(max_length=200)
    DVD_Herschrijfsnelheid = StringField(max_length=200)
    CD_Leessnelheid = StringField(max_length=200)
    CD_Schrijfsnelheid = StringField(max_length=200)
    Kleuren= StringField(max_length=200)
    Verkoopstatus = StringField(max_length=200)

class Geheugen(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    Geheugen_Specificatie = StringField(max_length=500)
    Afbeelding = StringField(max_length=500)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = DecimalField()
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
    Merk = StringField(max_length=200)
    Serie = StringField(max_length=200)
    Uitvoering = StringField(max_length=200)
    Afbeelding = StringField(max_length=200)
    Product = StringField(max_length=200)
    Geheugengrootte = StringField(max_length=200)
    Aantal = StringField(max_length=200)
    Modulegrootte = StringField(max_length=200)
    Prijs_per_GB = StringField(max_length=200)
    Geheugentype = StringField(max_length=200)
    Geheugen_Specificatie = StringField(max_length=200)
    Low_Voltage_DDR = StringField(max_length=200)
    Geheugen_CAS_Latency = StringField(max_length=200)
    Spanning = StringField(max_length=200)
    Fabrieksgarantie = StringField(max_length=200)
    Bijzonderheden = StringField(max_length=200)

class Voeding(Document):
    
    categorie = StringField(max_length=120)
    naam = StringField(max_length=500)
    subnaam = StringField(max_length=500,required=True)
    info = StringField(max_length=500)
    stock = StringField(max_length=500)
    prijs = DecimalField()
    ean = StringField(max_length=200)
    sku = StringField(max_length=200)
    herkomst = StringField(max_length=200)  
    link = StringField(max_length=200)
    Merk = StringField(max_length=200)
    Vermogen_watt = StringField(max_length=200)
    Uitvoering = StringField(max_length=200)
    Afbeelding = StringField(max_length=200)
    Product = StringField(max_length=200)
    _12V_Rails = StringField(max_length=200)
    Capaciteit_12V1_rail = StringField(max_length=200)
    Voeding_certificering = StringField(max_length=200)
    Aantal_Sata_aansluitingen = StringField(max_length=200)
    Aantal_molex_aansluitingen = StringField(max_length=200)
    PCI_Express_aansluitingen = StringField(max_length=200)
    Aantal_6_pins_aansluitingen = StringField(max_length=200)
    Aantal_6_2_pins_aansluitingen = StringField(max_length=200)
    Modulair = StringField(max_length=200)
    Aantal_ventilatoren = StringField(max_length=200)
    Diameter_ventilator = StringField(max_length=200)
    Type_koeling = StringField(max_length=200)
    Ventilator_locatie = StringField(max_length=200)
    Voedingtype = StringField(max_length=200)
    Stroomspanningbeveiliging = StringField(max_length=200)
    Breedte = StringField(max_length=200)
    Hoogte = StringField(max_length=200)
    Diepte = StringField(max_length=200)
    Fabrieksgarantie = StringField(max_length=200)
    Bijzonderheden = StringField(max_length=200)
