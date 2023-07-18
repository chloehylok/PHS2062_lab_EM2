# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 00:00:12 2022

@author: chlok

PHS2062: Lab 2 EM 2
"""

# Import Statements
import sympy as sp
import numpy as np
import math as math
import matplotlib.pyplot as plt
import monashspa.PHS1011 as spa

# Part 1: Velocity vs Pump Current

current = [1.70, 1.83, 1.96, 2.10, 2.28, 2.42, 2.58, 2.75, 2.89] #A
u_current = 0.02
water_volume = [0.998, 0.913, 0.964, 0.948, 0.97, 0.966, 0.921, 0.969, 0.873] #L
u_water_volume = 0.0035
time = [6.06, 5.31, 5.38, 4.90, 4.63, 4.46, 4.19, 4.44, 3.72] #s
u_time = 0.3

tube_diameter = 0.01302 #m
u_tube_diameter = 0.000005
tube_radius = tube_diameter/2
u_tube_radius = u_tube_diameter/2
area_tube = math.pi*tube_radius**2
u_area_tube = 2*math.pi*tube_radius * u_tube_radius

flow_rate = np.divide(water_volume, time) #L/s
u_flow_rate = flow_rate * ( (np.divide(u_water_volume,water_volume))**2 + (np.divide(u_time, time))**2 )**(1/2)
velocity= flow_rate*10**-3/area_tube #m/s
u_velocity = velocity * ( (np.divide(u_flow_rate,flow_rate))**2 + (np.divide(u_area_tube, area_tube))**2 ) **(1/2)


# Creating plot for Velocity vs Pump Current

stat_fit_results = spa.linear_fit(current, velocity, u_y = u_velocity)
stat_y_fit = stat_fit_results.best_fit
stat_u_y_fit = stat_fit_results.eval_uncertainty(sigma=1)
stat_parameters_from_fit = spa.get_fit_parameters(stat_fit_results)
stat_slope = stat_parameters_from_fit["slope"]
stat_u_slope = stat_parameters_from_fit["u_slope"]
stat_intercept = stat_parameters_from_fit["intercept"]
stat_u_intercept = stat_parameters_from_fit["u_intercept"]

title="Velocity (m/s) vs Pump Current (A)"
pltid=1
fname='rawdata1.png'

plt.figure(pltid)
plt.title(title)
plt.errorbar(current, velocity, yerr=u_velocity, marker=".", linestyle="None", color="red", label="data")
plt.errorbar(current, velocity, xerr=u_current, marker=".", linestyle="None", color="red")
plt.plot(current, stat_y_fit, marker="None", linestyle="-", color="black",label="linear fit for data")
plt.fill_between(current,stat_y_fit-stat_u_y_fit,stat_y_fit+stat_u_y_fit, color="lightgrey",label="uncertainty in linear fit")
plt.xlabel("Pump Current (A)")
plt.ylabel("Velocity (m/s)")
leg = plt.legend(bbox_to_anchor=(1,1))
plt.xlim(1.6, 3)
plt.ylim(0, 2)
plt.show()

# Part 2: Hall Voltage

hall_voltage_1 = [18.700, 19.375, 20.000, 21.250, 23.125, 25.000, 26.250, 26.875, 28.000]
hall_voltage_2 = [18.750, 21.250, 21.875, 25.000, 25.625, 26.250, 27.500, 28.750, 30.000]
hall_voltage_ave = np.divide(np.add(hall_voltage_1,hall_voltage_2),2) / 1000
u_hall_voltage = 0.002


# Creating plot for Hall Voltage vs Pump Current 

hall_fit_results = spa.linear_fit(current, hall_voltage_ave, u_y = u_hall_voltage)
hall_y_fit = hall_fit_results.best_fit
hall_u_y_fit = hall_fit_results.eval_uncertainty(sigma=1)
hall_parameters_from_fit = spa.get_fit_parameters(hall_fit_results)
hall_slope = hall_parameters_from_fit["slope"]
hall_u_slope = hall_parameters_from_fit["u_slope"]
hall_intercept = hall_parameters_from_fit["intercept"]
hall_u_intercept = hall_parameters_from_fit["u_intercept"]

title2="Hall Voltage (V) vs Pump Current (A)"
pltid=2
fname='rawdata2.png'

plt.figure(pltid)
plt.title(title2)
plt.errorbar(current, hall_voltage_ave, yerr=u_hall_voltage, marker=".", linestyle="None", color="blue", label="Hall Voltage")
plt.errorbar(current, hall_voltage_ave, xerr=u_current, marker=".", linestyle="None", color="blue")
plt.plot(current, hall_y_fit, marker="None", linestyle="-", color="black",label="linear fit for data")
plt.fill_between(current,hall_y_fit-hall_u_y_fit,hall_y_fit+hall_u_y_fit, color="lightgrey",label="uncertainty in linear fit")
plt.xlabel("Pump Current (A)")
plt.ylabel("Hall Voltage (V)")
leg = plt.legend(bbox_to_anchor=(1,1))
plt.xlim(1.6, 3)
plt.ylim(0, 0.03)
plt.show()

# Print equation of linearised fits
print("\nFit Results:\n")
print("Velocity vs Current Data Fit:\ny =",round(stat_slope,2),"x","+/-",round(stat_u_slope,2),"+",round(stat_intercept,2),"+/-", round(stat_u_intercept,2))
print("Hall Voltage vs Current Fit:\ny =",round(hall_slope,4),"x","+/-",'%s' % float('%.3g' % hall_u_slope),"+",round(hall_intercept,4),"+/-", '%s' % float('%.3g' % hall_u_intercept))
