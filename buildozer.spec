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
# Add other dependencies here if needed (e.g., requirements = python3,kivy,requests)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0


#
# Android specific configuration
#

# (int) Target Android API, matching platforms;android-33 in your workflow
android.api = 33

# (int) Minimum API level supported
android.minapi = 24

# (str) Pin a stable NDK version to prevent build hangs
android.ndk = 25b

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

# (list) Supported Architectures
android.archs = arm64-v8a


#
# Buildozer Global Settings
#

[buildozer]

# (int) Log level (2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# (str) Path to build output, matching path: bin/*.apk in your workflow
bin_dir = ./bin


