import numpy as np
import matplotlib.pyplot as plt

# Dimensões da área de mata
area_size = 1000  # 10.000m² representados em 100x100 unidades

# Criando o mapa da área
# 0 = terreno plano, 1 = rio, 2 = lago, 3 = montanha
np.random.seed(42)  # Para reprodução dos resultados
terrain = np.random.choice([0, 1, 2, 3], size=(area_size, area_size), p=[0.85, 0.05, 0.05, 0.05])

# Função para criar drones e rovers
def create_agents(num_drones, num_rovers):
    drones = {
        'x': np.random.randint(0, area_size, size=num_drones),
        'y': np.random.randint(0, area_size, size=num_drones),
        'type': 'drone'
    }
    
    rovers = {
        'x': np.random.randint(0, area_size, size=num_rovers),
        'y': np.random.randint(0, area_size, size=num_rovers),
        'type': 'rover'
    }
    
    return drones, rovers

# Criando 10 drones e 5 rovers
drones, rovers = create_agents(10, 5)

# Função para mover os drones e rovers
def move_agents(drones, rovers):
    for i in range(len(drones['x'])):
        # Movimentação aleatória em uma área de 3x3 ao redor
        drones['x'][i] = np.clip(drones['x'][i] + np.random.randint(-1, 2), 0, area_size - 1)
        drones['y'][i] = np.clip(drones['y'][i] + np.random.randint(-1, 2), 0, area_size - 1)
        
    for i in range(len(rovers['x'])):
        # Movimentação mais restrita devido à natureza terrestre
        rovers['x'][i] = np.clip(rovers['x'][i] + np.random.randint(-1, 2), 0, area_size - 1)
        rovers['y'][i] = np.clip(rovers['y'][i] + np.random.randint(-1, 2), 0, area_size - 1)

# Movendo os agentes algumas vezes para simulação
for _ in range(10):
    move_agents(drones, rovers)

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

# Definindo locais de estações bases onde bombeiros e militares ficam (coordenadas X, Y)
stations = [(10, 10), (80, 80), (50, 50)]

# Simulação de focos de incêndio em coordenadas específicas
fire_spots = [(20, 30), (70, 60), (40, 85)]

# Função para exibir informações de coordenadas e comunicação de incêndio
def communicate_fire_spots(fire_spots):
    print("Comunicação de focos de incêndio e coordenadas (latitude e longitude):")
    for i, spot in enumerate(fire_spots):
        print(f"Foco de incêndio {i + 1}: Coordenadas X: {spot[0]}, Y: {spot[1]}")

# Mapeando a simulação com as novas informações
terrain_color_map = np.zeros((area_size, area_size, 3))

# Atribuindo as cores para o terreno
terrain_color_map[terrain == 0] = [0, 1, 0]  # Verde para terreno plano
terrain_color_map[terrain == 1] = [0, 0, 1]  # Azul para rios
terrain_color_map[terrain == 2] = [0.5, 0.8, 1]  # Azul claro para lagos
terrain_color_map[terrain == 3] = [0.5, 0.5, 0.5]  # Cinza para montanhas

plt.figure(figsize=(10, 10))
plt.title('Simulação de Vigilância com Drones e Rovers - Focos de Incêndio e Estações Base')

# Desenhando o mapa do terreno
plt.imshow(terrain_color_map, interpolation='none')

# Plotando rovers (quadrados azuis)
plt.scatter(rovers['x'], rovers['y'], c='blue', marker='s', label='Rovers', s=100)

# Plotando drones (quadrados vermelhos)
plt.scatter(drones['x'], drones['y'], c='red', marker='s', label='Drones', s=100)

# Plotando estações base (quadrados pretos)
for station in stations:
    plt.scatter(station[0], station[1], c='black', marker='s', label='Estações Base', s=200)

# Plotando focos de incêndio (círculos vermelhos com borda preta)
for fire in fire_spots:
    plt.scatter(fire[0], fire[1], facecolor='red', edgecolor='black', marker='o', label='Focos de Incêndio', s=150)

# Simplificando a legenda para mostrar apenas um símbolo de cada
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc='upper right')

# Informações do gráfico
plt.xlabel('Posição X (metros)')
plt.ylabel('Posição Y (metros)')
plt.grid(True)
plt.show()

# Exibindo dados no terminal
print("Capacidades dos drones:")
for drone, specs in drone_capacities.items():
    print(f"{drone}: Capacidade de carga: {specs['capacidade_carga']} kg, Autonomia de voo: {specs['autonomia_voo']} minutos")

print("\nCapacidades dos rovers:")
for rover, specs in rover_capacities.items():
    print(f"{rover}: Capacidade de reboque: {specs['capacidade_reboque']} kg, Operação em platoon: {specs['platoon']}")

# Exibindo a comunicação de focos de incêndio no terminal
communicate_fire_spots(fire_spots)
