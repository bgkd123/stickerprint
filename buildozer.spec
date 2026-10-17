[app]
title = Sticker Print
package.name = stickerprint
package.domain = org.sanil

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,mp3
source.include_patterns = assets/*,images/*

version = 1.0

# 'android' removed to fix 403 error
requirements = python3,kivy==2.3.0,pillow,reportlab,plyer,pyjnius

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.accept_sdk_license = True

android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, READ_MEDIA_IMAGES

android.archs = arm64-v8a
android.allow_backup = True

# Changed to develop to fix download issues
p4a.branch = develop

android.logcat_filters = *:S python:D
