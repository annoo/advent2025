"""pytest configuration - adds project root to Python path."""
import sys
from pathlib import Path

# Add project root to path so day1, day2, etc. can be imported
sys.path.insert(0, str(Path(__file__).parent))
