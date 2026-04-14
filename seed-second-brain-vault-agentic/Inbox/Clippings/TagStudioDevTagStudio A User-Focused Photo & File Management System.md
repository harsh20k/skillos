---
title: "TagStudioDev/TagStudio: A User-Focused Photo & File Management System"
source: https://github.com/TagStudioDev/TagStudio?tab=readme-ov-file
author:
  - "[[GitHub]]"
published: 
created: 2024-12-12
description: A User-Focused Photo & File Management System. Contribute to TagStudioDev/TagStudio development by creating an account on GitHub.
tags:
  - "#inbox/fleetingNotes/devIdeas"
  - "#inbox/mediaNotes"
dg-publish: true
---
## TagStudio: A User-Focused Document Management System[![Translation](https://camo.githubusercontent.com/45e19234beb7858bc61ae397d899e157ecce8bec4ac21c8a2bf2341dc83edf20/68747470733a2f2f686f737465642e7765626c6174652e6f72672f7769646765742f74616773747564696f2f737472696e67732f7376672d62616467652e737667)](https://hosted.weblate.org/projects/tagstudio/strings/) [![PyTest](https://github.com/TagStudioDev/TagStudio/actions/workflows/pytest.yaml/badge.svg)](https://github.com/TagStudioDev/TagStudio/actions/workflows/pytest.yaml) [![MyPy](https://github.com/TagStudioDev/TagStudio/actions/workflows/mypy.yaml/badge.svg)](https://github.com/TagStudioDev/TagStudio/actions/workflows/mypy.yaml) [![Ruff](https://github.com/TagStudioDev/TagStudio/actions/workflows/ruff.yaml/badge.svg)](https://github.com/TagStudioDev/TagStudio/actions/workflows/ruff.yaml) [![Downloads](https://camo.githubusercontent.com/e4946cec45a1515d166f6b08db8c4a3ddfff012cb5dece7b5da6cc7304673ac3/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f646f776e6c6f6164732f54616753747564696f4465762f54616753747564696f2f746f74616c2e7376673f6d61784167653d32353932303031)](https://github.com/TagStudioDev/TagStudio/releases)

[![](https://github.com/TagStudioDev/TagStudio/raw/main/docs/assets/github_header.png)](https://github.com/TagStudioDev/TagStudio/blob/main/docs/assets/github_header.png)

TagStudio is a photo & file organization application with an underlying tag-based system that focuses on giving freedom and flexibility to the user. No proprietary programs or formats, no sea of sidecar files, and no complete upheaval of your filesystem structure. **Read the documentation and more at [docs.tagstud.io](https://docs.tagstud.io/)!**

Caution

As of Pull Request [#332](https://github.com/TagStudioDev/TagStudio/pull/332) (SQLite Migration) the `main` branch will be an open test bed to get full JSON to SQL parity operational. This notice will be removed once parity between v9.4 and v9.5 is reached.

For the most recent stable feature release branch, see the [`Alpha-v9.4`](https://github.com/TagStudioDev/TagStudio/tree/Alpha-v9.4) branch. These v9.4 specific features are currently being backported to the SQL-ized `main` branch. [Feel free to help!](https://github.com/TagStudioDev/TagStudio/blob/main/CONTRIBUTING.md)

Note

This project is still in an early state. There are many missing optimizations and QoL features, as well as the presence of general quirks and occasional jankiness. Making frequent backups of your library save data is **always** important, regardless of what state the program is in.

With this in mind, TagStudio will *NOT:*

- Touch, move, or mess with your files in any way *(unless explicitly using the "Delete File(s)" feature, which is locked behind a confirmation dialog)*.
- Ask you to recreate your tags or libraries after new releases. It's our highest priority to ensure that your data safely and smoothly transfers over to newer versions.
- Cause you to suddenly be able to recall your 10 trillion downloaded images that you probably haven't even seen firsthand before. You're in control here, and even tools out there that use machine learning still needed to be verified by human eyes before being deemed accurate.

[![TagStudio Screenshot](https://github.com/TagStudioDev/TagStudio/raw/main/docs/assets/screenshot.jpg)](https://github.com/TagStudioDev/TagStudio/blob/main/docs/assets/screenshot.jpg)

*TagStudio Alpha v9.4.2 running on Windows 10.*

## Contents- [Goals](https://github.com/TagStudioDev/?tab=readme-ov-file#goals)
- [Priorities](https://github.com/TagStudioDev/?tab=readme-ov-file#priorities)
- [Current Features](https://github.com/TagStudioDev/?tab=readme-ov-file#current-features)
- [Contributing](https://github.com/TagStudioDev/?tab=readme-ov-file#contributing)
- [Installation](https://github.com/TagStudioDev/?tab=readme-ov-file#installation)
- [Usage](https://github.com/TagStudioDev/?tab=readme-ov-file#usage)
- [FAQ](https://github.com/TagStudioDev/?tab=readme-ov-file#faq)

## Goals- To achieve a portable, private, extensible, open-format, and feature-rich system of organizing and rediscovering files.
- To provide powerful methods for organization, notably the concept of tag inheritance, or “taggable tags” *(and in the near future, the combination of composition-based tags).*
- To create an implementation of such a system that is resilient against a user’s actions outside the program (modifying, moving, or renaming files) while also not burdening the user with mandatory sidecar files or requiring them to change their existing file structures and workflows.
- To support a wide range of users spanning across different platforms, multi-user setups, and those with large (several terabyte) libraries.
- To make the darn thing look like nice, too. It’s 2024, not 1994.

## Priorities1. **The concept.** Even if TagStudio as an application fails, I’d hope that the idea lives on in a superior project. The [goals](https://github.com/TagStudioDev/?tab=readme-ov-file#goals) outlined above don’t reference TagStudio once - *TagStudio* is what references the *goals.*
2. **The system.** Frontends and implementations can vary, as they should. The core underlying metadata management system is what should be interoperable between different frontends, programs, and operating systems. A standard implementation for this should settle as development continues. This opens up the doors for improved and varied clients, integration with third-party applications, and more.
3. **The application.** If nothing else, TagStudio the application serves as the first (and so far only) implementation for this system of metadata management. This has the responsibility of doing the idea justice and showing just what’s possible when it comes to user file management.
4. (The name.) I think it’s fine for an app or client, but it doesn’t really make sense for a system or standard. I suppose this will evolve with time...

## ContributingIf you're interested in contributing to TagStudio, please take a look at the [contribution guidelines](https://github.com/TagStudioDev/TagStudio/blob/main/CONTRIBUTING.md) for how to get started!

Translation hosting generously provided by [Weblate](https://weblate.org/en/). Check out our project page to help translate TagStudio!

## Current Features### Libraries- Create libraries/vaults centered around a system directory. Libraries contain a series of entries: the representations of your files combined with metadata fields. Each entry represents a file in your library’s directory, and is linked to its location.
- Address moved, deleted, or otherwise "unlinked" files by using the "Fix Unlinked Entries" option in the Tools menu.

### Metadata + Tagging- Add metadata to your library entries, including:
- Name, Author, Artist (Single-Line Text Fields)
- Description, Notes (Multiline Text Fields)
- Tags, Meta Tags, Content Tags (Tag Boxes)
- Create rich tags composed of a name, a list of aliases, and a list of “parent tags” - being tags in which these tags inherit values from.
- Copy and paste tags and fields across file entries
- Generate tags from your existing folder structure with the "Folders to Tags" macro (NOTE: these tags do NOT sync with folders after they are created)

### Search- Search for entries based on tags, ~~metadata~~ (TBA), or filenames/filetypes (using `filename: <query>`).
- Special search conditions for entries that are: `untagged` and `empty`.

### File Entries- All\* file types are supported in TagStudio libraries - just not all have dedicated thumbnail support.
- Preview most image file types, animated GIFs, videos, plain text documents, audio files\*\*, Blender projects, and more!
- Open files or file locations by right-clicking on thumbnails and previews and selecting the respective context menu options. You can also click on the preview panel image to open the file, and click the file path label to open its location.
- Delete files from both your library and drive by right-clicking the thumbnail(s) and selecting the "Move to Trash"/"Move to Recycle Bin" option.

> *\* Weird files with no extension or files such as ".\_DS\_Store" currently have limited support.*
> 
> *\*\* Audio playback coming in v9.5*

Note

For more information on the project itself, please see the [FAQ](https://github.com/TagStudioDev/?tab=readme-ov-file#faq) section as well as the [documentation](https://docs.tagstud.io/).

## InstallationTo download TagStudio, visit the [Releases](https://github.com/TagStudioDev/TagStudio/releases) section of the GitHub repository and download the latest release for your system under the "Assets" section. TagStudio is available for **Windows**, **macOS** *(Apple Silicon & Intel)*, and **Linux**. Windows and Linux builds are also available in portable versions if you want a more self-contained executable to move around.

**We do not currently publish TagStudio to any package managers. Any TagStudio distributions outside of the GitHub releases page are *unofficial* and not maintained by us.** Installation support will not be given to users installing from unofficial sources. Use these versions at your own risk.

Important

On macOS, you may be met with a message saying *""TagStudio" can't be opened because Apple cannot check it for malicious software."* If you encounter this, then you'll need to go to the "Settings" app, navigate to "Privacy & Security", and scroll down to a section that says *""TagStudio" was blocked from use because it is not from an identified developer."* Click the "Open Anyway" button to allow TagStudio to run. You should only have to do this once after downloading the application.

### Third-Party Dependencies- For video thumbnails and playback, you'll also need [FFmpeg](https://ffmpeg.org/download.html) installed on your system.

### Optional ArgumentsArguments available to pass to the program, either via the command line or a shortcut.

> `--open <path>` / `-o <path>` Path to a TagStudio Library folder to open on start.
> 
> `--config-file <path>` / `-c <path>` Path to the TagStudio config file to load.

## Usage### Creating/Opening a LibraryWith TagStudio opened, start by creating a new library or opening an existing one using File -> Open/Create Library from the menu bar. TagStudio will automatically create a new library from the chosen directory if one does not already exist. Upon creating a new library, TagStudio will automatically scan your folders for files and add those to your library (no files are moved during this process!).

### Refreshing the LibraryIn order to scan for new files or file changes, you’ll need to manually go to File -> Refresh Directories.

Note

In the future, library refreshing will also be automatically done in the background, or additionally on app startup.

### Adding Metadata to EntriesTo add a metadata field to a file entry, start by clicking the “Add Field” button under the file preview in the right-hand preview panel. From the dropdown menu, select the type of metadata field you’d like to add to the entry.

### Editing Metadata Fields#### Text Line / Text BoxHover over the field and click the pencil icon. From there, add or edit text in the dialog box popup.

#### Tag BoxClick the “+” button at the end of the Tags list, and search for tags to add inside the new dialog popup. Click the “+” button next to whichever tags you want to add. Alternatively, after you search for a tag, press the Enter/Return key to add the add the first item in the list. Press Enter/Return once more to close the dialog box

Warning

Keyboard control and navigation is currently *very* buggy, but will be improved in future versions.

### Creating TagsTo create a new tag, click on Edit -> New Tag from the menu bar. From there, enter a tag name, shorthand name, any tag aliases separated by newlines, any subtags, and an optional color.

- The tag **shorthand** is a type of alias that displays in situations when screen space is more valuable (ex. as a subtag for other tags).
- **Aliases** are alternate names for a tag. These let you search for terms other than the exact tag name in order to find the tag again.
- **Subtags** are tags in which this tag is a child tag of. In other words, tags under this section are parents of this tag. For example, if you had a tag for a character from a show, you would make the show a subtag of this character. This would display as “Character (Show)” in most areas of the app. The first tag in this list is used as the tag shown in parentheses for specification.
- The **color** dropdown lets you select an optional color for this tag to display as.

### Editing TagsTo edit a tag, right-click the tag in the tag field of the preview pane and select “Edit Tag”

### Relinking Renamed/Moved FilesInevitably, some of the files inside your library will be renamed, moved, or deleted. If a file has been renamed or moved, TagStudio will display the thumbnail as a red tag with a cross through it *(this icon is also used for items with broken thumbnails).* To relink moved files or delete these entries, go to Tools -> Manage Unlinked Entries. Click the “Refresh” button to scan your library for unlinked entries. Once complete, you can attempt to “Search & Relink” any unlinked entries to their respective files, or “Delete Unlinked Entries” in the event the original files have been deleted and you no longer wish to keep their metadata entries inside your library.

Warning

There is currently no method to relink entries to files that have been renamed - only moved or deleted. This is a top priority for future releases.

Warning

If multiple matches for a moved file are found (matches are currently defined as files with a matching filename as the original), TagStudio will currently ignore the match groups. Adding a GUI for manual selection, as well as smarter automated relinking, are top priorities for future versions.

### Saving the LibraryLibraries are saved upon exiting the program. To manually save, select File -> Save Library from the menu bar. To save a backup of your library, select File -> Save Library Backup from the menu bar. Automatic backups are created when loading a library, and are automatically loaded from in the event of a crash or unexpected system shutdown.

### Half-Implemented Features#### Fix Duplicate FilesLoad in a .dupeguru file generated by [dupeGuru](https://github.com/arsenetar/dupeguru/) and mirror metadata across entries marked as duplicates. After mirroring, return to dupeGuru to manage deletion of the duplicate files. After deletion, use the “Fix Unlinked Entries” feature in TagStudio to delete the duplicate set of entries for the now-deleted files

Caution

While this feature is functional, it’s a pretty roundabout process and can be streamlined in the future.

#### Image CollageCreate an image collage of your photos and videos.

Caution

Collage sizes and options are hardcoded, and there's no GUI indicating the process of the collage creation.

#### MacrosApply tags and other metadata automatically depending on certain criteria. Set specific macros to run when the files are added to the library. Part of this includes applying tags automatically based on parent folders.

Caution

Macro options are hardcoded, and there’s currently no way for the user to interface with this (still incomplete) system at all.

#### Gallery-dl Sidecar ImportingImport JSON sidecar data generated by [gallery-dl](https://github.com/mikf/gallery-dl).

Caution

This feature is not supported or documented in any official capacity whatsoever. It will likely be rolled-in to a larger and more generalized sidecar importing feature in the future.

## Launching/Building From SourceSee instructions in the "[Creating Development Environment](https://github.com/TagStudioDev/TagStudio/blob/main/CONTRIBUTING.md/#creating-a-development-environment)" section from the [contribution documentation](https://github.com/TagStudioDev/TagStudio/blob/main/CONTRIBUTING.md).

## FAQ### What State Is the Project Currently In?As of writing (Alpha v9.4.2) the project is in a useable state, however includes several metadata field bugs and lacks several quality of life features. Focus has been on developing v9.5 with a new SQLite backend which will allow us to not only fix these bugs but also to give us a jumping off point for some [pretty cool](https://docs.tagstud.io/updates/roadmap/) features we've been wanting to add for quite a while now!

### What Features Are You Planning on Adding?See the [Feature Roadmap](https://docs.tagstud.io/updates/roadmap/) page for the core features being planned and implemented for TagStudio. For a more up to date look on what's currently being added for upcoming releases, see our GitHub [milestones](https://github.com/TagStudioDev/TagStudio/milestones) for versioned releases.

### Features That Will NOT Be Added- Native Cloud Integration
- There are plenty of services already (native or third-party) that allow you to mount your cloud drives as virtual drives on your system. Hosting a TagStudio library on one of these mounts should function similarly to what native integration would look like.
- Supporting native cloud integrations such as these would be an unnecessary "reinventing the wheel" burden for us that is outside the scope of this project.
- Native ChatGPT/Non-Local LLM Integration
- This could mean different things depending on your intentions. Whether it's trying to use an LLM to replace the native search, or to trying to use a model for image recognition, I'm not interested in hooking people's TagStudio libraries into non-local LLMs such as ChatGPT and/or turn the program into a "chatbot" interface (see: [Goals/Privacy](https://github.com/TagStudioDev/?tab=readme-ov-file#goals)). I wouldn't, however, mind using **locally** hosted models to provide the *optional* ability for additional searching and tagging methods (especially when it comes to facial recognition) - but this would likely take the form of plugins external to the core program anyway.

### Why Is this Already Version 9?Over the first few years of private development the project went through several major iterations and rewrites. These major version bumps came quickly, and by the time TagStudio was opened-sourced the version number had already reached v9.0. Instead of resetting to "v0.0" or "v1.0" for this public release I decided to keep my v9.x numbering scheme and reserve v10.0 for when all the core features on the [Feature Roadmap](https://docs.tagstud.io/updates/roadmap/) are implemented. I’ve also labeled this version as an "Alpha" and will drop this once either all of the core features are implemented or the project feels stable and feature-rich enough to be considered "Beta" and beyond.