# import os
import sys
import yaml
from urllib.parse import quote # url encode for the lang name for Wikipedia (handles spaces and special chars?)

# install pyyaml with pip or this won't work
# usage: python git_colors.py languages.yml output.md

def main():
    if len(sys.argv) < 3:
        print("bruh missing files Usage: python script.py input.yml output.md")
        return

    infile = sys.argv[1]
    outfile = sys.argv[2]

    f = open(infile, 'r')
    data = yaml.safe_load(f)
    f.close()

    md_output = "| Language | Color | Type | Extensions |\n"
    md_output += "| --- | --- | --- | --- |\n"

    prog_total = 0
    data_total = 0
    markup_total = 0
    prose_total = 0
    for lang in data:
        info = data[lang]
        
        if "color" in info and "type" in info:
            color = info["color"]
            l_type = info["type"]
            exts = info.get("extensions", "none")

            
            # color_swatch = f"![{color}](https://placehold.co/15x15/{color.replace('#', '')}/{color.replace('#', '')}.png)"

            # row = f"| {lang} | {color_swatch} `{color}` | {l_type} | `{exts}` |\n"
            wiki_url = f"https://en.wikipedia.org/wiki/{quote(lang)}"
            color_swatch = f"[![{color}](https://placehold.co/15x15/{color.replace('#', '')}/{color.replace('#', '')}.png)]({wiki_url})"

            row = f"| {lang} | {color_swatch} `{color}` | {l_type} | `{exts}` |\n"
            
            md_output += row

            # for curiosity reasons:
            if l_type == "programming":
                prog_total += 1
            if l_type == "data":
                data_total += 1
            if l_type == "markup":
                markup_total += 1
            if l_type == "prose":
                prose_total += 1
    print("Programming total: ", prog_total)
    print("Data total: ", data_total)
    print("Markup total: ", markup_total)
    print("Prose total: ", prose_total)


    out = open(outfile, 'w')
    out.write(md_output)
    out.close()
    
    print("Check " + outfile)

if __name__ == "__main__":
    main()
