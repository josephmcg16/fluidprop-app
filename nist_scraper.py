"""Module for scraping Thermophysical Properties of Fluid Systems data from the Nist Webbook."""
from urllib.error import HTTPError
import pandas as pd


def scrape_point(
    fluid_id: str,
    temperature: float,
    pressure: float,
) -> pd.DataFrame:
    """Scrape fluid properties data from the NIST Webbook for a pressure and temperature.
    
    Args:
        fluid_id (str): The fluid ID to scrape.
        temperature (float): The process temperature, degC.
        pressure (float): The process pressure, bar(a).
    
    Returns:
        pd.DataFrame: The scraped fluid data.
    """
    scraper_string = (
        f"https://webbook.nist.gov/cgi/fluid.cgi?T={temperature}&PLow={pressure}&"
        f"PHigh={pressure}&PInc=0&Digits=5&ID={fluid_id}&Action=Load&"
        "Type=IsoTherm&TUnit=C&PUnit=bar&DUnit=kg%2Fm3&HUnit=kJ%2Fkg&WUnit=m%2Fs&VisUnit=Pa*s&"
        "STUnit=N%2Fm&RefState=DEF"
    )
    try:
        return pd.read_html(scraper_string, index_col=False)[0]
    except HTTPError as exception:
        print(exception)
        return -1
