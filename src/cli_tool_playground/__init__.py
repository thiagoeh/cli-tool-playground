import click
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from loguru import logger


@click.command
def main() -> None:
    logger.debug("Initializing Spotipy")
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id="dd8ea0543cfc47e591a32204fc4418f3",
            client_secret="29fda597b6044cf5b91c2eb1689e6b9b",
            redirect_uri="http://127.0.0.1:9090",
            scope="user-read-recently-played",
        )
    )

    results = sp.current_user_recently_played(limit=20)  # Fetch up to 50 tracks
    for item in results["items"]:
        track = item["track"]
        played_at = item["played_at"]
        print(f"{track['name']} by {track['artists'][0]['name']} at {played_at}")


if __name__ == "__main__":
    main()
