# TODO: asyncio

import json
import logging
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from uuid import uuid4

import pandas as pd
import requests
from fake_useragent import UserAgent

# TODO:
# - change format of logging
# - change to streamHandler and json logger
logging.basicConfig(
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(Path(__file__).parent.parent / "local_data" / "metadata.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def get_packages_slice(directory: Path) -> None:
    try:
        response = requests.get("https://hugovk.github.io/top-pypi-packages/top-pypi-packages.csv")
        if not response.ok:
            message = (
                f"Cannot access the resource or it is not available,"
                f"debug information: {e}"
            )
            logger.error(message)
            raise Exception(message)
    except requests.exceptions.RequestException as e:
        message = (
            f"Cannot access the resource due to network connection error,"
            f"debug information: {e}"
        )
        logger.error(message)
        raise Exception(message)
    package_slice_file = directory / "package_slice.csv"
    try:
        with package_slice_file.open("w") as file:
            file.write(response.text)
    except OSError as e:
        message = (
            f"Cannot write the data to file due to filesystem error,"
            f"debug information: {e}"
        )
        logger.error(message)
        raise Exception(message)

# TODO:
# - change to pypi sample api
# - def get_list_of_packages(url: str):
# - write to csv file and read in pandas (instead of reading from pandas firsthand)
# - change to async loop
def get_package_metadata(package_name: str, user_agent_generator: UserAgent, directory: Path) -> None:
    """
    package_name is unique name within pypi
    - according to https://docs.pypi.org/api/json/
    """
    headers = {
        "user-agent": user_agent_generator.random,
        "Accept": "application/json"
    }
    with requests.Session() as client:
        client.headers.update(headers)
        try:
            response = client.get(f"https://pypi.org/pypi/{package_name}/json")
            if not response.ok:
                message = f"Cannot access the resource or not available for '{package_name}'"
                logger.error(message)
                raise Exception(message)
        except requests.RequestException as e:
            message = (
                f"Cannot access the resource or not available for '{package_name}',"
                f"debug information: {e}"
            )
            logger.error(message)
            raise Exception(message)
    try:
        metadata = json.dumps(response.json(), ensure_ascii=False)
    except Exception as e:
        message = (
            f"Cannot convert the resource metadata to JSON for '{package_name}',"
            f"debug information: {e}"
        )
        logger.error(message)
        raise Exception(message)
    
    # TODO: add compression / serialization of json to binary data
    metadata_file = directory / f"{str(uuid4())}.json"
    try:
        with metadata_file.open("w") as file:
            file.write(metadata)
    except OSError as e:
        message = (
            f"Cannot write the package metadata to file for '{package_name}',"
            f"debug information: {e}"
        )
        logger.error(message)
        raise Exception(message)
    message = f"The resource metadata is saved successfully for '{package_name}'"
    logger.info(message)

def main() -> None:
    base_directory = Path(__file__).parent.parent
    local_data_directory = base_directory / "local_data"
    local_data_directory.mkdir(exist_ok=True)
    metadata_directory = local_data_directory / "metadata"
    metadata_directory.mkdir(exist_ok=True)
    user_agent_generator = UserAgent()

    get_packages_slice(directory=local_data_directory)
    df = pd.read_csv(str(local_data_directory / "package_slice.csv"))
    packages_slice = df["project"].to_list()

    # TODO: retry requests and errors
    # handle futures errors
    futures = list()
    with ProcessPoolExecutor() as executor:
        for package in packages_slice:
            future = executor.submit(get_package_metadata, package, user_agent_generator, metadata_directory)
            futures.append(future)
    for future in futures:
        print(future.result())

if __name__ == "__main__":
    main()

