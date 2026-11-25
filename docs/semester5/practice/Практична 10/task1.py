from pathlib import Path


def main():
    cwd = Path.cwd()
    script = Path(__file__).resolve()
    script_dir = script.parent
    home = Path.home()

    print(f"cwd:         {cwd}")
    print(f"script:      {script}")
    print(f"script dir:  {script_dir}")
    print(f"home:        {home}")

    data_dir = script_dir / "data"
    reports_dir = script_dir / "reports"
    backups_dir = script_dir / "backups"

    data_dir.mkdir(exist_ok=True)
    reports_dir.mkdir(exist_ok=True)
    backups_dir.mkdir(exist_ok=True)

    profile = data_dir / "profile.txt"

    profile.write_text(
        "name: Illia\n"
        "surname: Basalukk\n"
        "group: IT-31\n"
        "year: 2009\n"
        "language: Python\n",
        encoding="utf-8"
    )

    print()
    print(f"profile path: {profile.resolve()}")
    print(f"relative:     {profile.relative_to(script_dir)}")
    print(f"name:         {profile.name}")
    print(f"stem:         {profile.stem}")
    print(f"suffix:       {profile.suffix}")
    print(f"parent:       {profile.parent.name}")
    print(f"size:         {profile.stat().st_size} bytes")

    print()
    print("project tree:")

    for directory in sorted(script_dir.iterdir()):
        if directory.is_dir():
            print(f"  {directory.name}/")

            for item in sorted(directory.iterdir()):
                if item.is_file():
                    print(f"    {item.name}")


if __name__ == "__main__":
    main()