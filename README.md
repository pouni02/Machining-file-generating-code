This repository contains a set of Python tools to generate and process machining files for a Roland MDX-40A milling machine.

 --> The main goal is to reduce machining time and cost by :

- Limiting tool changes during the process

- Avoiding unnecessary manual steps

- Providing visualization tools to check toolpaths on the stock

The project is divided into several steps : 

 Step 1 – Merge machining files

Problem: In the standard workflow, each operation (drilling, pocketing, contouring…) is saved in a separate file. The operator must stop the machine and manually load the next file, which is inefficient.

Solution: Merge all machining files that use the same tool into a single file.

Example: group all drilling operations done with a ∅2 mm drill bit in one file.

Implementation : PyQt5 interface where the user selects multiple input files, and the program outputs a merged file.

 Step 2 – Transformations (Translation & Rotation)

Problem: By default, toolpaths are generated for a single part. To produce multiple parts on the 305×305 mm stock, manual repositioning is needed.

Solution: Apply automatic translation and rotation of the toolpaths to place multiple parts within the stock dimensions.

Implementation:

Extract only the necessary coordinate instructions (Z... lines).

Apply coordinate transformations.

Output a new machining file with transformed toolpaths.

 Step 3 – Series machining (Multiple parts on the same stock)

Problem: When producing several identical parts, the operator must manually repeat the process for each one. This leads to wasted time and a higher risk of positioning errors.

Solution: Automate the duplication of a single part’s toolpaths over the 305×305 mm stock.

The user specifies the number of repetitions (e.g., 3×2 grid of parts).

The program applies systematic translations of the original coordinates to place each part in the stock.

Implementation:

Parse the machining file to extract coordinates.

Apply a translation offset for each new part (e.g., +100 mm in X for the next part, +100 mm in Y for the next row).

Generate a single output file containing the toolpaths for all repeated parts.

Benefit:

Avoids restarting the machine for each part.

Makes full use of the stock dimensions.

Reduces operator workload and machining time.

🔹 Toolpath Visualization

Purpose: Allow the operator to visualize toolpaths before machining, to validate part placement and stock usage.

Implementation: Python + Matplotlib

The stock (305×305 mm) is displayed as a bounding box.

Toolpaths are drawn in different colors (depending on passes or files).

🛠️ Technologies

Python (NumPy, Matplotlib)

PyQt5 (GUI for file selection & user interaction)

