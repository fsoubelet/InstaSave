"""
Running directly from python module.
"""
import requests
import typer

from instasave.save_post import (
    determine_media_type,
    download_image,
    download_video,
    is_connected,
    is_instagram_domain,
    set_logger_level,
)

app = typer.Typer()


@app.command()
def save(
    url: str = typer.Argument(
        None, help="Link to the Instagram post you want to download the content of."
    ),
    log_level: str = typer.Option(
        "info",
        help="The base console logging level. Can be 'debug', 'info', 'warning' and 'error'.",
    ),
) -> None:
    """Download media from Instagram posts."""
    set_logger_level(log_level)

    if not is_connected():
        raise typer.Exit(code=1)

    if not is_instagram_domain(url):
        logger.error("The entered test_url does not link to a valid Instagram post")
        raise typer.Exit(code=1)

    media_content = requests.get(url).content.decode("utf-8")
    media_type = determine_media_type(media_content)

    if media_type == "image":
        download_image(media_content)

    elif media_type == "video":
        download_video(media_content)

    else:
        logger.error("Media content type could not be identified as an image or a video")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
