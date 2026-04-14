---
title: Create MOC in Obsidian
category: General
priority: Medium
starred: None
created: 2025-08-09T10:04:55.775024
updated: 2025-08-09T10:05:04.171112
dg-publish: true
---
# Create MOC in Obsidian

**Priority:** Medium

## Conversation

### Assistant

Got it — you want to make a **Map of Content (MOC)** in Obsidian that looks like the screenshot you shared.  

Here’s how you can recreate this style step-by-step:  

---

## 1. **Structure Your MOC**
Use headings to create sections, and list the related note links under them.

```markdown
# Home

---

## Topics
- 🌐 [[Social Sciences Index]]
- 📈 [[Tools For Life Index]]
- 🧠 [[Psychology & Neurodiversity Index]]
- 📌 [[Topics to Research]]

---

## Creativity
- 🎸 [[Guitar Index]]
- ✍️ [[Writing Index]]
- 📺 [[YouTube Index]]

---

## Media
- 🎬 [[Movies & Shows to Watch]]
- 📚 [[Books Index]]

---

## Other
- 🍲 [[Food Index]]
- 📍 [[Balkon Project]]
```

---

## 2. **Add Icons**
- Use emoji directly in your markdown (as above) for quick styling.
- Alternatively, install the **Obsidian Emoji Toolbar** or **Iconize** plugin to add icons.

---

## 3. **Style with CSS**
If you want the purple lines and clean spacing:
1. Create or edit your vault’s `obsidian.css` or `snippets` folder.
2. Add something like:

```css
.markdown-preview-view h2 {
    border-bottom: 2px solid #a084ca;
    padding-bottom: 4px;
    margin-top: 20px;
}

.markdown-preview-view a {
    color: #6a5acd;
    text-decoration: none;
}

.markdown-preview-view a:hover {
    text-decoration: underline;
}

.markdown-preview-view ul {
    list-style: none;
    padding-left: 0;
}

.markdown-preview-view ul li {
    padding: 4px 0;
}
```
Then enable the snippet from **Settings → Appearance → CSS snippets**.

---

## 4. **Make it Interactive**
- Use the **Advanced URI** plugin to link directly to searches, tags, or templates.
- Use **Dataview** if you want the lists to be automatically generated from tags.

---

If you’d like, I can **give you a ready-to-use Obsidian template file** with this layout and CSS so it will look exactly like your screenshot.  
Do you want me to prepare that?

---

