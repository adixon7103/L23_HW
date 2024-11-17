## main.py
import numpy as np
import matplotlib.pyplot as plt

def sine_wave(frequency=1.0, amplitude=1.0, duration=1.0, sampling_rate=44100):

    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    y = amplitude * np.sin(2 * np.pi * frequency * t)

    return t, y

def plot_sine_wave(frequency=1.0, amplitude=1.0, duration=1.0, sampling_rate=44100):

    t, y = sine_wave(frequency, amplitude, duration, sampling_rate)

    plt.figure(figsize=(10, 4))
    plt.plot(t, y)
    plt.title(f"Sine Wave - {frequency} HZ")
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (dB')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    plot_sine_wave(frequency=1.0, amplitude=1.0, duration=1.0, sampling_rate=44100)