# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TestItem(scrapy.Item):
    categorie = scrapy.Field()
    naam = scrapy.Field()
    subnaam = scrapy.Field()
    info = scrapy.Field()
    stock = scrapy.Field()
    prijs = scrapy.Field()
    link = scrapy.Field()
    ean = scrapy.Field()

class BobItem(scrapy.Item):
    categorie = scrapy.Field()
    naam = scrapy.Field()
    subnaam = scrapy.Field()
    info = scrapy.Field()
    stock = scrapy.Field()
    prijs = scrapy.Field()
    link = scrapy.Field()
    ean = scrapy.Field()
    herkomst = scrapy.Field()

class ParadigitItem(scrapy.Item):
    categorie = scrapy.Field()
    naam = scrapy.Field()
    #subnaam = scrapy.Field()
    info = scrapy.Field()
    stock = scrapy.Field()
    prijs = scrapy.Field()
    sku = scrapy.Field()
    link = scrapy.Field()
    herkomst = scrapy.Field()

class ComputerlandItem(scrapy.Item):
    categorie = scrapy.Field()
    naam = scrapy.Field()
    subnaam = scrapy.Field()
    stock = scrapy.Field()
    prijs = scrapy.Field()
    link = scrapy.Field()
    sku = scrapy.Field()

class InformatiqueItem(scrapy.Item):
    categorie = scrapy.Field()
    naam = scrapy.Field()
    stock = scrapy.Field()
    prijs = scrapy.Field()
    link = scrapy.Field()
    sku = scrapy.Field()

class BolItem(scrapy.Item):
    categorie = scrapy.Field()
    naam = scrapy.Field()
    stock = scrapy.Field()
    prijs = scrapy.Field()
    link = scrapy.Field()
    ean = scrapy.Field()
    herkomst = scrapy.Field()

class AfutureItem(scrapy.Item):
    categorie = scrapy.Field()
    naam = scrapy.Field()
    #subnaam = scrapy.Field()
    stock = scrapy.Field()
    prijs = scrapy.Field()
    link = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()

class AzertyItem(scrapy.Item):
    categorie = scrapy.Field()
    naam = scrapy.Field()
    subnaam = scrapy.Field()
    stock = scrapy.Field()
    prijs = scrapy.Field()
    link = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()
    herkomst = scrapy.Field()

#specificatie items
class GPU(scrapy.Item):
    categorie = scrapy.Field()
    Merk = scrapy.Field()
    Product = scrapy.Field()
    Uitvoering = scrapy.Field()
    Afbeelding = scrapy.Field()
    Videochip = scrapy.Field()
    Chipset_generatie = scrapy.Field()
    Videochipfabrikant = scrapy.Field()
    Nominale_snelheid_videochip = scrapy.Field()
    Maximale_turbo_frequentie = scrapy.Field()
    Rekenkernen = scrapy.Field()
    Geheugengrootte = scrapy.Field()
    Geheugen_Type = scrapy.Field()
    Geheugen_Nominale_snelheid_videochip = scrapy.Field()
    Geheugen_Busbreedte = scrapy.Field()
    Card_Interface = scrapy.Field()
    Video_uit = scrapy.Field()
    Hoogste_HDMI_versie = scrapy.Field()
    Hoogste_DisplayPort_versie = scrapy.Field()
    Video_Adapter = scrapy.Field()
    DirectX_versie = scrapy.Field()
    OpenGL_versie = scrapy.Field()
    Shader_model = scrapy.Field()
    Lengte = scrapy.Field()
    Hoogte = scrapy.Field()
    Breedte = scrapy.Field()
    Aantal_slots = scrapy.Field()
    Aantal_pins = scrapy.Field()
    Aantal_6_pins = scrapy.Field()
    Aantal_8_pins = scrapy.Field()
    Stroomverbruik = scrapy.Field()
    Type_koeling = scrapy.Field()
    Link_Interface = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()

class Geheugen(scrapy.Item):
    categorie = scrapy.Field()
    Merk = scrapy.Field()
    Serie = scrapy.Field()
    Uitvoering = scrapy.Field()
    Afbeelding = scrapy.Field()
    Product = scrapy.Field()
    Geheugengrootte = scrapy.Field()
    Aantal_pins = scrapy.Field()
    Modulegrootte = scrapy.Field()
    Prijs_per_GB = scrapy.Field()
    Geheugentype = scrapy.Field()
    Geheugen_Specificatie = scrapy.Field()
    Low_Voltage_DDR = scrapy.Field()
    Geheugen_CAS_Latency = scrapy.Field()
    Spanning = scrapy.Field()
    Fabrieksgarantie = scrapy.Field()
    Bijzonderheden = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()

class Moederbord(scrapy.Item):
    categorie = scrapy.Field()
    Merk = scrapy.Field()
    Serie = scrapy.Field()
    Uitvoering = scrapy.Field()
    Afbeelding = scrapy.Field()
    Product = scrapy.Field()
    Socket = scrapy.Field()
    Aantal_socket = scrapy.Field()
    Form_Factor = scrapy.Field()
    BIOS_of_UEFI = scrapy.Field()
    Dual_of_Single_BIOS_UEFI = scrapy.Field()
    Moederbordchipset = scrapy.Field()
    Geheugentype = scrapy.Field()
    Maximum_geheugengrootte  = scrapy.Field()
    Hardeschijf_bus = scrapy.Field()
    Raid_modi = scrapy.Field()
    Card_Interface = scrapy.Field()
    Aantal_PCIe = scrapy.Field()
    Link_Interface  = scrapy.Field()
    Verbinding_Ethernet = scrapy.Field()
    Netwerkchip = scrapy.Field()
    Bluetooth_aanwezig = scrapy.Field()
    Verbinding_USB = scrapy.Field()
    Video_uit = scrapy.Field()
    Verbinding = scrapy.Field()
    Audio_kanalen = scrapy.Field()
    Audio_uitgangen = scrapy.Field()
    Audiochip = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()

class Behuizing(scrapy.Item):
    categorie = scrapy.Field()
    Merk = scrapy.Field()
    Serie = scrapy.Field()
    Product = scrapy.Field()
    Uitvoering = scrapy.Field()
    Behuizingtype = scrapy.Field()
    Form_Factor = scrapy.Field()
    Behuizing_Panel = scrapy.Field()
    Materialen_Staal = scrapy.Field()
    Grafische_kaart_maximum_lengte = scrapy.Field()
    CPU_koeler_maximum_hoogte = scrapy.Field()
    Kleuren = scrapy.Field()
    Behuizing_bay_intern = scrapy.Field()
    Behuizing_bay_extern = scrapy.Field()
    Aansluitingen_voorzijde = scrapy.Field()
    Inclusief_voeding = scrapy.Field()
    Voeding_plaats = scrapy.Field()
    Voeding_form_factor = scrapy.Field()
    Fan_poorten = scrapy.Field()
    Meegeleverde_fans = scrapy.Field()
    Kabelmanagement = scrapy.Field()
    Hoogte = scrapy.Field()
    Breedte = scrapy.Field()
    Diepte = scrapy.Field()
    Volume = scrapy.Field()
    Gewicht = scrapy.Field()
    Fabrieksgarantie = scrapy.Field()
    Bijzonderheden = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()

class Processor(scrapy.Item):
    categorie = scrapy.Field()
    Merk = scrapy.Field()
    Serie = scrapy.Field()
    Product = scrapy.Field()
    Uitvoering = scrapy.Field()
    Afbeelding = scrapy.Field()
    Socket = scrapy.Field()
    Aantal_cores = scrapy.Field()
    CPU_sSpec_Number = scrapy.Field()
    Snelheid = scrapy.Field()
    Maximale_turbo_frequentie = scrapy.Field()
    Geheugen_Specificatie = scrapy.Field()
    Bus_snelheid = scrapy.Field()
    Procestechnologie = scrapy.Field()
    Thermal_Design_Power = scrapy.Field()
    Geintegreerde_graphics = scrapy.Field()
    Gpu = scrapy.Field()
    Nominale_snelheid_videochip = scrapy.Field()
    Maximale_snelheid_videochip = scrapy.Field()
    CPU_Cache_Level_1 = scrapy.Field()
    CPU_Cache_Level_2 = scrapy.Field()
    CPU_Cache_Level_3 = scrapy.Field()
    Threads_oud = scrapy.Field()
    Threads = scrapy.Field()
    Threads_nieuw = scrapy.Field()
    Virtualisatie = scrapy.Field()
    Virtualisatie_type = scrapy.Field()
    CPU_Multiplier = scrapy.Field()
    CPU_stepping = scrapy.Field()
    CPU_Instructieset = scrapy.Field()
    Type_koeling = scrapy.Field()
    Verkoopstatus_CPU = scrapy.Field()
    Fabrieksgarantie = scrapy.Field()
    Bijzonderheden = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()

class Voeding(scrapy.Item):
    categorie = scrapy.Field()
    Merk = scrapy.Field()
    Vermogen_watt = scrapy.Field()
    Product = scrapy.Field()
    _12V_Rails = scrapy.Field()
    Capaciteit_12V1_rail = scrapy.Field()
    Voeding_certificering = scrapy.Field()
    Aantal_Sata_aansluitingen = scrapy.Field()
    Aantal_molex_aansluitingen = scrapy.Field()
    PCI_Express_aansluitingen = scrapy.Field()
    Aantal_6_pins_aansluitingen = scrapy.Field()
    Aantal_6_2_pins_aansluitingen = scrapy.Field()
    Modulair = scrapy.Field()
    Aantal_ventilatoren = scrapy.Field()
    Diameter_ventilator = scrapy.Field()
    Type_koeling = scrapy.Field()
    Ventilator_locatie = scrapy.Field()
    Voedingtype = scrapy.Field()
    Stroomspanningbeveiliging = scrapy.Field()
    Breedte = scrapy.Field()
    Hoogte = scrapy.Field()
    Diepte = scrapy.Field()
    Fabrieksgarantie = scrapy.Field()
    Bijzonderheden = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()

class Koeling(scrapy.Item):  
    categorie = scrapy.Field()
    Merk = scrapy.Field()
    Serie = scrapy.Field()
    Uitvoering = scrapy.Field()
    Afbeelding = scrapy.Field()
    Product = scrapy.Field() 
    Socket = scrapy.Field()
    Aansluiting_processorkoeling = scrapy.Field()
    Heatpipes = scrapy.Field()
    Geluidssterkte = scrapy.Field()
    Rotatiesnelheid_min = scrapy.Field()
    Rotatiesnelheid_max = scrapy.Field()
    Type_koeling = scrapy.Field()
    Hoogte = scrapy.Field()
    Diameter = scrapy.Field()
    Kleuren = scrapy.Field()
    Materialen = scrapy.Field()
    Fabrieksgarantie = scrapy.Field()
    Bijzonderheden = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()

class Barebones(scrapy.Item):
    categorie = scrapy.Field()
    Merk = scrapy.Field()
    Afbeelding = scrapy.Field()
    Uitvoering = scrapy.Field()
    Barebonetype = scrapy.Field()
    Socket = scrapy.Field()
    CPU_SoC = scrapy.Field()
    Geheugentype_moederbord = scrapy.Field()
    Form_Factor = scrapy.Field()
    Aansluitingen = scrapy.Field()
    Hardeschijf_bus = scrapy.Field()
    Videochip = scrapy.Field()
    Behuizing_Voeding = scrapy.Field()
    Verbinding_Ethernet = scrapy.Field()
    Verbinding_wlan = scrapy.Field()
    Bluetooth_versie = scrapy.Field()
    Verbinding_USB_FW = scrapy.Field()
    Audio_uitgangen = scrapy.Field()
    Video_uit = scrapy.Field()
    Aansluitingen_voorzijde = scrapy.Field()
    Materialen = scrapy.Field()
    Kleuren = scrapy.Field()
    Behuizing_bay_intern = scrapy.Field()
    Hoogte = scrapy.Field()
    Breedte = scrapy.Field()
    Diepte = scrapy.Field()
    Bijzonderheden = scrapy.Field()
    ean = scrapy.Field()
    sku = scrapy.Field()