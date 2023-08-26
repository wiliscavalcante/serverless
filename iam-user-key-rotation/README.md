# AWS Key Rotator Lambda Function

## Descrição

Esta função Lambda é projetada para rotacionar automaticamente as chaves de acesso IAM da AWS para usuários com uma tag específica. A função é escrita em Python e utiliza o Serverless Framework para implantação. O objetivo é melhorar a segurança através da rotação programada de chaves.

## Pré-requisitos

- Conta AWS com privilégios administrativos
- AWS CLI instalada e configurada
- Node.js e NPM instalados
- Serverless Framework instalado
- Python 3.9 ou superior instalado

## Instalação e Configuração

### Configuração AWS CLI e Serverless Framework

1. Configurar AWS CLI, se ainda não estiver configurada:

    ```bash
    aws configure
    ```

2. Instalar o Serverless Framework:

    ```bash
    npm install -g serverless
    ```

### Clonar e Configurar o Projeto

1. Clone o repositório:

    ```bash
    git clone <URL_DO_REPOSITÓRIO>
    ```

2. Instale as dependências do Python:

    ```bash
    pip install -r requirements.txt
    ```

### Variáveis de Ambiente e Configurações

Certifique-se de fornecer qualquer variável de ambiente ou configuração necessária no `serverless.yaml`.

## Deploy da Função Lambda

1. No diretório raiz do projeto, execute:

    ```bash
    serverless deploy
    ```

Este comando fará o deploy da sua função Lambda e criará todas as políticas e roles IAM necessárias, conforme definido no `serverless.yaml`.

## Como Usar

Esta função Lambda será executada com base em um cron job ou um evento disparado pelo EventBridge. Para testá-la manualmente, você pode invocá-la usando a AWS CLI ou o console da AWS Lambda.

## Segurança e Permissões

A função Lambda requer as seguintes permissões IAM:

- Listar usuários (`iam:ListUsers`)
- Listar chaves de acesso (`iam:ListAccessKeys`)
- Criar chave de acesso (`iam:CreateAccessKey`)
- Excluir chave de acesso (`iam:DeleteAccessKey`)

As políticas IAM necessárias são definidas em `iamRoleStatements` dentro do `serverless.yaml`.

## Contribuições e Problemas

Para contribuições, por favor, abra um pull request. Para problemas, sinta-se à vontade para abrir uma issue.
