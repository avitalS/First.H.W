import os


def run_build():
    print("--- Starting Build Process ---")
    # כאן אנחנו מדמים הכנה - למשל יצירת תיקיית פלט
    if not os.path.exists('output'):
        os.makedirs('output')
        print("Created output directory.")

    print("Installing dependencies... (Simulated)")
    print("Build completed successfully!")


if __name__ == "__main__":
    run_build()