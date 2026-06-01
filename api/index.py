import sys
import os

# Append the root path so index.py can import modules from the parent directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT_DIR)

# Set working directory to project root so CSV and DB paths resolve correctly
os.chdir(ROOT_DIR)

from main import app

# Vercel Serverless entry point
handler = app
