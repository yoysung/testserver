import os
import subprocess
import django
from django.core.management import call_command
import sys

def build_react():
    # Get the absolute path to the project root (where package.json is located)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    react_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    
    # Verify package.json exists
    if not os.path.exists(os.path.join(react_root, 'package.json')):
        print(f"Error: package.json not found in {react_root}")
        print("Make sure you're running this script from the correct directory")
        sys.exit(1)

    print(f"Building React app in: {react_root}")
    
    try:
        # On Windows, we need to explicitly use npm.cmd
        npm_command = 'npm.cmd' if os.name == 'nt' else 'npm'
        
        # First install dependencies
        subprocess.run([npm_command, 'install'], cwd=react_root, check=True)
        
        # Then build
        subprocess.run([npm_command, 'run', 'build'], cwd=react_root, check=True)
        
        print("React build completed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error building React app: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: npm not found. Please make sure Node.js and npm are installed and in your PATH")
        sys.exit(1)

def collect_static():
    print("Collecting static files...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gameCatalog.settings')
    django.setup()
    try:
        call_command('collectstatic', '--noinput')
        print("Static files collected successfully")
    except Exception as e:
        print(f"Error collecting static files: {e}")
        sys.exit(1)

if __name__ == '__main__':
    print("Starting build and collect process...")
    build_react()
    collect_static()
    print("Build and collect process completed successfully")
