---
dg-publish: true
---

## Contents

---

```dataviewjs
// === SETTINGS ===
const ROOT = "Inbox";     // "" for whole vault, or a folder like "Slipbox"
const OPEN_LEVEL = 1;        // auto-expand depth
const SHOW_ONLY = null;      // e.g. ["md","pdf","png"] or null for all

// --- collect all vault files (works for md + attachments) ---
const allFiles = app.vault.getFiles(); // TFile[]

// helpers
const folderOf = f => f.path.split("/").slice(0, -1).join("/");
const nameOf   = p => p.split("/").pop();

// files directly inside a folder
function filesIn(folder) {
  return allFiles
    .filter(f => folderOf(f.path ? f : f) === (folder || ""))
    .filter(f => !SHOW_ONLY || SHOW_ONLY.includes(f.extension.toLowerCase()))
    .sort((a,b) => a.name.localeCompare(b.name));
}

// immediate child folders under a folder
function childFoldersOf(folder) {
  const prefix = folder ? folder + "/" : "";
  const set = new Set();
  for (const f of allFiles) {
    const fld = folderOf(f.path ? f : f);
    if (folder && fld === folder) continue;
    if (folder ? fld.startsWith(prefix) : true) {
      const rel = folder ? fld.slice(prefix.length) : fld;
      if (!rel) continue;
      const first = rel.split("/")[0];
      if (first) set.add(first);
    }
  }
  return [...set].sort((a,b) => a.localeCompare(b));
}

// safe internal link for any file (md or attachment)
function linkEl(path, display, parent) {
  // Try dv.fileLink (HTMLElement in newer Dataview)
  try {
    const el = dv.fileLink(path, false, display);
    if (el && el.nodeType === Node.ELEMENT_NODE) return el;
  } catch (_) {}
  // Fallback: clickable <a> that opens within Obsidian
  const a = parent.createEl("a", { text: display || nameOf(path), href: "#" });
  a.addEventListener("click", (e) => {
    e.preventDefault();
    app.workspace.openLinkText(path, dv.current().file.path, false);
  });
  return a;
}

// render a folder node (FOLDERS FIRST)
function renderFolder(folder, depth = 0, parent = dv.container) {
  const title = folder || (ROOT || "Vault");
  const details = parent.createEl("details", { cls: "dv-folder" });
  if (depth <= OPEN_LEVEL) details.setAttribute("open", "open");

  const summary = details.createEl("summary");
  summary.createEl("strong", { text: nameOf(title) || title });
  // Count files directly in this folder
  const directFiles = filesIn(folder);
  summary.createSpan({ text: `  (${directFiles.length} files)` });
  if (folder) summary.createEl("small", { text: "  • " + folder, cls: "dv-muted" });

  // --- 1) Child folders (FIRST) ---
  const kids = childFoldersOf(folder).map(n => (folder ? `${folder}/${n}` : n));
  for (const k of kids) renderFolder(k, depth + 1, details);

  // --- 2) Direct files (THEN) ---
  if (directFiles.length) {
    const ul = details.createEl("ul");
    for (const f of directFiles) {
      const li = ul.createEl("li");
      li.appendChild(linkEl(f.path, f.name, li));
      // If you had "show extension" earlier, keep it commented:
      // li.createEl("small", { text: "  · " + f.extension.toUpperCase(), cls: "dv-muted" });
    }
  }
}

// ENTRY
renderFolder(ROOT, 0);
```

---