# PDF Merger

This project provides a simple Python script to merge multiple PDF files into a single PDF using [PyPDF2](https://pypdf2.readthedocs.io/).

## Requirements

- Python 3.x
- [PyPDF2](https://pypdf2.readthedocs.io/) library

Install PyPDF2 using pip:

```sh
pip install PyPDF2
```

## Usage

1. Place the PDF files you want to merge in the same directory as `merge.py`.
2. Edit the `pdf_files` list in [`merge.py`](merge.py) to include the filenames of the PDFs you want to merge.
3. Run the script:

```sh
python merge.py
```

The merged PDF will be saved as `merged_output.pdf` in the same directory.

## Example

```python
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]
```

## Output

After running the script, you will see:

```
PDFs merged successfully into merged_output.pdf
```

## License

This project is licensed under