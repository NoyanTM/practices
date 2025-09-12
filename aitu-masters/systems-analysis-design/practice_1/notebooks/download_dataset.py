# TODO: do not suppress initial exception data, pass them with custom exception to debug

import json
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from uuid import uuid4

import requests
from fake_useragent import UserAgent

def generate_random_user_agent() -> str:
    global user_agent_generator_global
    return user_agent_generator_global.random

def get_packages_slice(directory: Path) -> None:
    """
    source for dataset:
    - https://github.com/hugovk/top-pypi-packages
    """

    try:
        response = requests.get("https://hugovk.github.io/top-pypi-packages/top-pypi-packages.csv")
        if not response.ok:
            message = f"Cannot access the resource or it is not available"
         = response.json()
    except requests.exceptions.RequestException as e:
        message = f"Cannot access the resource due to network connection error"
        logger.
        raise Exception(message)
    packages_slice = 
    try:
        with directory.open("w") as file:
            file.write()
    except OSError as e:
        message = f"Cannot write the data to file due to filesystem error"
        logger.error(message)
        raise Exception(message)

# TODO:
# - change to pypi sample api
# - def get_list_of_packages(url: str):
# - write to csv file and read in pandas (instead of reading from pandas firsthand)
# - change to async loop
def get_package_metadata(package_name: str) -> None:
    """
    package_name is unique name within pypi
    - according to https://docs.pypi.org/api/json/
    """

    headers = {
        "user-agent": generate_user_agent()
    }
    with httpx.Client(headers=headers) as client:
        try:
            response = client.get(f"https://pypi.org/pypi/{package_name}/json")
            if not response.ok:
                message = f"Cannot access the resource or not available for '{package_name}'"
                logger.error(message)
                raise Exception(message)
        except httpx.HTTPError as e:
            message = f"Cannot access the resource or not available for '{package_name}'"
            logger.error(message)
            raise Exception(message)
    try:
        metadata = json.dumps(response.json())
    except Exception as e:
        message = f"Cannot convert the resource metadata to JSON for '{package_name}'"
        logger.error(message)
        raise Exception(message)
    try:
        with open(f"../local_data/packages/{str(uuid4())}") as file:
            file.write(response.json())
    except OSError as e:
        message = f"Cannot write the package metadata to file for '{package_name}'"
        logger.error(message)
        raise Exception(message)
    message = f"The resource metadata is saved successfully for '{package_name}'"
    logger.info(message)

def main() -> None:
    base_directory = Path(__file__).parent
    local_data_directory = base_directory / "local_data"
    local_data_directory.mkdir(exist_ok=True)
    metadata_directory = local_data_directory / "metadata"
    metadata_directory.mkdir(exist_ok=True)
    user_agent_generator_global = UserAgent()

    get_packages_slice()

    # TODO: handle errors here via Future object instead
    # and for that error retry again
    with ProcessPoolExecutor() as executor:
        results = executor.map(get_package_metadata, pypi_packages)


if __name__ == "__main__":
    main()

pypi_packages = df["project"].to_list()

logging.basicConfig(
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", # TODO: change format of logging
    handlers=[
        logging.FileHandler("../local_data/metadata.log") # TODO: change to streamHandler and json logger
    ]
)
logger = logging.getLogger(__name__)

