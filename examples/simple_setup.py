#!/usr/bin/env python3
"""
Simple setup script for Field Manager API examples
"""

import subprocess
import sys
import os


def main():
    print("🚀 Setting up Field Manager API examples...")

    # Check Python version
    if sys.version_info < (3, 9):
        print("❌ Python 3.9 or higher is required")
        sys.exit(1)

    print("✅ Python version OK")

    # Create output directory
    os.makedirs("output", exist_ok=True)
    print("✅ Created output directory")

    # Install dependencies
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("✅ Dependencies installed")
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        sys.exit(1)

    # Test import
    try:
        import field_manager_python_client

        print("✅ Package import successful")
    except ImportError:
        print("❌ Failed to import field_manager_python_client")
        sys.exit(1)

    print()
    print("🎉 Setup complete!")
    print()
    print("Next steps:")
    print("1. Set your email in .env file (optional):")
    print("   cp examples/.env.template examples/.env")
    print("   # Edit examples/.env")
    print()
    print("2. Run your first example:")
    print("   python examples/ex_list_organizations_and_projects.py")
    print()


if __name__ == "__main__":
    main()
