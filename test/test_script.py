import sys
import os
sys.path.append(os.getcwd())
# הוספת נתיב התיקייה כדי שנוכל לייבא את main
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.main import calculate_square

def test_logic():
    assert calculate_square() == 4
    print("Test Passed!")

if __name__ == "__main__":
    test_logic()