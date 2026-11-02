      - name: Install Android SDK packages and configure Buildozer
        shell: bash
        run: |
          SDKMANAGER="$(command -v sdkmanager)"
          SDKMANAGER_REAL="$(readlink -f "$SDKMANAGER")"
          SDK_ROOT="${ANDROID_HOME:-${ANDROID_SDK_ROOT:-}}"

          if [[ -z "$SDK_ROOT" ]]; then
            SDK_ROOT="$(dirname "$(dirname "$(dirname "$(dirname "$SDKMANAGER_REAL")")")")"
          fi

          echo "ANDROID_HOME=$SDK_ROOT" >> "$GITHUB_ENV"
          echo "ANDROID_SDK_ROOT=$SDK_ROOT" >> "$GITHUB_ENV"

          # Buildozer expects sdkmanager at the legacy tools/bin location.
          mkdir -p "$SDK_ROOT/tools/bin"
          ln -sf "$SDKMANAGER_REAL" "$SDK_ROOT/tools/bin/sdkmanager"

          "$SDKMANAGER" --install \
            "platform-tools" \
            "platforms;android-33" \
            "build-tools;33.0.2"
