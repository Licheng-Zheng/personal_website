import os
import re
import glob

# Paths
base_dir = r"c:\Users\liche\OneDrive\Desktop\PycharmProjects\Personal_Website"
root_htmls = [os.path.join(base_dir, "index.html"), os.path.join(base_dir, "projects.html")]
project_htmls = glob.glob(os.path.join(base_dir, "project_pages", "*.html"))

# 1. Update L. ZHENG logo links
logo_pattern = re.compile(r'<div class="font-serif font-bold text-xl tracking-tight">\s*L\. ZHENG\s*</div>')

for f in root_htmls:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = logo_pattern.sub(r'<a href="index.html" class="font-serif font-bold text-xl tracking-tight hover:underline block">L. ZHENG</a>', content)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

for f in project_htmls:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = logo_pattern.sub(r'<a href="../index.html" class="font-serif font-bold text-xl tracking-tight hover:underline block">L. ZHENG</a>', content)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# 2. Update index.html hero links
index_path = os.path.join(base_dir, "index.html")
with open(index_path, 'r', encoding='utf-8') as file:
    index_content = file.read()

hero_pattern = re.compile(r'<a href="assets/resume\.pdf" target="_blank" rel="noopener noreferrer" class="inline-block border border-black bg-white text-black px-8 py-3 font-mono text-sm uppercase tracking-widest hover:bg-black hover:text-white transition-colors duration-200">\s*Download Resume \[\.pdf\]\s*</a>')

hero_replacement = """<div class="flex flex-wrap items-center gap-4">
                    <a href="assets/documents/resume.pdf" target="_blank" rel="noopener noreferrer" class="inline-block border border-black bg-white text-black px-8 py-3 font-mono text-sm uppercase tracking-widest hover:bg-black hover:text-white transition-colors duration-200">
                        Download Resume [.pdf]
                    </a>
                    <a href="https://github.com/yourusername" target="_blank" rel="noopener noreferrer" class="inline-block border border-black text-black px-8 py-3 font-mono text-sm uppercase tracking-widest hover:bg-slate-50 transition-colors duration-200">
                        GitHub &nearr;
                    </a>
                    <a href="https://linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer" class="inline-block border border-black text-black px-8 py-3 font-mono text-sm uppercase tracking-widest hover:bg-slate-50 transition-colors duration-200">
                        LinkedIn &nearr;
                    </a>
                </div>"""
index_content = hero_pattern.sub(hero_replacement, index_content)

with open(index_path, 'w', encoding='utf-8') as file:
    file.write(index_content)


# 3. Update project pages to include GitHub link in the tech stack grid
grid_start_pattern = re.compile(r'<div class="grid grid-cols-2 gap-4 border-y border-black py-4 mb-8">')
tech_stack_pattern = re.compile(r'(<div>\s*<span class="font-mono text-\[10px\] text-slate-500 uppercase block mb-1">Tech Stack</span>\s*<span class="font-mono text-sm">.*?</span>\s*</div>\s*)</div>', re.DOTALL)

for f in project_htmls:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Change grid to 3 columns
    content = grid_start_pattern.sub(r'<div class="grid grid-cols-2 md:grid-cols-3 gap-4 border-y border-black py-4 mb-8">', content)
    
    # Insert github section
    repo_block = r'\1<div class="col-span-2 md:col-span-1">\n                            <span class="font-mono text-[10px] text-slate-500 uppercase block mb-1">Repository</span>\n                            <a href="#" target="_blank" class="font-mono text-sm text-blue-600 hover:underline">View on GitHub &nearr;</a>\n                        </div>\n                    </div>'
    content = tech_stack_pattern.sub(repo_block, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updates completed successfully.")
