"""
Simple script to download Instagram media content, because they don't normally let you
"""
import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

import requests
from loguru import logger
from tqdm import tqdm

BLOCK_SIZE: int = 1024


def is_connected(test_url: str = "https://instagram.com", timeout: int = 2) -> bool:
    """
    Checks the user's internet connection.

    Args:
        test_url: string, a valid url to test connection against.
        timeout: int, number of seconds to try for before giving up.

    Returns:
        Whether or not the user has a valid connection.
    """
    try:
        test_connection = requests.get(test_url, timeout=timeout)
        test_connection.raise_for_status()
        logger.debug("Internet connection is valid")
        return True
    except requests.HTTPError as error:
        logger.exception(
            f"Internet connection check failed with status code {error.response.status_code}"
        )
    except requests.exceptions.ConnectionError:
        logger.exception("An error happened when trying to establish a connection to Instagram.")
    return False


def is_instagram_domain(post_url: str = None) -> bool:
    """
    Confirms whether the provided test_url is a valid instagram link to download from.

    Args:
        post_url: string, link to an instagram post.

    Returns:
        True is it is a valid instagram post, False otherwise.
    """
    is_match = re.match(r"^(https:)[/][/]www.([^/]+[.])*instagram.com", post_url)
    if is_match:
        logger.debug("Provided test_url is a valid Instagram link")
        return True
    else:
        logger.debug("Provided test_url does not link to an Instagram post.")
        return False


def determine_media_type(media_content: str = None) -> str:
    """
    Determine the content type in the media_content from a request.

    Args:
        media_content: string, the html content decoded from a request to a
        valid Instagram post.

    Returns:
        A string classifying the media as either "image", "video", or something else
        that would be invalid".
    """
    logger.debug("Searching for content header in downloaded html media content")
    content_type_header: str = re.search(
        r'<meta name="medium" content=[\'"]?([^\'" >]+)', media_content
    ).group()
    logger.debug("Determining content type")
    content_type = re.sub(r'<meta name="medium" content="', "", content_type_header)
    logger.debug(f"Identified content type: {content_type}")
    return content_type


def extract_image_direct_link(media_content: str = None) -> str:
    """
    Find the exact test_url to the image embedded in the page content.

    Args:
        media_content: string, the html content decoded from a request to a valid Instagram post.

    Returns:
        A string with the exact test_url to the image in the Instagram post.
    """
    logger.debug("Searching for image header in downloaded html media content")
    image_link_header: str = re.search(
        r'meta property="og:image" content=[\'"]?([^\'" >]+)', media_content
    ).group()
    logger.debug("Determining image's direct link")
    image_link: str = re.sub(r'meta property="og:image" content="', "", image_link_header)
    return image_link


def extract_video_direct_link(media_content: str = None) -> str:
    """
    Find the exact test_url to the video embedded in the page content.

    Args:
        media_content: string, the html content decoded from a request to a valid Instagram post.

    Returns:
        A string with the exact test_url to the video in the Instagram post.
    """
    logger.debug("Searching for video header in downloaded html media content")
    image_link_header: str = re.search(
        r'meta property="og:video" content=[\'"]?([^\'" >]+)', media_content
    ).group()
    logger.debug("Determining video's direct link")
    video_link: str = re.sub(r'meta property="og:video" content="', "", image_link_header)
    return video_link


@logger.catch
def download_image(post_content: str = None) -> None:
    """
    Downloads the image from the post.

    Args:
        post_content: the html content extracted by a request to the post's url.

    Returns:
        Nothing, downloads and exits.
    """
    image_direct_url: str = extract_image_direct_link(post_content)

    logger.debug("Extracting image content")
    image_content = requests.get(image_direct_url, stream=True)
    image_size = int(image_content.headers["Content-Length"])

    logger.debug("Writing image file")
    image_file_path = Path(
        f"image_download_{datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')}.jpg"
    )
    progress_bar = tqdm(
        total=image_size, unit="B", unit_scale=True, desc="Writing Process", ascii=False
    )
    with image_file_path.open("wb") as image_file:
        for data_block in image_content.iter_content(BLOCK_SIZE):
            progress_bar.update(len(data_block))
            image_file.write(data_block)
    progress_bar.close()
    logger.success("Successfully downloaded image")


@logger.catch
def download_video(post_content: str = None) -> None:
    """
    Downloads the video from the post.

    Args:
        post_content: the html content extracted by a request to the post's url.

    Returns:
        Nothing, downloads and exits.
    """
    video_direct_url: str = extract_video_direct_link(post_content)

    logger.info("Extracting video content")
    video_content = requests.get(video_direct_url, stream=True)
    video_size = int(video_content.headers["Content-Length"])

    logger.debug("Writing video file")
    video_file_path = Path(
        f"video_download_{datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')}.mp4"
    )
    progress_bar = tqdm(
        total=video_size, unit="B", unit_scale=True, desc="Writing Progress", ascii=False
    )
    with video_file_path.open("wb") as video_file:
        for data_block in video_content.iter_content(BLOCK_SIZE):
            progress_bar.update(len(data_block))
            video_file.write(data_block)
    progress_bar.close()
    logger.success("Successfully downloaded video")


def set_logger_level(log_level: str = "info") -> None:
    """
    Sets the logger level to the one provided at the commandline.
    Default loguru handler will have DEBUG level and ID 0.
    We need to first remove this default handler and add ours with the wanted level.
    Args:
        log_level: string, the default logging level to print out.
    Returns:
        Nothing, acts in place.
    """
    logger.remove(0)
    logger.add(sys.stderr, level=log_level.upper())
