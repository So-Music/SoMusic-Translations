# So' Music Translations

Official localization repository for **So' Music**.

This repository contains all translation files used by the So' Music Discord bot. It is maintained by the community and synchronized with the private bot repository.

## 🌍 Contributing

Everyone is welcome to contribute.

You can help by:

* Translating So' Music into a new language.
* Improving existing translations.
* Fixing grammar or spelling mistakes.
* Updating translations when new features are added.

Please read the **CONTRIBUTING.md** file before opening a Pull Request.

## Repository structure

```text
langs/
├── en_US.json
├── fr_FR.json
├── de_DE.json
├── ...
```

Each file contains the complete translations for one locale.

## Adding a language

1. Copy `en_US.json`.
2. Rename it using the appropriate locale code (for example `it_IT.json` or `es_ES.json`).
3. Translate every value.
4. Open a Pull Request.

## Translation guidelines

* Never modify translation keys.
* Translate only the values.
* Preserve placeholders such as `%s`, `%d`, `%f`, etc.
* Keep Markdown formatting intact.
* Preserve line breaks (`\n`).
* Do not modify URLs.
* Keep emojis and Discord formatting.

## Automatic validation

Every Pull Request is automatically checked to ensure:

* Valid JSON syntax.
* No missing translation keys.
* No additional translation keys.
* Placeholders are preserved.

Pull Requests that fail validation cannot be merged.

## Reporting issues

Found an incorrect translation?

Open an Issue or submit a Pull Request.

We appreciate every contribution that helps make So' Music available to more communities around the world. ❤️
