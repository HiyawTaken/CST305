Server Queue Performance Model

This program solves and visualizes a first-order ODE that models how a server queue changes over time using SciPy.

Install

Python 3.9 or higher is required.

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
