---
dg-publish: true
---

## Index

---

```dataviewjs
/***** CONFIG *****/
const ROOT = "Projects/Rituals";   // <- change to your folder path
const INCLUDE_ROOT_SECTION = true;         // list notes directly in ROOT
const EXCLUDE_PREFIXES = ["_", "."];       // skip files/folders starting with these
/******************/

// Helper: should we skip this path or name?
const skip = (name) => EXCLUDE_PREFIXES.some(p => name.startsWith(p));

// Collect .md files under ROOT
const files = app.vault.getFiles().filter(f => {
  if (f.extension.toLowerCase() !== "md") return false;
  const parent = f.parent?.path ?? "";
  const inRoot = parent === ROOT;
  const underRoot = parent.startsWith(ROOT + "/");
  if (!(inRoot || underRoot)) return false;
  // Exclude hidden/prefixed folders in the path segments
  const segments = parent === "" ? [] : parent.split("/");
  if (segments.some(skip)) return false;
  // Exclude files by prefix if needed
  if (skip(f.name)) return false;
  return true;
});

// Group by immediate subfolder under ROOT
const groups = new Map(); // key -> array of TFiles
for (const f of files) {
  const parent = f.parent?.path ?? "";
  let key;
  if (parent === ROOT) {
    key = "(root)";
  } else {
    const rel = parent.slice(ROOT.length + 1);       // e.g. "Sub/Deeper"
    key = rel.split("/")[0];                         // immediate subfolder, e.g. "Sub"
  }
  if (!INCLUDE_ROOT_SECTION && key === "(root)") continue;
  if (!groups.has(key)) groups.set(key, []);
  groups.get(key).push(f);
}

// Render: sections sorted by folder name, files by title
const sectionOrder = [...groups.keys()].sort((a, b) => {
  if (a === "(root)") return -1;      // root first
  if (b === "(root)") return 1;
  return a.localeCompare(b, undefined, { sensitivity: "base" });
});

for (const key of sectionOrder) {
  const list = groups.get(key).sort((a, b) =>
    a.basename.localeCompare(b.basename, undefined, { sensitivity: "base" })
  );

  // Collapsible section
  const det = dv.el("details", "");
  dv.el("summary", `${key} (${list.length})`, det);

  // File links
  dv.list(list.map(f => dv.fileLink(f.path)), det);
}
```

---