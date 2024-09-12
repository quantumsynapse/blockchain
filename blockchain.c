#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Estrutura de dados para uma cidade
struct Cidade {
    char nome[50];
    double densidade_populacional;        // habitantes/km2 (contínuo)
    double trafego_medio;                 // veículos (milhões) (contínuo)
    double infraestrutura_blockchain;     // nível de adoção de blockchain (1 a 10) (contínuo)
    int area_cidade_km2;                  // km2 (fixo)
    double consumo_energia_medio;         // MW (megawatts) (contínuo)
    double emissao_co2_veicular;          // toneladas de CO2/ano (contínuo)
    double numero_drones;                 // drones em operação (contínuo)
    double numero_veiculos_autonomos;     // veículos autônomos (contínuo)
    double taxa_uso_veiculos_autonomos;   // percentual de uso de veículos autônomos (%) (contínuo)
    double infraestrutura_5g;             // nível de infraestrutura 5G (1 a 10) (contínuo)
    double nivel_mobilidade_sustentavel;  // nível de práticas sustentáveis (1 a 10) (contínuo)
    double emissoes_reduzidas_blockchain; // redução de emissões com blockchain (%) (contínuo)
    double impacto_mobilidade_autonoma;   // impacto geral da mobilidade autônoma (1 a 10) (contínuo)
    double eficiencia_gestao_frotas;      // eficiência da gestão de frotas (1 a 10) (contínuo)
    double nivel_conectividade_iot;       // nível de conectividade via IoT (1 a 10) (contínuo)
    double uso_blockchain_na_gestao;      // nível de uso de blockchain na gestão (1 a 10) (contínuo)
    double custo_operacional_blockchain;  // percentual do custo operacional com blockchain (%) (contínuo)
};

// Função para gerar valores contínuos dentro de um intervalo
double gerarValorAleatorio(double minimo, double maximo) {
    double escala = rand() / (double) RAND_MAX;  // Gera valor entre 0 e 1
    return minimo + escala * (maximo - minimo);  // Escala para o intervalo desejado
}

// Função para simular os cenários em tempo real com valores contínuos
void simularCenario(struct Cidade *cidade) {
    cidade->densidade_populacional = gerarValorAleatorio(7000.0, 16000.0);  // Densidade populacional (hab/km²)
    cidade->trafego_medio = gerarValorAleatorio(2.0, 15.0);                 // Tráfego médio (milhões de veículos)
    cidade->infraestrutura_blockchain = gerarValorAleatorio(6.0, 10.0);     // Nível de blockchain (1 a 10)
    cidade->consumo_energia_medio = gerarValorAleatorio(3000.0, 10000.0);   // Consumo de energia (MW)
    cidade->emissao_co2_veicular = gerarValorAleatorio(200.0, 2000.0);      // Emissão de CO2 (toneladas/ano)
    cidade->numero_drones = gerarValorAleatorio(500.0, 10000.0);            // Drones em operação
    cidade->numero_veiculos_autonomos = gerarValorAleatorio(25.0, 60.0);    // Veículos autônomos em uso
    cidade->taxa_uso_veiculos_autonomos = gerarValorAleatorio(5.0, 15.0);   // Percentual de uso de veículos autônomos
    cidade->infraestrutura_5g = gerarValorAleatorio(6.0, 10.0);             // Infraestrutura 5G (1 a 10)
    cidade->nivel_mobilidade_sustentavel = gerarValorAleatorio(6.0, 10.0);  // Mobilidade sustentável (1 a 10)
    cidade->emissoes_reduzidas_blockchain = gerarValorAleatorio(5.0, 30.0); // Redução de emissões via blockchain (%)
    cidade->impacto_mobilidade_autonoma = gerarValorAleatorio(7.0, 10.0);   // Impacto da mobilidade autônoma (1 a 10)
    cidade->eficiencia_gestao_frotas = gerarValorAleatorio(8.0, 10.0);      // Eficiência de gestão de frotas (1 a 10)
    cidade->nivel_conectividade_iot = gerarValorAleatorio(7.0, 10.0);       // Conectividade via IoT (1 a 10)
    cidade->uso_blockchain_na_gestao = gerarValorAleatorio(6.0, 10.0);      // Uso de blockchain na gestão (1 a 10)
    cidade->custo_operacional_blockchain = gerarValorAleatorio(15.0, 35.0); // Custo operacional do blockchain (%)
}

// Fonte dos dados utilizados
void fontesDados() {
    printf("Fontes dos Dados Utilizados:\n");
    printf("1. Our World in Data: CO2 e Mobilidade\n");
    printf("2. International Energy Agency (IEA): Consumo de Energia\n");
    printf("3. PwC Relatório sobre Cidades Inteligentes: Blockchain e 5G\n");
    printf("4. Relatórios Globais de Mobilidade Autônoma e Drones Urbanos\n\n");
}

int main() {
    srand(time(NULL));  // Inicializa o gerador de números aleatórios

    // Inicializa cidades com dados fixos apenas para a área
    struct Cidade cidades[] = {
        {"São Paulo", 0, 0, 0, 1521, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {"Brasília", 0, 0, 0, 5800, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {"Curitiba", 0, 0, 0, 434, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {"Seoul", 0, 0, 0, 605, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {"Tokyo", 0, 0, 0, 2191, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {"Rio de Janeiro", 0, 0, 0, 1200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
    };

    fontesDados();  // Exibe as fontes dos dados

    // Simular cenários estocásticos para cada cidade
    for (int i = 0; i < 6; i++) {
        simularCenario(&cidades[i]);
        printf("-----------------------------------------\n");
        printf("Simulação em tempo real para a cidade: %s\n", cidades[i].nome);
        printf("Densidade Populacional: %.2f habitantes/km²\n", cidades[i].densidade_populacional);
        printf("Tráfego Médio: %.2f milhões de veículos\n", cidades[i].trafego_medio);
        printf("Infraestrutura de Blockchain: %.2f/10\n", cidades[i].infraestrutura_blockchain);
        printf("Área da Cidade: %d km²\n", cidades[i].area_cidade_km2);
        printf("Consumo Médio de Energia: %.2f MW\n", cidades[i].consumo_energia_medio);
        printf("Emissão de CO2 Veicular: %.2f toneladas/ano\n", cidades[i].emissao_co2_veicular);
        printf("Número de Drones em Uso: %.2f\n", cidades[i].numero_drones);
        printf("Número de Veículos Autônomos: %.2f\n", cidades[i].numero_veiculos_autonomos);
        printf("Taxa de Uso de Veículos Autônomos: %.2f%%\n", cidades[i].taxa_uso_veiculos_autonomos);
        printf("Infraestrutura 5G: %.2f/10\n", cidades[i].infraestrutura_5g);
        printf("Nível de Mobilidade Sustentável: %.2f/10\n", cidades[i].nivel_mobilidade_sustentavel);
        printf("Redução de Emissões com Blockchain: %.2f%%\n", cidades[i].emissoes_reduzidas_blockchain);
        printf("Impacto da Mobilidade Autônoma: %.2f/10\n", cidades[i].impacto_mobilidade_autonoma);
        printf("Eficiência da Gestão de Frotas: %.2f/10\n", cidades[i].eficiencia_gestao_frotas);
        printf("Nível de Conectividade IoT: %.2f/10\n", cidades[i].nivel_conectividade_iot);
        printf("Uso de Blockchain na Gestão: %.2f/10\n", cidades[i].uso_blockchain_na_gestao);
        printf("Custo Operacional com Blockchain: %.2f%%\n", cidades[i].custo_operacional_blockchain);
    }

    return 0;
}
