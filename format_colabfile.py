import nbformat

notebook_path = "D:\\VNIT\\Semester4\\NLP\\MT24AAI094_NLP_TicketTriaging\\TicketTriage_.ipynb"

# Read notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove only widget metadata
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]


# Save notebook with outputs preserved
with open(notebook_path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Notebook fixed. Outputs preserved.")