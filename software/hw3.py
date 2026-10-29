"""Execute HW3 training, fresh-kernel evaluation, and submission exports."""

import argparse
import os
from pathlib import Path
import zipfile

import nbformat
from nbclient import NotebookClient
from nbconvert import PDFExporter


SOFTWARE = Path(__file__).resolve().parent
NOTEBOOKS = [SOFTWARE / 'hw' / f'[HW3]_{name}_CIFAR10.ipynb'
             for name in ('ResNet20', 'VGG16')]
SUBMISSION = SOFTWARE / 'output' / 'submission' / 'hw3'


def execute(path, training=False):
    notebook = nbformat.read(path, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
    os.environ['HW3_TRAIN'] = '1' if training else '0'
    client = NotebookClient(notebook, timeout=None, kernel_name='python3',
                            resources={'metadata': {'path': str(path.parent)}})
    if training:
        # Training runs only setup, definitions, and the silent training cell.
        notebook.cells = [cell for cell in notebook.cells
                          if set(cell.metadata.get('tags', [])) &
                          {'setup', 'definitions', 'training'}]
    print(f"{'Training' if training else 'Evaluating'} {path.name}", flush=True)
    client.execute()
    if not training:
        nbformat.validate(notebook)
        for cell in notebook.cells:
            assert not any(output.output_type == 'error'
                           for output in cell.get('outputs', []))
        nbformat.write(notebook, path)


def export():
    SUBMISSION.mkdir(parents=True, exist_ok=True)
    pdf_directory = SOFTWARE / 'output' / 'pdf'
    pdf_directory.mkdir(parents=True, exist_ok=True)
    for path in NOTEBOOKS:
        notebook = nbformat.read(path, as_version=4)
        for cell in notebook.cells:
            if cell.cell_type == 'code':
                assert cell.execution_count is not None, 'Execute before export.'
                if 'training' in cell.metadata.get('tags', []):
                    assert not cell.outputs, 'Remove intermediate training logs.'
        exporter = PDFExporter(template_file=str(SOFTWARE / 'hw3_pdf.tex.j2'))
        pdf, _ = exporter.from_notebook_node(notebook)
        destination = SUBMISSION / path.with_suffix('.pdf').name.replace('[HW3]', 'HW3')
        (pdf_directory / destination.name).write_bytes(pdf)
        destination.write_bytes(pdf)
    archive = SUBMISSION / 'ECE284_HW3_notebooks.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as output:
        for path in NOTEBOOKS:
            output.write(path, path.name)
    with zipfile.ZipFile(archive) as output:
        assert output.testzip() is None and len(output.namelist()) == 2
    print(SUBMISSION, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['train', 'evaluate', 'export'])
    args = parser.parse_args()
    if args.action == 'train':
        for path in NOTEBOOKS:
            execute(path, training=True)
            execute(path)  # New kernel, cleared outputs, checkpoint reload.
    elif args.action == 'evaluate':
        for path in NOTEBOOKS:
            execute(path)
    else:
        export()


if __name__ == '__main__':
    main()
