import os
import json

# --- DUMMY DATA ---
# In a real scenario, this data would be scraped from Wattpad.
DUMMY_STORIES = [
    {
        "id": "1001", "title": "The Last Technomancer", "author": "Alex Ray",
        "cover_url": "https://placehold.co/300x450/2E2A4F/FFF?text=The+Last\\nTechnomancer",
        "description": "In a world where magic has faded, a young engineer discovers she can talk to machines.",
        "tags": ["sci-fi", "magic", "dystopian"],
        "chapters": [ {"id": "c101", "title": "Part 1: The Ghost"}, {"id": "c102", "title": "Part 2: The Signal"} ]
    },
    {
        "id": "1002", "title": "Ocean's Echo", "author": "Maria Garcia",
        "cover_url": "https://placehold.co/300x450/007991/FFF?text=Ocean's\\nEcho",
        "description": "A marine biologist finds a lost city, but its secrets were meant to stay buried.",
        "tags": ["adventure", "mystery", "fantasy"],
        "chapters": [ {"id": "c201", "title": "Chapter I: The Dive"}, {"id": "c202", "title": "Chapter II: The Murmur"} ]
    }
]

DUMMY_CHAPTERS_CONTENT = {
    "c101": "<p>The old workshop hummed, not with electricity, but with something else. Something ancient.</p>",
    "c102": "<p>The static on the radio wasn't static. It was a voice, and it knew her name.</p>",
    "c201": "<p>The submersible descended into the crushing dark, its lights cutting through the gloom to reveal impossible architecture.</p>",
    "c202": "<p>A low, resonant hum vibrated through the hull. It was the sound of a sleeping giant.</p>"
}
# --- END DUMMY DATA ---

def create_dirs():
    """Create necessary data directories."""
    os.makedirs("data/stories", exist_ok=True)
    os.makedirs("data/chapters", exist_ok=True)

def write_json(data, path):
    """Write dictionary to a JSON file."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def run_scraper():
    """Main function to simulate scraping and generate files."""
    create_dirs()
    print("🤖 Starting scraper simulation...")

    # 1. Scrape "home page" stories
    home_data = [{"id": s["id"], "title": s["title"], "cover_url": s["cover_url"]} for s in DUMMY_STORIES]
    write_json(home_data, "data/home.json")
    print(" ✓ Created data/home.json")

    # 2. Scrape individual story and chapter details
    search_index = []
    for story in DUMMY_STORIES:
        # Create story detail file
        story_detail = {k: v for k, v in story.items()}
        write_json(story_detail, f"data/stories/{story['id']}.json")

        # Create chapter files for this story
        for chapter in story["chapters"]:
            chapter_content = {"title": chapter["title"], "content": DUMMY_CHAPTERS_CONTENT.get(chapter["id"], "")}
            write_json(chapter_content, f"data/chapters/{chapter['id']}.json")
        
        # Add to search index
        search_index.append({"id": story["id"], "title": story["title"], "author": story["author"], "tags": story["tags"]})

    print(f" ✓ Created {len(DUMMY_STORIES)} story files and their chapter files.")
    
    # 3. Create the master search index
    write_json(search_index, "data/search_index.json")
    print(" ✓ Created data/search_index.json")
    print("✅ Scraper simulation finished!")


if __name__ == "__main__":
    run_scraper()
