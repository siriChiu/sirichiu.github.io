---
title: "Morphological Fingerprint Feature Extraction: Noise Suppression and Structure Enhancement Based on Bowler-Hat Transform"
slug: fingerprint-dirt-fix
date: 2022-04-22
categories:
- Graduate Project
tags: 
- MATLAB
- Image Processing
- Mathematical Morphology
- Feature Extraction
- Noise Reduction
- Fingerprint Recognition

thumbnailImagePosition: left
thumbnailImage: /postImg/fingerprint-dirt-fix/1.jpg
katex: true
---

<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
This project implements an advanced mathematical morphology processing pipeline using **MATLAB**. Through **Top-Hat operations** to filter out background stains, and introducing **Bowler-Hat Transform** for structure enhancement. Experimental results confirm that this algorithm can effectively restore ridge features of contaminated fingerprints while also validating the algorithm's versatility for image processing in different domains.

<!--more-->


---

Fingerprint images and ultrasound vascular images share high topological similarity (both are tubular/linear structures), but also face the same problems of background noise (stains) and insufficient contrast.

---

## 🛑 The Problem

In the preprocessing stage of fingerprint recognition, we commonly face the following challenges:

1.  **Background Noise:** Stains, ink unevenness, or sensor contamination during acquisition create irregular block noise on the image (as shown in the large-area stains in the left image).
2.  **Weak Structure:** Low contrast between fingerprint ridges and valleys causes traditional binarization methods (like Otsu's method) to produce breaks or adhesions.

Our goal is to remove low-frequency background noise while enhancing high-frequency texture, preserving fingerprint details.

---

## 🛠️ Technical Deep Dive

The core concept of this project is viewing fingerprints as "terrain" - ridges are peaks, valleys are troughs, and stains are gentle slopes. We use Mathematical Morphology to separate these features.

### 1. Morphology Fundamentals and Structuring Element
Using **MATLAB**'s Image Processing Toolbox, I first defined the Structuring Element (SE, $B$). To match the physical characteristics of fingerprints, $B$ was designed slightly larger than typical ridge width to ensure correct texture capture.

### 2. Noise Removal: Top-Hat Operations
To remove large-area background stains (low-frequency noise), I used Top-Hat operations.

* **White Top-Hat (WTH):** Extracts features that are brighter than surroundings and smaller than the structuring element (i.e., bright details/ridges).
    $$WTH(f) = f - (f \circ B)$$
    *(Where $\circ$ represents the Opening operation)*

* **Black Top-Hat (BTH):** Extracts features that are darker than surroundings and smaller than the structuring element (i.e., dark details/valleys).
    $$BTH(f) = (f \bullet B) - f$$
    *(Where $\bullet$ represents the Closing operation)*

Through these two operations, we can "peel away" local bright and dark spots from the uneven background.

### 3. Structure Enhancement: Bowler-Hat Transform
Simple Top-Hat often only retains partial information. To simultaneously enhance ridges (bright) and valleys (dark) while maximizing contrast between them, I implemented the **Bowler-Hat Transform (BHT)**.

Referencing *Meftah et al. (2018)*, the standard BHT definition is White Top-Hat minus Black Top-Hat:

$$BHT(f) = WTH(f) - BTH(f)$$

Expanding this:

$$BHT(f) = [f - (f \circ B)] - [(f \bullet B) - f]$$

**Physical Meaning:**
* $WTH(f)$ contributes "positive features" (ridges) in the image.
* $BTH(f)$ contributes "negative features" (valleys) in the image.
* The subtraction operation ($WTH - BTH$) mathematically maximizes local contrast while canceling out slow variations in the background (i.e., removing stains), resulting in clean, high-contrast texture structure.

---

## 📊 Results & Validation

The figure below shows the algorithm's processing results:

![Fingerprint Before-After Comparison](/postImg/fingerprint-dirt-fix/1.jpg)
*Figure 1: Fingerprint enhancement before-after comparison. Left: Original image with severe stains and noise; Right: Result after Bowler-Hat Transform and binarization.*

**Analysis Results:**
* **Noise Reduction:** The large-area blur stains in the top-left corner and edges of the original image were successfully removed. This is because the geometric scale of these stains exceeds our defined structuring element $B$, so they were treated as background and filtered out in Top-Hat operations.
* **Structure Enhancement:** The spiral structure (Whorl) at the fingerprint center became clearly visible, and ridge continuity and separation significantly improved, proving BHT's effectiveness in enhancing tubular structures.

### Conclusion
This project successfully used morphological techniques to solve noise interference problems in fingerprint extraction. More importantly, it served as a validation set, proving that my developed **vascular enhancement algorithm** has strong robustness and cross-domain application potential, capable of effectively processing various biomedical images with "tubular structure" characteristics.