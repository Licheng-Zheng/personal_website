import os
import re
from urllib.parse import urlparse
import urllib.request

def check_website(base_dir):
    html_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    broken_links = []
    
    href_pattern = re.compile(r'href=["\'](.*?)["\']')
    src_pattern = re.compile(r'src=["\'](.*?)["\']')

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        links = href_pattern.findall(content) + src_pattern.findall(content)
        
        for link in links:
            if link.startswith('data:') or link.startswith('#') or link == '':
                continue
                
            if link.startswith('http://') or link.startswith('https://'):
                # We can skip checking external links if we only care about internal site structure, 
                # but let's just do a quick check, though it might take time. Let's skip external for now to be fast,
                # or only flag them as external. Actually, let's just check internal links first.
                pass
            else:
                # Internal link
                # Remove query params or fragments
                clean_link = link.split('#')[0].split('?')[0]
                if not clean_link:
                    continue
                
                # Resolve relative path
                dir_name = os.path.dirname(filepath)
                target_path = os.path.normpath(os.path.join(dir_name, clean_link))
                
                if not os.path.exists(target_path):
                    broken_links.append((filepath, link, target_path))
                    
    return broken_links

if __name__ == "__main__":
    base_dir = r"c:\Users\liche\OneDrive\Desktop\PycharmProjects\Personal_Website"
    broken = check_website(base_dir)
    if broken:
        print(f"Found {len(broken)} broken internal links:")
        for source, link, target in broken:
            # print relative path for easier reading
            rel_source = os.path.relpath(source, base_dir)
            print(f"File: {rel_source} | Broken Link: '{link}' | Resolves to missing file: {target}")
    else:
        print("No broken internal links found!")
