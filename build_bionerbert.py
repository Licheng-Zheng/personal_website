import os

TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TITLE} | Licheng Zheng</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;700&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{ extend: {{ fontFamily: {{ sans: ['Inter', 'sans-serif'], serif: ['Playfair Display', 'serif'], mono: ['JetBrains Mono', 'monospace'], }} }} }}
        }}
    </script>
    <style>
        :root {{ color-scheme: light; }}
        ::selection {{ background-color: black; color: white; }}
        .article-body p {{ margin-bottom: 1.5rem; line-height: 1.8; }}
        .article-body ul {{ list-style-type: square; margin-left: 1.5rem; margin-bottom: 1.5rem; }}
        .article-body li {{ margin-bottom: 0.5rem; }}
    </style>
</head>
<body class="bg-white text-black font-sans antialiased min-h-screen flex flex-col">

    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-white border-b border-black w-full px-6 py-4">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-4">
            <a href="../index.html" class="font-serif font-bold text-xl tracking-tight hover:underline block">L. ZHENG</a>
            <div class="flex flex-wrap justify-center gap-6">
                <a href="../index.html" class="font-mono text-sm text-black hover:underline hover:font-bold transition-all">Home</a>
                <a href="../projects.html" class="font-mono text-sm text-black hover:underline hover:font-bold transition-all">Projects</a>
            </div>
        </div>
    </nav>

    <!-- Main Container -->
    <main class="flex-grow max-w-7xl mx-auto w-full px-6 py-12 md:py-16">
        <div class="mb-12 font-mono text-xs text-slate-500 uppercase tracking-widest border-b border-black pb-4">
            <a href="../projects.html" class="hover:text-black hover:underline">&larr; Projects</a> / {BREADCRUMB}
        </div>

        <div class="flex flex-col lg:flex-row gap-12 lg:gap-20 items-start">
            <aside class="hidden lg:block lg:w-64 flex-shrink-0 sticky top-28">
                <span class="font-mono text-xs uppercase font-bold tracking-widest border-b-2 border-black pb-2 mb-4 block w-full">Contents</span>
                <nav class="flex flex-col space-y-3 font-sans text-sm border-l border-slate-300 pl-4">
                    {TOC}
                </nav>
            </aside>

            <article class="flex-grow max-w-3xl article-body">
                <header class="mb-12" id="abstract">
                    <h1 class="font-serif text-5xl md:text-6xl font-bold tracking-tight leading-tight mb-6">{H1_TITLE}</h1>
                    <div class="grid grid-cols-2 md:grid-cols-3 gap-4 border-y border-black py-4 mb-8">
                        <div>
                            <span class="font-mono text-[10px] text-slate-500 uppercase block mb-1">Status</span>
                            <span class="font-mono text-sm font-bold bg-black text-white px-2 py-0.5">{STATUS}</span>
                        </div>
                        <div>
                            <span class="font-mono text-[10px] text-slate-500 uppercase block mb-1">Tech Stack</span>
                            <span class="font-mono text-sm">{TECH_STACK}</span>
                        </div>
                        <div class="col-span-2 md:col-span-1">
                            <span class="font-mono text-[10px] text-slate-500 uppercase block mb-1">Repository</span>
                            <a href="https://github.com/Licheng-Zheng/MLAR-Outside/tree/master/Model%20Documentation" target="_blank" class="font-mono text-sm text-blue-600 hover:underline">View on GitHub &nearr;</a>
                        </div>
                    </div>
                    <p class="font-sans text-xl leading-relaxed text-slate-800 font-bold">
                        {ABSTRACT}
                    </p>
                </header>
                {CONTENT}
            </article>
        </div>
    </main>

    <footer class="border-t border-black bg-white py-6 mt-12">
        <div class="max-w-7xl mx-auto px-6 text-center flex flex-col md:flex-row justify-between items-center gap-4">
            <p class="font-mono text-xs text-slate-500">&copy; 2026 Licheng Zheng.</p>
            <a href="#" class="font-mono text-xs font-bold uppercase hover:underline">&uarr; Back to Top</a>
        </div>
    </footer>
    <script>
        localStorage.setItem('visited_{ID}', 'true');
    </script>
</body>
</html>"""

out = TEMPLATE.format(
    TITLE="BioNERBERT Inference Pipeline",
    BREADCRUMB="BioNERBERT",
    H1_TITLE="BioNERBERT Inference Pipeline",
    STATUS="COMPLETED",
    TECH_STACK="FastAPI, PyTorch, Docker, Google Cloud Run",
    ID="bionerbert",
    ABSTRACT="Engineered a serverless inference pipeline for a custom Biomedical Named Entity Recognition (NER) model featuring a Conditional Random Fields (CRF) layer. Bypassed the architectural constraints of standard managed API services by containerizing a PyTorch and FastAPI backend with Docker, scaling dynamically to zero on Google Cloud Run to optimize infrastructure costs.",
    TOC="""<a href="#abstract" class="text-slate-500 hover:text-black transition-colors">0. Abstract & Metadata</a>
                    <a href="#architecture" class="text-slate-500 hover:text-black transition-colors">1. MLOps & Serverless Constraints</a>
                    <a href="#scalability" class="text-slate-500 hover:text-black transition-colors">2. Scalability & Cold Starts</a>
                    <a href="#security" class="text-slate-500 hover:text-black transition-colors">3. Security & Rate Limiting</a>""",
    CONTENT="""<p class="italic text-slate-500 mt-4 border-l-4 border-slate-300 pl-4 mb-10">Insert Application Screenshot / Live Demo Frontend Render here.</p>

                <h2 id="architecture" class="font-serif text-3xl font-bold border-b border-black pb-2 scroll-mt-24 mt-12 mb-6">1. MLOps Architecture & Serverless Constraints</h2>

                <p>Standard managed serverless inference endpoints (e.g., Hugging Face Inference Endpoints) enforce rigid model architecture constraints for security and sandboxing. Because this custom NER model utilizes a Conditional Random Fields (CRF) layer stacked upon the fine-tuned PubMedBERT backbone, standard free-tier inference APIs flag the execution of the custom CRF logic.</p>

                <p>To bypass this architectural limitation without spinning up expensive persistent EC2/GCE instances, a custom serving layer was engineered using FastAPI and PyTorch. The entire runtime was containerized with Docker and deployed to Google Cloud Run, allowing arbitrary model architectures to execute in a serverless, horizontally scaling environment.</p>
                
                <h2 id="scalability" class="font-serif text-3xl font-bold border-b border-black pb-2 scroll-mt-24 mt-12 mb-6">2. Scalability & Cold Starts</h2>

                <p>To strictly minimize costs, the Cloud Run instance scales to exactly 0 when inactive. Upon receiving a cold-start invocation, the container initializes the FastAPI server and pulls the ~400MB <code>.pt</code> weights directly from the Hugging Face Hub at runtime before beginning inference. This incurs a deliberate latency penalty of approximately 60 seconds during a cold start, trading execution speed for absolute cost efficiency.</p>

                <p class="italic text-slate-500 mt-4 border-l-4 border-slate-300 pl-4 mb-10">Insert Mermaid Sequence Diagram mapping the User -> FastAPI -> Hugging Face -> Inference flow here.</p>

                <h2 id="security" class="font-serif text-3xl font-bold border-b border-black pb-2 scroll-mt-24 mt-12 mb-6">3. Security & Rate Limiting</h2>

                <p>Due to the unpredictable scaling behavior of serverless instances under load, deliberate bottlenecks were engineered to prevent billing saturation.</p>

                <ul class="list-disc pl-5 mb-6">
                    <li><strong>Horizontal Cap:</strong> Cloud Run instances are strictly capped using <code>--max-instances 2</code> to prevent a high-traffic spike from causing unbounded infrastructure costs.</li>
                    <li><strong>Payload Constraints:</strong> Pydantic <code>Field(max_length=5000)</code> constraints are enforced at the API routing layer. Maliciously large payloads are instantly rejected via a 422 Unprocessable Entity response before they can saturate the PyTorch inference execution loop.</li>
                    <li><strong>Secrets Injection:</strong> Hugging Face API tokens for weight retrieval are isolated from the Docker image and injected at runtime via Google Cloud Console, pending migration to Google Cloud Secret Manager.</li>
                </ul>"""
)

with open(r"c:\Users\liche\OneDrive\Desktop\PycharmProjects\Personal_Website\project_pages\bionerbert.html", "w", encoding="utf-8") as f:
    f.write(out)
