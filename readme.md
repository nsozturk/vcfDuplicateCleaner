# VCF Duplicate Cleaner

VCF Duplicate Cleaner is a Python script that removes duplicate contacts from a VCF (vCard) file based on mobile phone numbers. The cleaned VCF file is saved to a specified output path.

## Features

- Reads VCF files and parses contacts.
- Removes duplicate contacts based on mobile phone numbers.
- Writes cleaned contacts to a new VCF file.
- Can be run from the terminal with command-line arguments.

## Requirements

- Python 3.9 or higher
- `vobject` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/nsozturk/vcfDuplicateCleaner.git
    cd vcfDuplicateCleaner
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the script from the terminal, use the following command:

```sh
python vcfDuplicateCleaner.py /path/to/input.vcf /path/to/output.vcf
```
## Tested Platforms

- [x] The script has been tested on VCF files exported from iCloud to ensure compatibility and correct functionality.
