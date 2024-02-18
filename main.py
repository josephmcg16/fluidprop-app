"""Main module of the API. Contains the FastAPI application."""

from fastapi import FastAPI

from nist_scraper import scrape_point
from fluid_constants import NistWebbookFluidIDs


# Create the FastAPI application
app = FastAPI()

# database code here
dummy_db = []


@app.get("/fluid-properties/scrape-point/")
async def root(fluid: str, temperature: float, pressure: float):
    """Endpoint for scraping a single point from the NIST Webbook."""
    response = scrape_point(
        NistWebbookFluidIDs.FLUIDS[fluid], temperature, pressure
    ).iloc[0].to_dict()
    dummy_db.append(response)
    return response


@app.get("/fluid-properties/get-points/")
async def get_points():
    """Endpoint for getting fluid properties from a dummy database."""
    return dummy_db
