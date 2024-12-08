import vobject
import os
import argparse

def read_vcf(file_path):
    with open(file_path, 'r') as file:
        return list(vobject.readComponents(file))

def write_vcf(file_path, contacts):
    with open(file_path, 'w') as file:
        for contact in contacts:
            file.write(contact.serialize())

def remove_duplicates(contacts):
    seen_numbers = set()
    unique_contacts = []
    for contact in contacts:
        if hasattr(contact, 'tel'):
            for tel in contact.tel_list:
                if tel.value not in seen_numbers:
                    seen_numbers.add(tel.value)
                    unique_contacts.append(contact)
                    break
    return unique_contacts

def main(input_path, output_path):
    contacts = read_vcf(input_path)
    unique_contacts = remove_duplicates(contacts)
    write_vcf(output_path, unique_contacts)
    print(f"Removed duplicates. {len(contacts) - len(unique_contacts)} duplicates found. Cleaned file written to {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='VCF Duplicate Cleaner')
    parser.add_argument('input_path', type=str, help='Path to the input VCF file')
    parser.add_argument('output_path', type=str, help='Path to the output cleaned VCF file')
    args = parser.parse_args()
    main(args.input_path, args.output_path)