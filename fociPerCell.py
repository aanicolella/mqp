# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:32:00 2020

@author: Ally Nicolella
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

'''foci = pd.read_csv('./data/foci_first20-15.csv')
nuclei = pd.read_csv('./data/Nuclei_first20-15.csv')
image = pd.read_csv('./data/Image_first20-15.csv')'''
foci = pd.read_csv('./data/merge1/foci_Merge_1_216.csv')
nuclei = pd.read_csv('./data/merge1/Nuclei_Merge_1_216.csv')
image = pd.read_csv('./data/merge1/Image_Merge_1_216.csv')

# Plotting num foci/cell from frame to frame
    
'''for i in range(1,217):
    temp = nuclei[nuclei['ImageNumber'] == i]
    figName = "./plots/merge1/fociNumByFrame/frame" + str(i) + ".png"
    freq = temp['Children_foci_Count'].value_counts()
    dam = freq[freq.index > 0 ]
    fig, ax = plt.subplots()
    ax.set_ylabel('Num Cells with x foci')
    ax.set_xlabel('Number of Foci')
    ax.set_title('Frequency of # Foci/Cell in Frame ' + str(i))
    plt.plot(dam.sort_index())
    plt.savefig(figName)'''

    
'''# Stack chart of ordered # foci/cell/image for first 20 images
    
fig, ax = plt.subplots(5,4)
fig.suptitle('A) Frequency of # Foci/Cell by Image (first 20 frames)')
    
for i in range(1,21):
    temp = nuclei[nuclei['ImageNumber'] == i]
    freq = temp['Children_foci_Count'].value_counts()
    dam = freq[freq.index > 0 ]
    if i < 5:
        ax[0,i-1].plot(dam.sort_index())
    elif 5 <= i < 9:
        ax[1,i-5].plot(dam.sort_index())
    elif 9 <= i < 13:
        ax[2,i-9].plot(dam.sort_index())
    elif 13 <= i < 17:
        ax[3,i-13].plot(dam.sort_index())
    else:
        ax[4,i-17].plot(dam.sort_index())        

plt.savefig('./plots/merge1/fociNumByFrame/first20Stack.png')

# Stack chart of ordered # foci/cell/image for first 20 images        
        
fig, ax = plt.subplots(5,4)
fig.suptitle('B) Frequency of # Foci/Cell by Image (last 20 frames)')
    
for i in range(197,217):
    temp = nuclei[nuclei['ImageNumber'] == i]
    freq = temp['Children_foci_Count'].value_counts()
    dam = freq[freq.index > 0 ]
    if i < 201:
        ax[0,i-201].plot(dam.sort_index())
    elif 201 <= i < 205:
        ax[1,i-201].plot(dam.sort_index())
    elif 205 <= i < 209:
        ax[2,i-205].plot(dam.sort_index())
    elif 209 <= i < 213:
        ax[3,i-209].plot(dam.sort_index())
    else:
        ax[4,i-213].plot(dam.sort_index())        

plt.savefig('./plots/merge1/fociNumByFrame/last20Stack.png')'''

# Stacked bar chart of # of foci/cell/image in first 20 images
        
merge = pd.DataFrame(index=list(range(1,10)))
merge2 = pd.DataFrame(index=list(range(1,1)))
label = []

for i in range(1,21):
    temp = nuclei[nuclei['ImageNumber'] == i]
    freq = temp['Children_foci_Count'].value_counts()
    dam = (freq[freq.index > 0]).sort_index()
    merge['image{}'.format(i)] = dam
    label.append("first20")

#merge.loc[len(merge)] = "first20"
    
for i in range(197,217):
    temp = nuclei[nuclei['ImageNumber'] == i]
    freq = temp['Children_foci_Count'].value_counts()
    dam = (freq[freq.index > 0]).sort_index()
    merge2['image{}'.format(i)] = dam
    label.append("last20")
 
#merge2.loc[len(merge2)] = "last20"


mergeFinal = pd.concat([merge, merge2], axis=1, sort=False)

ax = mergeFinal.plot.bar(rot=0, legend=False, color=['C0', 'C0', 'C0', 'C0', 'C0', 'C0', 'C0', 'C0', 'C0', 'C0','C0', 'C0', 'C0', 'C0', 'C0', 'C0', 'C0', 'C0', 'C0', 'C0','C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1','C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1', 'C1'])
#ax.legend(label)
ax.set_title('Frequency of the # of foci per cell')
ax.set_ylabel('Frequency of n foci per cell')
ax.set_xlabel('# of foci')

'''
ax = merge.plot.bar(rot=0)
ax.set_title('Frequency of the # of foci per cell (first 20 frames)')
ax.set_ylabel('Frequency of n foci per cell')
ax.set_xlabel('# of foci')
#plt.savefig('./plots/merge1/fociNumByFrame/first20Column.png')

ax2 = merge2.plot.bar(rot=0)
ax2.set_title('Frequency of the # of foci per cell (last 20 frames)')
ax2.set_ylabel(('Frequency of n foci per cell'))
ax2.set_xlabel('# of foci')
#plt.savefig('./plots/merge1/fociNumByFrame/last20Column.png')
'''
  
# Avg num foci/cell (generalized)
# Take overall population from each frame and plot avg num foci for each frame
'''avg = []
for i in range(1,217):
    frame = foci[foci['ImageNumber'] == i]
    avg.append(frame['Parent_Nuclei'].value_counts().mean())

fig, ax = plt.subplots()
ax.set_ylabel('Average # Foci/Cell Displaying Damage')
ax.set_xlabel('Frame Number')
ax.set_title('Average Foci/Cell')
#plt.bar(range(1,216),avg,tick_label=range(1,21))
plt.plot(range(1,217),avg)
plt.savefig("./plots/merge1/avgOverTime.png")'''

# Number of cells identified over time + percentage of cells damaged over time

'''
damage = []

for i in range(1,217):
    temp = nuclei[nuclei['ImageNumber'] == i]
    total = temp['ImageNumber'].count()
    numDamage = (temp[temp['Children_foci_Count'] > 0]).count()['ImageNumber']
    percent = numDamage/total
    damage.append(percent*100)
    
numCells = []

for i in range(0,216):
    temp1 = image[image.index == i]
    val = temp1['Count_Nuclei']
    numCells.append(val.values[0])

fig, ax1 = plt.subplots()

# percent damage
ax1.set_ylabel('% Cells Damaged')
ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_xlabel('Frame Number')
ax1.set_title('% Cells Damaged vs # Cells Detected')
plt.plot(range(1,217),damage, label='% of cells damaged')
plt.legend()

# num cells/timepoint
ax2 = ax1.twinx()
ax2.set_ylabel('# Cells Detected')
plt.plot(numCells, color='tab:red', label='# cells identified')
ax2.tick_params(axis='y', labelcolor='tab:red')
plt.legend()


plt.savefig("./plots/merge1/damageOverTime.png")
'''


'''
Bonus graphs not kept/reported in paper
'''

# Plot num foci/cell from frame to frame, not arranged in descending order/frequency

'''for i in range(1,21):
    temp = nuclei[nuclei['ImageNumber'] == i]
    figName = "./plots/fociNumByFrame/frame" + str(i) + ".png"
    fig, ax = plt.subplots()
    ax.set_ylabel('Num Foci')
    ax.set_xlabel('Parent_Nuclei')
    ax.set_title('Num Foci/Cell in Frame ' + str(i))
    plt.plot(temp['ObjectNumber'],temp['Children_foci_Count'])
    #plt.savefig(figName)'''


# Stacked Num foci/cell/frame, unordered

'''fig, ax = plt.subplots(5,4)
#ax.set_ylabel('Num Foci')
#ax.set_xlabel('Parent_Nuclei')
fig.suptitle('Num Foci/Cell by Image')
    
for i in range(1,21):
    temp = nuclei[nuclei['ImageNumber'] == i]
    #figName = "./plots/fociNumByFrame/frame" + str(i) + ".png"
    #plt.plot(temp['Parent_Nuclei'].unique(),temp['Parent_Nuclei'].value_counts())
    if i < 5:
        ax[0,i-1].plot(temp['ObjectNumber'],temp['Children_foci_Count'])
    elif 5 <= i < 9:
        ax[1,i-5].plot(temp['ObjectNumber'],temp['Children_foci_Count'])
    elif 9 <= i < 13:
        ax[2,i-9].plot(temp['ObjectNumber'],temp['Children_foci_Count'])
    elif 13 <= i <= 16:
        ax[3,i-13].plot(temp['ObjectNumber'],temp['Children_foci_Count'])
    else:
        ax[4,i-17].plot(temp['ObjectNumber'],temp['Children_foci_Count'])        

#plt.savefig('./plots/54Stack.png')'''


'''fig, ax = plt.subplots(2)
ax[0].set_ylabel('Percent Cells Damaged')
ax[1].set_ylabel('Percent Cells Undamaged')
ax[1].set_xlabel('Frame Number')
fig.suptitle('Percent Damaged vs Non-Damaged Over Time')
ax[0].plot(range(1,21),damage)
ax[1].plot(range(1,21),nonDam)
plt.savefig("./plots/damageOT.png")'''


# Grab numFoci for each nuclei frame to frame and plot overall avg for that cell over time
# Percentage of cells w/ and w/o damage over time

'''damage = []
nonDam = []

for i in range(1,21):
    temp = nuclei[nuclei['ImageNumber'] == i]
    total = temp.count()['ImageNumber']
    numDamage = (temp[temp['Children_foci_Count'] > 0]).count()['ImageNumber']
    damage.append(numDamage/total)
    nonDam.append(1-(numDamage/total))

fig, ax = plt.subplots()
ax.set_ylabel('PercentDamage')
plt.yscale('logit')
ax.set_xlabel('Frame Number')
ax.set_title('Percent Damaged vs Non-Damaged Over Time')
plt.plot(range(1,21),damage,label='Damaged')
plt.plot(range(1,21),nonDam,label='Undamaged')
ax.legend()
plt.savefig("./plots/damageOverTime.png")'''

