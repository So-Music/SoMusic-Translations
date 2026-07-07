# So' Music Translations

Official localization repository for **So' Music**, the Discord music bot.

This repository contains the translation files used by the bot. It is maintained with community contributions and synchronized with the private bot repository.

## Overview

Use this repository to:

- Add support for a new language.
- Improve existing translations.
- Fix grammar, spelling, or wording issues.
- Update translations when new bot features are added.

## Repository Structure

```text
langs/
├── en_US.json
├── fr_FR.json
├── de_DE.json
└── ...
```

Each file contains the complete translation set for one locale. The English file, `langs/en_US.json`, is the reference file and defines the required keys.

## Contributing

All community contributions must go through the [`update-translations`](https://github.com/So-Music/SoMusic-Translations/tree/update-translations) branch.

Before opening a pull request:

1. Create your branch from `update-translations`.
2. Open your pull request against `update-translations`.
3. Do not target the `main` branch.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## Adding a Language

1. Copy `langs/en_US.json`.
2. Rename the copy using the appropriate locale code, for example `it_IT.json` or `es_ES.json`.
3. Translate every value.
4. Open a pull request against `update-translations`.

## Translation Guidelines

- Never modify translation keys.
- Translate only the values.
- Preserve placeholders such as `%s`, `%d`, and `%f`.
- Keep Markdown formatting intact.
- Preserve line breaks (`\n`).
- Do not modify URLs.
- Keep emojis and Discord formatting unchanged.

## Automatic Validation

Every pull request is automatically checked to ensure:

- JSON syntax is valid.
- No translation keys are missing.
- No additional translation keys have been added.
- Placeholders are preserved.

Pull requests that fail validation cannot be merged.

## Reporting Issues

Found an incorrect translation?

Open an issue or submit a pull request.

We appreciate every contribution that helps make So' Music available to more communities around the world. ❤️
