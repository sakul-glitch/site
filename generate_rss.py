from pathlib import Path
import xml.etree.ElementTree as ET

SITE_URL = "https://site.besoffener-kaese.workers.dev"
OUTPUT_PATH = Path("rss.xml")

posts = [
    {
        "title": "Erster Beitrag",
        "slug": "erster-beitrag",
        "date": "Mon, 28 Oct 2026 12:00:00 GMT",
        "description": "Beschreibung des ersten Beitrags.",
    },
    {
        "title": "Zweiter Beitrag",
        "slug": "zweiter-beitrag",
        "date": "Tue, 29 Oct 2026 12:00:00 GMT",
        "description": "Beschreibung des zweiten Beitrags.",
    },
]

rss = ET.Element("rss", {"version": "2.0"})
channel = ET.SubElement(rss, "channel")
ET.SubElement(channel, "title").text = "Besoffener Käse Blog"
ET.SubElement(channel, "link").text = SITE_URL + "/"
ET.SubElement(channel, "description").text = "Neueste Beiträge"
ET.SubElement(channel, "language").text = "de-de"

for post in posts:
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = post["title"]
    link = SITE_URL + "/blog/" + post["slug"]
    ET.SubElement(item, "link").text = link
    ET.SubElement(item, "guid").text = link
    ET.SubElement(item, "pubDate").text = post["date"]
    ET.SubElement(item, "description").text = post["description"]

ET.ElementTree(rss).write(OUTPUT_PATH, encoding="utf-8", xml_declaration=True)
print(f"Feed erstellt: {OUTPUT_PATH.resolve()}")
