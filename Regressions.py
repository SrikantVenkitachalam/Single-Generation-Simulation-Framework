'''
Authors: 
    Srikant Venkitachalam, Amitabh Joshi

Affiliation: 
    Jawaharlal Nehru Centre for Advanced Scientific Research,
    Bengaluru, India - 560064

Purpose of this code:
Generates the scatter plots for total or effective density vs. survivorship or mean/variance of time to wandering for the full framework design under the expanded model (see Manuscript/chapter 6 in thesis). Also performs linear regressions for survivorship as predicted by total or effective density.

NOTE: Please change the required directories for saving/reading data!!!
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
import scipy

Total_Data = pd.read_excel('Results/Compiled_Total30.xlsx', sheet_name = 'TotalData')


sns.set_theme(style='white', font = 'Arial', rc = {
    'axes.spines.right' : False,
    'axes.spines.top' : False,
    'xtick.bottom' : True,
    'ytick.left' : True,
    'axes.edgecolor' : 'black',
    'xtick.color' : 'black',
    'ytick.color' : 'black',
    'text.color' : 'black', 
    'figure.facecolor' : 'white', 
    'axes.labelcolor' : 'black'
    })



############## Survivorship ##################################################

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()


for axis in ['left', 'bottom']:
    ax1.spines[axis].set_linewidth(2)
    ax2.spines[axis].set_linewidth(2)


# Surv Total Density Regression

X = np.array(Total_Data['TotDens'])
Y = np.array(Total_Data['Surv'])

xaxis = np.arange(0, 601, 100)


slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X, Y)

slope2, intercept2 = np.polyfit(X, Y, 1)

assert (np.round(slope, 4)==np.round(slope2, 4) and 
        np.round(intercept, 4)==np.round(intercept2, 4))

yaxis = intercept + slope * xaxis

print('Total Density Survivorship R^2 = ', np.round(r_value**2, 2))

sns.scatterplot(ax = ax1, data = Total_Data, x = 'TotDens', y = 'Surv', 
                s = 100, marker = 'o', facecolor = 'plum', 
                edgecolor = 'purple', alpha = 0.9)

sns.lineplot(ax = ax1, x = xaxis, y = yaxis, color = 'purple', linewidth = 2)

ax1.text(450, 0.8, 'R^2 = ' + str(np.round(r_value**2, 4)))



ax1.set_ylim(0, 1.1)
ax1.set_xlim(0, 620)
ax1.set_xlabel('Total Density')
ax1.set_ylabel('Survivorship')


# Surv Effective Density Regression

X = np.array(Total_Data['EffDens'])
Y = np.array(Total_Data['Surv'])

xaxis = np.arange(0, 601, 100)


slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X, Y)

slope2, intercept2 = np.polyfit(X, Y, 1)

assert (np.round(slope, 4)==np.round(slope2, 4) and 
        np.round(intercept, 4)==np.round(intercept2, 4))

yaxis = intercept + slope * xaxis

print('Effective Density Survivorship R^2 = ', np.round(r_value**2, 2))

sns.scatterplot(ax = ax2, data = Total_Data, x = 'EffDens', y = 'Surv', 
                s = 100, marker = 'o', facecolor = 'lemonchiffon', 
                edgecolor = 'gold', alpha = 0.9)

sns.lineplot(ax = ax2, x = xaxis, y = yaxis, color = 'gold', linewidth = 2)

ax2.text(450, 0.8, 'R^2 = ' + str(np.round(r_value**2, 4)))

ax2.set_ylim(0, 1.1)
ax2.set_xlim(0, 620)
ax2.set_xlabel('Effective Density')
ax2.set_ylabel('Survivorship')



######### Log Survivorship ##################################################

fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()


for axis in ['left', 'bottom']:
    ax3.spines[axis].set_linewidth(2)
    ax4.spines[axis].set_linewidth(2)


# Log Surv Total Density Regression

X = np.array(Total_Data['TotDens'])
Y = np.log(np.array(Total_Data['Surv']))

xaxis = np.arange(0, 601, 100)


slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X, Y)

slope2, intercept2 = np.polyfit(X, Y, 1)

assert (np.round(slope, 4)==np.round(slope2, 4) and 
        np.round(intercept, 4)==np.round(intercept2, 4))

yaxis = intercept + slope * xaxis

print('Total Density Log Survivorship R^2 = ', np.round(r_value**2, 2))

sns.scatterplot(ax = ax3, x = X, y = Y, 
                s = 100, marker = 'o', facecolor = 'plum', 
                edgecolor = 'purple', alpha = 0.9)

sns.lineplot(ax = ax3, x = xaxis, y = yaxis, color = 'purple', linewidth = 2)

ax3.text(450, -0.25, 'R^2 = ' + str(np.round(r_value**2, 4)))



ax3.set_ylim(-2.1, 0.1)
ax3.set_xlim(0, 620)
ax3.set_xlabel('Total Density')
ax3.set_ylabel('Log Survivorship')


# Log Surv Effective Density Regression

X = np.array(Total_Data['EffDens'])
Y = np.log(np.array(Total_Data['Surv']))

xaxis = np.arange(0, 601, 100)


slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X, Y)

slope2, intercept2 = np.polyfit(X, Y, 1)

assert (np.round(slope, 4)==np.round(slope2, 4) and 
        np.round(intercept, 4)==np.round(intercept2, 4))

yaxis = intercept + slope * xaxis

print('Effective Density Log Survivorship R^2 = ', np.round(r_value**2, 2))

sns.scatterplot(ax = ax4, x = X, y = Y, 
                s = 100, marker = 'o', facecolor = 'lemonchiffon', 
                edgecolor = 'gold', alpha = 0.9)

sns.lineplot(ax = ax4, x = xaxis, y = yaxis, color = 'gold', linewidth = 2)

ax4.text(450, -0.25, 'R^2 = ' + str(np.round(r_value**2, 4)))

ax4.set_ylim(-2.1, 0.1)
ax4.set_xlim(0, 620)
ax4.set_xlabel('Effective Density')
ax4.set_ylabel('Log Survivorship')

########### Mean Wandering Time ############################################

fig5, ax5 = plt.subplots()
fig6, ax6 = plt.subplots()


for axis in ['left', 'bottom']:
    ax5.spines[axis].set_linewidth(2)
    ax6.spines[axis].set_linewidth(2)

# mWander Total Density Regression


X = np.array(Total_Data['TotDens'])
Y = np.array(Total_Data['mWander'])

xaxis = np.arange(0, 601, 100)


slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X, Y)

slope2, intercept2 = np.polyfit(X, Y, 1)

assert (np.round(slope, 4)==np.round(slope2, 4) and 
        np.round(intercept, 4)==np.round(intercept2, 4))

yaxis = intercept + slope * xaxis

print('Total Density Mean Wandering Time R^2 = ', np.round(r_value**2, 2))

sns.scatterplot(ax = ax5, data = Total_Data, x = 'TotDens', y = 'mWander', 
                s = 100, marker = 'o', facecolor = 'plum', 
                edgecolor = 'purple', alpha = 0.9)

sns.lineplot(ax = ax5, x = xaxis, y = yaxis, color = 'purple', linewidth = 2)

ax5.text(450, 150, 'R^2 = ' + str(np.round(r_value**2, 4)))

# ax5.set_ylim(0, 1.1)
ax5.set_xlim(0, 620)
ax5.set_xlabel('Total Density')
ax5.set_ylabel('Mean Time to Wandering (hrs)')

# mWander Effective Density Regression

X = np.array(Total_Data['EffDens'])
Y = np.array(Total_Data['mWander'])

xaxis = np.arange(0, 601, 100)


slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X, Y)

slope2, intercept2 = np.polyfit(X, Y, 1)

assert (np.round(slope, 4)==np.round(slope2, 4) and 
        np.round(intercept, 4)==np.round(intercept2, 4))

yaxis = intercept + slope * xaxis

print('Effective Density Mean Wandering Time R^2 = ', np.round(r_value**2, 2))


sns.scatterplot(ax = ax6, data = Total_Data, x = 'EffDens', y = 'mWander', 
                s = 100, marker = 'o', facecolor = 'lemonchiffon', 
                edgecolor = 'gold', alpha = 0.9)

sns.lineplot(ax = ax6, x = xaxis, y = yaxis, color = 'gold', linewidth = 2)

ax6.text(450, 150, 'R^2 = ' + str(np.round(r_value**2, 4)))

# ax6.set_ylim(0, 1.1)
ax6.set_xlim(0, 620)
ax6.set_xlabel('Effective Density')
ax6.set_ylabel('Mean Time to Wandering (hrs)')



######### Variance Wandering Time #########################################

fig7, ax7 = plt.subplots()
fig8, ax8 = plt.subplots()


for axis in ['left', 'bottom']:
    ax7.spines[axis].set_linewidth(2)
    ax8.spines[axis].set_linewidth(2)

# vWander Total Density Regression

X = np.array(Total_Data['TotDens'])
Y = np.array(Total_Data['vWander'])

xaxis = np.arange(0, 601, 100)


slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X, Y)

slope2, intercept2 = np.polyfit(X, Y, 1)

assert (np.round(slope, 4)==np.round(slope2, 4) and 
        np.round(intercept, 4)==np.round(intercept2, 4))

yaxis = intercept + slope * xaxis

print('Total Density Variance Wandering Time R^2 = ', np.round(r_value**2, 2))


sns.scatterplot(ax = ax7, data = Total_Data, x = 'TotDens', y = 'vWander', 
                s = 100, marker = 'o', facecolor = 'plum', 
                edgecolor = 'purple', alpha = 0.9)

sns.lineplot(ax = ax7, x = xaxis, y = yaxis, color = 'purple', linewidth = 2)

ax7.text(450, 70000, 'R^2 = ' + str(np.round(r_value**2, 4)))

# ax8.set_ylim(0, 1.1)
ax7.set_xlim(0, 620)
ax7.set_xlabel('Total Density')
ax7.set_ylabel('Variance Time to Wandering (hrs^2)')


# vWander Effective Density Regression


X = np.array(Total_Data['EffDens'])
Y = np.array(Total_Data['vWander'])

xaxis = np.arange(0, 601, 100)


slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X, Y)

slope2, intercept2 = np.polyfit(X, Y, 1)

assert (np.round(slope, 4)==np.round(slope2, 4) and 
        np.round(intercept, 4)==np.round(intercept2, 4))

yaxis = intercept + slope * xaxis

print('Effective Density Variance Wandering Time R^2 = ', 
      np.round(r_value**2, 2))

sns.scatterplot(ax = ax8, data = Total_Data, x = 'EffDens', y = 'vWander', 
                s = 100, marker = 'o', facecolor = 'lemonchiffon', 
                edgecolor = 'gold', alpha = 0.9)

sns.lineplot(ax = ax8, x = xaxis, y = yaxis, color = 'gold', linewidth = 2)

ax8.text(450, 70000, 'R^2 = ' + str(np.round(r_value**2, 4)))

# ax9.set_ylim(0, 1.1)
ax8.set_xlim(0, 620)
ax8.set_xlabel('Effective Density')
ax8.set_ylabel('Variance Time to Wandering (hrs^2)')
        



# fig1.savefig('Results/Plots/SurvTotEffComp.png', dpi=300)

# fig2.savefig('Results/Plots/SurvTotReg.png', dpi=300)

fig3.savefig('Results/Plots/LogSurvTotReg.png', dpi=300)


fig4.savefig('Results/Plots/LogSurvEffReg.png', dpi=300)

# fig5.savefig('Results/Plots/mWanderTotReg.png', dpi=300)

# fig6.savefig('Results/Plots/mWanderEffReg.png', dpi=300)


# fig7.savefig('Results/Plots/vWanderTotEffComp.png', dpi=300)

# fig8.savefig('Results/Plots/vWanderTotReg.png', dpi=300)

# fig9.savefig('Results/Plots/vWanderEffReg.png', dpi=300)
