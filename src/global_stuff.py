from typing import TypedDict
from enum import Enum


class Kategorie(Enum):
    """Arten von Kunden. Wieso is Kunde hier? walla!"""

    S = 'S'
    """Stammkunde"""
    N = 'N'
    """Neukunde"""
    P = 'P'
    """Probeabo"""
    K = 'K'
    """Krankenkasse"""
    

class Kunde(TypedDict):
    """Dictionary für Kunde"""
    
    id_kunde: str
    name: str
    vorname: str
    kategorie: Kategorie
    groesse: float
    gewicht: float
    PIN: str
    locked: bool
