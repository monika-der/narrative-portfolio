from flask import Flask, render_template, abort

app = Flask(__name__)

app.config["APPLICATION_ROOT"] = "/narrative-portfolio"

PROJECTS = {
    "the-arrow": {
        "number": "01", "title": "The Arrow",
        "subtitle": "A myth told by the one who was holding the bow.",
        "type": "Short fiction",
        "focus": ["Character voice", "Myth retelling", "Emotional storytelling"],
        "intro": "A short story inspired by Medea, retold through the eyes of Eros — a god forced to confront the consequences of what his arrows set in motion.",
        "sections": [
            ("The premise", "What happens when a god of desire is forced to look at the consequences of his own work? The story uses a familiar myth as a starting point, then moves the camera away from its centre."),
            ("Narrative approach", "The story is built around an intimate first-person voice. Eros becomes both witness and participant, allowing the reader to experience an ancient tragedy through a perspective that is usually absent from it."),
            ("What I explored", "Character voice · perspective · subtext · mythological adaptation · emotional stakes")],
        "artifact": "story"
    },
    "two-sides": {
        "number": "02",
        "title": "Two Sides of the Same Night",
        "subtitle": "Two vampires. One dead woman. And a truth neither of them tells in full.",
        "type": "Interactive fiction / Twine",
        "focus": ["Dual perspective", "Branching investigation", "Unreliable narration"],
        "intro": "An interactive mystery about the death of Claudette, a human who uncovered something Helix Ward was willing to kill to protect. By questioning two vampires who knew her, the player pieces together what she discovered, why she became a threat, and how two very different acts of betrayal led to the same night.",
        "sections": [
            ("The premise", "The investigation is built around perspective and information. The player chooses who to question, which leads to follow, and when to stop digging. Some choices reveal the central mystery, while others uncover the relationships and memories surrounding it."),
            ("Narrative approach", "Andrew and Samuel remember the same woman very differently. Andrew is open and emotional but unable to confront his own role in her death. Samuel is guarded and suspicious, yet often more truthful than he appears. Contradictions, omissions and changes in perspective become clues."),
            ("What I explored", "Branching narrative · dialogue design · unreliable narration · environmental storytelling · information control · player-led investigation")
        ],
        "artifact": "twine"
    },
}

@app.route("/")
def index():
    return render_template("index.html", projects=PROJECTS)

@app.route("/project/<slug>")
def project(slug):
    data = PROJECTS.get(slug)
    if not data:
        abort(404)
    return render_template("projects/project.html", project=data, slug=slug)

if __name__ == "__main__":
    app.run(debug=True)
