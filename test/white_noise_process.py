import numpy as np
import matplotlib.pyplot as plt

def white_noise_process(mean: float, std: float, samples: int) -> np.ndarray:
    """
    Генерирует гауссовский белый шум

    Args:
        mean (float): Мат. ожидание
        std (float): Средн. квадратичное отклонение
        samples (int): Количество точек

    Returns:
        np.ndarray: дискретный белый шум
    """
    return np.random.normal(mean, std, size=samples)

if __name__ == "__main__":
    # В данном случае `samples` выступает как отрезок на котором генерируются
    # значения функции белого шума. 
    # TODO: добавить более точное разбиение
    samples = 1000
    noise_lst = white_noise_process(0, 1, samples)

    fig, ax = plt.subplots(figsize=(13, 7), layout='tight')
    
    ax.grid(True)
    
    plt.xlabel("Время, c", fontsize=14, fontweight="bold")
    plt.ylabel("Значение", fontsize=14, fontweight="bold")

    ax.plot(np.linspace(0.0, samples, samples), noise_lst)

    plt.show()