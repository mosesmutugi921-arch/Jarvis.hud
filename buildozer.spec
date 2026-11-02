[app]

# (str) Title of your application
title = Jarvis

# (str) Package name
package.name = jarvis

# (str) Package domain (needed for android packaging)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (empty includes all)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (str) Application version
version = 0.1

# (list) Application requirements
# Comma-separated list of packages or recipes (e.g. requirements = python3,kivy)
requirements = python3,kivy

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0


#
# Android specific configuration
#

# (int) Target Android API level matching your GitHub workflow (android-33)
android.api = 33

# (int) Minimum API level supported (Android 7.0+)
android.minapi = 24

# (str) Android NDK version (leave blank for automatic match with API 33)
# android.ndk = 25b

# (bool) Automatically accept SDK licenses (already configured in workflow)
android.accept_sdk_license = True

# (list) Supported Architectures for modern Android devices
android.archs = arm64-v8a, armeabi-v7a

# (list) Permissions required by the app (add if your app uses internet, storage, etc.)
# android.permissions = INTERNET


#
# Buildozer Global Settings
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# (str) Path to build output (matches path: bin/*.apk in your workflow)
bin_dir = ./bin

