# HTML Style Guide & Cheatsheet

This document contains pre-styled HTML snippets used across the project pages. You can copy and paste these blocks directly into any project HTML file to maintain a consistent brutalist/minimalist aesthetic.

## 1. Text & Headings

**Section Header (H2)**
```html
<h2 id="section-id" class="font-serif text-3xl font-bold border-b border-black pb-2 scroll-mt-24 mt-12 mb-6">
    Section Title
</h2>
```

**Abstract / Intro Paragraph**
```html
<p class="font-sans text-xl leading-relaxed text-slate-800 font-bold">
    This is the bold intro paragraph used at the top of the project pages to summarize the work.
</p>
```

**Standard Body Text & Lists**
```html
<p>
    This is a standard body paragraph. It inherits styling from the `.article-body p` global CSS rule (1.5rem bottom margin, 1.8 line height).
</p>

<ul class="list-disc pl-5 mb-6">
    <li>First bullet point</li>
    <li>Second bullet point</li>
</ul>

<ol class="list-decimal pl-5 mb-6">
    <li>First numbered item</li>
    <li>Second numbered item</li>
</ol>
```

---

## 2. Media

**Standard Image**
```html
<img src="../assets/images/projects/project_name/image.webp" alt="Image Description" class="w-full border border-black mb-10 shadow-sm">
```

**YouTube Video Embed (Custom Brutalist Facade)**
*(Replace `VIDEO_ID` with the actual YouTube ID in both the `src` and the `img` tags)*
```html
<!-- YouTube Embed Facade -->
<div class="relative w-full aspect-video border border-black mb-10 shadow-sm bg-black group cursor-pointer overflow-hidden" 
     onclick="this.innerHTML='<iframe class=\'w-full h-full\' src=\'https://www.youtube-nocookie.com/embed/VIDEO_ID?autoplay=1&rel=0&modestbranding=1\' frameborder=\'0\' allow=\'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\' allowfullscreen></iframe>'">
    
    <!-- Thumbnail Image -->
    <img src="https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg" alt="Video Thumbnail" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity">
    
    <!-- Custom Play Button Overlay -->
    <div class="absolute inset-0 flex items-center justify-center">
        <div class="bg-black text-white font-mono font-bold px-6 py-3 border-2 border-white group-hover:bg-white group-hover:text-black transition-colors flex items-center gap-3 shadow-[4px_4px_0px_0px_rgba(255,255,255,1)] group-hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
            <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
            PLAY DEMO
        </div>
    </div>
</div>
```

---

## 3. Diagrams & Code

**Mermaid Diagram (Scrollable)**
*(Note: Requires the Mermaid script block at the bottom of the HTML page with `flowchart: {useMaxWidth: false}` and `sequence: {useMaxWidth: false}`)*
```html
<pre class="mermaid border border-black p-4 bg-slate-50 mb-10 shadow-sm max-h-[400px] overflow-auto cursor-grab">
sequenceDiagram
    participant User
    participant Server
    User->>Server: Request
    Server-->>User: Response
</pre>
```

**Code Block**
```html
<pre class="bg-slate-900 text-green-400 p-4 mb-6 overflow-x-auto font-mono text-sm border border-black leading-relaxed"><code>const char* example = "Hello World";
// Syntax highlighted code here
</code></pre>
```

**Inline Code**
```html
<p>Run the <code class="bg-slate-100 text-red-600 px-1 py-0.5 rounded font-mono text-sm border border-slate-300">npm install</code> command.</p>
```

---

## 4. Components

**Callout / Quote Box (Architectural Decisions)**
```html
<div class="my-8 border-l-4 border-black bg-slate-50 p-6 relative">
    <span class="absolute top-0 left-0 bg-black text-white font-mono text-[10px] px-2 py-1 transform -translate-y-1/2 ml-4">
        Callout Label
    </span>
    <p class="font-serif text-xl italic text-black mt-2">
        "Important architectural note, quote, or key takeaway here."
    </p>
</div>
```

**Standard Table (Bill of Materials / Metrics)**
```html
<table class="w-full text-sm text-left font-sans border-collapse mb-8 mt-8">
    <thead>
        <tr>
            <th class="border border-black bg-slate-100 p-2 font-mono text-xs">Component / Metric</th>
            <th class="border border-black bg-slate-100 p-2 font-mono text-xs">Cost / Value</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="border border-slate-300 p-2">
                <strong>Item Name</strong><br>
                <span class="text-xs text-slate-500">Secondary description text.</span>
            </td>
            <td class="border border-slate-300 p-2">$0.00</td>
        </tr>
        <tr>
            <td class="border border-slate-300 p-2">
                <strong>Highlighted Item</strong>
            </td>
            <td class="border border-slate-300 p-2 font-bold text-green-700">Free</td>
        </tr>
    </tbody>
</table>
```

**Collapsible Accordion (Troubleshooting/Logs)**
```html
<details class="my-8 group border border-black open:bg-slate-50 cursor-pointer">
    <summary class="font-mono text-sm font-bold bg-white p-4 border-b border-transparent group-open:border-black flex justify-between items-center transition-colors hover:bg-slate-100 list-none" style="list-style: none;">
        <span>[+] Expandable Title</span>
        <span class="text-slate-400 group-open:rotate-180 transition-transform">&#9660;</span>
    </summary>
    <div class="p-4 border-t border-black text-sm">
        <p>Hidden content goes here. You can put lists, tables, or text inside.</p>
    </div>
</details>
```
