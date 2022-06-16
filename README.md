- **Descrição**: O plugin Typescript OpenAPI permite a criação de Lambda com base em um arquivo de especificação OpenAPI.
- **Categoria**: App
- **Stack:** Lambda
- **Criado em**: 11/02/2022
- **Última atualização**: 13/06/2022
- **Download:** [app-typescript-openapi-plugin](https://github.com/stack-spot/app-typescript-openapi-plugin)

# Indice
- [Visao Geral](#Visao-Geral)
- [Uso](#Uso)
  - [Pre-requisitos](#Pre-requisitos)
  - [Recomendado](#Recomendado)
  - [Configuração Stack CLI](#Configuração-Stack-CLI)
    - [Verificacao template e plugin](#Verificacao_template_e_plugin)
  - [Instalacao](#Instalacao)
- [Tutorial](#Tutorial)
- [Useful commands](#Useful-commands)
- [Next Steps](#Next-steps)

## Visao Geral
### Como Typescript OpenAPI Plugin funciona
Por meio das linhas de comando StackSpot é possível aplicar o plugin em uma aplicação do tipo APP  
Ao realizar a aplicação o template de _construct_ cdk é criado na aplicação, utilizando o componente `@stackspot/cdk-component-openapi-typescript`  
Durante a aplicação do plugin é gerado o código lambda baseado na especificação OpenAPI definida no arquivo `infra/spec/{{spec_file_name}}.yaml`

## Uso
Nessa seção mostra como é feita a utilização do plugin por meio do CLI, criando uma aplicação baseada no template [**app-typescript-template**](https://github.com/stack-spot/app-typescript-template)  
Após a criação da aplicação é possível aplicar o plugin **app-typescript-openapi-plugin**  

### Pre-requisitos
Necessário a configuração de alguns pré-requisitos para utilização do plugin.  
- [**Instalação StakSpot CLI**](https://docs.stackspot.com/v3.0.0/os-cli/installation/)
- [**NodeJS**](https://nodejs.org/en/)
- [**Git**](https://git-scm.com/)
- [**AWS CLI**](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
- [**CDK**](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)

### Recomendado
Recomendamos a utilização de algumas ferramentas para desenvolvimento  
- [**LocalStack**](https://github.com/localstack/localstack)

### Configuração Stack CLI
Executar comando abaixo para atualização de local com catálogo que contém OpenAPI plugin:  
```bash
stk add stack https://github.com/stack-spot/skynet-typescript-api-stack
```

#### Verificacao template e plugin
Executando os comandos abaixo é possível verificar que o catálogo foi carregado localmente  
**Listagem plugin disponíveis localmente:**
```bash
stk list plugin
```

**Exemplo output:**
```bash
Stack: skynet-typescript-api-stack
+-----------------------------------+-------------------------------------------------------------------------------------------+---------+-----------------+
| name                              | description                                                                               | types   | version(latest) |
+-----------------------------------+-------------------------------------------------------------------------------------------+---------+-----------------+
| app-typescript-openapi-plugin     | Plugin that applies contract first driven by an OpenAPI contract and auto generate source | ['app'] | 0.1.0           |
|                                   | codes for lambdas and the nested CDK infrastructure                                       |         |                 |
|                                   |                                                                                           |         |                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+---------+-----------------+
```

**Listagem template disponíveis localmente:**
```bash
stk list template
```

**Exemplo output:**
```bash
Stack: skynet-typescript-api-stack
+----------------------+---------------------------------------------+------------------+-----------------+
| name                 | description                                 | types            | version(latest) |
+----------------------+---------------------------------------------+------------------+-----------------+
| base-app-ts-template | Base template to work with typescript stack | ['app-template'] | no release      |
|                      |                                             |                  |                 |
+----------------------+---------------------------------------------+------------------+-----------------+
```

### Instalacao
Os passos dessa seção mostram como criar e configurar o plugin na aplicação  

**Passo 1.** Copie e cole a URL abaixo no seu terminal:
```bash
stk create app meu-teste-app -t skynet-typescript-api-stack/base-app-ts-template
```

**Passo 2.** Acessar projeto criado:  
```bash
cd meu-teste-app
```

**Passo 3.** Aplicação de plugin baseado em catálogo:  
```bash
stk apply plugin skynet-typescript-api-stack/app-typescript-openapi-plugin
```

### Inputs
Abaixo estão listados os inputs do plugin.

Os inputs necessários para utilizar o plugin são:  

| Campo                              | Tipo | Descrição                                                                                                     | Valor Padrão       |
| :---                               | :--- | :---                                                                                                          | :---               |
| *api_name*                         | text | Define o nome da API, também utilizado para fazer o link de códigos gerados e referências de código.          | **api_name**       |
| *spec_file_name*                   | text | Define o nome do arquivo de especificação OpenAPI localizado no diretório /spec, por padrão é spec-file-name. | **spec-file-name** |
| *source_dir*                       | text | Define o caminho, a partir da raiz do projeto, dos arquivos OpenAPI lambda gerados, por padrão é src.         | src                |
| *access_control_allow_origin*      | text | Define a utilização de Access-Control-Allow-Origin customizado dos endpoints.                                 | *                  |
| *access_control_allow_headers*     | text | Define a utilização de Access-Control-Allow-Headers customizado dos endpoints.                                | *                  |
| *access_control_allow_methods*     | text | Define a utilização de Access-Control-Allow-Methods customizado dos endpoints.                                | *                  |
| *access_control_allow_credentials* | text | Define a utilização de Access-Control-Allow-Credentials customizado dos endpoints.                            | *                  |

## Tutorial
Após criação e aplicação de plugin é possível realizar deploy de aplicação _Lambda_ gerada

### 1. CDK bootstrap
Executa _CDK bootstrap_ para preparar a stack e gerar os arquivos do serviço  
```
cdk bootstrap --profile <your-aws-profile>
```

#### Problema relacionado ao acesso publico do S3
Se problema de configuração de acesso publico bloqueado ao S3, na execução do comando _bootstrap_ é possível tentar com a opção `--public-access-block-configuration false` como demonstrado abaixo:  
```
cdk bootstrap --profile <your-aws-profile> --public-access-block-configuration false
```
> Obs.: Se utilizar _npm run cdk bootstrap_ para utilizar essa opção é necessário adicionar `--` após o comando (bootstrap):  
> ```
> npm run cdk bootstrap -- --public-access-block-configuration false
> ```

#### CDK Local
Esse plugin configura automaticamente (para ambiente de desenvolvimento) o uso de _CDK Local_ 
Para usar _LocalStack_ e realizar o bootstrap localmente, executar o comando abaixo:  
```
npm run local bootstrap
```

### 2. Alterar retorno do endpoint
Editar o arquivo _usecase_ gerado (`{{source_dir}}/post-hello/usecase.ts`) e implementar o código para gerar uma resposta esperada com o _import_ `{{source_dir}}/api-models.ts` como mostra abaixo:  
```javascript
import { HelloRequest, HelloResponse } from '../api-schemas';

export type PostHelloParams = {
  requestBody: HelloRequest,
};

export const postHello = async ({ requestBody }: PostHelloParams): Promise<HelloResponse> => {
  return {
    greeting: `Hello ${requestBody.name}!`,
  };
};
```

### 3. Build, deploy e chamada da API
Execute `npm run build`, `cdk deploy` e faça uma chamada com _curl_ ao endpoint criado, com o _payload_ apropriado  
```
npm run build
cdk deploy
curl -X POST -H 'Content-Type: application/json' -d '{"name": "USERNAME"}' https://mhi8zrb3c7.execute-api.us-east-1.amazonaws.com/prod/hello
```

Parabéns! Você criou sua API baseado em uma especificação OpenAPI, realizou o deploy dela na AWS e ja esta configurado com API Gateway e Lambda!  

## Comandos Úteis

- `npm run build` compila typescript para jsii
- `npm run watch` observa mudanças e compila
- `npm run test` executa testes unitários com jest
- `npm run coverage` executa cobertura de testes
- `npm run local synth` sintetiza o projeto CDK com _cdk local_ e gera/atualiza o projeto
- `npm run local deploy` realiza o deploy para o localstack
- `npm run cdk synth` sintetiza o projeto CDK com _cdk_ e gera/atualiza o projeto
- `npm run cdk deploy` realiza o deploy para a conta AWS configurada

## Próximos passos

Depois do Plugin OpenAPI aplicado, ao editar o arquivo `{{spec_file_name}}.yaml` habilita atualizar os arquivos baseados nessa especificação
