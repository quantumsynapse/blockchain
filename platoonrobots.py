import numpy as np
import matplotlib.pyplot as plt

# Definindo latitudes e longitudes reais para uma área geográfica (por exemplo, uma região de floresta no Brasil)
lat_base = -23.55  # Latitude base de referência
long_base = -46.63  # Longitude base de referência

# Função para gerar uma variação geográfica de lat e long em uma escala pequena (representando 10.000m²)
def generate_geolocation(lat_base, long_base, variation):
    lat_variation = np.random.uniform(-variation, variation)
    long_variation = np.random.uniform(-variation, variation)
    return lat_base + lat_variation, long_base + long_variation

# Definindo locais de estações bases (bombeiros e militares) com latitudes e longitudes reais
stations_geo = [generate_geolocation(lat_base, long_base, 0.05) for _ in range(3)]  # Três estações

# Função para gerar focos de incêndio distantes das estações base
def generate_distant_fire_spots(stations, min_distance):
    fire_spots_geo = []
    while len(fire_spots_geo) < 3:
        lat, long = generate_geolocation(lat_base, long_base, 0.08)  # Gera latitude e longitude
        if all(np.sqrt((lat - s[0])**2 + (long - s[1])**2) > min_distance for s in stations):
            fire_spots_geo.append((lat, long))
    return fire_spots_geo

# Gerando 3 focos de incêndio distantes das bases de apoio (mínimo de 5 km de distância)
fire_spots_geo = generate_distant_fire_spots(stations_geo, 0.05)

# Capacidades dos drones e rovers
drone_capacities = {
    'drone1': {'capacidade_carga': 10, 'autonomia_voo': 30},  # Capacidade de carga em kg e autonomia em minutos
    'drone2': {'capacidade_carga': 8, 'autonomia_voo': 40},
    'drone3': {'capacidade_carga': 12, 'autonomia_voo': 25},
    'drone4': {'capacidade_carga': 15, 'autonomia_voo': 35},
    'drone5': {'capacidade_carga': 9, 'autonomia_voo': 45},
}

rover_capacities = {
    'rover1': {'capacidade_reboque': 50, 'platoon': True},  # Capacidade de reboque em kg
    'rover2': {'capacidade_reboque': 60, 'platoon': True},
    'rover3': {'capacidade_reboque': 70, 'platoon': False},
}

# Função para exibir informações de coordenadas e comunicação de incêndio
def communicate_fire_spots_geo(fire_spots):
    print("Comunicação de focos de incêndio e coordenadas geográficas (latitude e longitude):")
    for i, spot in enumerate(fire_spots):
        print(f"Foco de incêndio {i + 1}: Latitude: {spot[0]:.6f}, Longitude: {spot[1]:.6f}")

# Mapeando a simulação com as novas informações
plt.figure(figsize=(10, 10))
plt.title('Simulação de Vigilância com Drones e Rovers - Focos de Incêndio e Estações Base (Lat/Long)')

# Plotando estações base (quadrados pretos) com coordenadas reais
for station in stations_geo:
    plt.scatter(station[1], station[0], c='black', marker='s', label='Estações Base', s=200)

# Plotando focos de incêndio (círculos vermelhos com borda preta) distantes das bases
for fire in fire_spots_geo:
    plt.scatter(fire[1], fire[0], facecolor='red', edgecolor='black', marker='o', label='Focos de Incêndio', s=150)

# Simplificando a legenda para mostrar apenas um símbolo de cada
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc='upper right')

# Informações do gráfico
plt.xlabel('Longitude (graus)')
plt.ylabel('Latitude (graus)')
plt.grid(True)
plt.show()

# Exibindo dados no terminal
print("Capacidades dos drones:")
for drone, specs in drone_capacities.items():
    print(f"{drone}: Capacidade de carga: {specs['capacidade_carga']} kg, Autonomia de voo: {specs['autonomia_voo']} minutos")

print("\nCapacidades dos rovers:")
for rover, specs in rover_capacities.items():
    print(f"{rover}: Capacidade de reboque: {specs['capacidade_reboque']} kg, Operação em platoon: {specs['platoon']}")

# Exibindo a comunicação de focos de incêndio no terminal com latitudes e longitudes reais
communicate_fire_spots_geo(fire_spots_geo)

