# Final Pre-Deployment Review Checklist

Use this checklist to systematically review your portfolio before pushing it live. 

## 1. Missing Assets
- [x] **Resume**: Drop your actual resume into `assets/documents/resume.pdf`.
- [x] **Propeller Optimizer Report**: Drop the validation report into `assets/data/propeller_optimizer_report.pdf`.
- [x] **Timmy & Tommy PCA Plot**: Add `pca_plot.webp` to `assets/images/projects/timmy_and_tommy/` (This is the final unchecked image from `IMAGE_CHECKLIST.md`).

## 2. Content & Copywriting Review
- [ ] **Homepage (`index.html`)**: Read through your "About Me" and "Context and Background" sections. Ensure the tone is professional, confident, and accurately reflects your current goals.
- [ ] **Project Pages**: Read through the descriptions on every project page (`compoxel.html`, `timmy_and_tommy.html`, etc.). Look for any lingering placeholder text or "TODOs" in the paragraphs.
- [ ] **Metadata**: Check that the "Tech Stack" and "Status" metadata at the top of each project page is accurate.

## 3. External Links Validation
- [ ] **Socials**: Click the **GitHub** and **LinkedIn** buttons on your homepage to ensure they route to your exact profiles.
- [ ] **Project Repos**: Click the "View on GitHub &nearr;" links on each project page to ensure they point to the correct public repositories.
- [ ] **Live Apps**: Test the "Live App" links for BioNERBERT and Timmy & Tommy on the `projects.html` grid.
- [ ] **Task Tracker**: Ensure the Task Tracker telemetry links route to your actual live dashboard.

## 4. Mobile & UI Testing
- [ ] **Mobile Layout**: Open the site in your browser, press `F12`, and toggle the "Device Toolbar" (or just shrink the window horizontally). Make sure the navigation, masonry grid on the homepage, and project text scale nicely on mobile.
- [ ] **D3 Graphs**: Ensure the interactive D3 nodes on `projects.html` and individual project pages are usable and don't overflow on small screens.
- [ ] **Scroll Progress Bars**: Scroll down a long project page and verify the black progress bar at the very top of the screen fills up correctly.

## 5. Performance & Cleanup
- [ ] **Lighthouse Audit**: Run a quick Google Lighthouse audit in Chrome DevTools on your homepage to catch any last-minute contrast or SEO issues.
- [ ] **Delete Draft Files**: Delete any sandbox files that shouldn't be deployed to your live server (e.g., `components.html`, `test.html`, `sample_long_post.html`, and the old `blog_posts/` folder).

## 6. Deployment Setup
- [ ] Ensure your root directory has an `index.html`. (It does!)
- [ ] Push the final codebase to your hosting provider (GitHub Pages, Vercel, Netlify, etc.).
