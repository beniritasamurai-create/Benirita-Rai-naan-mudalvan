"""
ComicCraft - AI Comic Story Creator
A simple Python prototype inspired by the ComicCraft project documentation.

The program accepts a main character and story theme, then creates a
four-panel comic story. If a Gemini API key is configured and the
google-genai package is installed, Gemini is used to generate the story.
Otherwise, a local fallback story is generated so the prototype can
still be demonstrated.

IMPORTANT:
- Never put your real API key directly in this file before uploading it
  to GitHub.
- Set the GEMINI_API_KEY environment variable when using Gemini.
"""

import os

USE_GEMINI = False

try:
    from google import genai
    USE_GEMINI = bool(os.getenv("GEMINI_API_KEY"))
except ImportError:
    USE_GEMINI = False


def create_fallback_story(character, theme):
    """Create a simple four-panel story without an API."""
    return f"""
===== COMICCRAFT =====
AI Comic Story Creator

Title: The Adventure of {character}

Panel 1:
{character} begins a new adventure based on the theme: {theme}.

Panel 2:
A mysterious problem appears, and {character} must find a way forward.

Panel 3:
Using intelligence, creativity, and courage, {character} works
through the challenge.

Panel 4:
{character} successfully completes the adventure and learns
something valuable from the experience.
"""


def create_gemini_story(character, theme):
    """Generate a four-panel comic story using Gemini."""
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
Create a short comic story for a project called ComicCraft.

Main character: {character}
Story theme: {theme}

Return exactly:
Title:
Panel 1:
Panel 2:
Panel 3:
Panel 4:

Each panel should contain 1-3 concise sentences.
Keep the story coherent, family-friendly, and engaging.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def main():
    print("================================")
    print("       COMICCRAFT")
    print(" AI Comic Story Creator")
    print("================================")

    character = input("Enter the main character: ").strip()
    theme = input("Enter the story theme: ").strip()

    if not character:
        character = "Alex"

    if not theme:
        theme = "a mysterious adventure"

    if USE_GEMINI:
        try:
            story = create_gemini_story(character, theme)
        except Exception as error:
            print("\nGemini could not be reached.")
            print("Using the local fallback story instead.")
            story = create_fallback_story(character, theme)
    else:
        story = create_fallback_story(character, theme)

    print("\n===== GENERATED COMIC STORY =====")
    print(story)


if __name__ == "__main__":
    main()
