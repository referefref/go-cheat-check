import os
import difflib
import re

def extract_features(file_content):
    """Extract features from Go code"""
    # Extract imports
    imports = re.findall(r'^\s*import\s*\(\s*([\s\S]*?)\s*\)', file_content, re.MULTILINE)
    imports = [imp.strip().split('\n') for imp in imports]
    imports = [item for sublist in imports for item in sublist if item]

    # Extract functions
    functions = re.findall(r'func\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(', file_content)

    # Extract comments
    comments = re.findall(r'(\/\/.*|\/\*[\s\S]*?\*\/)', file_content)

    # Extract package
    package = re.search(r'^\s*package\s+(\w+)', file_content, re.MULTILINE)
    package = package.group(1) if package else ''

    return {
        'imports': imports,
        'functions': functions,
        'comments': comments,
        'package': package
    }

def compare_files(file_content, reference_files):
    """Compare file content with reference files"""
    features = extract_features(file_content)

    comparison_results = []

    for ref_file in reference_files:
        with open(ref_file, 'r') as f:
            ref_content = f.read()

        ref_features = extract_features(ref_content)

        # Compare package names
        package_match = int(features['package'] == ref_features['package'])

        # Compare imports
        import_diff = difflib.SequenceMatcher(None, '\n'.join(features['imports']), '\n'.join(ref_features['imports'])).ratio()

        # Compare functions
        func_diff = difflib.SequenceMatcher(None, '\n'.join(features['functions']), '\n'.join(ref_features['functions'])).ratio()

        # Compare comments
        comment_diff = difflib.SequenceMatcher(None, '\n'.join(features['comments']), '\n'.join(ref_features['comments'])).ratio()

        # Aggregate match percentage
        total_score = (package_match + import_diff + func_diff + comment_diff) / 4

        comparison_results.append({
            'reference_file': ref_file,
            'package_match': package_match,
            'import_diff': import_diff,
            'func_diff': func_diff,
            'comment_diff': comment_diff,
            'total_score': total_score * 100
        })

    return comparison_results

def main(target_file, reference_files):
    """Main function"""
    with open(target_file, 'r') as f:
        target_content = f.read()

    results = compare_files(target_content, reference_files)

    print(f"Comparison results for {target_file}:")
    for result in results:
        print(f"\nReference File: {result['reference_file']}")
        print(f"Package Match: {result['package_match'] * 100:.2f}%")
        print(f"Import Similarity: {result['import_diff'] * 100:.2f}%")
        print(f"Function Similarity: {result['func_diff'] * 100:.2f}%")
        print(f"Comment Similarity: {result['comment_diff'] * 100:.2f}%")
        print(f"Total Match Score: {result['total_score']:.2f}%")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Compare Go code file against a set of reference files.')
    parser.add_argument('target_file', type=str, help='The Go code file to compare')
    parser.add_argument('reference_files', type=str, nargs='+', help='The set of reference Go code files')

    args = parser.parse_args()
    main(args.target_file, args.reference_files)
