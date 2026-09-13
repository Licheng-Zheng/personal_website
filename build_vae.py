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
                            <a href="#" target="_blank" class="font-mono text-sm text-blue-600 hover:underline">View on GitHub &nearr;</a>
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
    TITLE="Hyperspectral VAE",
    BREADCRUMB="Hyperspectral VAE",
    H1_TITLE="Hyperspectral VAE",
    STATUS="COMPLETED",
    TECH_STACK="PyTorch, TorchVision",
    ID="utat_vae",
    ABSTRACT="Engineered a Variational Autoencoder tailored specifically for hyperspectral data distributions to compress and analyze data efficiently. The architecture implements a lazy dataset loader for dynamic chunking and utilizes a combined MSE and KL Divergence loss function to enforce a smooth, continuous latent space for reliable data augmentation.",
    TOC="""<a href="#abstract" class="text-slate-500 hover:text-black transition-colors">0. Abstract & Metadata</a>
                    <a href="#architecture" class="text-slate-500 hover:text-black transition-colors">1. Architectural Pipeline</a>
                    <a href="#loss-function" class="text-slate-500 hover:text-black transition-colors">2. Loss Optimization</a>""",
    CONTENT="""<p class="italic text-slate-500 mt-4 border-l-4 border-slate-300 pl-4 mb-10">Insert System Architecture Block Diagram for the Hyperspectral VAE here.</p>

                <h2 id="architecture" class="font-serif text-3xl font-bold border-b border-black pb-2 scroll-mt-24 mt-12 mb-6">1. Architectural Pipeline</h2>

                <p>The system was designed for the strict constraints of hyperspectral image processing, where data dimensions are vast. Rather than generating a single latent vector like a standard autoencoder, the encoder projects the input into a probabilistic latent space defined by a mean ($\mu$) and variance ($\sigma^2$) vector.</p>

                <h3 class="font-bold text-lg mt-6 mb-2">Lazy Dataset Loading & Chunking</h3>
                <p>To prevent out-of-memory (OOM) faults when ingesting hyperspectral imagery, a lazy dataset loader was implemented. It dynamically chunks, rotates, and crops training data into localized kernels before feeding it into the encoder, ensuring the VRAM ceiling is never breached during forward passes.</p>
                
                <h3 class="font-bold text-lg mt-6 mb-2">Probabilistic Encoding</h3>
                <p>The encoder maps the localized hyperspectral chunks into a multi-dimensional Gaussian distribution. The reparameterization trick is applied to sample from this space differentially, feeding a dense vector of size <code>latent_dimension</code> into the decoder network to reconstruct the original geometry.</p>

                <h2 id="loss-function" class="font-serif text-3xl font-bold border-b border-black pb-2 scroll-mt-24 mt-12 mb-6">2. Loss Optimization & Constraints</h2>

                <p>A dual-component loss function was engineered to balance reconstruction accuracy with latent space continuity.</p>

                <ul class="list-disc pl-5 mb-6">
                    <li><strong>Mean Squared Error (MSE):</strong> Enforces pixel-level fidelity between the reconstructed image and the original hyperspectral chunk.</li>
                    <li><strong>Kullback-Leibler (KL) Divergence:</strong> Acts as a regularization term forcing the aggregated posterior distribution to match a standard normal distribution. This ensures the latent space remains smooth. Without this constraint, sampling nearby vectors (e.g., $x + 0.01$) could result in physically impossible artifacts.</li>
                </ul>

                <p class="italic text-slate-500 mt-4 border-l-4 border-slate-300 pl-4 mb-10">Insert Latent Space Visualization / t-SNE Plot here.</p>

                <h3 class="font-bold text-lg mt-6 mb-4">Pipeline Structure</h3>
                <table class="w-full text-sm text-left font-sans border-collapse mb-8">
                    <thead>
                        <tr>
                            <th class="border border-black bg-slate-100 p-2 font-mono text-xs uppercase">Component</th>
                            <th class="border border-black bg-slate-100 p-2 font-mono text-xs uppercase">File Location</th>
                            <th class="border border-black bg-slate-100 p-2 font-mono text-xs uppercase">Execution Role</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border border-slate-300 p-2">HyperspectralEncoder</td>
                            <td class="border border-slate-300 p-2"><code>VAE_v3.py</code></td>
                            <td class="border border-slate-300 p-2">Downsamples chunks to probabilistic $\mu$ and $\sigma^2$</td>
                        </tr>
                        <tr>
                            <td class="border border-slate-300 p-2">HyperspectralDecoder</td>
                            <td class="border border-slate-300 p-2"><code>VAE_v3.py</code></td>
                            <td class="border border-slate-300 p-2">Reconstructs spatial arrays from latent vectors</td>
                        </tr>
                        <tr>
                            <td class="border border-slate-300 p-2">LazyDatasetLoader</td>
                            <td class="border border-slate-300 p-2"><code>VAE_v3.py</code></td>
                            <td class="border border-slate-300 p-2">OOM-safe memory batching and augmentation</td>
                        </tr>
                    </tbody>
                </table>"""
)

with open(r"c:\Users\liche\OneDrive\Desktop\PycharmProjects\Personal_Website\project_pages\utat_vae.html", "w", encoding="utf-8") as f:
    f.write(out)
