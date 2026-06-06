#!/usr/bin/env python3
"""Post-process the EPUB: inject chapter vignettes and fix front matter styling."""

import zipfile
import shutil
import os
import re
from pathlib import Path

EPUB_PATH = Path("demons_at_work.epub")
VIGNETTE_DIR = Path("art/vignettes")

CHAPTER_VIGNETTES = {
    "ch002.xhtml": "01-on-paper.png",
    "ch003.xhtml": "02-hat.png",
    "ch004.xhtml": "03-the-canvas.png",
    "ch005.xhtml": "04-fourteen-minutes.png",
    "ch006.xhtml": "05-good-acoustics.png",
    "ch007.xhtml": "06-six-minutes-early.png",
    "ch008.xhtml": "07-the-garden.png",
    "ch009.xhtml": "08-cancellation.png",
    "ch010.xhtml": "09-trust-the-process.png",
    "ch011.xhtml": "10-revised-protocols.png",
    "ch012.xhtml": "11-wednesday-night.png",
    "ch013.xhtml": "12-middlemarch.png",
    "ch014.xhtml": "13-the-report.png",
    "ch015.xhtml": "14-eleven-minutes.png",
    "ch016.xhtml": "15-two-cups.png",
    "ch017.xhtml": "16-mid-cycle.png",
    "ch018.xhtml": "17-the-doorway.png",
    "ch019.xhtml": "18-please-address.png",
    "ch020.xhtml": "19-direct-interface.png",
    "ch021.xhtml": "20-meri.png",
    "ch022.xhtml": "21-the-field.png",
    "ch023.xhtml": "22-completion.png",
    "ch024.xhtml": "23-the-next-file.png",
}

VIGNETTE_CSS = """
/* Chapter vignettes */
.chapter-vignette {
  display: inline-block;
  height: 1.2em;
  vertical-align: middle;
  margin-left: 0.4em;
}
/* Epigraph */
.epigraph {
  text-align: center;
  font-style: italic;
  margin-top: 30%;
  page-break-before: always;
}
.epigraph p {
  text-indent: 0;
}
.epigraph .attribution {
  font-style: normal;
  font-size: 0.9em;
  margin-top: 0.5em;
}
"""


def process_epub():
    tmp = EPUB_PATH.with_suffix(".epub.tmp")
    shutil.copy2(EPUB_PATH, tmp)

    images_added = []

    with zipfile.ZipFile(tmp, "r") as zin, zipfile.ZipFile(EPUB_PATH, "w") as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)

            if item.filename == "EPUB/styles/stylesheet1.css":
                data = data + VIGNETTE_CSS.encode("utf-8")

            elif item.filename.startswith("EPUB/text/ch") and item.filename.endswith(".xhtml"):
                fname = os.path.basename(item.filename)
                if fname in CHAPTER_VIGNETTES:
                    vimg = CHAPTER_VIGNETTES[fname]
                    content = data.decode("utf-8")
                    content = re.sub(
                        r"(<h1[^>]*>)(.*?)(</h1>)",
                        rf'\1\2 <img class="chapter-vignette" src="../images/{vimg}" alt="" />\3',
                        content,
                    )
                    data = content.encode("utf-8")
                    images_added.append(vimg)

            elif item.filename == "EPUB/content.opf":
                content = data.decode("utf-8")
                img_manifest = ""
                for vimg in CHAPTER_VIGNETTES.values():
                    img_id = vimg.replace(".png", "").replace("-", "_")
                    img_manifest += f'    <item id="{img_id}" href="images/{vimg}" media-type="image/png" />\n'
                content = content.replace("</manifest>", img_manifest + "  </manifest>")
                data = content.encode("utf-8")

            zout.writestr(item, data)

        for vimg in CHAPTER_VIGNETTES.values():
            vpath = VIGNETTE_DIR / vimg
            if vpath.exists():
                zout.write(vpath, f"EPUB/images/{vimg}")

    tmp.unlink()
    print(f"EPUB fixed: {len(images_added)} vignettes injected, CSS updated.")


if __name__ == "__main__":
    process_epub()
