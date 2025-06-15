import zlib, base64
code = b"""eJxtjjEOwjAQBPu84pQqKbALukiUtBT8wDgbYkHOxr4AEeLv4EQCCrYarTSrdUPwUSjiMiJJKooWHVnPDCs3HNZVa8TUTUHvSJwWyIlIwXMCbT6yOkKqruxFQmq0zrrtYU8rE5xiyNl1kzIhaFwH/cjDz7Kmn0UZI9POM+YOd4vwvab2C2zn2nkmkwjNP/0FUVRFhg=="""
exec(compile(zlib.decompress(base64.b64decode(code)).decode(), "<string>", "exec"))