"""Main module of the API. Contains the FastAPI application."""

from fastapi import FastAPI, HTTPException
import pandas as pd
import numpy as np

from nist_scraper import scrape_point, scrape_properties
from fluid_constants import NistWebbookFluidIDs


# Create the FastAPI application
app = FastAPI()

# database code here
dummy_db = []


@app.get("/fluid-properties/scrape-point/")
async def get_point(fluid: str, temperature: float, pressure: float):
    """Endpoint for scraping a single point from the NIST Webbook."""
    scraped_data = scrape_point(
        NistWebbookFluidIDs.FLUIDS[fluid], temperature, pressure
    )
    if not isinstance(scraped_data, pd.DataFrame):
        raise HTTPException(status_code=404, detail="No response from NIST Webbook.")
    scraped_data["Timestamp"] = pd.Timestamp.now()
    response = scraped_data.to_dict(orient="records")[0]
    dummy_db.append(response)
    return response


@app.get("/fluid-properties/scrape-properties/")
async def get_properties(
    fluid: str,
    min_temperature: float,
    max_temperature: float,
    min_pressure: float,
    max_pressure: float,
    num_points_temperature: int,
    num_points_pressure: int
):
    """Endpoint for scraping a single point from the NIST Webbook."""
    temperature_range = np.linspace(min_temperature, max_temperature, num_points_temperature)
    pressure_range = np.linspace(min_pressure, max_pressure, num_points_pressure)

    scraped_data = scrape_properties(
        NistWebbookFluidIDs.FLUIDS[fluid], temperature_range, pressure_range
    )
    if not isinstance(scraped_data, pd.DataFrame):
        raise HTTPException(status_code=404, detail="No response from NIST Webbook.")
    scraped_data["Timestamp"] = pd.Timestamp.now()
    response = scraped_data.to_dict(orient="records")
    dummy_db.append(response)
    return response


@app.get("/fluid-properties/get-points/")
async def get_previous_points():
    """Endpoint for getting fluid properties from a dummy database."""
    return dummy_db
