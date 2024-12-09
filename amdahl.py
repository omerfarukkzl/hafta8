def amdahl_law(parallel_fraction, num_processors):
    """
    Amdahl Yasası ile hızlanmayı hesaplar.
    
    Args:
    parallel_fraction (float): Paralel çalışabilen kısmın oranı (0.0 ile 1.0 arasında).
    num_processors (int): İşlemci çekirdeği sayısı.
    
    Returns:
    float: Hızlanma oranı.
    """
    if num_processors == 0:
        raise ValueError("İşlemci sayısı sıfır olamaz.")
    if not (0 <= parallel_fraction <= 1):
        raise ValueError("Paralel kısım oranı 0 ile 1 arasında olmalıdır.")
    
    return 1 / ((1 - parallel_fraction) + (parallel_fraction / num_processors))

try:
    parallel_fraction = float(input("Paralel çalışabilen kısmın oranını gir (0 ile 1 arasında): "))
    num_processors = int(input("İşlemci çekirdeği sayısını gir: "))
    
    speedup = amdahl_law(parallel_fraction, num_processors)
    print(f"{num_processors} işlemci çekirdeği ile hızlanma: {speedup:.2f}")
except ValueError as e:
    print(f"Hata: {e}")
