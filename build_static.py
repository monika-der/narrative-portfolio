from pathlib import Path
import shutil

from app import app, PROJECTS

OUTPUT_DIR = Path("_site")


def write_page(path: str, content: str) -> None:
    output_path = OUTPUT_DIR / path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")


def check_response(response, path: str) -> None:
    if response.status_code != 200:
        raise RuntimeError(
            f"Failed to render {path}: HTTP {response.status_code}"
        )


def build():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    OUTPUT_DIR.mkdir()

    # Copy CSS, JavaScript and interactive projects
    shutil.copytree(
        "static",
        OUTPUT_DIR / "static",
        dirs_exist_ok=True,
    )

    with app.test_client() as client:
        # Homepage
        response = client.get("/")
        check_response(response, "/")

        write_page(
            "index.html",
            response.get_data(as_text=True),
        )

        # Project pages
        for slug in PROJECTS:
            path = f"/project/{slug}"
            response = client.get(path)
            check_response(response, path)

            write_page(
                f"project/{slug}/index.html",
                response.get_data(as_text=True),
            )

    # Prevent GitHub Pages from processing the site with Jekyll
    (OUTPUT_DIR / ".nojekyll").touch()

    print()
    print("✓ Static portfolio built successfully")
    print(f"✓ Output: {OUTPUT_DIR.resolve()}")
    print()
    print("Generated pages:")
    print("  /")

    for slug in PROJECTS:
        print(f"  /project/{slug}/")


if __name__ == "__main__":
    build()