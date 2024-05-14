# Gerador de Lista de Estabelecimentos
Este é um programa em Python que utiliza a biblioteca Selenium para automatizar a navegação no Google Maps e extrair informações sobre estabelecimentos comerciais, como nome, endereço e contato telefônico. As informações extraídas são então organizadas em um arquivo Excel para posterior análise ou referência.

## Requisitos:
Python 3.12.1

Bibliotecas Python:

Selenium

Pandas

Chromedriver_autoinstaller_fix

Webdriver_manager

## Instalação
Clone ou faça o download deste repositório para o seu computador.

Instale as dependências Python executando o seguinte comando no terminal:
"pip install selenium pandas chromedriver_autoinstaller_fix webdriver_manager"

Certifique-se de ter o Google Chrome instalado em seu sistema, pois o programa usa o navegador Chrome para automatizar a navegação no Google Maps.

## Como Usar
Execute o arquivo table_stablishments.py em um ambiente Python.

Quando solicitado, insira o nome do estabelecimento que deseja pesquisar.

Informe também a quantidade de estabelecimentos que deseja encontrar.

O programa abrirá o Google Maps no navegador Chrome, pesquisará pelo estabelecimento e extrairá as informações solicitadas.

As informações extraídas serão salvas em um arquivo Excel com o nome fornecido.

## Limitações e Avisos
Este programa foi projetado para uso educacional e fins de demonstração. O uso excessivo ou automatizado pode violar os termos de serviço do Google Maps.

Esteja ciente de que a extração de dados de sites pode ser sensível a alterações na estrutura da página. Se o Google Maps alterar sua estrutura ou políticas, o programa pode não funcionar conforme esperado.

Este programa utiliza automação para interagir com o Google Maps. Certifique-se de estar ciente das leis e regulamentos locais relacionados à automação da web antes de usar este programa em grande escala.

