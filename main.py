import RawLoad

"""
Recreation of Caro-Martin and Sanchez-Campusano's SS-SPDF unsupervised spikesorter published in
Nature under DOI 10.1038/s41598-018-35491-4

Steps described in the paper are as follows:
1) FIR bandpass filter between 450-2050 Hz

Must be a forward-backward filter to avoid phase distortion

2) Threshold Detection

Threshold is defined as Thr = +/-q * sigmaN, sigmaN = median(voltage-with-respect-to-time/0.6745)
TODO: Look into the first-derivative threshold described in the paper

3) Waveforms are then aligned along their negative peak prior to feature extraction

4) Next 6 points are recorded
TODO: Optimize space by doing this feature extraction alongside alignment, no need to hold all the actual waveforms in memory
P1 - First zero-crossing of the first derivative before the action potential has been detected (pre-threshold)
P2 - Valley of the first-derivative of the action potential
P3 - Second zero-crossing of the first derivative at the action potential (threshold)
P4 - Peak of the first-derivative after the action potential
P5 - Third zero-crossing of the first derivative after the action potential (post-threshold)
P6 - Valley of the first-derivative after the action potential

5) Extract shape-based features F1-F11, algebraic definitions enclosed in FeatureDescription.png
F1 - Waveform duration of the first domain of the action potential
F2 - Peak-to-valley amplitude of the first-derivative of the action potential
F3 - Valley-to-calley amplitude of the first-derivative of the action potential
F4 - Correlation coefficient between the first-derivative of the action potential and the reference spike-waveform,
     considering their corresponding standard deviation
F5 - Logarithm of the positive deflection of the first-derivative of the action potential
F6 - Negative deflection of the first-derivative of the action potential
F7 - Logarithm of the slope among valleys of the first-derivative of the action potential
F8 - Root-mean-square of pre-event amplitudes of the first-derivative of the action potential
F9 - Negative slope ratio of the first-derivative of the action potential
F10 - Positive slop ratio of the first-derivative of the action potential
F11 - Peak-to-valley ratio of the first derivative of the action potential

6) Extract phase-space features F12-F19 using the first-derivative and second-derivative of the action potential,
   algebraic definitions enclosed in FeatureDescription.png
F12 - Amplitude of the first-derivative of the action potential relating to P1
F13 - Amplitude of the first-derivative of the action potential relating to P3
F14 - Amplitude of the first-derivative of the action potential relating to P4
F15 - Amplitude of the first-derivative of the action potential relating to P5
F16 - Amplitude of the first-derivative of the action potential relating to P6
F17 - Amplitude of the second-derivative of the action potential relating to P1
F18 - Amplitude of the second-derivative of the action potential relating to P3
F19 - Amplitude of the second-derivative of the action potential relating to P5

7) Extract distribution-based features F20-F24, algebraic definitions enclosed in FeatureDescription.png
F20 - Inter-quartile range (Q3-Q1) of the first-derivative of the action potential, considering percentiles of
      the first-derivative
F21 - Inter-quartile range (Q3-Q1) of the first-derivative of the action potential, considering percentiles of
      the second-derivative
F22 - Kurtosis coefficient of the first-derivative of the action potential, considering the
      fourth sampling moment of n amplitudes about it's mean and standard deviation
F23 - Fisher asymmetry coefficient of the first-derivative of the first-derivative, considering the
      third sampling moment of n amplitudes about it's mean and standard deviation
F24 -Fisher asymmetry coefficient of the second-derivative of the first-derivative, considering the
      third sampling moment of n amplitudes about it's mean and standard deviation

8) Apply K-TOPS clustering
First use K-means clustering, iterating between k = 2 and square root s where s is the total number of spikes
    - This helps separate single unit spikes into unique clusters, with the largest and densest clusters being selected 
      as candidate single-unit clusters
    - After selecting single-unit clusters, other clusters are determined to be overlapping waveforms, multi-unit
      waveforms with small amplitude, stimulus artifacts, and outliers
    - Less representative clusters with small amplitude and non-representative events are automatically exluded
    - Remaining events clearly labelled as outliers are also removed
"""

if __name__ == '__main__':
    pass