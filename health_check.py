import os

def check_encoding(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Basic heuristic for common Mojibake artifacts of double-encoded UTF-8 as cp1252
            if '\u00c3' in content or '\u00c5' in content or '\u00f0\u0178' in content:
                print(f"⚠️ Warning: Possible Mojibake encoding error in {filepath}")
                idx = content.find('\u00c3')
                if idx == -1: idx = content.find('\u00c5')
                if idx == -1: idx = content.find('\u00f0\u0178')
                print("Context:", repr(content[max(0, idx-10):idx+10]))
                return False
        return True
    except UnicodeDecodeError:
        print(f"❌ Error: Not a valid UTF-8 file: {filepath}")
        return False

def check_spoilers(filepath):
    if not filepath.endswith('.md') or 'Exercices' not in filepath:
        return True
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if there are answers without details tags
    if 'Réponse' in content and '<details>' not in content:
        print(f"⚠️ Warning: Possible missing <details> for answers in {filepath}")
        return False
    return True

def check_duplicates(directory):
    duplicate_types = ['Synthese', 'Exercices', 'Dashboard', 'CheatSheet', 'Flashcards']
    all_good = True
    
    for course_dir in os.listdir(directory):
        course_path = os.path.join(directory, course_dir)
        if os.path.isdir(course_path) and not course_dir.startswith(('.', '_')):
            files = os.listdir(course_path)
            for dtype in duplicate_types:
                matching_files = [f for f in files if dtype in f]
                if len(matching_files) > 1:
                    print(f"❌ Error: Duplicated files found for {dtype} in course {course_dir}: {matching_files}")
                    all_good = False
    return all_good

def run_health_check(directory):
    print("Running Health Check on generated materials...")
    all_good = True
    
    # 1. Check for duplicates
    if not check_duplicates(directory):
        all_good = False

    # 2. Check individual files for encoding and spoilers
    for root, dirs, files in os.walk(directory):
        if '.agent' in root or '.git' in root or '.gemini' in root:
            continue
        for file in files:
            if file.endswith('.md') or file.endswith('.csv') or file.endswith('.html') or file.endswith('.js'):
                filepath = os.path.join(root, file)
                if not check_encoding(filepath):
                    all_good = False
                if not check_spoilers(filepath):
                    all_good = False

    if all_good:
        print("\n✅ Health Check passed! No duplicates, encoding errors, or missing spoiler tags found.")
    else:
        print("\n❌ Health Check failed! Please review the warnings above before deploying or committing.")

if __name__ == "__main__":
    run_health_check("c:/Users/natha/OneDrive/Bureau/superapp")
