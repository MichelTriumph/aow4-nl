import polib
import sys

def convert_po_to_mo_with_swapped_msgctxt_and_msgid(input_po, output_mo):
    # Parse the input .po file
    po = polib.pofile(input_po)

    # Swap msgctxt and msgid for each entry
    for entry in po:
        entry.msgid = entry.msgctxt
        entry.msgctxt = ""

    # Save the updated .po file temporarily
    po.save(input_po + "~")

    # Compile the updated .po file to .mo
    mo = polib.pofile(input_po + "~")
    mo.save_as_mofile(output_mo)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.po output.mo")
    else:
        input_po = sys.argv[1]
        output_mo = sys.argv[2]
        convert_po_to_mo_with_swapped_msgctxt_and_msgid(input_po, output_mo)