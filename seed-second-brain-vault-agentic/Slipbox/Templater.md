---
dg-publish: true
---

# ⚙️ Templater Snippets

---

## Promote to Slipbox
```javascript
<%*
/**
 * Promote current note to Slipbox
 * - Create Slipbox/{title}.md with current content
 * - Replace current note with pointer link
 * - Rename current note as pointer
 */
const TARGET = "Slipbox";
const POINTER_SUFFIX = " (pointer)";
const DATE = tp.date.now("YYYY-MM-DD HH:mm");

const fm = app.fileManager;
const vault = app.vault;
const src = tp.file.find_tfile(tp.file.path(true));

if (!src) { new Notice("No active file"); return; }
if (src.path.startsWith(TARGET + "/")) {
  new Notice("Already in Slipbox"); 
  return;
}

const baseTitle = tp.file.title || "Untitled";

function uniquePathInSlipbox(base) {
  let p = `${TARGET}/${base}.md`;
  let i = 1;
  const exists = async () => await vault.adapter.exists(p);
  return (async ()=>{
    while (await exists()) {
      p = `${TARGET}/${base} (${i}).md`;
      i++;
    }
    return p;
  })();
}

const destPath = await uniquePathInSlipbox(baseTitle);

const content = await vault.read(src);
await vault.create(destPath, content);

const destWikilink = `[[${destPath.replace(/\.md$/, "")}]]`;
const pointerText = `> ⟶ **Moved to** ${destWikilink}\n> on ${DATE}\n\n`;
await vault.modify(src, pointerText);

const srcFolder = src.path.split("/").slice(0, -1).join("/");
const newNameBase = baseTitle + POINTER_SUFFIX;
let newName = `${newNameBase}.md`;
let i = 1;
while (await vault.adapter.exists((srcFolder ? srcFolder + "/" : "") + newName)) {
  newName = `${newNameBase} (${i}).md`;
  i++;
}
const newSrcPath = (srcFolder ? srcFolder + "/" : "") + newName;
await fm.renameFile(src, newSrcPath);

new Notice("Promoted to Slipbox → " + destPath);
-%>
```
