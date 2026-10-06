from pathlib import Path
import shutil

from app import app, PROJECTS


OUTPUT_DIR = Path("_site")
BASE_PATH = "/narrative-portfolio"


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

    shutil.copytree(
        "static",
        OUTPUT_DIR / "static",
        dirs_exist_ok=True,
    )

    with app.test_request_context(
        "/",
        environ_base={
            "SCRIPT_NAME": BASE_PATH
        }
    ):
        # Homepage
        html = app.jinja_env.get_template(
            "index.html"
        ).render(
            projects=PROJECTS
        )

        write_page(
            "index.html",
            html,
        )

        # Project pages
        for slug, project in PROJECTS.items():
            html = app.jinja_env.get_template(
                "projects/project.html"
            ).render(
                project=project,
                slug=slug,
            )

            write_page(
                f"project/{slug}/index.html",
                html,
            )

    (OUTPUT_DIR / ".nojekyll").touch()

    print()
    print("✓ Static portfolio built successfully")
    print(f"✓ Output: {OUTPUT_DIR.resolve()}")
    print()
    print("Generated pages:")
    print(f"  {BASE_PATH}/")

    for slug in PROJECTS:
        print(f"  {BASE_PATH}/project/{slug}/")


if __name__ == "__main__":
    build()