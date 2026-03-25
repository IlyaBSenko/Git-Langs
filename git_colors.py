import os
import sys
import yaml

# install pyyaml with pip or this won't work
# usage: python script.py languages.yml output.md

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

    for lang in data:
        info = data[lang]
        
        if "color" in info and "type" in info:
            color = info["color"]
            l_type = info["type"]
            exts = info.get("extensions", "none")

            # just use a colored circle emoji or a simple text box 
            # instead of making 500 separate SVG files lol
            color_swatch = f"![{color}](https://placehold.co/15x15/{color.replace('#', '')}/{color.replace('#', '')}.png)"

            row = f"| {lang} | {color_swatch} `{color}` | {l_type} | `{exts}` |\n"
            md_output += row

    out = open(outfile, 'w')
    out.write(md_output)
    out.close()
    
    print("YO CHILL CHECK " + outfile)

if __name__ == "__main__":
    main()
