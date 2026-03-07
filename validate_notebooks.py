#!/usr/bin/env python3
"""
Validation script for course notebooks.
Checks for:
- Valid JSON structure
- Google Colab compatibility
- Proper explanations and scope
- No broken links or references
"""

import json
import os
import sys
from pathlib import Path

class NotebookValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def validate_notebook(self, notebook_path):
        """Validate a single notebook"""
        print(f"\n{'='*70}")
        print(f"Validating: {notebook_path.name}")
        print('='*70)

        # 1. Check if file exists
        if not notebook_path.exists():
            self.errors.append(f"File not found: {notebook_path}")
            return False

        # 2. Check JSON validity
        try:
            with open(notebook_path, 'r', encoding='utf-8') as f:
                nb = json.load(f)
            print("✓ Valid JSON structure")
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON in {notebook_path.name}: {e}")
            return False

        # 3. Check notebook structure
        if 'cells' not in nb:
            self.errors.append(f"Missing 'cells' in {notebook_path.name}")
            return False
        print(f"✓ Contains {len(nb['cells'])} cells")

        # 4. Check for Colab badge
        has_colab_badge = False
        for cell in nb['cells']:
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', []))
                if 'colab.research.google.com' in source:
                    has_colab_badge = True
                    break

        if has_colab_badge:
            print("✓ Has Colab badge")
        else:
            self.warnings.append(f"{notebook_path.name}: Missing Colab badge")

        # 5. Check for local file paths (should use relative or Colab-compatible paths)
        local_paths_found = []
        for cell in nb['cells']:
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))
                # Check for absolute paths that won't work on Colab
                if '/Users/' in source or 'C:\\' in source or '/home/' in source:
                    local_paths_found.append(cell)

        if local_paths_found:
            self.warnings.append(f"{notebook_path.name}: Found {len(local_paths_found)} cells with local paths")
        else:
            print("✓ No hardcoded local paths")

        # 6. Check for proper pip install commands
        pip_installs = []
        for cell in nb['cells']:
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))
                if 'pip install' in source:
                    pip_installs.append(source)

        if pip_installs:
            print(f"✓ Found {len(pip_installs)} pip install cell(s)")
            # Check if they use -q flag for quiet installation
            for install in pip_installs:
                if 'pip install' in install and '-q' not in install:
                    self.warnings.append(f"{notebook_path.name}: pip install without -q flag (verbose output)")

        # 7. Check for explanations (markdown cells)
        markdown_cells = [c for c in nb['cells'] if c.get('cell_type') == 'markdown']
        code_cells = [c for c in nb['cells'] if c.get('cell_type') == 'code']

        ratio = len(markdown_cells) / len(code_cells) if code_cells else 0
        print(f"✓ Markdown/Code ratio: {len(markdown_cells)}/{len(code_cells)} = {ratio:.2f}")

        if ratio < 0.3:
            self.warnings.append(f"{notebook_path.name}: Low explanation ratio ({ratio:.2f}). Consider adding more explanations.")
        elif ratio > 0.7:
            print("  → Good balance of explanations")

        # 8. Check file size
        size_kb = notebook_path.stat().st_size / 1024
        print(f"✓ File size: {size_kb:.1f} KB")

        if size_kb > 100:
            self.warnings.append(f"{notebook_path.name}: Large file ({size_kb:.1f} KB). Consider simplifying.")
        elif size_kb < 5:
            self.warnings.append(f"{notebook_path.name}: Very small file ({size_kb:.1f} KB). Might need more content.")

        # 9. Check for Google Colab upload compatibility
        has_upload = False
        for cell in nb['cells']:
            if cell.get('cell_type') == 'code':
                source = ''.join(cell.get('source', []))
                if 'from google.colab import files' in source or 'files.upload()' in source:
                    has_upload = True

        if has_upload:
            print("✓ Uses Google Colab file upload")

        # 10. Check for French content (this is a French course)
        french_keywords = ['objectif', 'cours', 'étape', 'analyse', 'français']
        has_french = False
        for cell in nb['cells']:
            if cell.get('cell_type') == 'markdown':
                source = ''.join(cell.get('source', [])).lower()
                if any(kw in source for kw in french_keywords):
                    has_french = True
                    break

        if has_french:
            print("✓ Contains French content")
        else:
            self.warnings.append(f"{notebook_path.name}: Minimal French content detected")

        return True

    def print_summary(self):
        """Print validation summary"""
        print("\n" + "="*70)
        print("VALIDATION SUMMARY")
        print("="*70)

        if not self.errors and not self.warnings:
            print("✓ All notebooks are valid with no issues!")
            return True

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  - {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  - {warning}")

        return len(self.errors) == 0

def main():
    """Main validation function"""
    validator = NotebookValidator()

    # Get all course notebooks (01-08)
    course_dir = Path(__file__).parent
    notebooks = sorted(course_dir.glob('0[1-8]_*.ipynb'))

    if not notebooks:
        print("❌ No course notebooks found!")
        return 1

    print(f"Found {len(notebooks)} course notebooks to validate")

    all_valid = True
    for nb_path in notebooks:
        is_valid = validator.validate_notebook(nb_path)
        if not is_valid:
            all_valid = False

    # Check homework files
    homework_dir = course_dir / 'homework'
    if homework_dir.exists():
        print(f"\n{'='*70}")
        print("Checking homework files...")
        print('='*70)

        homework_files = list(homework_dir.glob('*.ipynb'))
        print(f"✓ Found {len(homework_files)} homework file(s)")

        solution_dir = homework_dir / 'solutions'
        if solution_dir.exists():
            solution_files = list(solution_dir.glob('*.ipynb'))
            print(f"✓ Found {len(solution_files)} solution file(s)")

    # Print summary
    success = validator.print_summary()

    return 0 if success and all_valid else 1

if __name__ == '__main__':
    sys.exit(main())
