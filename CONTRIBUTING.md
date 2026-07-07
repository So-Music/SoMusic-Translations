# Contributing

Thank you for contributing to **So' Music**!

Whether you're correcting a typo or translating the entire bot into another language, every contribution is appreciated.

## Before you start

The English translation (`en_US.json`) is the reference for every language.

Every locale file must contain exactly the same translation keys.

All translation contributions must be made through the `update-translations` branch:

https://github.com/So-Music/SoMusic-Translations/tree/update-translations

Before creating your Pull Request:

* Create your branch from `update-translations`.
* Open your Pull Request targeting the `update-translations` branch.
* Do not target the `main` branch.

## Rules

### ✅ Translate only the values

Example:

```json
"music.now-playing.title": "Now Playing"
```

↓

```json
"music.now-playing.title": "Lecture en cours"
```

### ❌ Never change translation keys

Incorrect:

```json
"music.playing.title": "Lecture en cours"
```

## Preserve placeholders

Some translations contain placeholders.

Examples:

* `%s`
* `%d`
* `%f`

They **must remain unchanged**.

Correct:

```text
Now playing: %s
```

↓

```text
Lecture en cours : %s
```

Incorrect:

```text
Lecture en cours
```

## Preserve formatting

Do not modify:

* Markdown links
* URLs
* Line breaks (`\n`)
* Discord code blocks
* Inline code
* Emojis
* Discord mentions

Example:

```text
Please join our [Support Server](https://...)
```

↓

```text
Rejoignez notre [serveur de support](https://...)
```

Only the visible text should be translated.

## Pull Requests

Before submitting a Pull Request, make sure that:

* The JSON is valid.
* Every translation key is present.
* No additional keys have been added.
* Placeholders are preserved.
* Only translation files have been modified.
* Your Pull Request targets the `update-translations` branch.

Keep Pull Requests focused on a single language whenever possible.

## Need help?

If you're unsure about a translation, feel free to open an Issue or start a Discussion.

Thank you for helping improve So' Music for users around the world! ❤️
