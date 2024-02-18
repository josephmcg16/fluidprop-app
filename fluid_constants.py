"""Class for handling of constants within the package."""
from dataclasses import dataclass


@dataclass
class NistWebbookFluidIDs:
    """Dataclass for the fluid IDs used in the NIST Webbook scraper."""
    WATER = "C7732185"
    NITROGEN = "C7727379"
    HYDROGEN = "C1333740"
    CARBON_DIOXIDE = "C124389"
    METHANE = "C74828"

    FLUIDS = {
        "H20": WATER,
        "N2": NITROGEN,
        "H2": HYDROGEN,
        "CO2": CARBON_DIOXIDE,
        "CH4": METHANE,
    }
