Server Queue Performance Model

This program solves and visualizes a first-order ODE that models how a server queue changes over time using SciPy.

Python 3.9 or higher is required.


Quick Start (Recommended)

This project includes a pre-configured .venv folder containing all necessary modules (numpy, scipy, matplotlib). To run the program without installing anything else, use the environment-specific launcher:

Windows:
Run this in powershell

".\.venv\Scripts\python.exe .\Project1-VisualizeODE.py"

MacOS:
Run this in your Terminal:

"./.venv/bin/python Project1-VisualizeODE.py"


Manual Start

Install required packages:

pip install numpy scipy matplotlib

Run

Run the program from the directory containing the script:

python server_queue_model.py

Usage

When prompted, enter:
Request arrival rate λ (requests per second)
Service efficiency μ (1 per second)
Initial queue size x(0)
Simulation time (seconds)

The program will solve the ODE, display a plot of queue size versus time, and print a performance summary.
