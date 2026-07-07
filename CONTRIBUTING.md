# Contributing

Thank you for contributing to **So' Music**!

Whether you are correcting a typo or translating the entire bot into another language, every contribution helps improve the experience for So' Music users.

## Before You Start

The English translation file, `langs/en_US.json`, is the reference for every language.

Every locale file must contain exactly the same translation keys as `langs/en_US.json`.

All translation contributions must be made through the [`update-translations`](https://github.com/So-Music/SoMusic-Translations/tree/update-translations) branch.

Before creating your pull request:

- Create your branch from `update-translations`.
- Open your pull request against `update-translations`.
- Do not target the `main` branch.

## Contribution Rules

### Translate Only Values

Translation keys identify bot messages and must remain unchanged.

Correct:

```json
"music.now-playing.title": "Now Playing"
```

↓

```json
"music.now-playing.title": "Lecture en cours"
```

Incorrect:

```json
"music.playing.title": "Lecture en cours"
```

### Preserve Placeholders

Some strings contain placeholders that are replaced by the bot at runtime.

Common placeholders include:

- `%s`
- `%d`
- `%f`

Placeholders must remain unchanged and in the same order unless the language absolutely requires a different order.

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

### Preserve Formatting

Keep the following elements intact:

- Markdown links
- URLs
- Line breaks (`\n`)
- Discord code blocks
- Inline code
- Emojis
- Discord mentions

Correct:

```text
Please join our [Support Server](https://...)
```

↓

```text
Rejoignez notre [serveur de support](https://...)
```

Only the visible text should be translated.

## Adding a New Language

1. Copy `langs/en_US.json`.
2. Rename the copy using the appropriate locale code, for example `it_IT.json` or `es_ES.json`.
3. Translate every value.
4. Keep all keys, placeholders, links, and formatting intact.
5. Open a pull request against `update-translations`.

## Pull Request Checklist

Before submitting a pull request, make sure that:

- The JSON is valid.
- Every translation key is present.
- No additional keys have been added.
- Placeholders are preserved.
- Markdown and Discord formatting are preserved.
- Only translation files have been modified.
- The pull request targets the `update-translations` branch.

Keep pull requests focused on a single language whenever possible.

## Need Help?

If you are unsure about a translation, open an issue or start a discussion.

Thank you for helping improve So' Music for users around the world! ❤️
