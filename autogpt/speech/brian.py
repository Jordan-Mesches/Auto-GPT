""" Brian speech module for autogpt """
import os
from playsound import playsound

from autogpt.speech.base import VoiceBase
from security import safe_requests


class BrianSpeech(VoiceBase):
    """Brian speech module for autogpt"""

    def _setup(self) -> None:
        """Setup the voices, API key, etc."""
        pass

    def _speech(self, text: str, _: int = 0) -> bool:
        """Speak text using Brian with the streamelements API

        Args:
            text (str): The text to speak

        Returns:
            bool: True if the request was successful, False otherwise
        """
        tts_url = (
            f"https://api.streamelements.com/kappa/v2/speech?voice=Brian&text={text}"
        )
        response = safe_requests.get(tts_url)

        if response.status_code == 200:
            with open("speech.mp3", "wb") as f:
                f.write(response.content)
            playsound("speech.mp3")
            os.remove("speech.mp3")
            return True
        else:
            print("Request failed with status code:", response.status_code)
            print("Response content:", response.content)
            return False
