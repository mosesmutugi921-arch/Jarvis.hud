name: Build APK

on:
  push:
  pull_request:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  build:
    runs-on: ubuntu-22.04
    timeout-minutes: 60

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip

      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "17"

      - name: Set up Android SDK
        uses: android-actions/setup-android@v4
        with:
          accept-android-sdk-licenses: true
          packages: ""

      - name: Install Android SDK packages
        run: |
          sdkmanager --install \
            "platform-tools" \
            "platforms;android-33" \
            "build-tools;33.0.2"

      - name: Check Buildozer configuration
        run: |
          python - <<'PY'
          from configparser import ConfigParser
          from pathlib import Path

          path = Path("buildozer.spec")
          config = ConfigParser()

          if not path.is_file():
              raise SystemExit("buildozer.spec is missing")

          if not config.read(path):
              raise SystemExit("Could not read buildozer.spec")

          if not config.has_section("app"):
              raise SystemExit(
                  "buildozer.spec must contain an [app] section. "
                  "Do not put GitHub Actions YAML in this file."
              )

          print("buildozer.spec is readable and contains [app].")
          PY

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y --no-install-recommends \
            autoconf \
            build-essential \
            cmake \
            git \
            libffi-dev \
            libltdl-dev \
            libncurses5-dev \
            libncursesw5-dev \
            libssl-dev \
            libsqlite3-dev \
            pkg-config \
            unzip \
            zip \
            zlib1g-dev

      - name: Install Buildozer and Python build dependencies
        run: |
          python -m pip install --upgrade pip setuptools wheel
          python -m pip install "Cython==0.29.36" buildozer

      - name: Build debug APK
        run: buildozer -v android debug

      - name: Upload APK artifact
        uses: actions/upload-artifact@v4
        with:
          name: jarvis-debug-apk
          path: bin/*.apk
          if-no-files-found: error
          retention-days: 14
