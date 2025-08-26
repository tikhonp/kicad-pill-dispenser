#!/usr/bin/env python3

import os
import sys
import shutil
import zipfile

MAP = {
    "F_Cu.gbr": "Top.gtl",
    "B_Cu.gbr": "Bot.gbl",
    "F_Mask.gbr": "MaskTop.gts",
    "B_Mask.gbr": "MaskBot.gbs",
    "F_Silkscreen.gbr": "TopSilk.gto",
    "B_Silkscreen.gbr": "BotSilk.gbo",
    "Edge_Cuts.gbr": "Board.gko",
    "NPTH.drl": "Drill-npth.drl",
    "PTH.drl": "Drill.drl",
    "F_Paste.gbr": "PasteTop.gtp",
    "B_Paste.gbr": "PasteBot.gbp",
}

def rename_gerbers(path):
    for fname in os.listdir(path):
        for key, newname in MAP.items():
            if fname.endswith(key):
                old = os.path.join(path, fname)
                new = os.path.join(path, newname)
                print(f"{fname} -> {newname}")
                os.rename(old, new)
                break

def zip_folder(folder, zip_name="gerbers.zip"):
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(folder):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, folder)
                zf.write(filepath, arcname)
    print(f"Created {zip_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rename_gerbers.py <gerbers_folder>")
        sys.exit(1)

    src_folder = sys.argv[1]
    rename_gerbers(src_folder)
    zip_folder(src_folder)

